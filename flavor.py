from flask import Flask, render_template, redirect, url_for, request
import requests
import json
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user


app = Flask(__name__)
app.debug = True

#conn = MySQLdb.connect(host="localhost", user="root", password="",db="tugasakhir")

# app.config['SECRET_KEY'] = 'Idabagusrathuekasuryawibawa!'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/gustu/websample/database/database.db'
# Bootstrap(app)
# db = SQLAlchemy(app)
# login_manager = LoginManager()
# login_manager.init_app(app)
# login_manager.login_view = 'login'

# class User (UserMixin, db.Model):
#     id = db.Column(db.Integer,primary_key=True)
#     username = db.Column(db.String(20), unique=True)
#     email = db.Column(db.String(50), unique=True)
#     password = db.Column(db.String(80))

# @login_manager.user_loader
# def load_user(user_id):
#     return User.query.get(int(user_id))

# class LoginForm(FlaskForm):
#     username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
#     password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
#     remember = BooleanField('remember me')

# class RegisterForm(FlaskForm):
#     email = StringField('email', validators=[InputRequired(), Email(message='email salah'), Length(max=50)])
#     username = StringField('username', validators=[InputRequired(), Length(min=4, max=20)])
#     password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])

# fungsi untuk menampilkan list kebutuhan CPU VM
def getflavor():
    userid = "admin"
    password = "ajuztuwibawa"
    namaproject = "myclouds"
    url = 'http://192.168.1.10/identity/v3/auth/tokens'
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
    url = 'http://192.168.1.10/compute/v2.1/flavors/detail'
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
    namaproject = "myclouds"
    url = 'http://192.168.1.10/identity/v3/auth/tokens'
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
    url = 'http://192.168.1.10/compute/v2.1/images/detail'
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
    namaproject = "myclouds"
    url = 'http://192.168.1.10/identity/v3/auth/tokens'
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
    return render_template('index.html')

# @app.route('/login', methods=['GET','POST'])
# def login():
#     form=LoginForm()

#     if form.validate_on_submit():
#         user = User.query.filter_by(username=form.username.data).first()
#         if user:
#             if check_password_hash(user.password, form.password.data):
#                 login_user(user, remember=form.remember.data)
#                 return redirect(url_for('dashboard'))
#         return redirect(url_for('login'))

#     return render_template('login.html', form=form)

# @app.route('/signup', methods=['GET','POST'])
# def signup():
#     form=RegisterForm()

#     if form.validate_on_submit():
#         hashed_password = generate_password_hash(form.password.data, method='sha256')
#         new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
#         db.session.add(new_user)
#         db.session.commit()
#         return '<h1> User created </h1>'

#     return render_template('signup.html', form=form)

@app.route('/dashboard')
#@login_required
def dashboard():
    return render_template('dashboard.html')#, name= current_user.username)

@app.route('/profil')
@login_required
def profil():
    return render_template('user.html', name= current_user.username)

@app.route('/buatbaru')
def buatbaru():
    json_data = {}
    json_data.update(getflavor())
    json_data.update(getimages())
    return render_template('buatbaru.html',json_data = json_data)#, name= current_user.username)

@app.route('/listserver', methods=['POST'])
def listserver():
    # get the data form
    data = request.form
        
    # create vm
    url = 'http://192.168.1.10/compute/v2.1/servers'
    name = data['namaproject']
    flavor = data['cpu']
    image = data['sistem_operasi']
    adminPass = 'qwerty'
    keyname = 'admincode'
    headers = {
        'content-type': 'application/json',
        'X-Auth-Token':str(getTokenAuth())
    }
    payloads = {
        'server': {
            'name': name,
            'flavorRef':flavor,
            'imageRef':image,
            'adminPass':adminPass,
            'key_name':keyname
        }
    }
    create = requests.post(url, data=json.dumps(payloads), headers=headers)
    create.close()

    # return template
    return render_template('listserver.html', data = data)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)