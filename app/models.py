from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime
from . import db

@login_manager.user_loader
def load_user(user_id):
    
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    
    __tablename__ ='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    posts = db.relationship("Post", backref="user", lazy = "dynamic")
    comment = db.relationship("Comments", backref="user", lazy = "dynamic")
    vote = db.relationship("Votes", backref="user", lazy = "dynamic")
    
    
    @property
    def password(self):
        raise AttributeError('You can not read the password Attribute')


    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)


    def __repr__(self):
        return f'User {self.username}'
    
    
class PostCategory(db.Model):
    
    __tablename__ = 'categories'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))


    def save_category(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_categories(cls):
        categories = PostCategory.query.all()
        return categories
  
class Post(db.Model):
    
    __tablename__ = 'posts'

    id = db.Column(db.Integer,primary_key = True)
    content = db.Column(db.String())
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    comment = db.relationship("Comments", backref="posts", lazy = "dynamic")
    vote = db.relationship("Votes", backref="posts", lazy = "dynamic")



    def save_post(self):
        """
        Save the posts
        """
        db.session.add(self)
        db.session.commit()

    def delete_post(self):
        db.session.delete(self)
        db.session.commit()

    # display pitches

    def get_posts(id):
        posts = Post.query.filter_by(category_id=id).all()
        return posts

class Comments(db.Model):
    
     __tablename__ = 'comments'     

    
     id = db.Column(db. Integer, primary_key=True)
     opinion = db.Column(db.String(255))
     time_posted = db.Column(db.DateTime, default=datetime.utcnow)
     user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
     posts_id = db.Column(db.Integer, db.ForeignKey("posts.id"))


     def save_comment(self):
        """
        Save the Comments/comments per post
        """
        db.session.add(self)
        db.session.commit()
        
     @classmethod
     def delete_comment(cls, id):
        gone = Comment.query.filter_by(id = id).first()
        db.session.delete(gone)
        db.session.commit()    

     @classmethod
     def get_comments(self, id):
        comment = Comments.query.order_by(Comments.time_posted.desc()).filter_by(posts_id=id).all()
        return comment

class Votes(db.Model):
    """
    class to model votes
    """
    __tablename__='votes'

    id = db.Column(db. Integer, primary_key=True)
    vote = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    posts_id = db.Column(db.Integer, db.ForeignKey("posts.id"))

    def save_vote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_votes(cls,user_id,pitches_id):
        votes = Votes.query.filter_by(user_id=user_id, posts_id=posts_id).all()
        return votes

    def __repr__(self):
        return f'{self.vote}:{self.user_id}:{self.posts_id}'   
    
class Quote:
    """
    Blueprint class for quotes consumed from API
    """
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote

class Subscribers(db.Model):
    __tablename__ = "subscribers"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255), unique = True, index = True)
             
   
    
    





