####################################
#data model of the application
####################################
from gluon import current

db = DAL('sqlite://storage.sqlite')
current.db = db

db.define_table('users',
   Field('username', 'string'),
   Field('password', 'string'))

db.define_table('athlete',
   Field('year', 'integer'),
   Field('name', 'string'),
   Field('score', 'integer'),
   Field('aam', 'integer'),
   format = '%(name)s')
    
#one athlete does many sports (one to many)
db.define_table('sport',
    Field('athlete_id', db.athlete),
    Field('name', 'string'),
    Field('result', 'double'),
    Field('points', 'integer'))


    
