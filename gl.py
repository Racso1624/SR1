import struct

def char(c):
    #1 byte
    return struct.pack('=c', c.encode('ascii'))

def word(h):
    #2 bytes
    return struct.pack('=h', h)

def dword(l):
    #4 bytes
    return struct.pack('=l', l)

def setColor(r, b, g):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])

class Render(object):

    def __init__(self):
        self.width = 0
        self.height = 0
        self.clear_color = setColor(1, 1, 1)
        self.render_color = setColor(0, 0, 0)
        self.viewport_color = setColor(1, 1, 1)
        self.viewport_x = 0
        self.viewport_y = 0
        self.viewport_height = 0
        self.viewport_width = 0

    def glClear(self):
        self.framebuffer = [[self.clear_color for x in range(self.width)]
        for y in range(self.height)]

    def glCreateWindow(self, width, height):
        self.width = width
        self.height = height

    def glViewportColor(self, r, g, b):
        self.viewport_color = setColor(r, g, b)

    def glClearColor(self, r, g, b):
        self.clear_color = setColor(r, g, b)

    def glClearViewport(self):
        for x in range(self.viewport_x, self.viewport_x + self.viewport_width + 1):
            for y in range(self.viewport_y, self.viewport_y + self.viewport_height + 1):
                self.glPoint(x,y, self.viewport_color)    
        

    def glColor(self, r, g, b):
        self.render_color = setColor(r, g, b)

    def glViewPort(self, x, y, width, height):
        self.viewport_x = x
        self.viewport_y = y
        self.viewport_height = height
        self.viewport_width = width

    def glVertex(self, x, y):
        if x > 1 or x < -1 or y > 1 or y < -1:
            print('Error')
        else:
            x = int((x + 1) * (self.viewport_width / 2) + self.viewport_x)
            y = int((y + 1) * (self.viewport_height / 2) + self.viewport_y)

            self.glPoint(x, y)

    def glPoint(self, x, y, color = None):
        self.framebuffer[x][y] = color or self.render_color

    def glFinish(self, filename):
        f = open(filename, 'bw')

        #pixel header
        f.write(char('B'))
        f.write(char('M'))
        f.write(dword(14 + 40 + self.width * self.height * 3))
        f.write(word(0))
        f.write(word(0))
        f.write(dword(14 + 40))

        #info header
        f.write(dword(40))
        f.write(dword(self.width))
        f.write(dword(self.height))
        f.write(word(1))
        f.write(word(24))
        f.write(dword(0))
        f.write(dword(self.width * self.height * 3))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))
        f.write(dword(0))

        #pixel data
        for x in range (self.height):
            for y in range(self.width):
                f.write(self.framebuffer[x][y])

        f.close()