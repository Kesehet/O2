from . import settings as S
from . import plugins as P
from flask import render_template

def the404page(email,redirect=False):
  addHtml = ""
  if redirect:
    addHtml += "<script>window.location.href = '"+S.Urls["login"]+"'</script>"
  return render_template("dashboard.html",data = {
      "Settings":S,
      "pluginLinks":P.getAllHomeLinks(email),
      "pluginHTML":"<h1>404</h1>"+addHtml,
      "pageTitle":" | "+ "404",
      })


def theDashboardHomePage(email):
  return render_template("dashboard.html",data = {
      "Settings":S,
      "pluginLinks":P.getAllHomeLinks(email),
      "pluginHTML":'''
        <div class="w3-container">
          <h1>Welcome To The O2</h1>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
          <br>
        </div>
      ''',
      "pageTitle":" | "+ "Home",
      })
