from flask import Flask
from flask_sqlalchemy import SQLAlchemy
database = SQLAlchemy()

class Books(database.Model):
     __tablename__ = "Books"
     title =database.Column(database.String, unique=True, nullable = False, primary_key=True)
     author = database.Column(database.String, nullable = False)
     isbn = database.Column(database.String,nullable = False)
     year = database.Column(database.String,nullable = False)