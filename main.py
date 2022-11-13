from gl import Render

r = Render()

r.glCreateWindow(100, 100)

r.glViewPort(25, 25, 30, 30)

r.glClearColor(0.2, 0.4, 0.6)

r.glColor(0.5, 0.3, 0.6)

r.glViewportColor(0.1, 0.6, 0.4)

r.glClear()

r.glClearViewport()

r.glVertex(0, 0)

r.glFinish("punto.bmp")