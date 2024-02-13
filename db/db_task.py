from sqlalchemy.orm.session import Session  
from fastapi import APIRouter, Depends, File,UploadFile, HTTPException
from schemas import TaskBase, PriorityEnum, TaskDisplay                                 
from db.models import DbTask, DbUser
from fastapi import HTTPException,status, Query
from sqlalchemy import desc
from typing import Optional
from sqlalchemy import desc
import shutil
from sqlalchemy.orm import joinedload


#Get all user's tasks
def get_all_task(db:Session):
    return  db.query(DbTask).all()


#Get filtered tasks of users    
def get_filter_tasks(db: Session, user_id: int, priority_filter: PriorityEnum = None):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {user_id} not found")
    query = db.query(DbTask).filter(DbTask.user_id == user_id)
    if priority_filter:
        query = query.filter(DbTask.priority == priority_filter)
    tasks = query.order_by(desc(DbTask.priority)).all()
    return tasks


#Create task
def create_task(db:Session, request:TaskBase):
    new_task = DbTask(                                      
        content=request.content,
        priority=request.priority,
        is_completed=request.is_completed,
        created_date=request.created_date,
        deadline=request.deadline,
        attachment_url= request.attachment_url,
        attachment_url_type=request.attachment_url_type,
        user_id=request.creator_id

    ) 
   
    db.add(new_task)
    db.commit()
    db.refresh(new_task)                                    
    return new_task


#Update task
def update_task(id:int, db:Session, request:TaskBase ):
    task=db.query(DbTask).filter(DbTask.id==id)                           
    if not task.first():
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
      detail=f'User with id {id} not found')
    task.update({
       DbTask.content:request.content,
       DbTask.priority:request.priority,
       DbTask.user_id:request.creator_id,
       DbTask.attachment_url:request.attachment_url,
       DbTask.attachment_url_type:request.attachment_url_type
    })
    updated_task= [request.content,request.priority, request.creator_id,request.attachment_url,request.attachment_url_type]
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
    




# def get_filter_tasks(db: Session, user_id:int = Query(...), priority_filter: PriorityEnum = None):
#     query = db.query(DbTask).filter(DbTask.user_id ==user_id)
#     if priority_filter:
#         query = query.filter(DbTask.priority == priority_filter)
#     tasks = (
#         query
#         .order_by(desc(DbTask.priority))
#         .all()
#     )
#     return tasks

# #get task                                                                                                                                  
# def get_task(id:int, db:Session):
#     task=db.query(DbTask).filter(DbTask.id==id).first()
#     if not task:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#         detail=f'User with id {id} not found')
#     return task 