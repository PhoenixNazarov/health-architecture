from injectable import load_injection_container

load_injection_container()

from modules.backend.app import start

start()
