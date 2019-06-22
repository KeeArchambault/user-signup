from flask import Flask, request, redirect, render_template

import cgi

import os

app = Flask(__name__)

app.config['DEBUG'] = True 


@app.route("/")
def index():
    
    return render_template("index.html", username= "", username_error= "", password= "", password_error= "", verify= "", verify_error="", email="", email_error= "")


@app.route("/validate_input", methods= ["POST"])
def validate_inputs():
    username = request.form["username"]
    password = request.form["password"]
    verify= request.form["verify"]
    password = request.form["password"]
    email = request.form["email"]

    username_error= ""
    password_error= ""
    verify_error= ""
    email_error= ""

    if not username or len(username) < 3 or len(username) > 20 or " " in username:
        username_error = "Please provide a valid username."
        username= ""
       

    if not password or len(password) < 3 or len(password) > 20 or " " in password:
        password_error = "Please provide a valid password."
        password= ""
    else:
        password_error= ""
        

    if password:
        if verify != password:
            verify_error="Passwords do not match."
            verify= ""
              

    if email and len(email) < 3 or len(email) > 20 or " " in email or email.count("@") != 1 or email.count(".")!= 1:
        email_error = "Please provide a valid email."
        email= ""
             

    if not username_error and not password_error and not verify_error and not email_error:
        return render_template("home.html", username=username)
    else:
        return render_template("index.html", username=username, username_error=username_error, password=password, password_error=password_error, verify=verify, verify_error=verify_error, email=email, email_error=email_error)


app.run() 

    