import os
import sys
from . import settings as S
from . import users as U

def getAllPlugins():
  for root, dirs, files in os.walk(r'plugins/'):
    return dirs

    
    

def getAllHomeLinks(email):
  ret = []
  for plugin in getAllPlugins():
    
    __import__("plugins."+plugin+"."+plugin)
    pluginInstance = sys.modules["plugins."+plugin+"."+plugin]
    if U.canAccessPlugin(email,getattr(pluginInstance,"privLevel")):  
      ret.append({"name":str.title(plugin),"link":getHomeLink(plugin),"fa_icon":getattr(pluginInstance,"fa_icon") })
  return ret

  
def getHomeLink(name):
  return SettingUrlToMain(name)
  



def SettingUrlToMain(name):
  return S.Urls["plugin"].replace("<name>",name).replace("<functionCall>","main")