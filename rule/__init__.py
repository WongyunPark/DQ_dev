from flask import request

from flask_appbuilder.api import BaseApi, expose


class Rule(BaseApi):
    
    route_base = "/dq/rule"
    @expose("/getRuleList",methods=["Get"])
    def getRuleList(self):
        return "RuleList"
    
    @expose("/deleteRule",methods=["Delete"])
    def deleteRule(self):
        return "deleteRule"
    
    @expose("/saveRule",methods=["Post"])
    def deleteRule(self):
        return "registerRule"
    
    

