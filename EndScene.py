from manimlib.imports import *

class EndScene(Scene):
    CONFIG={
        "MyBLUE":"#3b5998",
        "MyRED":"#FF0000"
    }

    def construct(self):

        #youtube
        rect1 = RoundedRectangle(height = 1.5, width = 2, color = self.MyRED).shift(2*UP)
        tri1 = Triangle(color = WHITE).rotate(270*DEGREES).scale(0.5)
        tri1.move_to(rect1)

        group1 = VGroup(rect1, tri1)

        #facebook
        frect1 = RoundedRectangle(height = 1.5, width = 1.5, color = self.MyBLUE).shift(2*DOWN)

        ftext1 = TextMobject('f').move_to(frect1).scale(3)
        ftext1.set_stroke(color = WHITE)
        ftext1.set_fill(None)

        fgroup1 = VGroup(frect1, ftext1)

        self.play(ShowCreation(group1), ShowCreation(frect1), Write(ftext1), rate_function = linear, run_time = 2)

        #Filling youtube
        rect2 = RoundedRectangle(height = 1.5, width = 2, color = self.MyRED, fill_opacity = 1).shift(2*UP)
        tri2 = Triangle(color = WHITE, fill_opacity = 1).rotate(270*DEGREES).scale(0.5)
        tri2.move_to(rect1)

        group2 = VGroup(rect2, tri2)

        #filling facebook
        frect2 = RoundedRectangle(height = 1.5, width = 1.5, color = self.MyBLUE, fill_opacity = 1).shift(2*DOWN)
        ftext2 = TextMobject('f').move_to(frect2).scale(3)
        ftext2.set_stroke(color = WHITE)

        fgroup2 = VGroup(frect2, ftext2)

        self.play(Write(group2), Write(fgroup2), rate_function = linear, run_time = 2)

        group3 = VGroup(group1, group2)
        fgroup3 = VGroup(fgroup1, fgroup2)

        self.play(ApplyMethod(group3.shift,3*LEFT), ApplyMethod(fgroup3.shift,3*LEFT), rate_function = linear)

        # links
        yt = TexMobject(r'http://bit.ly/ProMatLit').next_to(group3, RIGHT, buff = 0.5)

        fb = TexMobject(r'https://bit.ly/PMLiterature').next_to(fgroup3, RIGHT, buff = 0.5)

        self.play(Write(yt), Write(fb))
        self.wait()