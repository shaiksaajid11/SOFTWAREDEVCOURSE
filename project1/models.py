from flask import Flask
from flask_sqlalchemy import SQLAlchemy
database = SQLAlchemy()

class USERS(database.Model):
   
   __tablename__ = "USER"
   username =database.Column(database.String, unique=True, nullable = False, primary_key=True)
   email = database.Column(database.String, unique=True)
   password = database.Column(database.String,nullable = False)
   time = database.Column(database.DateTime,nullable = False)