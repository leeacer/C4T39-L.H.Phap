import pyglet
import datetime

music = pyglet.resource.media('3243.wav')

stop = False
while stop == False:
    rn = str(datetime.datetime.now().time())
    if rn == "20:00:00.000000":
        stop = True
        music.play()

        pyglet.app.run()