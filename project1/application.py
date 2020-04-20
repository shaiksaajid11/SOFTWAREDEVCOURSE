import os,sys   
import time
from flask import Flask, render_template, request
from flask_session import Session
from models import *
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__,static_url_path="/static")

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#Session(app)
database.init_app(app)
with app.app_context():
    database.create_all()
# Set up database
#engine = create_engine(os.getenv("DATABASE_URL"))
#db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")


# @app.route("/login",methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         uname = request.form["uname"]
#         passw = request.form["passw"]
        
#         login = user.query.filter_by(username=uname, password=passw).first()
#         if login is not None:
#             return redirect(url_for("index"))
#     return render_template("login.html")

@app.route("/user_details", methods=["POST", "GET"])
def user_details():
    Username = request.form.get("username")
    Email = request.form.get("email")
    Password = request.form.get("password")
    Time = time.ctime(time.time())
    try:
        var = USERS(username = Username, email = Email, password = Password, time=Time)
        database.session.add(var)
        database.session.commit()
    except ValueError:
        return render_template("error.html")
    
    return render_template("user_details.html", username=Username, email=Email)

@app.route("/admin")
def admin():
    Admin = USERS.query.all()
    return render_template("admin.html", Admin=Admin)