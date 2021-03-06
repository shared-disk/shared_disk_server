from app import db


class TaskProtocolTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer)
    worker_id = db.Column(db.Integer)
    start_time = db.Column(db.DATETIME, nullable=True, default=None)
    end_time = db.Column(db.DATETIME, nullable=True, default=None)
