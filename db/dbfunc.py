import peewee
from db.dbmodels import *

def get_user_ids():
    query = SpotifyData.select(SpotifyData.user_id)
    ids = [row.user_id for row in query]
    return ids

def get_track_ids(user_id:int):
    query = SpotifyData.select().where(SpotifyData.user_id == user_id)
    if len(query) == 1:
        for row in query:
            return row.track_ids
    else:
        return None

def set_track_ids(user_id:int, track_ids: str):
    query = SpotifyData.update(track_ids=track_ids).where(SpotifyData.user_id == user_id)
    query.execute()




