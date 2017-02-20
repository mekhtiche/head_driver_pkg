#!/usr/bin/env python
import thread
import rospy
from std_msgs.msg import String
from Tkinter import *
import time
import os

global new_emotion, emotion, starting
new_emotion = False
label = dict()
var = dict()
self=dict()
emotion = dict()
starting = True
buffer = {}



def start_animation(data):
    global new_emotion
    new_emotion=True
    time.sleep(0.1)
    show_emotion(data)

def show_emotion(data):
    global new_emotion
    new_emotion=False
    while True:
        for frame in range(len(emotion[data.data])):
            image1 = emotion[data.data][str(frame)]
            label["emot"].config(image=image1)
            label["emot"].image = image1
            frame += 1
            time.sleep(0.5)
            if new_emotion:
                return

def show_text(data):
    print "showing text : " + data.data
    label["emot"].config(image='')
    var["text"].set(data.data)

def Close():
    self["root"].destroy()

def face():
    global emotion, starting
    path = "/home/pi/catkin_ws/src/head_driver/src/emotions/"
    dirs = os.listdir(path)
    for file in dirs: #glob.glob(directory + "*.gif"):
        if file[-4:] == ".gif":
            print file[:-4]
            emotion[file[:-4]]={}
    self["root"] = Tk()
    self["root"].config(bg="white")
    self["root"].attributes("-fullscreen", True)
    var["text"]=StringVar()
    label["emot"] = Label(self["root"] , bg = "white", textvariable = var["text"], font="Helvetica 120 bold italic")
    label["emot"].pack(anchor=CENTER)
    close = Button(self["root"] , text='.', bg="white", relief=FLAT, command=Close)
    close.pack(anchor=SE)

    for file in emotion:
        print file
        ndx = 0
        while True:
            try:
                img = PhotoImage(file=path + file +'.gif', format="gif -index " + str(ndx))
                emotion[file].update({str(ndx): img})
                ndx += 1
            except Exception, err:
                print err
                break
    starting = False
    print "DONE"

    self["root"].mainloop()


def subscribers():
    rospy.init_node('robot_face', anonymous=True)
    rospy.Subscriber('poppy/face/emotion', String, callback=start_animation)
    rospy.Subscriber('poppy/face/text', String, callback=show_text)
    print 'FACE subscribers successful Initial'
    rospy.spin()

if __name__ == '__main__':
    print "starting..."
    thread.start_new_thread(face, ())
    while starting:
        time.sleep(1)
    subscribers()

