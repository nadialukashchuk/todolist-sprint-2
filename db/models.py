from .database import Base
from sqlalchemy import Column, Integer, String, Boolean, JSON
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Enum

from datetime import datetime,date
from sqlalchemy import Date, Table
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
    priority=Column(Enum(PriorityEnum))  # создаем Enum и добавляем наш приорити инум из скимас
    is_completed=Column(Boolean)
    user_id=Column(Integer, ForeignKey('Users.id'))
    user=relationship('DbUser', back_populates='items')
    created_date=Column(Date)
    deadline=Column(Date,nullable=True)
    image_url= Column(String,nullable=True)
    image_url_type = Column(String,nullable=True)


