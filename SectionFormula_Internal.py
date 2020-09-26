from manimlib.imports import *

class SectionFormula1(Scene):
    def construct(self):
        back_rect = Rectangle(width = FRAME_WIDTH, height = FRAME_HEIGHT, stroke_width = 0, fill_color = LIGHT_GREY, fill_opacity = 1)
        self.add(back_rect)

        #intro
        show_text = TexMobject(r'Section\ Formula\ (Internal)').set_color(BLACK)
        self.play(Write(show_text), run_time = 3)
        self.wait(10)

        plane = NumberPlane()
        # self.play(ShowCreation(plane))
        # self.wait()

        self.play(Transform(show_text, plane), run_time = 2)
        self.wait(10)

        #creating points
        A = Dot(np.array([1,1,0]))
        text_A = TexMobject(r'A(x_1,y_1)').scale(0.8)
        text_A.shift(2* RIGHT + 0.75 * UP)
        text_A.set_color(BLACK)

        self.play(Write(A), Write(text_A))
        self.wait(10)

        B = Dot(np.array([5,3,0]))
        text_B = TexMobject(r'B(x_2,y_2)').scale(0.8)
        text_B.shift(5.5*RIGHT + 3.25*UP)
        text_B.set_color(BLACK)

        self.play(Write(B),Write(text_B))
        self.wait(10)

        #creating line
        line = Line(np.array([1,1,0]), np.array([5,3,0]), color = RED, stroke_width = 6)
        self.play(ShowCreation(line))
        self.wait(10)

        #creating section point
        C = Dot(np.array([3.5, 2.25, 0]))
        text_C = TexMobject(r'C(x,y)').scale(0.8)
        text_C.shift(2.75*RIGHT + 2.5*UP)
        text_C.set_color(BLACK)

        self.play(Write(C),Write(text_C))
        self.wait(10)

        #section line
        d1 = Line(A,C, color = GREEN, stroke_wifth = 4)
        self.play(ShowCreation(d1))
        self.wait(10)

        #creating ratio
        #m = Dot(np.array([2.5,1.5,0]))
        text_m = TexMobject(r'm_1').scale(0.8)
        text_m.shift(2.5*RIGHT + 1.5*UP)
        text_m.set_color(BLACK)

        self.play(Write(text_m))
        self.wait()

        self.play(Uncreate(d1), run_time = 0.5)
        self.wait(10)

        #section line
        d2 = Line(B,C, color = GREEN, stroke_wifth = 4)
        self.play(ShowCreation(d2))
        self.wait(10)

        #creating ratio
        text_n = TexMobject(r'm_2').scale(0.8)
        text_n.shift(4.5*RIGHT + 2.5*UP)
        text_n.set_color(BLACK)

        self.play(Write(text_n))
        self.wait()

        self.play(Uncreate(d2), run_time = 0.5)
        self.wait(10)

        # creating line for triangle
        line_AD = Line(np.array([1,1,0]), np.array([3.5,1,0]), color = YELLOW, stroke_width = 6)
        line_CD = Line(np.array([3.5,2.25,0]), np.array([3.5,1,0]), color = YELLOW, stroke_width = 6)

        self.play(ShowCreation(line_AD),ShowCreation(line_CD))
        self.wait(10)

        #intersecting point of AD,CD
        D = Dot(np.array([3.5,1,0]))
        text_D = TexMobject(r'D').scale(0.8)
        text_D.next_to(D, RIGHT, buff = 0.125)
        text_D.set_color(BLACK)

        self.play(Write(D), Write(text_D))
        self.wait(10)

        line_CE = Line(np.array([3.5,2.25,0]), np.array([5,2.25,0]), color = YELLOW, stroke_width = 6)
        line_BE = Line(np.array([5,3,0]), np.array([5,2.25,0]), color = YELLOW, stroke_width = 6)

        self.play(ShowCreation(line_CE), ShowCreation(line_BE))
        self.wait(10)

        #intersecting point of CE,BE
        E = Dot(np.array([5,2.25,0]))
        text_E = TexMobject(r'E').scale(0.8)
        text_E.next_to(E, RIGHT, buff = 0.125)
        text_E.set_color(BLACK)

        self.play(Write(E), Write(text_E))
        self.wait(10)

        #creating triangle CAD and CBE
        tri1 = Polygon(np.array([1,1,0]), np.array([3.5,2.25,0]), np.array([3.5,1,0]), fill_opacity = 0.6, fill_color = PURPLE)
        tri2 = Polygon(np.array([3.5,2.25,0]), np.array([5,3,0]), np.array([5,2.25,0]), fill_opacity = 0.6, fill_color = PURPLE)

        group_tri = VGroup(tri1,tri2)

        self.play(ShowCreation(tri1), ShowCreation(tri2))
        self.wait(10)

        #creating writing board
        rect = Rectangle(width = 0.4*FRAME_WIDTH, height = FRAME_HEIGHT- 1, stroke_width = 0, fill_color = BLUE_A, fill_opacity = 0.5)
        rect.to_edge(LEFT)

        #formula
        f1 = TexMobject(r'\frac{AD}{CE}',r'=',r'\frac{CD}{BE} =',r'\frac{AC}{BC}').scale(0.7).set_color(BLACK)
        f1.to_edge(UL)

        self.play(ShowCreation(rect), ReplacementTransform(group_tri, f1))
        self.wait(10)

        #formulas and rect around formulas
        #rect0_f1 = Rectangle(width = f1[0].get_width(), height = f1[0].get_height(), color =RED)
        #rect0_f1.move_to(f1[0])

        rect3_f1 = Rectangle(width = f1[3].get_width(), height = f1[3].get_height(), color =RED)
        rect3_f1.move_to(f1[3])

        self.play(ShowCreation(rect3_f1))
        self.wait(10)

        group_rectf1 = VGroup(f1,rect3_f1)

        f3 = TexMobject(r'\frac{AD}{CE}',r'=',r'\frac{CD}{BE} =',r'\frac{m_1}{m_2}').scale(0.7).set_color(BLACK)
        f3.to_edge(UL)

        self.play(FadeOut(group_rectf1))
        self.wait(10)

        self.play(Write(f3))
        self.wait(10)

        #making lines on axes
        #for x1
        line_x1 = Line(np.array([0, 0, 0]), np.array([1, 0, 0]), color = ORANGE, stroke_width = 4)

        text_line_x1 = TexMobject(r'x_1').scale(0.8).set_color(BLACK)
        text_line_x1.next_to(line_x1, DOWN, buff = 0.10)

        group_line_x1 = VGroup(line_x1,text_line_x1)

        self.play(ShowCreation(line_x1), Write(text_line_x1))
        self.wait(10)

        #for y1
        line_y1 = Line(np.array([1, 0, 0]), np.array([1, 1, 0]), color = ORANGE, stroke_width = 4)

        text_line_y1 = TexMobject(r'y_1').scale(0.8).set_color(BLACK)
        text_line_y1.next_to(line_y1, LEFT, buff = 0.10)

        group_line_y1 = VGroup(line_y1,text_line_y1)

        self.play(ShowCreation(line_y1), Write(text_line_y1))
        self.wait(10)

        #shifting both
        # self.play(ShowCreation(group_line_x1.shift(0.25*DOWN)), ShowCreation(group_line_y1.shift(1.25*LEFT)))
        # self.wait()

        self.play(ApplyMethod(group_line_x1.shift, 0.25*DOWN), ApplyMethod(group_line_y1.shift, 1.25*LEFT))
        self.wait(10)

        #for x
        line_x = Line(np.array([0, 0, 0]), np.array([3.5, 0, 0]), color = ORANGE, stroke_width = 4)

        text_line_x = TexMobject(r'x').scale(0.8).set_color(BLACK)
        text_line_x.next_to(line_x, UP, buff = 0.10)

        # group_line_x = VGroup(line_x,text_line_x)

        self.play(ShowCreation(line_x), Write(text_line_x))
        self.wait(10)

        #for y
        line_y = Line(np.array([3.5, 0, 0]), np.array([3.5, 2.25, 0]), color = ORANGE, stroke_width = 4)

        text_line_y = TexMobject(r'y').scale(0.8).set_color(BLACK)
        text_line_y.next_to(line_y, RIGHT, buff = 0.10)

        group_line_y = VGroup(line_y,text_line_y)

        self.play(ShowCreation(line_y), Write(text_line_y))
        self.wait(10)

        #shifting y
        self.play(ApplyMethod(group_line_y.shift, 3.5*LEFT))
        self.wait(10)

        #for x-x1
        line_xx1 = Line(np.array([1, -0.25, 0]), np.array([3.5, -0.25, 0]), color = PURPLE, stroke_width = 4)

        text_line_xx1 = TexMobject(r'x-x_1').scale(0.8).set_color(BLACK)
        text_line_xx1.next_to(line_xx1, DOWN, buff = 0.10)

        self.play(ShowCreation(line_xx1), Write(text_line_xx1))
        self.wait(10)

        #for y-y1
        line_yy1 = Line(np.array([-0.25, 1, 0]), np.array([-0.25, 2.25, 0]), color = PURPLE, stroke_width = 4)

        text_line_yy1 = TexMobject(r'y-y_1').scale(0.8).set_color(BLACK)
        text_line_yy1.next_to(line_yy1, LEFT, buff = 0.10)

        self.play(ShowCreation(line_yy1), Write(text_line_yy1))
        self.wait(10)

        #value of AD,CD
        f4 = TexMobject(r'\frac{x-x_1}{CE} = \frac{y-y_1}{BE} = \frac{m_1}{m_2}').scale(0.7).set_color(BLACK).next_to(f3,DOWN, buff = 0.25)
        f4.align_to(f3, LEFT)

        self.play(Write(f4))
        self.wait(10)

        #removing all lines
        self.remove(group_line_x1, group_line_y1, group_line_y)
        self.remove(line_xx1, text_line_xx1, line_yy1, text_line_yy1, line_x, text_line_x)

        #line for CE, BE
        #line x2
        line_x2 = Line(np.array([0, 0, 0]), np.array([5, 0, 0]), color = ORANGE, stroke_width = 4)

        text_line_x2 = TexMobject(r'x_2').scale(0.8).set_color(BLACK)
        text_line_x2.next_to(line_x2, UP, buff = 0.10)

        group_line_x2 = VGroup(line_x2,text_line_x2)

        #line y2
        line_y2 = Line(np.array([0, 0, 0]), np.array([0, 3, 0]), color = ORANGE, stroke_width = 4)

        text_line_y2 = TexMobject(r'y_2').scale(0.8).set_color(BLACK)
        text_line_y2.next_to(line_y2, RIGHT, buff = 0.10)

        group_line_y2 = VGroup(line_y2,text_line_y2)

        #for x
        line_x = Line(np.array([0, -0.25, 0]), np.array([3.5, -0.25, 0]), color = ORANGE, stroke_width = 4)

        text_line_x = TexMobject(r'x').scale(0.8).set_color(BLACK)
        text_line_x.next_to(line_x, DOWN, buff = 0.10)

        group_x = VGroup(line_x,text_line_x)

        #for y
        line_y = Line(np.array([-0.25, 0, 0]), np.array([-0.25, 2.25, 0]), color = ORANGE, stroke_width = 4)

        text_line_y = TexMobject(r'y').scale(0.8).set_color(BLACK)
        text_line_y.next_to(line_y, LEFT, buff = 0.10)

        group_y = VGroup(line_y, text_line_y)

        #for x2x
        line_x2x = Line(np.array([3.5, -0.25, 0]), np.array([5, -0.25, 0]), color = PURPLE, stroke_width = 4)
        text_line_x2x = TexMobject(r'x_2-x').scale(0.8).set_color(BLACK)
        text_line_x2x.next_to(line_x2x, DOWN, buff = 0.10)

        group_x2x = VGroup(line_x2x,text_line_x2x)

        #for y2y
        line_y2y = Line(np.array([-0.25, 2.25, 0]), np.array([-0.25, 3, 0]), color = PURPLE, stroke_width = 4)
        text_line_y2y = TexMobject(r'y_2-y').scale(0.8).set_color(BLACK)
        text_line_y2y.next_to(line_y2y, LEFT, buff = 0.10)

        group_y2y = VGroup(line_y2y,text_line_y2y)

        #creating all together

        g = VGroup(group_line_x2, group_line_y2, group_x, group_y, group_x2x, group_y2y)

        self.play(FadeIn(g), run_time = 2)
        self.wait(10)

        #value of CE,BE
        f5 = TexMobject(r'\frac{x-x_1}{x_2-x} = \frac{y-y_1}{y_2-y} = \frac{m_1}{m_2}').scale(0.7).set_color(BLACK).next_to(f4,DOWN, buff = 0.25)
        f5.align_to(f4, LEFT)

        self.play(Write(f5))
        self.wait(10)

        #rectangle around formula
        rect3_f5 = Rectangle(width = f5.get_width(), height = f5.get_height(), color =RED)
        rect3_f5.move_to(f5)

        group_eq5 = VGroup(f5, rect3_f5)

        self.play(ShowCreation(rect3_f5))
        self.wait(10)

        #x formula
        f6 = TexMobject(r'x = \frac{m_1x_2 + m_2x_1}{m_1 + m_2}').scale(0.7).set_color(BLACK).next_to(f5, DOWN, buff = 0.5)
        f6.align_to(f5, LEFT)

        self.play(TransformFromCopy(group_eq5, f6))
        self.wait(10)

        #y formula
        f7 = TexMobject(r'y = \frac{m_1y_2 + m_2y_1}{m_1 + m_2}').scale(0.7).set_color(BLACK).next_to(f6, DOWN, buff = 0.25)
        f7.align_to(f6, LEFT)

        self.play(TransformFromCopy(group_eq5, f7))
        self.wait(10)

        #(x,y) form
        f_final = TexMobject(r'(x,y) = \left(\frac{m_1x_2+m_2x_1}{m_1+m_2}, \frac{m_1y_2+m_2y_1}{m_1+m_2}\right)').scale(0.6)
        f_final.set_color(BLACK).next_to(f7, DOWN, buff = 0.5)
        f_final.align_to(f7, LEFT)

        self.play(Write(f_final))
        self.wait(10)

        #end
        picture = Group(*self.mobjects)
        self.play(Transform(picture, back_rect), run_time = 2)
        self.wait(2)

        img = ImageMobject(
            'OnlyPNG.png',
            color = BLUE,
            height = 3
        )

        self.play(FadeIn(img), run_time = 2)
        self.wait()

        text = Text('Programming & Mathematics Literature', font = 'Brush Script MT', size = 1.2, stroke_color = GOLD_E)
        text.move_to(img)
        text.set_color_by_gradient(GOLD, GREY_BROWN, DARK_GREY)

        self.play(ApplyMethod(img.shift, 2*UP))

        self.play(Write(text), run_time = 2.5)
        self.wait()