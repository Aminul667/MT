from manim import *

class Table1(Scene):
    def construct(self):
        num_rects = 9
        rects = VGroup()
        for r in range(num_rects):
            rect = Square()
            rects.add(rect)
        rects.arrange_in_grid(buff=0)
        self.add(rects)

class Stuff(Scene):
    def construct(self):
        num_rects = 9
        rects = VGroup()
        for r in range(num_rects):
            rect = Square()
            rect.add(Integer(r+1))
            rects.add(rect)
        rects.arrange_in_grid(buff=0)
        rects[4].set_fill(LIGHT_PINK, 1)
        self.add(rects)

class Stuff2(Scene):
    def construct(self):
        num_rects = 12
        rects = VGroup()
        x = range(num_rects)
        for r in x:
            if r in x[:4]:
                rect = Rectangle(width=2, height=0.75)
            else:
                rect = Rectangle(width=2, height=1.5)

            rect.add(Integer(r+1))
            rects.add(rect)
        rects.arrange_in_grid(buff=0, n_cols=4)
        self.add(rects)