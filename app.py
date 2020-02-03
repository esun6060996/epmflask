from app import create_app,db
from app.models import User,OrganizationUnit,Label，School

app = create_app()

#添加Flask Shell上下文环境
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User,'OrganizationUnit':OrganizationUnit}