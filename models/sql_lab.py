from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Code(db.Model):
    __tablename__ = "code"
    
    code = db.Column()
