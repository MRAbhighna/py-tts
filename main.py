import pyttsx3 as ts # type: ignore (For Visual Studio)

e = ts.init()

e.setProperty('rate', 150)
e.setProperty('volume', 1)

vI = int(input("Enter voice ID (Enter for DEFUALT): "))

v = e.getProperty('voices')
e.setProperty('voice', v[vI].id)

t = input("Enter text to speak: ")

e.say(t)
e.runAndWait()