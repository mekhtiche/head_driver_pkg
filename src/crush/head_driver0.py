#!/usr/bin/env python
import thread
from PIL import Image
import pygame
from pygame.locals import *
import time





def load_images():
    img={}
    print "Loading Images"
    im = Image.open('/home/pi/catkin_ws/src/head_driver/src/emotions/happy1.gif')
    frame = 0
    while True:
        print "loading frame : " + str(frame)
        data = im.tostring()
        size = im.size
        mode = im.mode
        img[frame] = pygame.image.fromstring(data, size, mode)
        try:
            im.seek(frame)
        except Exception, err:
            print err
            break
        frame+=1
    print "Loading images DONE"
    return img

def play_gif(gif_image):
    for frame in range(len(gif_image)):
        screen.blit(gif_image[frame],(0,0))
        pygame.display.flip()
        time.sleep(0.2)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((800, 480))
    gif_image_splited = load_images()
    for frame in range(len(gif_image_splited)):
        screen.blit(gif_image_splited[frame],(0,0))
        pygame.display.flip()
        time.sleep(0.1)
    
    print "OK"
