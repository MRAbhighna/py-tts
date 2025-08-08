import pyttsx3 as ts

e = ts.init()

e.setProperty('rate', 150)
e.setProperty('volume', 1)

vI = input("Enter voice ID (Enter for DEFAULT): ")

if vI != '':
    vI = int(vI)
else:
    vI = 0

v = e.getProperty('voices')
e.setProperty('voice', v[vI].id) # type: ignore (For Visual Studio)

t = input("Enter text to speak: ")

e.say(t)
e.runAndWait()