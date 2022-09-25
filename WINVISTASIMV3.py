from cmu_graphics import *

# windows vista sim full #
# the user must click on password promts or icons to log in or use programs #
##logon screen##
#logon screen background#
app.background = gradient('aquaMarine', 'turquoise', 'skyBlue', 'skyBlue', 'limeGreen', 'lime', start='top')
loginstructions = Label('click on the password prompt to log on', 200, 350)
#profile image and password prompt#
user = Image('https://yt3.ggpht.com/ytc/AKedOLReRkhT4TQh3cfXghjykPHXQ_-1kDXpJGwDXSHmfA=s900-c-k-c0x00ffffff-no-rj', 150, 120)
user.width = 100
user.height = 100
app.name = app.getTextInput('set username')
username = Label(app.name, 200, 230, size=15, bold=True)
passprompt = Rect(150, 240, 100, 15, fill='white', border='black', borderWidth = 1)
wrong = Label('Wrong Password', 200, 270, size=20, bold=True, italic=True)
wrong.visible = False
#logon sound#
logonsound = Sound('https://ia803406.us.archive.org/13/items/soundcloud-277989610/277989610.mp3')
logoff = Sound('https://archive.org/download/windows_7_shutdown_sound/windows_7_shut_down.mp3')
##desktop##
startButton = Image('https://www.kindpng.com/picc/m/343-3432040_windows-vista-logo-png-logo-windows-media-center.png', 0, 350)
startButton.width = 50
startButton.height = 50
taskbar = Group(Rect(0, 350, 400, 50), startButton)
taskbar.visible = False
deskinstructions = Label('click on an icon to open the program', 200, 275)
desk = Label('click on an icon again to close the program', 200, 300)
pslabel = Label("p.s. the start button changes your username", 200, 325)
deskinstructions.visible = False
desk.visible = False
pslabel.visible = False
##IE app##
ieLogo = Image('https://d1yjjnpx0p53s8.cloudfront.net/styles/logo-thumbnail/s3/0025/0402/brand.gif?itok=XzBrKPj2', 25, 25)
ieLogo.width = 50
ieLogo.height = 50
ieLogo.visible = False
#IE window#
ieWindow = Group(Rect(100, 50, 200, 225, fill='white'), Label('Internet Explorer', 200, 60),
Label('Not Connected To Internet', 200, 100))
ieWindow.visible = False
##aim app##
#draws aim icon#
aimLogo = Image("https://media.gannett-cdn.com/29906170001/29906170001_5600284871001_5600252232001-vs.jpg?pubId=29906170001&width=660&height=371&format=pjpg&auto=webp", 25, 100)
aimLogo.width = 50
aimLogo.height = 50
aimLogo.visible = False
#draws aim window#
textBox = Rect(100, 250, 200, 25, fill='skyBlue')
textBox.visible = False
textIn = Label('Enter Message Here', 200, 262, size=10)
textIn.visible = False
aimWindow = Group(Rect(100, 50, 200, 225, fill='white'), textBox, textIn, Label("AIM", 200, 60)) 
aimWindow.visible= False
#aim message#
def aimMessage(fill, x, y, message):
    messagebox = Group(Rect(x, y, 185, 50, fill=fill),
    Label(message, 200, 205, size=10), 
    Label(app.name, 140, 190))
    aimWindow.add(messagebox)
    
#onMousePress check#
def onMousePress(x, y):
    if(passprompt.hits(x, y)):
        app.password = app.getTextInput('enter 1234 to log in')
        if(app.password == '1234'):
            logonsound.play()
            wrong.visible = False
            loginstructions.visible = False
            user.visible = False
            username.visible = False
            passprompt.visible = False
            taskbar.visible = True
            ieLogo.visible = True
            aimLogo.visible = True
            deskinstructions.visible = True
            desk.visible = True
            pslabel.visible = True
        else:
            wrong.visible = True
    if(startButton.hits(x, y)):
        app.name = app.getTextInput('enter new username')
    if((aimLogo.hits(x, y)) and (aimWindow.visible == False)):
        aimWindow.visible = True
    elif((aimLogo.hits(x, y)) and (aimWindow.visible == True)):
        aimWindow.visible = False
    if((aimWindow.hits(x, y)) and (aimWindow.visible == True)):
        app.message = app.getTextInput('message')
        aimMessage('skyBlue', 110, 180, app.message)
    if((ieLogo.hits(x, y)) and (ieWindow.visible == False)):
        ieWindow.visible = True
    elif((ieLogo.hits(x, y)) and (ieWindow.visible == True)):
        ieWindow.visible = False
    if((x >= 390) and (y <= 10)):
        logoff.play()
        username.value = app.name
        loginstructions.visible = True
        user.visible = True
        username.visible = True
        passprompt.visible = True
        taskbar.visible = False
        ieLogo.visible = False
        aimLogo.visible = False
        deskinstructions.visible = False
        desk.visible = False
        pslabel.visible = False

cmu_graphics.run()