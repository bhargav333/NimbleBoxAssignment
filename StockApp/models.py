"""Database models."""
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from flask import jsonify, request
from functools import wraps
import jwt
from . import db


class User(UserMixin, db.Model):
	"""User account model."""

	__tablename__ = 'loginUsers'
	id = db.Column(
		db.Integer,
		primary_key=True
	)
	name = db.Column(
		db.String(100),
		nullable=False,
		unique=False
	)
	email = db.Column(
		db.String(40),
		unique=True,
		nullable=False
	)
	password = db.Column(
		db.String(200),
		primary_key=False,
		unique=False,
		nullable=False
	)
	created_on = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )
	last_login = db.Column(
        db.DateTime,
        index=False,
        unique=False,
        nullable=True
    )

	def set_password(self, password):
		"""Create hashed password."""
		self.password = generate_password_hash(password, method='sha256')

	def check_password(self, password):
		"""Check hashed password."""
		return check_password_hash(self.password, password)

	def __repr__(self):
		return '<User {}>'.format(self.username)


def token_required(f):  
    @wraps(f)  
    def decorator(*args, **kwargs):

       token = None 

       if 'x-access-tokens' in request.headers:  
          token = request.headers['x-access-tokens'] 


       if not token:  
          return jsonify({'message': 'a valid token is missing'})   


       try:  
          data = jwt.decode(token, app.config[SECRET_KEY]) 
          current_user = Users.query.filter_by(id=data['id']).first()  
       except:  
          return jsonify({'message': 'token is invalid'})  

          return f(current_user, *args,  **kwargs)  
    return decorator 