import re
from flask import request, jsonify, url_for
from app import db
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request
from app.models import Label
import json

@bp.route('/labels', methods=['GET'])
def get_labels():
    '''返回组织树型结构'''
    group_args = request.args.get('group')
    labels = Label.query.filter_by(group =group_args).first()
    #去除头和尾的','
    label_str=labels.label.strip(',')
    #分割
    label_list=label_str.split(',')
    return jsonify(label_list)