strHours = input("Enter Hours: ")
strRate = input("Enter Rate: ")
floatHour = float(strHours)
floatRate = float(strRate)
if floatHour > 40 :
  print("Overtime")
  reg = floatRate * floatHour
  over = (floatHour - 40) * (floatRate * 0.5)
  xPay = reg + over
else:
  print("Regular")
  xPay = floatHour * floatRate
print ("Pay:", xPay)