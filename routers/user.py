from fastapi import APIRouter,Depends
from schemas import UserDisplay,UserBase#,AllUserDisplay
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user
from typing import List
from auth.oauth2 import get_current_user


router=APIRouter(
    prefix='/user',
    tags=['user'],
)

#Create user
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase ,db:Session=Depends(get_db)): 
    return db_user.create_user(request, db)#I changed the order here


#Read all users
@router.get('/',response_model=List[UserDisplay])
def get_all_users(db:Session=Depends(get_db)):
    return db_user.get_all_users(db)

#Read a user
@router.get('/{id}',response_model=UserDisplay)
def get_user_by_id(id:int, db:Session=Depends(get_db)): 
        
    return db_user.get_user_by_id(id,db)
    
        
#return db_user.get_user_by_username(db,id) 

#update a user
@router.put('/{id}')
def update_user(id:int, request:UserBase ,db:Session=Depends(get_db),current_user: UserBase= Depends(get_current_user)):
    return db_user.update_user(db,id,request)                                                                          

#Delete a user
@router.delete('/{id}') 
def delete_user(id:int,db:Session=Depends(get_db),current_user: UserBase= Depends(get_current_user)):
    return db_user.delete_user(db,id)