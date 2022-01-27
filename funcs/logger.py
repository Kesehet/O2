''' 
Log Types
  Error
  DB Update
  Login Update


'''




def writeLog(event,logType,error):
  print(event,logType+":",error)
