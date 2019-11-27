import re
from flask import request, jsonify, url_for
from app import db
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request
from app.models import OrganizationUnit

@bp.route('/organizationunits', methods=['GET'])
def get_organizationunits():
    '''返回组织树型结构'''
    data = OrganizationUnit.query.filter_by(parentid = None).first()
    return data.to_json()