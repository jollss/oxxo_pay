import datetime
import pytz

from sqlalchemy import Column, String, Text,Integer, DateTime, Date, BigInteger, Float
from sqlalchemy_utils import UUIDType
from app.database import Base

tz = pytz.timezone('America/Mexico_City')


class Bitacora_oxxopay(Base):
    __tablename__ = 'bitacora_pagos_recurrentes'
    id = Column(Integer, primary_key=True)
    user_id = Column(UUIDType(binary=False))
    recived_data_magneton = Column(Text(16777215), nullable=True)
    response_data_conekta = Column(Text(16777215), nullable=True)
    status_conekta=Column(Integer)
    created_at = Column(DateTime, nullable=True,default=datetime.datetime.now(tz=tz))

    def __init__(self, user_id,recived_data_magneton,response_data_conekta,status_conekta):
        self.user_id = user_id
        self.recived_data_magneton = recived_data_magneton
        self.response_data_conekta = response_data_conekta
        self.status_conekta=status_conekta

    def __repr__(self):
        return '%r' % (self.id)
    
    def update(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                if value is not None:
                    setattr(self, key, value)