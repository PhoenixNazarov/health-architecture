import os
from sqlmodel import Session, SQLModel, create_engine, select, func
from injectable import injectable

from .db_config import DB_REQUISITES, DbConfig
from ..dto.view_params import ViewParams


class SqlSubController:
    def __init__(self, config: DbConfig):
        user = config.user
        password = config.password
        ip = config.ip
        port = config.port
        name = config.name

        self.engine = create_engine(f"postgresql://{user}:{password}@{ip}:{port}/{name}")

    @staticmethod
    def __unpack(rows):
        return [i[0] for i in rows]

    @staticmethod
    def __build_statement_by_view_params(model: type(SQLModel), view_params):
        statement = select(model)
        for f in view_params.filters:
            if type(f.value) == list:
                statement = statement.where(f.field.in_(f.value))
            else:
                statement = statement.where(f.field == f.value)

        for o in view_params.orders:
            if o.desc:
                statement = statement.order_by(o.field.desc())
            else:
                statement = statement.order_by(o.field.asc())

        if view_params.count:
            statement = statement.limit(view_params.count)

        if view_params.page:
            statement = statement.offset(view_params.count * view_params.page)

        return statement

    def find_by_view_params_all(self, model: type(SQLModel), view_params: ViewParams):
        statement = self.__build_statement_by_view_params(model, view_params)
        with Session(self.engine) as session:
            rows = session.execute(statement).all()
            return self.__unpack(rows)

    def find_by_view_params_count(self, model: type(SQLModel), view_params: ViewParams):
        statement = self.__build_statement_by_view_params(model, view_params)
        statement = statement.with_only_columns([func.count()]).select_from(model)
        with Session(self.engine) as session:
            return session.execute(statement).scalar()

    def find_with_filter_first(self, model: type(SQLModel), field, value):
        statement = select(model)
        if type(value) == list:
            statement = statement.where(field.in_(value))
        else:
            statement = statement.where(field == value)

        with Session(self.engine) as session:
            model = session.execute(statement).first()
            if model:
                return model[0]
            return

    def find_with_filter_all(self, model: type(SQLModel), field, value):
        statement = select(model)
        if type(value) == list:
            statement = statement.where(field.in_(value))
        else:
            statement = statement.where(field == value)

        with Session(self.engine) as session:
            rows = session.execute(statement).all()
            return self.__unpack(rows)

    def find_with_filter_count(self, model: type(SQLModel), field, value):
        statement = select(model)
        if type(value) == list:
            statement = statement.where(field.in_(value))
        else:
            statement = statement.where(field == value)
        statement = statement.with_only_columns([func.count()])

        with Session(self.engine) as session:
            return session.execute(statement).scalar()

    def save(self, model: type(SQLModel)):
        with Session(self.engine) as session:
            session.add(model)
            session.flush()
            session.expunge(model)
            session.commit()
            return model

    def save_all(self, models: list[type(SQLModel)]):
        with Session(self.engine) as session:
            session.add_all(models)
            session.flush()
            for i in models:
                session.expunge(i)
            session.commit()
        return models

    def remove(self, model: type(SQLModel)):
        with Session(self.engine) as session:
            session.delete(model)
            session.commit()
        return model

    def remove_all(self, models: list[type(SQLModel)]):
        with Session(self.engine) as session:
            for i in models:
                session.delete(i)
            session.commit()
        return models


@injectable(singleton=True)
class SqlController:
    def __init__(self):
        self.sub_controllers: dict[str, SqlSubController] = {}
        self.default_requisites = DB_REQUISITES.get("DEFAULT")
        self.default_sub_controller = SqlSubController(self.default_requisites)

    def get_by_module(self) -> SqlSubController:
        return self.default_sub_controller
