import pyglet

image = "/home/pi/catkin_ws/src/head_driver/src/emotions/nod.gif"
animation = pyglet.resource.animation(image)
sprite = pyglet.sprite.Sprite(animation)
win = pyglet.windows.Windows(width=sprite.width, height=sprite.height)
green = 0,1,0,1
pyglet.gl.glClearColor(*green)
@win.event
def on_drow():
    win.clear()
    sprite.drow()

pyglet.app.run()
