from service import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(120), unique=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"user('{self.username}', '{self.email}')"


class Article(db.Model):
    __tablename__ = "articles"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    content = db.Column(db.Text())
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_show = db.Column(db.Boolean(), default=True)
    likes = db.Column(db.Integer(), default=0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)

    def user(self):
        return User.query.get(user_id)

    def __repr__(self):
        return f"article('{self.title}')"


class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text())
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    is_show = db.Column(db.Boolean(), default=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    person = db.Column(db.String(256))
    def __repr__(self):
        return f"article('{self.title}')"


class BoxItem(db.Model):
    __tablename__ = "box_items"
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(256))
    name = db.Column(db.String(256))
    profile = db.Column(db.Integer)
    phone_number = db.Column(db.String(256))
    objet = db.Column(db.String(256))
    message = db.Column(db.Text())
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def files(self):
        return Document.query.get(self.id)

class Document(db.Model):
    __tablename__ = "documents"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    description = db.Column(db.Text())
    filename = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    box_item_id = db.Column(db.Integer, db.ForeignKey(
        'box_items.id'), nullable=False)

class UsefulData(db.Model):
    __tablename__ = "useful_data"
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(256))
    value = db.Column(db.Text())
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)