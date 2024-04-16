
# app.py
 
from flask import Flask, render_template, request, redirect, session
 
app = Flask(__name__)



# Set a secret key for encrypting session data
#got from online just to encrypt
app.secret_key = 'my_secret_key'
 
# dictionary with all user and password
users = {
    'Wayne': '123',
    'Eric': '123',
    'Luke': '123'
}
 
# This is the loging page
@app.route('/')
def view_form():
    return render_template('login.html')
 
# For handling get request form we can get
# the form inputs value by using args attribute.
# this values after submitting you will see in the urls.
# e.g http://127.0.0.1:5000/handle_get?username=wayne&password=123
# this exploits our credentials so that's 
# why developers prefer POST request.
@app.route('/handle_get', methods=['GET'])
def handle_get():
    if request.method == 'GET':
        username = request.args['username']
        password = request.args['password']
        print(username, password)
        if username in users and users[username] == password:
            return '<h1>Aww man you got me</h1>'
        else:
            return '<h1>WRONG PASS OR USER NAME HOMIE</h1>'
    else:
        return render_template('login.html')
 
# For handling post request form we can get the form
# inputs value by using POST attribute.
# this values after submitting you will never see in the urls.
@app.route('/handle_post', methods=['POST'])
def handle_post():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        if username in users and users[username] == password:
            return '<h1>Dang you figured me out</h1>'
        else:
            return '<h1>WRONG PASS OR USER NAME HOMIE</h1>'
    else:
        return render_template('login.html')
 
if __name__ == '__main__':
    app.run()