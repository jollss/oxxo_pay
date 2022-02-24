import os
from os import path
import requests
from flask import Blueprint, jsonify, request

from app.conektaoxxopay.controllers import  *

oxxopay = Blueprint('oxxopay', __name__, url_prefix='/oxxopay')


@oxxopay.route('/', methods=['POST'])
def Oxxopay():
    if request.json:        
        v=Get_oxxopay(request.json)
        if v:            
            return jsonify(v), 200
    return jsonify(success=False), 400
        