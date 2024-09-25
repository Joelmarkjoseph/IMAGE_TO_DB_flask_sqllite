from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def db_init(app):
    db.init_app(app)
    
    # Ensure tables are created if they do not exist
    with app.app_context():
        db.create_all() 
