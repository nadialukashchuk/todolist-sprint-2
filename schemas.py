from pydantic import BaseModel
from datetime import date
from typing import List, Optional
from enum import Enum



class PriorityEnum(str, Enum):                                  #Creating enum/import from 
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"

class UserBase(BaseModel):                                                  
    username:str
    email:str
    password:str

class TaskBase (BaseModel):                                                 
    content:str
    priority: PriorityEnum = PriorityEnum.MEDIUM               #default value, could be only priority enum
    is_completed:bool =False
    creator_id:int
    created_date: date
    deadline: date 

    image_url:str               #image we want to display
    image_url_type:str          #relative-if upload image to API we or absolute-from the internet
    
class User(BaseModel):                                                              
    id:int                                                                      
    username:str
    class Config():
        orm_mode=True
                                                                           
class UserDisplay(BaseModel):                                               
    username:str
    email:str
    class Config():                                                         
        orm_mode=True      




class TaskDisplay (BaseModel):
    content:str
    priority:PriorityEnum
    is_completed:bool
    created_date: date                                                            
    deadline: date 
    user:User 

    image_url:str
    image_url_type: str   
    class Config():
        orm_mode=True


# class Task(BaseModel): #it's used in UserTaskDisplay
#     id:int
#     content:str
#     is_completed:bool
#     class Config():
#         orm_mode=True