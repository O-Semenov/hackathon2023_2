from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Analytics(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    forklift_id = db.Column(db.Integer, db.ForeignKey('forklift.id'))
    forklift = db.relationship('Forklift', backref='analytics')
    distance = db.Column(db.Float)
    tasks_count = db.Column(db.Integer)
    work_time = db.Column(db.Integer)
    for_order = db.Column(db.Integer)
    with_order = db.Column(db.Integer)
    date = db.Column(db.Date, nullable=False)

    def __init__(self, forklift_id, distance, tasks_count, work_time, for_order, with_order, date):
        self.forklift_id = forklift_id
        self.distance = distance
        self.tasks_count = tasks_count
        self.work_time = work_time
        self.for_order = for_order
        self.with_order = with_order
        self.date = date


class Forklift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_technical_services = db.Column(db.Date)
    status = db.Column(db.String(30))
    position = db.Column(db.String(30))
    task_id = db.Column(db.Integer)

    def __init__(self, date_technical_services, status, position, task_id):
        self.date_technical_services = date_technical_services
        self.status = status
        self.position = position
        self.task_id = task_id

