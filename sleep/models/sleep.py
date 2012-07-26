from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey
    )

from sqlalchemy.orm import relationship
from models import Base
import datetime

class Sleep(Base):
    __tablename__ = 'sleep'
    id = Column(Integer, primary_key=True)
    start = Column(Text)
    end = Column(Text)
    date = Column(Integer)
    quality = Column(Integer)
    user_id = Column(Integer, ForeignKey('users.id'))
    submitdate = Column(Integer)
    
    user = relationship("User", 
                        primaryjoin="Sleep.user_id == User.id")
    
    def ddate(self):
        ds = map(int,self.date.split('/'))
        
        # return a date object corresponding to this date
        return datetime.date(ds[2],ds[1],ds[0])

    def duration(self):
        tdelta = datetime.datetime.strptime(self.end,'%H,%M')-datetime.datetime.strptime(self.start,'%H,%M')
        
        # you slept for NEGATIVE TIME?
        if tdelta.days < 0:
            tdelta += datetime.timedelta(1)
            
        return tdelta.seconds