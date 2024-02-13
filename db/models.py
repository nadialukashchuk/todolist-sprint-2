from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, Date, Table, Enum
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime,date
from typing import List, Optional
from schemas import PriorityEnum

from sqlalchemy.types import Date as SQLAlchemyDate

 

class DbUser(Base):
    __tablename__='Users'
    
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String)
    email=Column(String)
    password=Column(String)
    items=relationship('DbTask',back_populates='user', cascade='all, delete-orphan')

class DbTask(Base):
    __tablename__='Tasks'

    id=Column(Integer, primary_key=True, index=True)
    content=Column(String)
    priority=Column(Enum(PriorityEnum))                                             #create Enum add priority enum from schemas
    is_completed=Column(Boolean)
    user_id=Column(Integer, ForeignKey('Users.id'))
    user=relationship('DbUser', back_populates='items')
    created_date=Column(Date)
    deadline=Column(Date,nullable=True)
    attachment_url= Column(String,nullable=True)
    attachment_url_type = Column(String,nullable=True)


