from sqlalchemy import Column, Integer, Float, DateTime, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Device(Base):
    __tablename__ = 'devices'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)


class Event(Base):
    __tablename__ = 'events'
    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey('devices.id'), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    temperature = Column(Float, nullable=False)
