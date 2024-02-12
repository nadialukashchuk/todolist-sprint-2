
from fastapi import FastAPI
from routers import user,task, file
from db.database import engine
from db import models
from auth import authentication
from db.hash import Hash

from fastapi.staticfiles import StaticFiles


app=FastAPI(
    title='To do list',
    description='This is a FastAPI project for managing tasks in a to-do list.'
)
app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(task.router)
#app.include_router(file.router)
@app.get('/')
def index():
    return 'To do list'

models.Base.metadata.create_all(engine)



app.mount('/files', StaticFiles(directory='files'), name ='files')