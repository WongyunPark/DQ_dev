from flask import request
from flask import Blueprint

from flask_appbuilder.api import BaseApi, expose
from app import appbuilder, app

bp = Blueprint('myapp', __name__, url_prefix='/myapp')

class Rule(BaseApi):
    @expose("/test")
    def test(self):
        return self.response(200,message="test")

appbuilder.add_api(Rule, '/rule')
bp.register_blueprint(appbuilder.get_api_blueprint(Rule), url_prefix='/rule')
app.register_blueprint(bp)
