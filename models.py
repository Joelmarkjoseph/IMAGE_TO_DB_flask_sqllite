from db import db 

class Img(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.LargeBinary, nullable=False)  # Changed to LargeBinary to store image data
    name = db.Column(db.String(300), nullable=False)  # Use String for file names with a reasonable length
    mimetype = db.Column(db.String(50), nullable=False)  # Use String for mimetype to limit the data length
