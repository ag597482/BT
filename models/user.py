from enums.gender import Gender
from sqlalchemy import Column, Integer, String

class Person:

  __tablename__ = 'users'

  id = Column(Integer, primary_key=True)
  name = Column(String(150))
  age = Column(Integer)
  gender = Column(String(150))
  email = Column(String(150))

  def __init__(self, name, email, age, gender):
    self.name = name
    self.gender = gender
    self.email = email
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

  def __repr__(self):
        return str(vars(self))

#   def getAge(self):
#     return self.age

#   def getGender(self):
#     return self.gender



