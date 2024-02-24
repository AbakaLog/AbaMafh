import random

score = 0
devPass = "MonkeyMoment32"
teacherPass = "TodayITeach64"
teacherCode = "5H"
devMode = False
isValid = True

#Functions
def PlayerType():
  playerSelect = input("Are you a teacher? y/n ")
  if playerSelect == "y":
    passwordChecker = input("No one is supposed to be able to access this! To prevent terrible things to happen, enter the teacher password: ")
    if passwordChecker == teacherPass:
      TeacherHistory = input("Please enter your class code (e.g. 5H) ")
      if TeacherHistory == teacherCode:
        TeacherPath = input("Hello, " + TeacherHistory + "! \n \n 1) Generate a code \n 2) Preview as student \n \n What do yo choose? ")
      print("---------------------------")
    else:
      print("Since you have guessed incorrectly, your teacher has been notified. Maybe try not to hack next time ¯\_(ツ)_/¯")
      print("---------------------------")
  elif playerSelect == "dev":
    passwordCheckerDev = input("No one is supposed to be able to access this! To prevent terrible things to happen, enter the developer password: ")
    if passwordCheckerDev == devPass:
      print("codin time")
      print("---------------------------")
      devMode = True
    else:
      print("Since you have guessed incorrectly, your teacher has been notified. Maybe try not to hack next time ¯\_(ツ)_/¯")
  else:
    print("mafh time")
    print("---------------------------")

def codeChecker():
  if isValid == True:
    print("Now entering:", code)
  else:
    print("I think you typed it wrong. The code is CASE SENSITIVE, so do worry about capitalization. Please restart the program :D")
    quit()

def makeQuestion():
  while True:
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    correctAnswer = num1 * num2
    if devMode == True:
      print("correctAnswer =", correctAnswer)
    userAnswer = int(input("What is " + str(num1) + " * " + str(num2) + "? "))
    if userAnswer == correctAnswer:
      print("Correct! You have gotten 1 point")
      print("---------------------------")
    else:
      print("Opps! You have gotten the problem wrong. You got", score, "points!")
      print("The correct answer was", str(correctAnswer))
      quit()

def readCode():
  first = code[:2]
  second = code[2:4]
  third = code[4:]
  print(first, second, third)


name = input("Hello! What is your name? ")
print("Welcome to AbaMafh", name)
print("---------------------------")
PlayerType()
code = input("Please enter the code given on the screen: ")
codeChecker()
readCode()
makeQuestion()
