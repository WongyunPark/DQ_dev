from flask import request

from flask_appbuilder.api import BaseApi, expose

class RuleBinding(BaseApi):
    route_base = "/dq/rulebinding"
    
    
    @expose("/getRuleBindingList")
    def ruleBindingList(self):
        return "getRuleBindingList"
    

