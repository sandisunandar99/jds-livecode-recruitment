import json
from flask import Blueprint, request
from exceptions.message import successResponse
from api import EmployeServices

bp = Blueprint(__name__, 'employe')
employe = EmployeServices()


@bp.route("/api/employe", methods=["POST"])
def create():

    try:
        # prepare json data
        json_request = request.get_json(silent=True)

        # insert dataset_class
        res, employeResult = employe.create(json_request)

        if res:
            return successResponse("Create data successfull", employeResult)
        else:
            return successResponse("Create data unsuccessfull", employeResult)

    except Exception as e:
        # fail response
        return successResponse("Create data unsuccessfull exceptions",  str(e))

