from flask import Flask, render_template, redirect, url_for, request
import requests
import os
import subprocess
import json

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import jsonify
from flask import json
import ruamel.yaml
from openstack import connection


app = Flask(__name__)
app.debug = True

osconn = connection.Connection(auth_url=os.environ['OS_AUTH_URL'],
                             project_name=os.environ['OS_PROJECT_NAME'],
                             username=os.environ['OS_USERNAME'],
                             password=os.environ['OS_PASSWORD'],
                             user_domain_id="default",
                             project_id=os.environ['OS_PROJECT_ID'],
                             project_domain_id=os.environ['OS_PROJECT_DOMAIN_ID'],
                             compute_api_version='2.1',
                             verify=False)
#print(osconn)

app.config['SECRET_KEY'] = 'Idabagusrathuekasuryawibawa!'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/gustu/myweb/database/database.db'
Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

level = 0

class User (UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))
    level = db.Column(db.Integer)

class Project(UserMixin, db.Model):
    id = db.Column(db.Integer,primary_key=True)
    project = db.Column(db.String(20), unique=True)
    description = db.Column(db.String(255))
    idos = db.Column(db.String(128))
    osdesc = db.Column(db.String(50))
    idcpu = db.Column(db.String(128))
    cpudesc = db.Column(db.String(50))
    user = db.Column(db.String(20))
    addr = db.Column(db.String(255))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    remember = BooleanField('remember me')

class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='email salah'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

class ProjectForm(FlaskForm):
    namaproject = StringField('namaproject', validators=[InputRequired(), Length(max=20)])
    deskripsi = StringField('deskripsi')
    sistem_operasi = StringField('sistem_operasi')
    cpu = StringField('cpu')

def getproject():
    servers = osconn.compute.servers()
    for server in osconn.compute.servers():
        print(server)

    json_data = [server]

    itr = True
    while itr:
        try:
            json_data.append(servers.next().to_dict())
        except:
            itr = False

#    print(json_data)
    return json_data

# fungsi untuk menampilkan list kebutuhan CPU VM
def getflavor():
    flavors = osconn.compute.flavors()
    for flavor in osconn.compute.flavors():
        print(flavor)

    json_data = [flavor]

    itr = True
    while itr:
        try:
            json_data.append(flavors.next().to_dict())
        except:
            itr = False

#    print(json_data)
    return json_data


# fungsi untuk melihat list sistem operasi yang tersedia
def getimages():
    images = osconn.compute.images()
    for image in osconn.compute.images():
        print(image)
    json_data = [image]

    itr = True
    while itr:
        try:
            json_data.append(images.next().to_dict())
        except:
            itr = False
 #   print(json_data)
    return json_data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():

    global level

    form=LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data) and user.level >= 0:
                login_user(user, remember=form.remember.data)
                level = user.level
                return redirect(url_for('dashboard'))
        return redirect(url_for('login'))

    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET','POST'])


def signup():
    form=RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, email=form.email.data, password=hashed_password, level=1)
        db.session.add(new_user)
        db.session.commit()
        return render_template('login_new.html', form=LoginForm())

    return render_template('signup.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', level=level, name= current_user.username)

@app.route('/userlist')
def userlist():
    user = User.query.all();
    return render_template('userlist.html', user=user, level=level)

@app.route('/userlist-save', methods=['GET','POST'])
def userlist_save():
    data = request.json['data']
    user = User.query.filter_by(username=data["username"]).first()

    if user.level == -1:
        user.level = 1
    else:
        user.level = -1

    db.session.merge(user)
    db.session.commit()

    json_data = {"status": True}

    response = app.response_class(
        response=json.dumps(json_data),
        mimetype='application/json'
    )
    #print(response)
    return response

@app.route('/profil')
def profil():
    user = User.query.filter_by(username=current_user.username).first()
    return render_template('user.html', username=user.username, email=user.email, level=level)

@app.route('/profil-save', methods=['GET','POST'])
def profil_save():
    data = request.json['data']

    hashed_password = generate_password_hash(data["password"], method='sha256')

    user = User.query.filter_by(username=data["username"]).first()
    user.email = data["email"]
    user.password = hashed_password

    db.session.merge(user)
    db.session.commit()

    json_data = {"status": True}

    response = app.response_class(
        response=json.dumps(json_data),
        mimetype='application/json'
    )

    return response


@app.route('/buatbaru')
def buatbaru():
    json_data = {}
    json_data.update({"flavors": getflavor()})
    json_data.update({"images": getimages()})
    return render_template('buatbaru.html',json_data = json_data, level=level, name= current_user.username)

@app.route('/project-save', methods=['GET','POST'])
def project_save():
    form=ProjectForm()

    osdesc = ""
    images = getimages()

    for image in images:
        if form.sistem_operasi.data == image["id"]:
            osdesc = image["name"]
            break

    cpudesc = ""
    flavors = getflavor()
    cduname = ""

    for flavor in flavors:
        if form.cpu.data == flavor["id"]:
            cpudesc = "Storage= "+str(flavor["disk"])+" GB, vCPU= "+str(flavor["vcpus"])+", RAM= "+str(flavor["ram"])+" MB"
            cpuname = str(flavor["name"])
            break

    new_project = Project(
        project=form.namaproject.data,
        description=form.deskripsi.data,
        idos=form.sistem_operasi.data,
        osdesc=osdesc,
        idcpu=form.cpu.data,
        cpudesc=cpudesc,
        user=current_user.username
    )
    db.session.add(new_project)
    db.session.commit()

    fin = open("yaml/deploy.yaml", "rt")
    data = fin.read()
    data = data.replace('<name>', form.namaproject.data)
    data = data.replace('<image>', osdesc)
    data = data.replace('<flav>', cpuname)
    fin.close()

    fin = open("yaml/deploy_"+current_user.username+".yaml", "wt")
    fin.write(data)
    fin.close()


    p = subprocess.Popen("ansible-playbook " + "yaml/deploy_"+current_user.username+".yaml", shell=True, stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()

    project = None
    if level == 0:
        project = Project.query.all();
    else:
        project = Project.query.filter_by(user=current_user.username).all();

    return render_template('projectlist.html', project=project, level=level)

@app.route('/projectlist-del', methods=['GET','POST'])
def project_del():
    data = request.json['data']

    project = Project.query.filter_by(id=data["id"]).first()


    fin = open("yaml/delete.yaml", "rt")
    data = fin.read()
    data = data.replace('<name>', project.project)
    fin.close()

    fin = open("yaml/delete_"+current_user.username+".yaml", "wt")
    fin.write(data)
    fin.close()

    p = subprocess.Popen("ansible-playbook " + "yaml/delete_"+current_user.username+".yaml", shell=True, stdout=subprocess.PIPE)
    stdout, stderr = p.communicate()

    db.session.delete(project)
    db.session.commit()

    json_data = {"status": True}

    response = app.response_class(
        response=json.dumps(json_data),
        mimetype='application/json'
    )

    return response

@app.route('/projectlist')
def projectlist():

    project = None
    if level == 0:
        project = Project.query.all();
    else:
        project = Project.query.filter_by(user=current_user.username).all();

    data = getproject()

    for pj in project:
        for dt in data:
            if pj.project == dt["name"]:
                pj.addr = dt["openstack.compute.v2.server.Server"]["addresses"]["int-ext"][0]["addr"]

    return render_template('projectlist.html', project=project, level=level)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.10', port=5005)
