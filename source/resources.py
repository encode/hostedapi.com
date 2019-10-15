from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from source import settings
import databases


templates = Jinja2Templates(directory="templates")
statics = StaticFiles(directory="statics")


if settings.TESTING:
    database = databases.Database(settings.TEST_DATABASE_URL, force_rollback=True)
else:  # pragma: nocover
    database = databases.Database(settings.DATABASE_URL)
