# 装备项目管理(epmflask)

Equipment Project Management是基于Vue和Flask构建的装备项目管理项目实践。
参考：https://madmalls.com/blog/post/first-flask-test-restful-api/

## 一、在github上创建项目

    登录github,创建项目
    本地配置git
    1.查看远端仓库
        git remote -v
    2.添加远程仓库
        git remote add origin <你的项目地址> //注:项目地址形式为:https://gitee.com/xxx/xxx.git或者 git@gitee.com:xxx/xxx.git 或者git@github.com:esun6060996/epmflask.git
    3.删除指定的远程仓库
        git remote rm origin
    4.初始化本地仓库
        git config --global user.email "you@example.com"
        git config --global user.name "Your Name"
        git init
    5.如果你想克隆一个项目，只需要执行
        git clone <项目地址>
    6.完成第一次提交
        git add .
        git commit -m "第一次提交"
        git push origin master
    7.创建 dev 开发分支：
        git checkout -b dev
    8.查看分支
        git branch

## 一、项目安装

    项目下载：git clone git@github.com:esun6060996/epmflask.git
    项目前端在admin目录下

### 前端安装

    进入前端目录：
    cd admin
    f:\epmflask\admin>npm install

### 前端运行

    npm run serve

### 前端生成

    npm run build

### 后端安装

    1.返回项目目录
    cd ..
    2.添加虚拟环境
    F:\epmflask>python -m venv venv
    3.进入虚拟环境
    F:\epmflask>venv\scripts\activate
    (venv) F:\epmflask>
    4.安装包
    (venv) F:\epmflask>pip install -r "requirements.txt"
    5.临时使用清华源
    (venv) F:\epmflask>pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r "requirements.txt"

    6.添加到requirements.txt
    (venv) F:\epmflask>pip freeze >requirements.txt
    6.在项目根目录下新建.env文件,贴入以下内容:
        FLASK_APP=app.py
        FLASK_DEBUG=1

### 后端数据库准备

    1.删除后端文件夹下的migrations文件夹
    2.第一次做数据迁移:
        (venv) F:\epmflask>flask db init
    3.生成迁移脚本
        (venv) F:\epmflask>flask db migrate -m "add users table"
    4.将迁移脚本应用到数据库中
        (venv) F:\epmflask>flask db upgrade

<a href="https://github.com/d2-projects/d2-admin" target="_blank"><img src="https://raw.githubusercontent.com/FairyEver/d2-admin/master/doc/image/d2-admin@2x.png" width="200"></a>
