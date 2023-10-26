class cat:
  def __init__(self, name):
    self.name = name

  def selfGreet(self):
    print("Hello", self.name)

  def greet(self, other_cat):
    print("Hello, I am ", self.name, "I see you are also a cool fluffy kitty", other_cat.name, ", let's go together purr, purr, purr at the human, so that they shall give us food.")