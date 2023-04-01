def hello():
  return "Hello World"
  
with open("1.output","w") as file:
  file.write(hello())
