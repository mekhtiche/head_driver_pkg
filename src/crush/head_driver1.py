#!/usr/bin/env python
import thread
import rospy
from std_msgs.msg import String
from Tkinter import *
from PIL import Image, ImageTk
import time
global new_emotion
new_emotion = False
label = dict()
var = dict()
self=dict()

def start_animation(data):
    global new_emotion
    new_emotion=True
    time.sleep(0.1)
    show_emotion(data)

def show_emotion(data):
    global new_emotion
    new_emotion=False
    frame = 0
    try:
        img = Image.open('emotions/' + data.data + '.gif')

    except Exception:
        return

    while True:
        try:
            image1 = ImageTk.PhotoImage(img)
            img.seek(frame)
        except Exception, err:
            frame = -1
        label["emot"].config(image=image1)
        label["emot"].image = image1
        frame += 1
        time.sleep(0.1)
        if new_emotion:
            return

def show_text(data):
    print "showing text : " + data.data
    label["emot"].config(image='')
    var["text"].set(data.data)

def Close():
    self["root"].destroy()

def face():
    self["root"] = Tk()
    self["root"].config(bg="white")
    self["root"].attributes("-fullscreen", True)
    var["text"]=StringVar()
    label["emot"] = Label(self["root"] , bg = "white", textvariable = var["text"], font="Helvetica 120 bold italic")
    label["emot"].pack(anchor=CENTER)
    #showimage = Button(self["root"] , text="Show Image", command = show_emotion)
    #showimage.pack(anchor=W)
    #showtext = Button(self["root"] , text="Show Text", command = show_text)
    #showtext.pack(anchor=W)
    close = Button(self["root"] , text='.', bg="white", relief=FLAT, command=Close)
    close.pack(anchor=SE)
    self["root"].mainloop()


def subscribers():
    rospy.init_node('robot_face', anonymous=True)
    rospy.Subscriber('poppy/face/emotion', String, callback=start_animation)
    rospy.Subscriber('poppy/face/text', String, callback=show_text)
    print 'FACE subscribers successful Initial'
    rospy.spin()

if __name__ == '__main__':
    thread.start_new_thread(face, ())
    subscribers()
