# # from fastapi import APIRouter, File, UploadFile
# # import shutil
# # from fastapi.responses import FileResponse

# # from fastapi import APIRouter, File, UploadFile, Query
# # import shutil
# # from fastapi.responses import FileResponse

# # router=APIRouter(
# #     prefix='/file',
# #     tags=['file']
# # )

# # @router.post('/uploadfile')
# # def get_uploadfile(upload_file: UploadFile = File(...)):
# #     path = f'files/{upload_file.filename}'
# #     with open(path, 'w+b') as buffer:
# #         shutil.copyfileobj(upload_file.file, buffer)
        
# #         return {
# #             'filename': path,
# #             'type': upload_file.content_type
# #         }
    

# # @router.get('/download/{name}', response_class=FileResponse)
# # def get_file(name:str):
# #     path = f'files/{name}'
# #     return path    


# from fastapi import APIRouter, File, UploadFile, Query, Depends, HTTPException
# import shutil
# from sqlalchemy.orm import Session
# from schemas import UserBase, FileTaskDisplay
# from db.database import get_db
# from db import db_file
# from db.models import DbUser

# router = APIRouter(
#     prefix='/file',
#     tags=['file']
# )

# from fastapi import HTTPException



# @router.post('/{task_id}/uploadfile')
# def upload_file(
#     task_id: int,
#     upload_file: UploadFile = File(...),
#     db: Session = Depends(get_db)
# ):
#      path = f'files/{upload_file.filename}'
#      with open(path, 'wb')as buffer:
#           shutil.copyfileobj
#      return {
#             'filename': path,
#              'type': upload_file.content_type
#          }
        
        
        
        
        
        
        
        
        
        
        
        # with open(path, 'wb') as buffer:
        #     shutil.copyfileobj(upload_file.file, buffer)
        #     return {
        #     'filename': path,
        #     'type': upload_file.content_type
        # }
    
    #     new_file = db_file.create_file(db)   #, user_id=user_id, filename=upload_file.filename
        
    #     return new_file
    # except Exception as e:
    #     raise HTTPException(status_code=500, detail=str(e))


# @router.get('/{id}', response_model:Fi):
# def 