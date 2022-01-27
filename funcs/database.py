from replit import db
from . import settings as S
from . import logger as Log




def replitGet(key):
  if S.databaseType == "replit":
    Log.writeLog("Database", "Update","Fetched "+key+ " From DB")
    return db[key]
  else:
    Log.writeLog("Database","Error","Incorrect database in settings....")



def replitSet(key,value):
  if S.databaseType == "replit":
    Log.writeLog("Database","Update","Inserted value: "+value+" at key: "+key+ " From DB")
    db[key] = value
  else:
    Log.writeLog("Database","Error","Incorrect database in settings....")



