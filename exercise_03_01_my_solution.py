# Rewrite your pay computation to give 
# the employee 1.5 times the hourly rate for 
# hours worked above 40 hours

hours = input("enter num: ")
rate = input("enter your rate: ")
if int(hours) <= 40 : 
  print("Regular")
  print ("Pay", int(hours) * int(rate))
else :
  print("Overtime")
  print(((int(hours) - 40) * (int(rate) * 1.5)) + (40 * int(rate)))


