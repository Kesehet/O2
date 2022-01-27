name = "adder"
description = "I am a simple addition plugin that calculates addition of two numbers."
fa_icon = "plus"
privLevel = 0


from funcs import settings as S



def main(request):
  return template("")

def mresult(request):
  ans = "<h1> Result: "+str(int(request.form.get("n1"))+int(request.form.get("n2")))+"</h1>"
  return template(ans)

def template(result):
  return '''
  <div class="w3-container">
    <h1>Adder Plugin</h1>
    <form method="post" action="'''+S.Urls["plugin"].replace('<name>',name).replace("<functionCall>","mresult")+'''">
      <input name="n1" type="number">
      <input name="n2" type="number">
      <input type="submit">
    </form>
    '''+result+'''
  </div>
  '''

