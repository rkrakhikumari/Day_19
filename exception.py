#errors and exceptions
class valueTooHighError (Exception):
    pass
class valueTooSmallError (Exception):
    def __init__(self, message, value):
     self.message = message
     self.value = value

def test_value(x):
   if x> 100:
      raise valueTooHighError("value is too high")
   if x<5 :
      raise valueTooSmallError("value is too small", x)

try:
   test_value(2)
except valueTooHighError as e:
   print(e)
except valueTooSmallError as e:
   print(e.message, e.value)
