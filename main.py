from gl import Render

r = Render()

r.glCreateWindow(100, 100)

r.glViewPort(25, 25, 30, 30)

r.glClearColor(0.2, 0.8, 0.6)

r.glClear()

r.glVertex(1, 1)

r.glFinish("punto.bmp")