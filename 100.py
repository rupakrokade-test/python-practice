name = raw_input("Kindly enter your name: ")
age = int(raw_input("Kindly enter your age in years to know in which year you will turn 100: "))
year=2016+(100-age)
if age<100:
  print(name, " will turn 100 in the year ", year)
else:
  print("Congratulations", name, "Your age is already above 100")
