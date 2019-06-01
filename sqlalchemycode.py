import sqlalchemy as db
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import aliased
from sqlalchemy import *
from sqlalchemy import func
from sqlalchemy.orm import mapper 
from sqlalchemy.ext.declarative import declarative_base
import pandas as pd
sql1='select * from tags limit 10'
engine= create_engine('mysql+mysqlconnector://root:tiger@localhost:3306/sqlalchemy_mysql',echo=True)
connection = engine.connect()
result=engine.execute(sql1)
print(result.fetchall())

''' In ORM the model we create is the class which containts the database table structure '''

# storing data in dataframe
print('\n--- storing data in pandas df ---')
df=pd.read_sql_query(sql1,engine)
print(df.head())

# Classical mapping using ORM
'''creating metadata using ORM'''
metadata = MetaData()

'''creating object used as a table in ORM '''
tags=Table('tags',metadata,
    Column('Id', Integer, primary_key=True),
    Column('Count', Integer),
    Column('ExcerptPostId', Integer),
    Column('TagName', String(255)),
    Column('WikiPostId', Integer))

''' creating class with same name as table '''
class Tags(object):
    def __init__(self,Count, ExcerptPostId, TagName, WikiPostId):
        self.Count=Count
        self.ExcerptPostId=ExcerptPostId
        self.TagName=TagName
        self.WikiPostId=WikiPostId

''' creating mapper to map class and table '''
tags_mapper=mapper(Tags,tags)

''' Using select method of tags object '''
sel_tags=tags.select(Tags.Count > 1000)
print('\n ---sql statement prepared :--- \n',sel_tags)
print('\n ---Data from table using ORM:---')
print(engine.execute(sel_tags).fetchall())



# Declarative base using ORM 
'''
1) import declarative base class using the below  
   from sqlalchemy.ext.declarative import declarative_base
2) create object of declarative_base class 
3) Define a model 
4) Query data
'''

''' the below function is used to create session for query execution '''
def sqlsession():
    session = sessionmaker()
    session.configure(bind=engine)
    my_session = session()
    return my_session

''' Base object created '''
Base= declarative_base()

''' creating model '''
'''create a class with the same name as table and inherit the base class'''
class Users(Base):
    __tablename__='users'
    Id = Column(db.Integer, primary_key = True)
    Reputation = db.Column(db.Integer)     
    CreationDate = db.Column(db.DateTime) 
    DisplayName = db.Column(db.String(255))
    LastAccessDate = db.Column(db.DateTime) 
    WebsiteUrl = db.Column(db.String(255))
    Location = db.Column(db.String(4096))
    AboutMe = db.Column(db.String(4096))
    Views = db.Column(db.Integer) 
    UpVotes = db.Column(db.Integer) 
    DownVotes = db.Column(db.Integer) 
    AccountId = db.Column(db.Integer)       
''' the below method is used for better representation of the details '''
def __repr__(self):
    return "<{0} Id: {1} – Name: {2}>".format(self.__class__.__name__, self.Id, self.DisplayName) 


class Posts(Base):
    __tablename__ = 'posts'
    Id = db.Column(db.Integer(), primary_key=True) 
    Title = db.Column(db.String(255), nullable=False)
    ViewCount = db.Column(db.Integer(), default=1000)  
    PostTypeId = db.Column(db.Integer(), default=True)
    OwnerUserId = db.Column(db.Integer())
    ''' The below keyword __table_args__ is used to extend Model Posts for self join '''
    __table_args__ = {'extend_existing': True}
    AnswerCount = db.Column(db.Integer)
    ParentId = db.Column(db.Integer)
    Score = db.Column(db.Integer)

''' querying data '''
print('\n --- querying data ---')
mysession=sqlsession()
print(mysession.query(Users.DisplayName).first()) # getting display name of first record
''' the below can be used to loop through records with column names 
for i in mysession.query(Users):
    print(i.DisplayName)
'''

# filter condition in a query
print('\n ---running filter conditions:---')
print(mysession.query(Users.DisplayName).filter(Users.DisplayName=='Community').all())

# clause statement used in a query
print('\n ---running clause statements:---')
print(mysession.query(Users.DisplayName).filter(Users.DisplayName.like ('%Com%')).all())

# using function generator to access the function in database
''' from sqlalchemy import func and by doing dir(func) we can see all the functions inside func module '''
print(mysession.query(func.sum(Tags.Count)).scalar())
print(mysession.query(func.sum(Tags.Count)).filter(Users.DisplayName.like('%Com%')).all())

'''using operators and labels'''
print('\n --operators and ordering--')
print(mysession.query(Users.DisplayName, db.cast((Users.UpVotes - Users.DownVotes), db.Numeric(12, 2)).label('vote_difference'), Users.UpVotes, Users.DownVotes).order_by(db.desc('vote_difference')).limit(5).all())

''' conjunctions - and_,or_,not_ '''
print('\n---conjunctions:and_,or_,not_---')
print(mysession.query(Users.DisplayName).filter(db.or_(Users.DisplayName == 'Community', Users.DownVotes.between(300,600))).all())

''' Joins '''
print('\n ---Implicit Joins--- ')
print(mysession.query(Users.DisplayName, Posts.Title).filter(Users.Id == Posts.OwnerUserId).limit(2).all())

print('\n ---Explicit Joins--- ')
print(mysession.query(Users.DisplayName, Posts.Title).join(Posts, Users.Id == Posts.OwnerUserId).limit(2).all())

''' for self join we need to extend the model (here : Posts)
and create model alias (like table alias) so that we can join the same table.
For this we use the below 
from sqlalchemy.orm import aliased
Questions = aliased(Posts) '''

print('\n ---Self joins---')
Questions = aliased(Posts)
print(mysession.query(Posts.Id, Questions.Id, Posts.ViewCount, Posts.Score, Questions.Score)\
.filter(Posts.Id == Questions.ParentId).order_by(db.desc(Posts.ViewCount)).limit(10).all())


''' The below code is for update and delete using sql alchemy 

Manipulating Your Database

- Updating Data Using SQL
# From Python
>>> engine = db.create_engine('sqlite:///sqlalchemy_sqlite.db')
>>> connection = engine.connect()
>>> engine.execute('select * from post where Id=1').fetchone()
>>> engine.execute('select ViewCount from post where Id=1').fetchone()
>>> engine.execute('Update post set ViewCount = 0 where Id = 1')
>>> engine.execute('select ViewCount from post where Id=1').fetchone()
>>> engine.execute('select * from post where Id=1').fetchone()


- Updating Data Using Update
# From Python
***** steps from the previous module that are required
>>> from sqlalchemy.orm import sessionmaker
>>> from sqlalchemy.orm import relationship
>>> from sqlalchemy.schema import ForeignKey
>>> from sqlalchemy.ext.declarative import declarative_base
>>> session = sessionmaker()
>>> session.configure(bind=engine)
>>> my_session = session()
>>> Base = declarative_base()
>>> class User(Base):
...     __tablename__ = 'user'
...     Id = db.Column(db.Integer(), primary_key=True)
...     Name = db.Column(db.String())
>>> class Post(Base):    
...     __tablename__ = 'post'
...     Id = db.Column(db.Integer(), primary_key=True)
...     Title = db.Column(db.String(255), nullable=False)
...     ViewCount = db.Column(db.Integer(), default=1000)
...     Question = db.Column(db.Boolean(), default=True)
...     OwnerUserId = db.Column(db.Integer(), ForeignKey('user.Id'), nullable=False)
...     User = relationship('User', backref='post')
*****


>>> query = db.update(Post).where(Post.Id == 1).values(ViewCount=1)
>>> result = connection.execute(query)
>>> post_query = my_session.query(Post).filter(Post.Id == 1)
>>> post_query.one.Id
>>> post_query.one.ViewCount
>>> post_query.one.Title

# From Python
>>> query = db.update(Post).values(ViewCount = Post.ViewCount + 50)
>>> result = connection.execute(query)

- Updating an Object
# From Python
>>> my_post = my_session.query(Post).filter(Post.Id == 1).one()
>>> my_post.Title
>>> my_post.Title = 'Modified Question'
>>> my_session.dirty
>>> my_session.commit()

- Correlated Updates
# From SQLite3
sqlite> select ViewCount from post;
sqlite> select avg(ViewCount) from post;


# From Python
>>> avg_views = db.select([db.func.avg(Post.ViewCount).label('Average_Views')])
>>> query = db.update(Post).values(ViewCount=avg_views)
>>> result = connection.execute(query)
>>> result.rowcount

- Deleting a Record
# From Python
>>> my_session.query(Post.Id).all()
>>> first_post = my_session.query(Post).first()
>>> first_post.Id
>>> my_session.delete(first_post) 
>>> my_session.query(Post.Id).all()

# From Python
>>> my_session.commit()

- Deleting Multiple Records
# From Python
>>> my_session.query(Post.Id).all()
>>> my_session.query(Post).filter(Post.Id > 2).delete()

# From Python
>>> my_session.commit()

# From Python
>>> my_session.query(Post.Id).all()


- Deleting a Table
# From Python
>>> metadata = db.MetaData() 
>>> metadata.reflect(bind=engine)
>>> metadata.tables.keys()
>>> post_table = metadata.tables['post']
>>> post_table
>>> post_table.drop(bind=engine)

'''