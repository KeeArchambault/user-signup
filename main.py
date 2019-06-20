from flask import Flask, request, redirect

import os

import jinja2

app = Flask(__name__)

app.config['DEBUG'] = True   


template_dir = os.path.join(os.path.dirname(__file__),
    'templates')

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

 index_form="""<form action="/">
            <label for="username">Username:</label>
            <input type="text" name="username" >{0}</input>
        </form>

         <form action="/password">
            <label for="password">Password:</label>
            <input type="text" name="password">{1}</input>
        </form>

        <form action="/verify">
            <label for="verify">Verify Password:</label>
            <input type="text" name="verify"></input>
        </form>

        <form action="/email">
            <label for="email">Email:</label>
            <input type="text" name="email"></input>
        </form>
    </body>

"""

@app.route("/")
def index():
    template= jinja_env.get_template("index.html")
    return template.render().format()

@app.route("/username", methods= ["post"])
def username():
    username = request.form["username"]
    if not "username":
        username_error = "Please provide a username."
        template= jinja_env.get_template("index.html")
        return redirect("/?username_error={0}".format(username_error))

@app.route("/password", methods=["post"])
def password():
    password = request.form["password"]
    if not "password":
        password_error = "Please provide a password."
        template= jinja_env.get_template("index.html")
        return redirect("/?password_error={0}".format(password_error))        

app.run()    
    