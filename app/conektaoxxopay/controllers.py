import os
from os import path
import pytz
import sys
import json
import requests
import datetime
from app.database import db_session

import traceback
from flask import render_template, current_app,request,jsonify

#import conekta
#conekta.api_key = "key_CdaSchjAsZ7RbrzsGkFuJg"
#conekta.api_version = "2.0.0"
from app.conektaoxxopay.models import *
from sentry_sdk import capture_exception

tz = pytz.timezone('America/Mexico_City')


def Get_oxxopay(datos):
    try:
    #customer = conekta.Customer.create({"name": "Fulanito","email": "fulanito@test.com","phone": "+5218181818181","payment_sources": [{ "type": "oxxo_recurrent"}]})
        data_oxxopay={ "name": request.json['name'],
        "email": request.json['email'],
        "phone": request.json['phone'],
        "payment_sources": [{ "type": request.json['type']  }]}
        headers = {"accept":"application/vnd.conekta-v2.0.0+json",
        "Content-Type": "application/json","Authorization":"Basic a2V5X0NkYVNjaGpBc1o3UmJyenNHa0Z1Smc6"}
        result_oxxopay = requests.post("https://api.conekta.io/customers",json=data_oxxopay ,headers=headers)
        if result_oxxopay.status_code==200:
            r= result_oxxopay.json()   
            v=save_oxxopay(datos,r,result_oxxopay.status_code)  
            return r
        return False
    except Exception as e:
        capture_exception(e)
        return False


def save_oxxopay(datos_magneton,datos,status):
    a = Bitacora_oxxopay(
        user_id=datos_magneton['user_id'],
        recived_data_magneton=str(datos_magneton),
        response_data_conekta=str(datos),
        status_conekta=status
        )
    db_session.add(a)
    db_session.commit()
    db_session.close()      