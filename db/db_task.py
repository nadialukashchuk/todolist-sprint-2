from sqlalchemy.orm.session import Session  
from fastapi import APIRouter, Depends, File,UploadFile, HTTPException

from schemas import TaskBase, PriorityEnum, TaskDisplay                                 
from db.models import DbTask
from fastapi import HTTPException,status, Query
from sqlalchemy import desc
from typing import Optional
from sqlalchemy import desc
import shutil
from sqlalchemy.orm import joinedload


def get_all_task(db:Session):
    return  db.query(DbTask).all()
    


def get_filter_tasks(db: Session, user_id:int = Query(...), priority_filter: PriorityEnum = None):
    query = db.query(DbTask).filter(DbTask.user_id ==user_id)
    if priority_filter:
        query = query.filter(DbTask.priority == priority_filter)
    tasks = (
        query
        .order_by(desc(DbTask.priority))
        .all()
    )
    return tasks


#create task
def create_task(db:Session, request:TaskBase):
    new_task = DbTask(                                      
        content=request.content,
        priority=request.priority,
        is_completed=request.is_completed,
        user_id=request.creator_id,
        created_date=request.created_date,
        deadline=request.deadline,
        image_url= request.image_url,
        image_url_type=request.image_url_type
    ) 
   
    db.add(new_task)
    db.commit()
    db.refresh(new_task)                                    
    return new_task


#get task                                                                                                                                  
def get_task(id:int, db:Session):
    task=db.query(DbTask).filter(DbTask.id==id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User with id {id} not found')
    return task 



#update task
def update_task(id:int, db:Session, request:TaskBase ):
    task=db.query(DbTask).filter(DbTask.id==id)                           
    if not task.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f'User with id {id} not found')
    task.update({
       DbTask.content:request.content,
       DbTask.priority:request.priority,
       DbTask.user_id:request.creator_id,
       DbTask.image_url:request.image_url,
       DbTask.image_url_type:request.image_url_type
    })
    updated_task= [request.content,request.priority, request.creator_id,request.image_url,request.image_url_type]
    db.commit()
    return {'updated task:': updated_task}   

#delete task
def delete_task(id:int, db:Session):
    task=db.query(DbTask).filter(DbTask.id==id).first()
    if not task:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'User with id {id} not found')
    if task: 
        db.delete(task)                                                             
        db.commit()                                                                 
        return 'sucsesfully deleted'
    else: 
        return None
    



##############################################################################################################################
