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

app.config['SECRET_KEY'] = 'Idabagusrathuekasuryawibawa!'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////D:\gustu\tugass\osclient\database\database.db'
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

    json_data = []

    itr = True
    while itr:
        try:
            json_data.append(servers.next().to_dict())
        except:
            itr = False

    return json_data

# fungsi untuk menampilkan list kebutuhan CPU VM
def getflavor():
    flavors = osconn.compute.flavors()

    json_data = []

    itr = True
    while itr:
        try:
            json_data.append(flavors.next().to_dict())
        except:
            itr = False

    return json_data

# fungsi untuk melihat list sistem operasi yang tersedia
def getflavor():
    userid = "admin"
    password = "ajuztuwibawa"
    namaproject = "mycloud"
    url = 'http://192.168.8.110/identity/v3/auth/tokens'
    headers = {
        'content-type': 'application/json'
    }
    payload = { 
        "auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "name": userid,
                        "domain": {
                             "id": "default"
                        },
                            "password":password
                    }
                }
            },
            "scope": {
                "project": {
                    "name": namaproject,
                    "domain": {
                        "id": "default"
                    }
                }
            }
        }
    }    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print r.headers.get('X-Subject-Token')
    #print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    json_data = r.json()
    r.close()
    tokens = r.headers.get('X-Subject-Token')
    url = 'http://192.168.8.110/compute/v2.1/flavors/detail'
    headers = {
        'X-Auth-Token':str(tokens)
    }
    r = requests.get(url, headers=headers)
    json_data = r.json()
    print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    r.close()
    return json_data

# fungsi untuk melihat list sistem operasi yang tersedia
def getimages():
    userid = "admin"
    password = "ajuztuwibawa"
    namaproject = "mycloud"
    url = 'http://192.168.8.110/identity/v3/auth/tokens'
    headers = {
        'content-type': 'application/json'
    }
    payload = { 
        "auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "name": userid,
                        "domain": {
                             "id": "default"
                        },
                            "password":password
                    }
                }
            },
            "scope": {
                "project": {
                    "name": namaproject,
                    "domain": {
                        "id": "default"
                    }
                }
            }
        }
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    print r.headers.get('X-Subject-Token')
    #print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    json_data = r.json()
    r.close()
    tokens = r.headers.get('X-Subject-Token')
    url = 'http://192.168.8.110/compute/v2.1/images/detail'
    headers = {
        'X-Auth-Token':str(tokens)
    }
    r = requests.get(url, headers=headers)
    json_data = r.json()
    print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
    r.close()
    return json_data

# fungsi untuk autentikasi pada server cloud
def getTokenAuth():
    userid = "admin"
    password = "ajuztuwibawa"
    namaproject = "mycloud"
    url = 'http://192.168.8.110/identity/v3/auth/tokens'
    headers = {
        'content-type': 'application/json'
    }
    payload = { 
        "auth": {
            "identity": {
                "methods": ["password"],
                "password": {
                    "user": {
                        "name": userid,
                        "domain": {
                             "id": "default"
                        },
                        "password": password
                    }
                }
            },
            "scope": {
                "project": {
                    "name": namaproject,
                    "domain": { 
                        "id": "default"
                    }
                }
            }
        }
    }    
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    token = r.headers.get('X-Subject-Token')
    r.close()
    return token


@app.route('/')
def index():
    return render_template('index.html', title='menuawal')

@app.route('/signup')
def signup():
    username =str(request.form['user'])
    email =str(request.form['email'])
    password =str(request.form['password'])


if __name__ =='__main__':
    app.run(debug=True)

