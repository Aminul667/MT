from manimlib.imports import*
import numpy as np

class Scalar(Scene):
    CONFIG = {
        # 'camera_config':{'background_color':RED},
        'MyRED':'#bf0000',
        'MyDRED':'#400000'
    }

    def construct(self):
        # plane = NumberPlane()
        scalar_text = TextMobject('Scalar').to_edge(UP)
        scalar_text.scale(2)

        self.play(FadeIn(scalar_text))
        self.wait()

        text1 = TexMobject(r'A\ Scalar\ is\ a\ quantity\ with\ magnitude').next_to(scalar_text, DOWN, buff = 0.25)

        self.play(Write(text1), run_time = 2, rate_function = linear)
        self.wait()

        # self.play(ShowCreation(plane), run_time = 2)
        # self.wait()

        # triangle
        tri = Triangle(color = self.MyRED).scale(0.7)
        tri.shift(3*LEFT)

        self.play(ShowCreation(tri), run_time = 2, rate_function = linear)
        self.wait()

        # rectangle
        rect = Rectangle(height = 1, width = 1, color = self.MyDRED)
        rect.shift(3*RIGHT)

        self.play(ShowCreation(rect), run_time = 2, rate_function = linear)
        self.wait()

        # dashed line
        line = DashedLine(np.array([-2.5, 0, 0]), np.array([2.5, 0, 0]), dash_length = 0.25)

        self.play(ShowCreation(line), rate_function = linear)
        self.wait()

        # sc1 = ScreenRectangle(height = 3)
        # self.play(Write(sc1))
        # self.wait()
        
        # tri, line and square group
        group1 = VGroup(tri, rect, line)

        cir = Circle(color = GOLD, fill_opacity = 1)

        self.play(Transform(group1, cir), run_time = 2)
        self.wait()


class VectorPart(GraphScene):
    CONFIG = {
        'x_min':-4,
        'x_max':4,
        'y_min':-4,
        'y_max':4,
        'x_axis_label':None,
        'y_axis_label':None
    }
    def construct(self):
        vector = TextMobject('Vector').scale(2)
        vector.to_edge(UL, buff = 0.5)

        self.play(FadeIn(vector))
        self.wait()

        axis = Axes(
            x_min = -3,
            x_max = 3,
            y_min = -3,
            y_max = 3,
            x_axis_config = {
                'include_tip':False,
                'include_ticks':True
            },
            y_axis_config = {
                'include_tip':False,
                'include_ticks':True
            }

        )
        
        n = TextMobject('N').next_to(axis, UP, buff = 0.25)
        s = TextMobject('S').next_to(axis, DOWN, buff = 0.25)
        e = TextMobject('E').next_to(axis, RIGHT, buff = 0.25)
        w = TextMobject('W').next_to(axis, LEFT, buff = 0.25)

        group2 = VGroup(n,s,e,w)

        self.play(AnimationGroup(
            Write(group2),
            ShowCreation(axis),
            run_time = 2,
            lag_ratio = 1
        ))
        self.wait()

        dot1 = Dot(np.array([0,0,0])).set_color(RED)
        dot2 = Dot(np.array([2,2.5,0])).set_color(RED)

        self.play(AnimationGroup(
            Write(dot1),
            Write(dot2),
            run_time = 2,
        ))
        self.wait()

        line = DashedLine(dot1, dot2, dash_length = 0.25)
        line.set_color(ORANGE)

        self.play(ShowCreation(line))
        self.wait()

        mag = TexMobject(r'Magnitude').next_to(vector, DOWN, buff =0.25)
        self.play(Write(mag), run_time = 2)
        self.wait()

        group1 = VGroup(dot1, line, dot2)

        vec = Vector(np.array([2,2.5,0])).set_color(RED)

        self.play(ReplacementTransform(group1, vec), run_time = 2)
        self.wait()

        # self.play(ApplyMethod(vec.rotate_about_origin, 2))
        # self.wait()

        di = TexMobject(r'Direction').next_to(mag, DOWN, buff = 0.25)
        di.align_to(mag, LEFT)

        self.play(AnimationGroup(
            Rotating(vec, radians = 2*PI, about_point = ORIGIN),
            Write(di),
            run_time = 10,
        ))
        self.wait()


        









