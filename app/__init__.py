from flask import Flask, current_app, jsonify, request, url_for, render_template
from flask.wrappers import Response
from werkzeug.exceptions import HTTPException, InternalServerError
from app.controllers import *
from app.database import db_session
from flask_cors import CORS
from app.conektaoxxopay import oxxopay
import os
import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration
from sentry_sdk import capture_exception, capture_message
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

def create_app():
    sentry_sdk.init(
    dsn="https://9d9117ae5e5f476fa021089ab54e3989@sentry.curadeuda.com/18",
    integrations=[FlaskIntegration(transaction_style='url'), SqlalchemyIntegration()],
    environment=os.environ.get('FLASK_ENV'),
    send_default_pii=True,
    )
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    CORS(app)


    app.register_blueprint(oxxopay)

    @app.route("/ping", methods=['GET'])
    def ping():
        
        return jsonify(success=True,response="cloyster!"), 200
    
    @app.errorhandler(Exception)
    def handle_exception(e):
        capture_exception(e)
        return jsonify(success=False, error_message="{}".format(e)), 500

    @app.errorhandler(HTTPException)
    def handle_bad_request(e):
        capture_exception(e)
        return jsonify(success=False, error_message="{}".format(e)), e.code
    
    

    return app