from . import login as L


Users = [
  {
    "email":"hamood.siddiqui@gmail.com",
    "level":0
  }
]


def getAllUsers():
  return Users


def canAccessPlugin(email,pluginLevel):
  for user in getAllUsers():
    if user["email"] == email and user["level"] >= pluginLevel:
      return 1
  return 0


def getUserLevelFromRequest(request):
  email = L.isLoggedIn(request)[1]
  for user in getAllUsers():
    if email == user["email"]:
      return user["level"]
  return None
  