#!/usr/bin/env python
import thread
import rospy
from std_msgs.msg import String
from Tkinter import *

label = dict()
var = dict()

def show_emotion(data):
    print "showing image : " + data.data
    #img = PhotoImage(file='emotion.gif', format='gif -index 2')
    img = PhotoImage(file='/home/pi/catkin_ws/src/head_driver/src/emitions/' + data.data + '.gif')
    label["emot"].config(image = img)
    label["emot"].image = img

def show_text(data):
    print "showing text : " + data.data
    label["emot"].config(image='')
    var["text"].set(data.data)

def face():
    root = Tk()
    root.config(bg="white")
    root.attributes("-fullscreen", True)
    var["text"]=StringVar()
    label["emot"] = Label(root, bg = "white", textvariable = var["text"], font="Helvetica 120 bold italic")
    label["emot"].pack(anchor=CENTER)
    #showimage = Button(root, text="Show Image", command = show_emotion)
    #showimage.pack(anchor=W)
    #showtext = Button(root, text="Show Text", command = show_text)
    #showtext.pack(anchor=W)
    root.mainloop()

def subscribers():
    rospy.init_node('robot_face', anonymous=True)
    rospy.Subscriber('poppy/face/emotion', String, callback=show_emotion)
    rospy.Subscriber('poppy/face/text', String, callback=show_text)
    print 'FACE subscribers successful Initial'
    rospy.spin()

if __name__ == '__main__':
    thread.start_new_thread(face, ())
    subscribers()
