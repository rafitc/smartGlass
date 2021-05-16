import pyglet

music = pyglet.resource.media('hello.mp3')
music.play()

pyglet.app.run()