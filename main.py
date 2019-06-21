from flask import Flask, request, redirect, render_template

import cgi

app = Flask(__name__)

app.config['DEBUG'] = True 

@app.route("/home", methods =["POST"])
def home():
    username= request.form["username"]
    return render_template("home.html")

@app.route("/", methods= ["POST","GET"])
def index():

    if request.args.get("username_error"):
        username_error= request.args.get("username_error")
    else:
        username_error= ""   

    if request.args.get("password_error"):
        password_error= request.args.get("password_error")
    else:
        password_error= "" 

    if request.args.get("verify_error"):
        verify_error= request.args.get("verify_error")
    else:
        verify_error= ""

    if request.args.get("email_error"):
        email_error= request.args.get("email_error")
    else:
        email_error= ""   

    return render_template("index.html")

@app.route("/", methods= ["POST"])
def username():
    username = request.form["username"]
    if not username or len(username) < 3 or len(username) > 20 or " " in username:
        username_error = "Please provide a valid username."
    else:
        username_error=""
    return redirect("/?username={username}&username_error={username_error}".format(username=username, password_error=password_error))    


@app.route("/", methods=["POST"])
def password():
    password = request.form["password"]
    if not password or len(password) < 3 or len(password) > 20 or " " in password:
        password_error = "Please provide a valid password."
    else:
        password_error=""
    return redirect("/?password={password}&password_error={password_error}".format(password=password, password_error=password_error))    

@app.route("/", methods=["POST"])
def verify_error():
    verify= request.form["verify"]
    password = request.form["password"]
    if password:
        if verify != password:
            verify_error="Passwords do not match."
            return redirect("/?verify_error={verify_error}".format(verify_error=verify_error)) 
        else:
            return redirect("/home.html")       

@app.route("/", methods=["POST"]) 
def email_error():       
    if email and len(email) < 3 or len(email) > 20 or " " in email or email.count("@") != 1 or email.count(".") != 1:
        email_error = "Please provide a valid email."
        return redirect("/?email_error={email_error}".format(email_error=email_error))
    else:
        return redirect("/home.html")

app.run()    
    