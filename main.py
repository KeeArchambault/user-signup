from flask import Flask, request, redirect, render_template

import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/")
def index():
    if request.args.get("username_error"):
        username_error= request.args.get("username_error")
    else:
        username_error= ""

    if request.args.get("password_error"):
        username_error= request.args.get("password_error")
    else:
        password_error= ""

    return render_template("index.html")

@app.route("/", methods= ["POST"])
def user_inputs():
    username = request.form["username"]
    if not username:
        username_error = "Please provide a username."
    else:
        username_error=""

    password = request.form["password"]
    if not password:
        password_error = "Please provide a password."
    else:
        password_error=""

    verify= request.form["verify"]
    password = request.form["password"]
    if password:
        if verify != password:
            verify_error="Passwords do not match."
        else:
            verify_error=""
        

    if email:
        email = request.form["email"]

    return render_template("index.html", username=username, username_error=usename_error, password=password, password_error=password_error, verify=verify, verify_error=verify_error, email=email)    



    



app.run()    
    