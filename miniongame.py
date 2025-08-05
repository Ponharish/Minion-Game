
#Mini Bossah Game

from tkinter import *
from tkinter import messagebox

import os
import pygame
import random
import sys

def getFilePath(path):
    if getattr(sys, 'frozen', False):
        return os.path.join(sys._MEIPASS, path)
    else:
        return os.path.join(os.path.dirname(__file__), path)

root=Tk()
root.title('Minion Game')
root.geometry('1280x800')
#root.configure(bg='#D648D7')

def on_closing():
    global scorenow
    global highscorenow
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        
        f=open(getFilePath('highscore.txt'),'w')
        f.write(str(highscorenow))
        f.close()
        pygame.mixer.music.stop()
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)


titleframe=Frame(root)
titleframe.pack(side=TOP)

titlelabel=Label(titleframe,text='MINION GAME', fg='blue',font= "applecherry 35")
titlelabel.pack()

scoreframe=Frame(root)
scoreframe.pack(side=TOP,fill='x', expand=False)
scorelabel=Label(scoreframe,text='Score: ', fg='green',font= "applecherry 18")
scorelabel.pack(side=LEFT)

hiscoreframe=Frame(root)
hiscoreframe.pack(side=TOP,fill='x', expand=False)
hiscorelabel=Label(hiscoreframe,text='High Score: ', fg='green',font= "applecherry 18")
hiscorelabel.pack(side=LEFT)

resetscoreframe=Frame(root)
resetscoreframe.pack(side=TOP,fill='x', expand=False)

def resetscorenow():
    global speed
    global scorenow
    scorenow=0
    speed=300
    currentscorelabel.config(text=str(scorenow))

def resethighscore():
    global highscorenow
    highscorenow=0
    hiscorelabelnow.config(text=str(highscorenow))
    if highscorenow < scorenow:
        temphighscorenow=scorenow
        hiscorelabelnow.config(text=str(temphighscorenow))
    
    
    
resetscorebtn=Button(resetscoreframe,text='Reset Score',command=resetscorenow)
resetscorebtn.pack(side=LEFT)
resethighscorebtn=Button(resetscoreframe,text='Reset High Score',command=resethighscore)
resethighscorebtn.pack(side=LEFT)

def helpfunction():
    messagebox.showinfo(title='Game Info', message='Select Your Desired Character. Then Try and catch the minion. Each successful catch will earn you 10 points')

helpiconimage=PhotoImage(file=getFilePath('help_icon.png'))
helpicon=Button(resetscoreframe,image=helpiconimage,borderwidth=2,command=helpfunction)
helpicon.pack(side=RIGHT)


try:
    f=open(getFilePath('highscore.txt'),'r')
    highscorenow=int(f.read())
    print(highscorenow)
    f.close()
except:
    highscorenow=0
hiscorelabelnow=Label(hiscoreframe,text=str(highscorenow), fg='green',font= "applecherry 18")
hiscorelabelnow.pack(side=LEFT)

#GAME MUSIC
pygame.mixer.init()
pygame.mixer.music.load(getFilePath('Bananasong.mp3'))



#GAME CODE

def startgame():
    global filename
    global imgnow
    def clickednow():
        global scorenow
        global highscorenow
        global speed

        if speed >=100:
            speed-=10
        button.place_configure(x=random.randint(330,650),y=random.randint(100,400))
        scorenow+=10
        if highscorenow < scorenow:
            temphighscorenow=scorenow
            hiscorelabelnow.config(text=str(temphighscorenow))
            highscorenow=scorenow
            
        currentscorelabel.config(text=str(scorenow))
        '''print('**')
        print(scorenow)
        print(highscorenow)
        print('**')'''

    def button_hover(e):
        global speed
        print(speed)
        root.after(speed)
        #filenumber=random.randint(1,6)
        #fileneame=str(filenumber)+'.png'
        #img=PhotoImage(file=fileneame)
        #button.config(image=img)
        but_pos_x=random.randint(50,1100)   # <----- moved into the function
        but_pos_y=random.randint(100,500)  # <----- moved into the function
        button.place_configure(x=but_pos_x,y=but_pos_y)
        #button.bind("<Enter>",button_hover)
        #gameframe.mainloop()

    gameframe=Frame(root)
    gameframe.pack(fill='both', expand=True)
    pygame.mixer.music.play()

    #imgnow=PhotoImage(file=filename)
    button =Button(gameframe,image=imgnow,borderwidth=2,command=clickednow)
    button.place(x=250,y=100,anchor=CENTER)


    button.bind("<Enter>",button_hover)
    def quitgame():
        pygame.mixer.music.stop()
        root.destroy()
    quitbtnframe=Frame(root)
    quitbtnframe.pack(side=BOTTOM)

    #quitbutton=Button(quitbtnframe, text='QUIT',command=quitgame)
    #quitbutton.pack()

#image selection frame

def selectimage1():
    global imgnow
    imgnow=img1
    imageselectionframe.pack_forget()
    startgame()

def selectimage2():
    global imgnow
    imgnow=img2
    imageselectionframe.pack_forget()
    startgame()

def selectimage3():
    global imgnow
    imgnow=img3
    imageselectionframe.pack_forget()
    startgame()
    
def selectimage4():
    global imgnow
    imgnow=img4
    imageselectionframe.pack_forget()
    startgame()

def selectimage5():
    global imgnow
    imgnow=img5
    imageselectionframe.pack_forget()
    startgame()

def selectimage6():
    global imgnow
    imgnow=img6
    imageselectionframe.pack_forget()
    startgame()
    
def selectimage7():
    global imgnow
    imgnow=img7
    imageselectionframe.pack_forget()
    startgame()
    
imageselectionframe=Frame(root)
imageselectionframe.pack()

selectguide=Label(imageselectionframe, text="Select Your Character", fg='red',font= "applecherry 18")
selectguide.pack()
img1=PhotoImage(file=getFilePath('1.png'))
imagebutton1=Button(imageselectionframe,image=img1,borderwidth=2,command=selectimage1)
imagebutton1.pack(side = LEFT)

img2=PhotoImage(file=getFilePath('2.png'))
imagebutton2=Button(imageselectionframe,image=img2,borderwidth=2,command=selectimage2)
imagebutton2.pack(side = LEFT)

img3=PhotoImage(file=getFilePath('3.png'))
imagebutton3=Button(imageselectionframe,image=img3,borderwidth=2,command=selectimage3)
imagebutton3.pack(side = LEFT)

img4=PhotoImage(file=getFilePath('4.png'))
imagebutton4=Button(imageselectionframe,image=img4,borderwidth=2,command=selectimage4)
imagebutton4.pack(side = LEFT)

img5=PhotoImage(file=getFilePath('5.png'))
imagebutton5=Button(imageselectionframe,image=img5,borderwidth=2,command=selectimage5)
imagebutton5.pack(side = LEFT)

img6=PhotoImage(file=getFilePath('6.png'))
imagebutton6=Button(imageselectionframe,image=img6,borderwidth=2,command=selectimage6)
imagebutton6.pack(side = LEFT)

img7=PhotoImage(file=getFilePath('7.png'))
imagebutton7=Button(imageselectionframe,image=img7,borderwidth=2,command=selectimage7)
imagebutton7.pack(side = LEFT)

#fileneame=str(filenumber)+'.png'
#img=PhotoImage(file=fileneame)


scorenow=0
speed=300
currentscorelabel=Label(scoreframe,text=scorenow, fg='green',font= "applecherry 18")
currentscorelabel.pack(side=LEFT)


canvas=Canvas(root, width=500, height=50)
canvas.pack(fill='x', expand=False)
# Create a line in canvas widget
canvas.create_line(0, 15, 20000, 15, width=3)



#GAME CODE
'''

'''
root.mainloop()