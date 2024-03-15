def  outer_function():
  num =20
  def inner_function():
    global num
    num = 7
  print("before  calling inner_function",num)
  inner_function()
  print("after calling inner_function",num)
outer_function()
print("outside  both fucntion ",num)
