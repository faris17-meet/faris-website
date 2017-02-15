
from sqlalchemy import Column,Integer,String, DateTime, ForeignKey, Float, Time 
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine, func, distinct

Base = declarative_base()

class User(Base):
	__tablename__='user'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	password = Column(String)
	email = Column(String)
	gender = Column(String)
	age = Column(Integer)
	region = Column(String)
	swimtimes = relationship("Swimtime",back_populates="user")

class Swimtime(Base):
	__tablename__='swimtime'
	id = Column(Integer, primary_key=True)
	stroke = Column(String)
	time = Column(Time)
	distance = Column(Integer)
	user_id = Column(Integer, ForeignKey('user.id'))
	user = relationship("User",back_populates="swimtimes")


















