from flask import Blueprint, request
from exceptions.message import successResponse

bp = Blueprint(__name__, 'index')

# DONE
@bp.route("/", methods=["GET"])
def index():
    msg = "JDS flask api is running"
    data = {}
    return successResponse(msg, data)

@bp.route("/api/", methods=["GET"])
def api():
    msg = "Welcome to Boilerplate API JDS."
    return successResponse(msg, None)


@bp.route("/api/ping", methods=["GET"])
def isAlive():
    '''Do something.

    Parameters
    ----------
    Returns
    -------
    '''
    
    data = {
        'api': 'api running',
        'database': 'database running'
    }

    return successResponse('Connected', data)
