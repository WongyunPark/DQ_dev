import os

from flask import Flask

import logging
from flask_appbuilder import AppBuilder, SQLA
from rule import Rule
from ruleBinding import RuleBinding
logger = logging.getLogger(__name__)


def create_app():
    app = Flask(__name__)
    # api = Api(app)
    
    # api.add_namespace(Rule,"/rules")
    try:
        # Allow user to override our config completely
        config_module = os.environ.get("DQ_CONFIG", "config")
        app.config.from_object(config_module)
        db = SQLA(app)
        appbuilder = AppBuilder(app, db.session)
        
        appbuilder.add_api(Rule)
        logger.info("Rule AppBuilder API Register")
        appbuilder.add_api(RuleBinding)
        logger.info("RuleBinding AppBuilder API Register")
        
        return app

    # Make sure that bootstrap errors ALWAYS get logged
    except Exception as ex:
        logger.exception("Failed to create app")
        raise ex
    