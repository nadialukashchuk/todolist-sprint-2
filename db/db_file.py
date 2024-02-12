# from sqlalchemy.orm.session import Session  
# from fastapi import APIRouter, Depends, File,UploadFile, HTTPException

# from schemas import TaskBase, PriorityEnum, TaskDisplay, File_                                 
# from db.models import DbTask
# from fastapi import HTTPException,status, Query
# from sqlalchemy import desc
# from typing import Optional
# import shutil



# from sqlalchemy.orm import Session
# from db.models import DbFile
# from db.models import DbUser




# def create_file(db: Session, file_name:str, task_id:int):
#     # if exist
#     new_file = DbFile(file_name=file_name,task_id=task_id)
#     db.add(new_file)
#     db.commit()
#     db.refresh(new_file)
#     return new_file


# # def get_file(id:int,db:Session):
# #     file=db.query(DbFile).filter(DbFile.id ==id).first()
# #     if not file:
# #         raise  HTTPException(status_code=status.HTTP_404_NOT_FOUND,
# #                            detail=f'Task with id {id} not found')



