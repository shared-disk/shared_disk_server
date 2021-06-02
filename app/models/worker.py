from app import db

from .credentials import Credentials

from hashlib import md5


class ProfessionType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)


class Worker(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), unique=True)
    email = db.Column(db.String(128), unique=True)
    password_hash = db.Column(db.String(128))

    __profession_type_id = db.Column(db.Integer, db.ForeignKey(ProfessionType.id))
    profession_type = db.relationship(ProfessionType, foreign_keys=__profession_type_id)

    token = db.Column(db.String(128))

    google_auth_state = db.Column(db.String(255))
    __credentials_id = db.Column(db.Integer, db.ForeignKey(Credentials.id))
    credentials = db.relationship(Credentials, foreign_keys=__credentials_id, uselist=False)

    def set_password(self, password):
        bytes_password = bytes(password, encoding='utf-8')
        self.password_hash = md5(bytes_password).hexdigest()

    def check_password(self, password):
        bytes_password = bytes(password, encoding='utf-8')
        return self.password_hash == md5(bytes_password).hexdigest()