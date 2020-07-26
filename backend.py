from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
import requests
import json



app = Flask(__name__)
app.debug = True


@app.route('/')
def create():

        userid = "admin"
        password = "00000000"
        namaproject = "demo"
        url = 'http://192.168.0.154/identity/v3/auth/tokens'
        headers = {'content-type': 'application/json'}
        payload = { "auth": {"identity": {"methods": ["password"],"password": {"user": {"name": userid,"domain": { "id": "default" },"password":password}}},"scope": {"project": {"name": namaproject,"domain": { "id": "default" }}}}}
        r = requests.post(url, data=json.dumps(payload), headers=headers)
        print r.headers.get('X-Subject-Token')
        #print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
        json_data = r.json()
        r.close()
        tokens = r.headers.get('X-Subject-Token')
        url = '	http://192.168.0.154:8042/v1/metric'
        headers = {'X-Auth-Token':str(tokens)}
        r = requests.get(url, headers=headers)
        json_data = r.json()
        print json.dumps(r.json(), sort_keys=True, indent=4, separators=(',', ': '))
        r.close()
       # return render_template(json_data = json_data)
        return render_template('coba.html', json_data = json_data)




if __name__ == "__main__":
    app.run()
