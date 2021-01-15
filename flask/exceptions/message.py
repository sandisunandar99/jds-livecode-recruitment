from flask import jsonify

def successResponse(msg, data = None):
    response = {
        "message": msg,
        "status": 'success',
        "data": data
    }
    return jsonify(response), 200
