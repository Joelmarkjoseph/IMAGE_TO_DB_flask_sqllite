from flask import Flask, request
from werkzeug.utils import secure_filename
from db import db, db_init
from models import Img 

app = Flask(__name__)

# Correct database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///img.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db_init(app)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/upload", methods=['POST'])
def upload():
    # Check if the 'pic' file is in the request
    if 'pic' not in request.files:
        return "No Pic Uploaded", 400

    pic = request.files['pic']

    if not pic.filename:
        return "No Pic Uploaded", 400
    
    filename = secure_filename(pic.filename)
    mimetype = pic.mimetype
    
    # Ensure that the file has content and mimetype is not empty
    if not filename or not mimetype:
        return "Bad upload", 400

    try:
        # Create an Img object and save it to the database
        img = Img(img=pic.read(), mimetype=mimetype, name=filename)
        db.session.add(img)
        db.session.commit()
    except Exception as e:
        # Rollback in case of error and provide feedback
        db.session.rollback()
        return f"An error occurred: {str(e)}", 500

    return "Image has been Uploaded"

if __name__ == "__main__":
    app.run(debug=True)
