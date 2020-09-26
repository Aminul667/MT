from manimlib.imports import *

class Background(Scene):
    def construct(self):
        back_rect = Rectangle(width = FRAME_WIDTH, height = FRAME_HEIGHT, stroke_width = 0, fill_color = DARK_GREY, fill_opacity = 1)
        self.add(back_rect)

        # plane = NumberPlane()
        # self.add(plane)

        img = ImageMobject(
            'OnlyPNG.png',
            color = BLUE,
            height = 3
        )

        self.play(FadeIn(img), run_time = 2)
        # self.wait()

        text = Text('Programming & Mathematics Literature', font = 'Brush Script MT', size = 1.2, stroke_color = GOLD_E)
        text.move_to(img)
        text.set_color_by_gradient(GOLD, GREY_BROWN, LIGHT_GREY)

        self.play(ApplyMethod(img.shift, 2*UP))

        self.play(Write(text), run_time = 2.5)
        self.wait(0.5)

        math = TexMobject(r'Math').shift(4*LEFT+3*UP)
        math.set_color(BLUE_C).set_stroke(color = None)
        # self.play(Write(math))
        # self.wait()

        linear = TexMobject(r'Linear\ Algebra').shift(1*DOWN+4*RIGHT)
        linear.set_color(BLUE_C).set_stroke(color = None)

        calculus = TexMobject(r'Calculus').shift(3*LEFT+1.5*DOWN)
        calculus.set_color(BLUE_C).set_stroke(color = None)

        mach = TexMobject(r'Machine\ Learning').shift(2.5*DOWN+0.5*RIGHT)
        mach.set_color(BLUE_C).set_stroke(color = None)

        data = TexMobject(r'Data\ Science').shift(3*UP+4*RIGHT)
        data.set_color(BLUE_C).set_stroke(color = None)

        group1 = VGroup(math, linear, calculus, mach, data)
        self.play(Write(group1), run_time = 3)
        self.wait(0.5)

        python = TexMobject(r'Python').shift(3.5*LEFT+1.5*UP)
        python.set_color(BLUE_C).set_stroke(color = None)

        matlab = TexMobject(r'matlab').shift(3.5*RIGHT+2*UP)
        matlab.set_color(BLUE_C).set_stroke(color = None)

        c = TexMobject(r'C').shift(LEFT+DOWN)
        c.set_color(BLUE_C).set_stroke(color = None)

        cpp = TexMobject(r'C++').shift(2*DOWN+3.5*RIGHT)
        cpp.set_color(BLUE_B).set_stroke(color = None)

        group2 = VGroup(python, matlab,c,cpp)
        self.play(Write(group2), run_time = 2)
        self.wait()