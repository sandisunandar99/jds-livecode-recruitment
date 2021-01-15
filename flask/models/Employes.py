from helpers.mysql_alchemy import mysql_alchemy as db

class EmployesModel(db.Model):
    """Model for the users table"""
    __tablename__ = 'employe'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(125))
    email = db.Column(db.String(100))
    alamat = db.Column(db.Text)

    def __init__(self, name, email, alamat):
        self.name = name
        self.email = email
        self.alamat = alamat
