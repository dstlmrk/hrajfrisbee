from __main__ import db
#from app import db

class Prospect(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), nullable=False)
    gender = db.Column(db.String(20), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    for_event = db.Column(db.String(120), nullable=False)


    def __repr__(self):
        return '<Prospect %r>' % self.name

    def to_dict(self):
        return {
            'email': self.email,
            'age': self.age,
            'gender': self.gender,
            'name': self.name,
            'for_event': self.for_event
        }


