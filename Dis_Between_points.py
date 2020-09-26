from manimlib.imports import *

class DistancePoint(GraphScene):
    CONFIG = {
        'x_min':-3.5,
        'x_max':3.5,
        'y_min':-4,
        'y_max':4,
        'x_axis_label': '$x$',
        'y_axis_label': '$y$',
        'graph_origin':ORIGIN
    }
    def construct(self):
        self.setup_axes(animate = True)
        self.wait(3.06)

        #making two points
        p1 = Dot(self.coords_to_point(1.5,2))
        t1 = TexMobject(r'(x_1,y_1)').next_to(p1, UL, buff = 0)
        t1.scale(0.7).set_color(BLUE)

        p2 = Dot(self.coords_to_point(3,4))
        t2 = TexMobject(r'(x_2,y_2)').next_to(p2, UR, buff = 0)
        t2.scale(0.7).set_color(BLUE)

        self.play(Write(p1))
        self.wait(5)
        self.play(Write(t1))
        self.wait(5)

        self.play(Write(p2))
        # self.wait(3)
        self.play(Write(t2))
        self.wait(5)

        #creating lines for triangle
        line_d = Line(p1, p2, color = RED)

        self.play(Write(line_d))

        dot = Dot(self.coords_to_point(2,4), color = BLACK)
        text = TexMobject(r'd').next_to(dot, DOWN, buff =0.25)
        d_text = VGroup(text,dot)

        self.play(Write(d_text))
        self.wait(5)

        line_h = Line(self.coords_to_point(1.5,2), self.coords_to_point(3,2), color = RED)
        a_text = TexMobject(r'a').next_to(line_h, DOWN, buff = 0.25)

        self.play(Write(line_h))
        self.wait(5)
        self.play(Write(a_text))
        self.wait(5)

        line_v = Line(self.coords_to_point(3,2), self.coords_to_point(3,4), color = RED)
        b_text = TexMobject(r'b').next_to(line_v, RIGHT, buff = 0.25)

        self.play(Write(line_v))
        self.wait(5)
        self.play(Write(b_text))
        self.wait(5)

        #picture frame
        picture = Group(*self.mobjects)
        # picture.scale(0.8).to_edge(LEFT, buff = SMALL_BUFF)
        # self.add(picture)
        # self.wait()
        self.play(ApplyMethod(picture.scale(0.8).to_edge, LEFT))
        self.wait(10)

        #equation reation
        #rect = Rectangle(width = 3, height = 3.5, stroke_color = RED).next_to(picture, RIGHT, buff = 0.5)
        rect = Line(UP,DOWN, color = BLACK).next_to(picture, RIGHT, buff = 0.5)
        self.add(rect)

        tri_group = VGroup(line_d, line_h, line_v)
        d_squ = TexMobject(r'd^2 = a^2 + b^2').move_to(rect, aligned_edge = UL)
        d_squ.scale(0.8)

        self.play(TransformFromCopy(tri_group, d_squ))
        self.wait(5)

        #d = TexMobject(r'd = \sqrt{a^2 + b^2}').next_to(d_squ, DOWN, buff = 0.25).align_to(d_squ, LEFT)
        d = TexMobject(r'd = \sqrt{a^2 + b^2}').move_to(rect, aligned_edge = UL)
        d.scale(0.8)

        self.play(Transform(d_squ, d))
        self.wait(5)

        #dashed line for x2
        d2 = DashedLine(self.coords_to_point(3,4), self.coords_to_point(3,0), color = YELLOW)
        self.play(Write(d2))
        self.wait(5)

        x2 = Line(self.coords_to_point(0,0), self.coords_to_point(3,0), color = ORANGE, size = 0.5)
        x2t1 = TexMobject(r'|').next_to(x2, LEFT, buff = 0).set_color(ORANGE).scale(0.5)
        x2t2 = TexMobject(r'|').next_to(x2, RIGHT, buff = 0).set_color(ORANGE).scale(0.5)

        x2_group = VGroup(x2,x2t1,x2t2)

        x2_text = TexMobject(r'x_2').next_to(x2_group,UP, buff = 0).shift(0.3*DOWN)
        x2_text.set_color(BLUE).scale(0.7)

        self.play(Write(x2_group))
        self.wait(5)

        self.play(Transform(x2_group, x2_group.shift(0.2*DOWN)))
        self.wait(5)

        self.play(Write(x2_text))
        self.wait(5)

        #dashed line for x1
        d1 = DashedLine(self.coords_to_point(1.5,2), self.coords_to_point(1.5,0), color = YELLOW)
        self.play(Write(d1))
        self.wait(5)

        x1 = Line(self.coords_to_point(0,0), self.coords_to_point(1.5,0), color = ORANGE, size = 0.5)
        x1t1 = TexMobject(r'|').next_to(x1, LEFT, buff = 0).set_color(ORANGE).scale(0.5)
        x1t2 = TexMobject(r'|').next_to(x1, RIGHT, buff = 0).set_color(ORANGE).scale(0.5)

        x1_group = VGroup(x1, x1t1,x1t2)

        x1_text = TexMobject(r'x_1').next_to(x1_group,DOWN, buff = 0).shift(0.4*DOWN)
        x1_text.set_color(BLUE).scale(0.7)
        
        self.play(Write(x1_group))
        self.wait(5)

        self.play(Transform(x1_group, x1_group.shift(0.4*DOWN)))
        self.wait(5)

        self.play(Write(x1_text))
        self.wait(5)

        #difference x2-x1
        x2_x1 = Line(self.coords_to_point(1.5,0), self.coords_to_point(3,0), color = RED, size = 0.5)
        x2_x1t1 = TexMobject(r'|').next_to(x2_x1,LEFT, buff = 0).set_color(RED).scale(0.5)
        x2_x1t2 = TexMobject(r'|').next_to(x2_x1,RIGHT, buff = 0).set_color(RED).scale(0.5)

        x2_x1_group = VGroup(x2_x1,x2_x1t1,x2_x1t2)

        x2_x1_text = TexMobject(r'x_2-x_1').next_to(x2_x1_group,DOWN, buff = 0).shift(0.4*DOWN)
        x2_x1_text.set_color(BLUE).scale(0.7)

        self.play(Write(x2_x1_group))
        self.wait(5)

        self.play(Transform(x2_x1_group, x2_x1_group.shift(0.4*DOWN)))
        self.wait(5)

        self.play(TransformFromCopy(a_text, x2_x1_text))
        self.wait(5)

        #dashed line for y2
        dy2 = DashedLine(self.coords_to_point(3,4), self.coords_to_point(0,4), color = YELLOW)
        self.play(Write(dy2))
        self.wait(5)

        y2 = Line(self.coords_to_point(0,0), self.coords_to_point(0,4), color = ORANGE, size = 0.5)
        y2t1 = TexMobject(r'--').next_to(y2, UP, buff = 0).set_color(ORANGE).scale(0.5)
        y2t2 = TexMobject(r'--').next_to(y2, DOWN, buff = 0).set_color(ORANGE).scale(0.5)

        y2_group = VGroup(y2,y2t1,y2t2)

        y2_text = TexMobject(r'y_2').next_to(y2_group,RIGHT, buff = 0).shift(0.3*LEFT)
        y2_text.set_color(BLUE).scale(0.7)

        self.play(Write(y2_group))
        self.wait(5)

        self.play(Transform(y2_group, y2_group.shift(0.2*LEFT)))
        self.wait(5)

        self.play(Write(y2_text))
        self.wait(5)

        #dashed line for y1
        dy1 = DashedLine(self.coords_to_point(1.5,2), self.coords_to_point(0,2), color = YELLOW)
        self.play(Write(dy1))
        self.wait(5)

        y1 = Line(self.coords_to_point(0,0), self.coords_to_point(0,2), color = ORANGE, size = 0.5)
        y1t1 = TexMobject(r'--').next_to(y1, UP, buff = 0).set_color(ORANGE).scale(0.5)
        y1t2 = TexMobject(r'--').next_to(y1, DOWN, buff = 0).set_color(ORANGE).scale(0.5)

        y1_group = VGroup(y1, y1t1,y1t2)

        y1_text = TexMobject(r'y_1').next_to(y1_group,LEFT, buff = 0).shift(0.4*LEFT)
        y1_text.set_color(BLUE).scale(0.7)

        self.play(Write(y1_group))
        self.wait(5)

        self.play(Transform(y1_group, y1_group.shift(0.4*LEFT)))
        self.wait(5)

        self.play(Write(y1_text))
        self.wait(5)

        #difference y2-y1
        y2_y1 = Line(self.coords_to_point(0,2), self.coords_to_point(0,4), color = RED, size = 0.5)
        y2_y1t1 = TexMobject(r'--').next_to(y2_y1,UP, buff = 0).set_color(RED).scale(0.5)
        y2_y1t2 = TexMobject(r'--').next_to(y2_y1,DOWN, buff = 0).set_color(RED).scale(0.5)

        y2_y1_group = VGroup(y2_y1,y2_y1t1,y2_y1t2)

        y2_y1_text = TexMobject(r'y_2-y_1').next_to(y2_y1_group,LEFT, buff = 0).shift(0.3*LEFT)
        y2_y1_text.set_color(BLUE).scale(0.7)

        self.play(Write(y2_y1_group))
        self.wait(5)

        self.play(Transform(y2_y1_group, y2_y1_group.shift(0.4*LEFT)))
        self.wait(5)

        self.play(TransformFromCopy(b_text, y2_y1_text))
        self.wait(5)

        #final Distance output
        eq_group = VGroup(d,x2_x1_text,y2_y1_text)

        distance = TexMobject(r'd = \sqrt{(x_2-x_1)^2 + (y_2-y_1)^2}').next_to(d, DOWN, buff = 0.5).scale(0.8)
        #distance.scale(0.8)
        distance.align_to(d, LEFT)

        self.play(TransformFromCopy(eq_group, distance))
        self.wait(5)

        #d = TexMobject(r'd = \sqrt{a^2 + b^2}').next_to(d_squ, DOWN, buff = 0.25).align_to(d_squ, LEFT)
