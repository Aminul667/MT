from manimlib.imports import *

class HasibIntro(Scene):
    def construct(self):
        text1 = TexMobject(r'Welcome\ to\ our\ Permutations\ Class').scale(1.2)
        text1.shift(UP)
        text1.set_color_by_gradient(GOLD_A, WHITE, GOLD_A)
        
        self.play(Write(text1), run_time = 2)
        self.wait()

        text2 = TexMobject(r'Lecture\ 3').scale(1.2).next_to(text1, DOWN, buff = 0.8)
        text2.set_color_by_gradient(GOLD_A, WHITE, GOLD_A)

        self.play(TransformFromCopy(text1, text2), run_time = 2)
        self.wait()


class HasibLast(Scene):
    # CONFIG = {
    #     'camera_config':{'background_color':WHITE}
    # }
    def construct(self):

        circle = Circle(fill_opacity = 2).scale(1.5)
        circle.set_fill()
        circle.set_color(BLUE)
        
        self.play(DrawBorderThenFill(circle))

        inte = TexMobject(r'\int').scale(3)
        inte.set_stroke(RED_A)
        inte.set_color(RED)
        inte.set_opacity(0.5)

        self.play(Write(inte))

        text = TextMobject('HA').scale(2.5)
        text.set_stroke(ORANGE)
        text.set_color(RED)

        self.play(Write(text), run_time = 2)
        self.wait()

        group = VGroup(circle, inte, text)

        self.play(ApplyMethod(group.shift,1*UP))

        text1 = TexMobject(r'Thanks\ for\ watching').scale(1.3)
        text1.set_color_by_gradient(GOLD_A, WHITE, GOLD_A)
        text1.next_to(group, DOWN, buff = 0.8)

        self.play(Write(text1), run_time = 2)
        self.wait()