#!/usr/bin/env python
import sys, os.path
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
import os
import thread
import time
import pygame
from GIFImage import GIFImage
import rospy
from head_driver_pkg.msg import Emotion
from std_msgs.msg import Empty

white = (255,255,255)
play = True
images = {}
emo=["normal"]
Text=[]

def shutdown(data):
    play=False
    time.sleep(2)
    rospy.signal_shutdown('manual shutdown')

def call_emotion(data):
    emo[0]=data.name
    time.sleep(data.time)
    emo[0]="normal"

def call_text(data):
    Text.append(data.name)
    time.sleep(data.time)
    Text.pop(0)

def loading_images():
    path = '/home/pi/catkin_ws/src/head_driver_pkg/src/emotions/'
    dirs = os.listdir(path)
    for file in dirs:
        if file[-4:] == ".gif":
            show_text("loading image : " + file[:-4], 75, (400, 240))
            images.update({file[:-4]: GIFImage(path + file)})
    
def emotion(emo, text):
    play = True
    while play:
        try:
            if text:
                screen.fill((0,0,0))
                font = pygame.font.SysFont("Times New Roman", 70)
                textToShow = font.render(text[0], 1, white)
                text_rect = textToShow.get_rect()
                text_rect.center = (400,240)
                screen.blit(textToShow, text_rect)
            else:
                emotion_name = emo[0]
                images[emotion_name].render(screen, (0,0))
            pygame.display.flip()
        except Exception,err:
            print err

def show_text(text, size=100, pos = (400,240)):
    screen.fill((0,0,0))
    font = pygame.font.SysFont("Times New Roman", size)
    textToShow = font.render(text, 1, white)
    text_rect = textToShow.get_rect()
    text_rect.center = pos
    screen.blit(textToShow, text_rect)
    pygame.display.flip()
    
def subscribers():
    rospy.init_node('Robot_face', anonymous=True)
    rospy.Subscriber('poppy/face/emotion', Emotion, callback=call_emotion)
    rospy.Subscriber('poppy/face/text', Emotion, callback=call_text)
    rospy.Subscriber('poppy/face/shutdown', Empty, callback=shutdown)
    print 'Head subscribers successful Initial'
    rospy.spin()


pygame.init()
screen = pygame.display.set_mode((800, 480), pygame.FULLSCREEN) #
if __name__ == '__main__':
    #show_text("Loading Images")      
    loading_images()
    thread.start_new_thread(emotion,(emo, Text,))
    subscribers()
