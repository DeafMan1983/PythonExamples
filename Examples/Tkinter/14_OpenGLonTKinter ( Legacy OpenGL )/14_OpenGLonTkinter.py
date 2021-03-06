import time
import tkinter
from OpenGL import GL
from pyopengltk import OpenGLFrame

class AppOgl(OpenGLFrame):

    def initgl(self):
        """Initalize gl states when the frame is created"""
        GL.glViewport(0, 0, self.width, self.height)
        GL.glClearColor(1.0, 0.25, 0.0, 1.0)
        self.start = time.time()
        self.nframes = 0

    def redraw(self):
        """Render a single frame"""
        GL.glClear(GL.GL_COLOR_BUFFER_BIT)

        GL.glBegin(GL.GL_TRIANGLES)
        GL.glVertex2f(-0.5, -0.5)
        GL.glVertex2f(0.5, -0.5)
        GL.glVertex2f(0.0, 0.5)
        GL.glEnd()

        tm = time.time() - self.start
        self.nframes += 1
        print("fps",self.nframes / tm, end="\r" )


if __name__ == '__main__':
    root = tkinter.Tk()
    root.title("Legacy OpenGL on Tkinter")
    app = AppOgl(root, width=480, height=320)
    app.pack(fill=tkinter.BOTH, expand=tkinter.YES)
    app.animate = 1
    app.after(100, app.printContext)
    app.mainloop()