from datetime import datetime, timedelta
from hashlib import md5
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from flask import url_for, current_app
from app import db
#from sqlalchemy.orm.collections import attribute_mapped_collection,mapped_collection,InstrumentedList
import json
from collections import Iterable
class Project(db.Model):
    '''
    项目库，此为项目总体库，一个项目一条记录
    '''
    __tablename__='projects'
    id = db.Column(db.Integer, primary_key=True)
    #项目名称
    name = db.Column(db.String(64))
    #标签
    label = db.Column(db.Text())
    #概述
    summary = db.Column(db.Text())
    #资金来源
    source = db.Column(db.String(64))
    #金额
    money = db.Column(db.Float)
    # 设置关联项目详细表(ProjectDetial)
    projectdetial = db.relationship('ProjectDetial',backref='project')

class ProjectDetial(db.Model):
    '''
    项目详细库，此为项目详细，细分项目
    '''
    __tablename__='projectdetials'
    id = db.Column(db.Integer, primary_key=True)
    #名称
    name = db.Column(db.String(64))
    #标签，用于分类和查询
    label = db.Column(db.Text())
    #概述
    summary = db.Column(db.Text())
    #数量单位
    unit = db.Column(db.String(10))
    #数量
    amount = db.Column(db.Float)
    #单价
    price = db.Column(db.Float)
    #金额
    money = db.Column(db.Float)
    #外键,项目id
    project_id = db.Column(db.Integer,db.ForeignKey('projects.id'))
    #外键,供应商id
    supplier_id = db.Column(db.Integer,db.ForeignKey('suppliers.id'))
    # 设置关联附件资料(Attach)
    attach = db.relationship('Attach',backref='projectdetial')


class Purchase(db.Model):
    '''
    采购库
    '''
    __tablename__='purchases'
    id = db.Column(db.Integer, primary_key=True)
    #采购项目名称
    name = db.Column(db.String(64))
    #项目编号
    number = db.Column(db.String(64))
    #公告时间
    noticedatatime = db.Column(db.DateTime())
    #招标时间
    tenderingdatatime = db.Column(db.DateTime())
    #中标金额
    money = db.Column(db.Float)
    #概述
    summary = db.Column(db.Text())
    #相关链接,公告、预公告、中标公示等链接存放于此，（预留），可以在概述中加链接。
    links = db.Column(db.Text())
    #附件资料列表链接？
    attachs = db.Column(db.Text())
    #外键,中标供应商id，如果是多个供应商，对应多条记录
    supplier_id = db.Column(db.Integer,db.ForeignKey('suppliers.id'))
    #外键,项目详细id
    projectdetial_id = db.Column(db.Integer,db.ForeignKey('projectdetials.id'))

class Supplier(db.Model):
    '''
    供应商
    '''
    __tablename__='suppliers'
    id = db.Column(db.Integer, primary_key=True)
    #供应商全称
    fullname = db.Column(db.String(64))
    #供应商简称
    name = db.Column(db.String(64))
    # 设置关联招标表(purchase)
    purchases = db.relationship('Purchase',backref='supplier')
    # 设置关联项目详细表(ProjectDetial)
    projectdetial = db.relationship('ProjectDetial',backref='supplier')

class Attach(db.Model):
    '''
    附件资料
    '''
    __tablename__='attachs'
    id = db.Column(db.Integer, primary_key=True)
    #附件资料名称
    name = db.Column(db.String(64))
    #附件文件类型，取扩展名。（备用）
    filetype = db.Column(db.String(64))
    #存放路径
    path = db.Column(db.String(255))
    #项目id
    projectdetial_id = db.Column(db.Integer,db.ForeignKey('projectdetials.id'))
    #设置外键关联采购id
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchases.id'))

    #sql = 'select * from student;'
    #stus = db.session.execute(sql)

class School(db.Model):
    '''
    学校库
    '''
    __tablename__='schools'
    id = db.Column(db.Integer, primary_key=True)
    #学校全称
    fullname = db.Column(db.String(64))
    #学校简称
    name = db.Column(db.String(64))
    #设置外键关联组织架构
    organizationunit_id = db.Column(db.Integer, db.ForeignKey('organizationunits.id'))
    #学校特性标签，用于分类和查找，标签用','分割，常用标签如“初中、小学、幼儿园、通南片、通中片、局直学校、局直单位”
    label = db.Column(db.String(255))
    # 设置关联用户(User)
    user = db.relationship('User',backref='school')

class Label(db.Model):
    '''
    标签库,用于客户端选择添加相应标签
    '''
    __tablename__ = 'labels'
    id = db.Column(db.Integer, primary_key=True)
    #标签名
    label = db.Column(db.Text())
    #分组,多组标签集中保存在此库，分组名与表名相同，如学校库的label，在此设为"school"
    group = db.Column(db.String(64))

    def __repr__(self):
        return '<Label {}>'.format(self.group)

    def to_list(self):
        """
        将用","分割的label,返回成list
        """
        label_str=self.label
        #去除头和尾的','
        label_str=label_str.strip(',')
        #分割
        label_list=label_str.split(',')
        return label_list


class Venue(db.Model):
    '''
    功能室库,此库为具体功能室库，区分不同学校，即每所学校不同的功能室对应一条记录
    '''
    __tablename__='venues'
    id = db.Column(db.Integer, primary_key=True)
    #功能室名称
    name = db.Column(db.String(64))
    #功能室标签，与名称不同的是此标签用于分类和查询，如“实验室、物理实验室、化学实验室、生物仪器室”，标签用“，”分割
    label = db.Column(db.Text())
    #学校id号
    school_id = db.Column(db.Integer,db.ForeignKey('schools.id'))

class EquipDetial(db.Model):
    '''
    设备详细信息，给EquipSeq表提供更详细的设备信息，每批设备一条记录
    '''
    __tablename__= 'equipDetials'
    id = db.Column(db.Integer, primary_key=True)
    #名称
    name = db.Column(db.String(64))
    #概述
    summary = db.Column(db.Text())
    #标签
    label = db.Column(db.Text())
    #技术参数
    parameter = db.Column(db.Text())
    #数量
    amount = db.Column(db.Integer)
    #单价
    price = db.Column(db.Float)
    #总价
    total = db.Column(db.Float)
    #设置外键关联EquipSeq
    equipseq_id = db.Column(db.Integer, db.ForeignKey('equipseqs.id'))

class SchoolSeq(db.Model):
    '''
    SchoolSeq：反映学校基本信息变化的时序
    当学校基本数据发生变化时添加一条记录
    '''
    __tablename__='schoolseqs'
    id = db.Column(db.Integer, primary_key=True)
    #时序
    seqdatatime = db.Column(db.DateTime(), default=datetime.utcnow, index=True, unique=True)
    #外键，学校id号
    school_id = db.Column(db.Integer,db.ForeignKey('schools.id'))
    #班级数
    classnum = db.Column(db.Integer)
    #学生数
    studentnum = db.Column(db.Integer)
    #功能室数量
    venuenum = db.Column(db.Integer)
    #教师人数
    teachernum = db.Column(db.Integer)
    #职工总数
    workernum = db.Column(db.Integer)


class EquipSeq(db.Model):
    '''
    EquipSeq:反映设备变化的时序数据
    当设备数量发生变化时会添加一条记录，数量变化包括：新添、报损报废
    允许是单台设备或者是一组设备。
        重要：如果是一组设备，必须是放置在一个功能室中，如果这组设备是放在多个功能室中的，应分成多个记录添加
    如果是一组设备，详细信息可以通过此记录的id号去查询Equips这个表中的groupid，在此没有做关联。
    '''
    __tablename__= 'equipseqs'
    id = db.Column(db.Integer, primary_key=True)
    #时序
    seqdatatime = db.Column(db.DateTime(), default=datetime.utcnow, index=True, unique=True)
    #名称
    name = db.Column(db.String(64))
    #数量是增加还是减少，add为真是增加。
    add = db.Column(db.Boolean)
    #数量
    amount = db.Column(db.Integer)
    #单价
    price = db.Column(db.Float)
    #总价
    total = db.Column(db.Float)
    #概述
    summary = db.Column(db.Text())
    #学校id号
    school_id = db.Column(db.Integer,db.ForeignKey('schools.id'))
    #功能室id号，由于一个功能室中可能会有多批次设备加入。
    venue_id = db.Column(db.Integer,db.ForeignKey('venues.id'))
    #项目id
    projectdetial_id = db.Column(db.Integer,db.ForeignKey('projectdetials.id'))
    #设置外键关联采购id
    purchase_id = db.Column(db.Integer, db.ForeignKey('purchases.id'))
    # 设置关联设备详细列表（EquipDetial）
    equipdetial = db.relationship('EquipDetial',backref='equipseq')

    def __repr__(self):
        return '<EquipSeq {}>'.format(self.name)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'name': self.name,
            'add': self.name,
            'amount': self.location,
            'price': self.location,
            'total': self.location,
            'summary': self.about_me,
            'seqdatatime': self.member_since.isoformat() + 'Z',
            'schoolid': self.schoolid,
            'projectid': self.projectid,
            'venueid': self.venueid,
            'purchaseid': self.purchaseid
        }
        return data

class OrganizationUnit(db.Model):
    #参考http://www.it1352.com/764337.html
    #参考https://flask.palletsprojects.com/en/1.0.x/patterns/sqlalchemy/
    #参考https://www.jianshu.com/p/a52cf3907f29
    #参考https://github.com/sqlalchemy/sqlalchemy/blob/master/examples/adjacency_list/adjacency_list.py
    #__TableName__="organization_units"
    #query = db.query_property()
    __tablename__= 'organizationunits'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String(255), unique=True)
    parentid = db.Column("parentid", db.Integer, db.ForeignKey('organizationunits.id'))
    #标签字段，辅助对组织架构进行分类，标签由用“，”分隔的多个关键字组成
    #label=db.Column("label",db.String(255),unique=True)

    children = db.relationship('OrganizationUnit',

                    # cascade deletions
                    cascade="all",
                    # many to one + adjacency list - remote_side
                    # is required to reference the 'remote' 
                    # column in the join condition.
                    backref=db.backref("parent", remote_side=id),

                    # children will be represented as a dictionary
                    # on the "name" attribute.
                    #collection_class = attribute_mapped_collection('name'),
                    collection_class=list
                ) 

    def __init__(self, name, children=None,parentid=None):
        self.id=id
        self.name = name
        self.parentid=parentid
        self.children = children

    def append(self, nodename):
        self.children[nodename] = OrganizationUnit(nodename, parent=self)

    def __repr__(self):
        return '{"id":%d,"name":"%s","children":%s}' % (self.id, self.name,self.children)

    def flatten(self,obj, ignore_itmes=(str, bytes)):
        for item in obj:
            if isinstance(item, Iterable) and not isinstance(item, ignore_itmes):
                yield from flatten(item)
            else:
                yield item

    def to_json(self):
        """
        flatten与__repr__()结合直接将多层树转换成json
        flatten(obj):obj必须是一个list,因此Model中的children应该使用"collection_class=list"
        OrganizationUnits并不是一个list,因此不能直接作为flatten的参数
        __repr__中内部必须用双引号,否则json.loads会报错,原因未知
        """
        childern_str=list(self.flatten(self.children)).__repr__()
        json_str='{"id":%d,"name":"%s","children":%s}' % (self.id, self.name, childern_str)
        return json.loads(json_str)


class PaginatedAPIMixin(object):
    @staticmethod
    def to_collection_dict(query, page, per_page, endpoint, **kwargs):
        resources = query.paginate(page, per_page, False)
        data = {
            'items': [item.to_dict() for item in resources.items],
            '_meta': {
                'page': page,
                'per_page': per_page,
                'total_pages': resources.pages,
                'total_items': resources.total
            },
            '_links': {
                'self': url_for(endpoint, page=page, per_page=per_page,
                                **kwargs),
                'next': url_for(endpoint, page=page + 1, per_page=per_page,
                                **kwargs) if resources.has_next else None,
                'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                                **kwargs) if resources.has_prev else None
            }
        }
        return data


class User(PaginatedAPIMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    #用户登录名
    username = db.Column(db.String(64), index=True, unique=True)
    #邮箱
    email = db.Column(db.String(120), index=True, unique=True)
    #登录密码
    password_hash = db.Column(db.String(128))  # 不保存原始密码
    #用户真实姓名
    name = db.Column(db.String(64))
    #外键,学校id号
    school_id = db.Column(db.Integer,db.ForeignKey('schools.id'))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # def avatar(self, size):
    #     '''头像'''
    #     digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    #     return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            'name': self.name
        }
        if include_email:
            data['email'] = self.email
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email', 'name']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

    def ping(self):
        self.last_seen = datetime.utcnow()
        db.session.add(self)

    def get_jwt(self, expires_in=3600):
        now = datetime.utcnow()
        payload = {
            'user_id': self.id,
            'name': self.name if self.name else self.username,
            'exp': now + timedelta(seconds=expires_in),
            'iat': now
        }
        return jwt.encode(
            payload,
            current_app.config['SECRET_KEY'],
            algorithm='HS256').decode('utf-8')

    @staticmethod
    def verify_jwt(token):
        try:
            payload = jwt.decode(
                token,
                current_app.config['SECRET_KEY'],
                algorithms=['HS256'])
        except jwt.exceptions.ExpiredSignatureError as e:
            return None
        return User.query.get(payload.get('user_id'))