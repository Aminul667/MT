from manim import *
import numpy as np 

# class Lec1(Scene):
#     def construct(self):
#         c = Circle(stroke_color = YELLOW, fill_color = BLUE_B, radius = 2, stroke_width = 5, fill_opacity = 0.8).to_edge(UL)

#         equ = MathTex(r'x^2+y^2 = 2^2').next_to(c, DOWN, buff = 0.5, aligned_edge = LEFT)

#         text = Tex('Md Aminul ', 'Islam ', 'Rahat')
#         text[0].set_color(BLUE)
#         text[1].set_color(GREEN)
#         text[2].set_color(GOLD)
#         text.next_to(c, RIGHT, buff = 1)

#         und = Underline(text[2])

#         num = MathTex(r'ln(2)=0.69').scale(2).next_to(text, DOWN, buff = 0.1)

#         self.play(DrawBorderThenFill(c), run_time = 3)
#         self.wait()

#         self.play(Write(equ), run_time = 2)
#         self.wait()

#         self.play(Write(text), ShowCreation(und), run_time = 2)
#         self.wait()

#         self.play(FadeIn(num))
#         self.wait()

#         self.play(c.animate.shift(3*RIGHT), run_time = 4)
#         self.wait()

# class LecAct1(Scene):
#     def construct(self):
#         rect = Rectangle(color = PURPLE, fill_color = GREY, fill_opacity = 1, height = 2, width = 4)
#         rect.to_edge(UR)

#         text = Tex('This is mad broskis').set_color(ORANGE)
#         und = Underline(text)



#         self.play(DrawBorderThenFill(rect), run_time = 2)
#         self.wait()

#         self.play(rect.animate.to_edge(DR), Write(text), ShowCreation(und), run_time = 3)
#         self.wait()
class LecLine(Scene):
    def construct(self):
        line = DashedLine(start=7*LEFT, end=7*RIGHT, dash_length = 0.25)
        num = MathTex(r'ln2 = 0.69').set_color(ORANGE).to_edge(DL)
        und = Underline(num)

        text = Tex('The number is too good mate')

        self.play(ShowCreation(line), run_time = 2)
        self.wait()
        self.play(Write(num),ShowCreation(und), Transform(line, text), run_time = 3)
        self.wait()