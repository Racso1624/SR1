from gl import Render

r = Render()

r.glCreateWindow(100, 100)

r.glViewPort(20, 20, 50, 50)

r.glClearColor(0.2, 0.4, 0.6)

r.glClear()

r.glVertex(1, 1)

r.glFinish("a.bmp")