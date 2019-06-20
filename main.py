from flask import Flask, request, redirect

import os

import jinja2

app = Flask(__name__)

app.config['DEBUG'] = True   


template_dir = os.path.join(os.path.dirname(__file__),
    'templates')

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True)


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

    template= jinja_env.get_template("index.html")
    return template.render()

@app.route("/username", methods= ["POST"])
def username():
    username = request.form["username"]
    username_error = "Please provide a username."
    template= jinja_env.get_template("/index.html")

    if not username:
        return template.render(username_error=username_error)

@app.route("/password", methods=["POST"])
def password():
    password = request.form["password"]
    password_error = "Please provide a password."
    template= jinja_env.get_template("/index.html")

    if not password:
        return template.render(password_error=password_error)

@app.route("/verify", methods=["POST"])
def verify():
    verify= request.form["verify"]
    password = request.form["password"]
    verify_error="Passwords do not match."

    if password and verify != password:
        return template.render(verify_error=verify_error)
        


app.run()    
    