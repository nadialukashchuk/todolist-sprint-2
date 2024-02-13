from fastapi import APIRouter, Depends, File,UploadFile, HTTPException
import shutil
from fastapi.responses import FileResponse
from schemas import TaskDisplay, TaskBase, UserBase
from db.database import get_db
from sqlalchemy.orm import Session
from db import db_task
from typing import List, Optional
from schemas import PriorityEnum
from auth.oauth2 import oauth2_scheme, get_current_user
from fastapi import UploadFile
import string
import random

router=APIRouter(
    prefix='/task',
    tags=['task']
)

image_url_types = ['absolute', 'relative']


#Create task
@router.post('/', response_model=TaskDisplay) 
def create_task(request:TaskBase, db:Session=Depends(get_db),current_user: UserBase= Depends(get_current_user)): #
    return db_task.create_task(db,request)


#Get all tasks
@router.get('/',response_model=List[TaskDisplay])
def get_all_task(db:Session=Depends(get_db),current_user: UserBase= Depends(get_current_user)):
    return db_task.get_all_task(db)


#Post file
@router.post('/attachment')
def upload_attachment(attachment: UploadFile = File(...),current_user: UserBase= Depends(get_current_user)):
    letters = string.ascii_letters
    rand_str = ''.join(random.choice(letters) for i in range(6))
    new = f'{rand_str}.'
    filename = new.join(attachment.filename.rsplit('.',1))
    path = f'files/{filename}'

    with open(path, 'w+b') as buffer:
        shutil.copyfileobj(attachment.file, buffer)

        return {'filename': path}

#Get filtered task
@router.get('/{priority}/{id}', response_model=List[TaskDisplay])
def get_filter_tasks(id:int,db: Session = Depends(get_db), priority_filter: PriorityEnum = None,current_user: UserBase= Depends(get_current_user)): #,current_user: UserBase= Depends(get_current_user)
    return db_task.get_filter_tasks(db,user_id=id, priority_filter=priority_filter)


#Update task
@router.put('/{id}') 
def update_task(id:int, request:TaskBase ,db:Session=Depends(get_db),current_user: UserBase= Depends(get_current_user)): 
    return db_task.update_task(id,db,request)


#Delete task
@router.delete('/{id}') 
def delete_task(id:int, db:Session=Depends(get_db),current_user: UserBase= Depends(get_current_user)):
    return db_task.delete_task(id,db)

#############################################################################################################

# #get speciefic task
# @router.get('/{id}',response_model=List[TaskDisplay]) #) 
# def get_task(id:int,request:TaskBase, db:Session=Depends(get_db),current_user: UserBase= Depends(get_current_user)): 
#     return{
#         'data':db_task.get_task(id,db),
#         'current_user': current_user
#     }
