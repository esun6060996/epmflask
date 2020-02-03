import re
from flask import request, jsonify, url_for
from app import db
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request
from app.models import School


@bp.route('/schools', methods=['POST'])
def create_school():
    '''添加一所学校'''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')

    school = School()
    school.from_dict(data)
    db.session.add(school)
    db.session.commit()
    response = jsonify(school.to_dict())
    response.status_code = 201
    return response


@bp.route('/schools', methods=['GET'])
#@token_auth.login_required
def get_schools():
    '''返回学校集合，分页'''
    page = request.args.get('page', 1, type=int)
    per_page = min(request.args.get('per_page', 10, type=int), 100)
    data = School.to_collection_dict(School.query, page, per_page, 'api.get_schools')
    return jsonify(data)


@bp.route('/schools/<int:id>', methods=['GET'])
@token_auth.login_required
def get_school(id):
    '''返回一所学校'''
    return jsonify(School.query.get_or_404(id).to_dict())


@bp.route('/schools/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_School(id):
    '''修改一所学校'''
    school = School.query.get_or_404(id)
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data.')

    message = {}
    if 'name' in data and not data.get('name', None):
        message['name'] = 'Please provide a valid name.'

    school.from_dict(data)
    db.session.commit()
    return jsonify(school.to_dict())


@bp.route('/schools/<int:id>', methods=['DELETE'])
@token_auth.login_required
def delete_school(id):
    '''删除一所学校'''
    pass