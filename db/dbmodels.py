from peewee import *

database = SqliteDatabase('db/userdata.db')

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class SpotifyData(BaseModel):
    genres = TextField(null=True)
    track_ids = TextField(null=True)
    user_id = IntegerField(null=True)

    class Meta:
        table_name = 'SpotifyData'
        primary_key = False

