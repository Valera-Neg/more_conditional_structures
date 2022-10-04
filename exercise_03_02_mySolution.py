# Refwrite your program using <try> and <except> 
# so that your program handels non-numeric input 
# gracefully by printing a message and exiting the program. 
# The following shows two wxecutions of the program:

# Example:
# Enter Hours: 20 
# Enter Rate: nune 
# Error, please enter numeric input


hours = input("enter num: ")
rate = input("enter your rate: ")
try:
 validNum = int(hours)
 validRate = int(rate)
except:
  print("Error, please enter numeric input")
  quit()
if validNum <= 40: 
  print("Regular")
  print ("Pay", validNum * validRate)
else:  
  print("Overtime")
  print(((validNum - 40) * (validRate * 1.5)) + (40 * validRate))  
 