from sqlalchemy import (
    Column,
    Integer,
    Text
    )

from sqlalchemy.orm import relationship
from models import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(Text, unique=True)
    email = Column(Text, unique=True)
    joindate = Column(Integer)
    password = Column(Text)
    
    records = relationship("Sleep", 
                           order_by="desc(Sleep.submitdate)",
                           primaryjoin="User.id == Sleep.user_id")
        