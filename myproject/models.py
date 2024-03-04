###############################
####### DATABASE MODELS #######
###############################

# Set up db inside the __init__.py in myproject folder
from myproject import db

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)

    # One to One: Puppy can have only one Owner
    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return "Puppy name is "+self.name+" and owner is "+self.owner.name
        else:
            return "Puppy name is "+self.name +" and has no owner assigned yet"


class Owner(db.Model):

    __tablename__ ="owners"
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer, db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return "Owner name:" + self.name