import os
import random
from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
# For tests
from russian_names import RussianNames


# Flask config
app = Flask(__name__)

# Flask SQLAlchemy config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.abspath(os.getcwd())+"/database.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)



# Run by file
if __name__ == "__main__":
    app.debug = True
    app.run()