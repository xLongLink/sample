from longlink import LongLink, create_engine
from src.routes import sample
from src.resources import env

create_engine(env)
app = LongLink(env=env)
app.include_router(sample.router)
