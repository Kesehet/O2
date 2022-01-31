name = "file_manager"
description = "I am a simple file_manager plugin that lets you get file on server."
fa_icon = "folder"
privLevel = 0
publicLinks = [
  "main",
  "showFile"
]
import os

pluginSettings = {"showHiddenFiles":False,"base":"/home/runner/O2/"}

def main(request):
  showDir = request.args.get("dir")
  if showDir == None:
    showDir = ""
  if (showDir.find("/funcs") >= 0 or showDir.find("/templates") >= 0 )and U.getUserLevelFromRequest(request) < 1:
    return "ACCESS DENIED"
  return template(showDir)

def showFile(request):
  ret = ""
  urlFile = request.args.get("file")
  breakName = urlFile.split(".")
  fileType = breakName[len(breakName)-1]
  if urlFile.endswith(".py"):
    fileType = "python"
  if urlFile.endswith(".js"):
    fileType = "javascript"
  
  filename = pluginSettings["base"]+urlFile
  file = open(filename,'r')
  ret = file.read()
  #ret = ret.replace("\n","<br>")
  
  file.close()
  return template(request.args.get("dir"))+'''
  <script src="https://pagecdn.io/lib/ace/1.4.13/ace.js" crossorigin="anonymous" integrity="sha256-bS3VAQePcKYmsvI+8BdG2QJAVb9FbiZLgM5vK2/+TcM=" ></script>
  <div id="id01" class="w3-modal">
    <div class="w3-modal-content">
      <div class="w3-container" >
        <span onclick="document.getElementById('id01').style.display='none'" class="w3-button w3-red w3-display-topright">&times;</span>
        <div class="w3-container" style="margin-top:50px;">
        <div id="editor" class="w3-col  s10 m10 l12 " style="min-height:60vh;">'''+ret+'''</div>
        </div>
      </div>
    </div>
  </div>
  <script>
  document.getElementById('id01').style.display='block';
  </script>
  <script>
    var editor = ace.edit("editor");
    editor.setTheme("ace/theme/monokai");
    editor.session.setMode("ace/mode/'''+fileType+'''");
</script>
  '''


from funcs import users as U

def template(showDir):
  if showDir == None:
    showDir = ""
  print(showDir)
  
  foldersHTML = getAllFoldersTemplate(showDir)
  filesHTML = getAllFilesTemplate(showDir)

  return   '''
  <div class="w3-container"> 
    <h1>'''+str.title(name.replace("_"," "))+'''</h1>
    <div class="w3-card w3-margin w3-white">
      '''+homeButton()+foldersHTML+filesHTML+'''
    </div>
  </div>'''

def folderRow(name,root):
  root = root.replace( pluginSettings["base"],"")
  return ''' 
    <div class="w3-container  w3-padding-large w3-text-teal w3-hover-teal" onclick="window.location.href='main?dir='''+str(root)+"/"+str(name)+''''">  
      <div class="w3-col l1 m1 s1">
      <i class="fa fa-folder fa-fw"></i>
      </div>
      <div class="w3-col l6 m6 s3">
      '''+name+'''
      </div>
    </div>
  '''
def homeButton():
  return ''' 
    <div class="w3-container  w3-padding-large w3-text-red w3-hover-red" onclick="window.location.href='main?dir='''+''''">  
      <div class="w3-col l1 m1 s1">
      <i class="fa fa-home fa-fw"></i>
      </div>
      <div class="w3-col l6 m6 s3">
      Home
      </div>
    </div>
  '''
def fileRow(name,root):
  root = root.replace( pluginSettings["base"],"")
  return ''' 
  <div class="w3-container w3-padding-large w3-text-black w3-hover-black" onclick="window.location.href='showFile?file='''+str(root)+"/"+str(name)+''''">  
    <div class="w3-col l1 m1 s1">
    <i class="fa fa-file fa-fw"></i>
    </div>
    <div class="w3-col l6 m6 s3">
    '''+name+'''
    </div>
    </div>
  '''

def getAllFilesTemplate(baseDir):
  filesHTML = ""
  x = listAllFiles(baseDir)
  for folder in x[1]:
    if not pluginSettings["showHiddenFiles"] and folder[0] == ".":
      continue
    filesHTML += fileRow(folder,x[2])
  return filesHTML

def getAllFoldersTemplate(baseDir):
  foldersHTML = ""
  x = listAllFiles(baseDir)
  for folder in x[0]:
    if not pluginSettings["showHiddenFiles"] and folder[0] == ".":
      continue
    foldersHTML += folderRow(folder,x[2])
  return foldersHTML

def listAllFiles(folderList):
  base = pluginSettings["base"]
  for root, dirs, files in os.walk(base+folderList):
    return [dirs,files,root]
  