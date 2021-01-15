from config.configuration import Configuration
from datetime import datetime
from dateutil import parser
from models import EmployesModel
from helpers.mysql_alchemy import mysql_alchemy as db

configuration = Configuration()

# referensi query model sql alchemy
# https://docs.sqlalchemy.org/en/latest/orm/query.html

class EmployeServices(object):

    def __init__(self, **kwargs):
        pass

    def create(self, json: dict):

        try:
            # generate json data
            json_send = {}
            json_send = json

            # prepare data model
            result = EmployesModel(**json_send)

            # execute database
            db.session.add(result)
            db.session.commit()

            # check if exist
            if(result):
                return True, json_send
            else:
                return False, {}

        except Exception as err:
            # fail response
            return err
