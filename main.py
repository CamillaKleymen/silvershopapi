from fastapi import FastAPI
from database import Base, engine
from api.photo_api.photo import photo_router
from api.users_api.users import users_router
from api.products_api.products import prod_routers


Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url="/")
app.include_router(photo_router)
app.include_router(users_router)
app.include_router(prod_routers)
