from flask import jsonify
from app.api import bp
import datetime


@bp.route('/ping', methods=['GET'])
def ping():
    '''前端Vue.js用来测试与后端Flask API的连通性'''
    return jsonify('Pong!')

@bp.route('/time', methods=['GET'])
def time():
    '''前端Vue.js测试datetime'''
    data = {
            "columns": ['日期', '标准值','实际值'],
            "rows": [
                {"日期":"2018-06","标准值":90,"实际值":65},
                {"日期":"2018-12","标准值":90,"实际值":78},
                {"日期":"2019-05","标准值":100,"实际值":98},
                {"日期":"2019-08","标准值":100,"实际值":102}
            ]
        }
    return jsonify(data)