from decouple import config

project_env = config("PROJECT_ENV", None)

if project_env:
    if project_env == "staging":
        from .staging import *
    else:
        from .production import *
else:
    from .local_settings import *
