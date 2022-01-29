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




