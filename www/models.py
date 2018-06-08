#coding=utf-8

from transwarp.orm import Model,StringField,FloatField,TextField,BooleanField
from transwarp.db import next_id

import time,uuid

__author__ = 'Lisl-thorn'



class User(Model):
	__table__ = 'users'

	id = StringField(primary_key=True,default=next_id,ddl='varchar(50)')
	email = StringField(updatable=False,ddl='varchar(50)')
	password = StringField(ddl='varchar(50)')
	admin = BooleanField()
	name = StringField(ddl='varchar(50)')
	image = StringField(ddl='varchar(500)')
	created_at = FloatField(updatable=False,default=time.time)


class Blog(Model):
	__table__ = 'blog'

	id = StringField(primary_key=True,default=next_id,ddl='varchar(50)')
	user_id = StringField(updatable=False,ddl='varchar(50)')
	user_name = StringField(ddl='varchar(50)')
	user_image = StringField(ddl='varchar(500)')
	name = StringField(ddl='varchar(50)')
	summary = StringField(ddl='varchar(200)')
	content = TextField()
	created_at = FloatField(updatable=False,default=time.time)				


class Comment(Model):
	__table__ = 'comments'

	id = StringField(primary_key=True,default=next_id,ddl='varchar(50)')
	blog_id = StringField(updatable=False,ddl='varchar(50)')
	user_id = StringField(updatable=False,ddl='varchar(50)')
	user_name = StringField(ddl='varchar(50)')
	user_image = StringField(ddl='varchar(500)')
	content = TextField()
	created_at = FloatField(updatable=False,default=time.time)
		