#!/usr/bin/env python

'''Base class for text tests.
'''

__docformat__ = 'restructuredtext'
__version__ = '$Id: $'

import unittest
import sys

from pyglet.GL.VERSION_1_1 import *
from pyglet.text import *
from pyglet.window import *
from pyglet.window.event import *

class TextTestBase(unittest.TestCase):
    font_name = ''
    font_size = 24
    text = 'Quick brown fox'

    def on_resize(self, width, height):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(0, width, 0, height, -1, 1)
        glMatrixMode(GL_MODELVIEW)

    def on_expose(self):
        glClearColor(0.5, 0, 0, 1)
        glClear(GL_COLOR_BUFFER_BIT)
        glLoadIdentity()
        glTranslatef(10, 10, 0)
        self.layout.draw()
        self.window.flip()

    def create_font(self):
        self.font = Font(self.font_name, self.font_size) 

    def render(self):
        self.layout = self.font.render('Quick brown fox')

    def test_main(self):
        width, height = 200, 200
        self.window = w = Window(width, height, visible=False)
        exit_handler = ExitHandler()
        w.push_handlers(exit_handler)
        w.push_handlers(self)

        self.create_font()
        self.render()

        w.set_visible()
        while not exit_handler.exit:
            w.dispatch_events()
        w.close()

if __name__ == '__main__':
    unittest.main()
