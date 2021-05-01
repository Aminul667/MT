from manim import *
import numpy as np 

class Limit0(GraphScene):
    def construct(self):
        self.x_min = -3
        self.x_max = 3
        self.y_min = -1
        self.y_max = 4
        self.x_axis_width = 7
        self.y_axis_height = 7
        self.axes_color = WHITE
        self.graph_origin = 2.5*DOWN+2*LEFT
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_labeled_nums = list(range(-3,4,1))
        self.y_labeled_nums = list(range(-1,5,1))

        self.setup_axes(animate=True)

        func = lambda x : x**2
        graph = self.get_graph(func, color = ORANGE, x_min = -2, x_max = 2)
        equ = MathTex("f(","x",")=","x^2").shift(self.coords_to_point(4,3))

        #horizontal line
        def get_horizontal_line(ax, color):
            return DashedLine(self.coords_to_point(0, graph.underlying_function(ax)),
            self.coords_to_point((ax), graph.underlying_function(ax)),
            stroke_width = 5, stroke_color = color)

        #vertical line
        def get_vertical_line(ay, color):
            return DashedLine(
                self.coords_to_point(ay,0),
                self.coords_to_point(ay, graph.underlying_function(ay)),
                stroke_width = 5,
                stroke_color = color
            )

        #triangle shape point tracker
        def  get_point_tracker(pt):
            tri = Triangle(color="#FF0000", fill_opacity = 1).scale(0.1)
            tri.shift(self.coords_to_point(pt, -0.5))
            return tri

        #values to track
        p = ValueTracker(-2)
        k = ValueTracker(4)

        #horizontal and vertical line
        trk = always_redraw(lambda : get_point_tracker(p.get_value()))

        h_line = always_redraw(lambda : get_horizontal_line(p.get_value(), BLUE))
        v_line = always_redraw(lambda : get_vertical_line(p.get_value(), BLUE))

        x_text_value = always_redraw(lambda : DecimalNumber(num_decimal_places=1).next_to(equ[1], RIGHT, buff =0).set_value(p.get_value()))

        #new position for ")="
        npos = MathTex(")=").next_to(x_text_value, RIGHT, buff = 0)

        f_text_value = always_redraw(lambda : DecimalNumber(num_decimal_places=2).next_to(npos,RIGHT,buff = 0.25).set_value(graph.underlying_function(p.get_value())))

        self.play(Create(graph), Write(equ), run_time = 4)
        self.wait(5)

        self.play(Create(trk))
        self.wait()

        self.play(
            Create(h_line),
            Create(v_line),
            FadeTransform(equ[1:3],x_text_value),
            FadeIn(npos),
            FadeTransform(equ[3],f_text_value),
            run_time = 2
        )
        self.wait()

        self.play(p.animate.set_value(2), run_time = 5)
        self.wait(5)

        qtn_mark = MathTex('?').scale(7).next_to(equ, DOWN, buff = 0.5).shift(RIGHT + 0.5 * DOWN)

        display_out = Rectangle(BLACK, config["frame_height"], config["frame_width"], fill_opacity=1)

        self.play(Write(qtn_mark), run_time = 2)
        self.wait(3)

        self.play(FadeIn(display_out), run_time = 2)
        self.wait(2)

class Limit1(GraphScene):
    def construct(self):
        self.x_min = -2
        self.x_max = 6
        self.y_min = -2
        self.y_max = 6
        self.x_axis_width = 7
        self.y_axis_height = 7
        self.axes_color = WHITE
        self.graph_origin = DOWN*2 + LEFT*4
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_labeled_nums = list(range(-2,7,2))
        self.y_labeled_nums = list(range(-2,7,2))

        self.setup_axes(animate=True)

        #defining function
        func = lambda x : (x**2-4)/(x-2)

        #graph of the function and equation to show
        graph = self.get_graph(func, color = GREEN, x_min = -2.5, x_max = 4.25)
        equ = MathTex("f(", "x", ")", r"= \frac{x^2-4}{x-2}").shift(self.coords_to_point(7,5))

        equ_xvalue = MathTex("2").move_to(equ[1])
        equ_yvalue = MathTex(r"=\frac{0}{0}").move_to(equ[3], aligned_edge=LEFT)

        cross = Cross(equ_xvalue)

        #dot circle at undefined value
        dotcirc = Circle(
            color = RED, radius = 0.075,
            fill_color=BLACK,
            fill_opacity=1
            ).move_to(self.coords_to_point(1.99, graph.underlying_function(1.99)))

        #horizontal line
        def get_horizontal_line(ax, color):
            return DashedLine(self.coords_to_point(0, graph.underlying_function(ax)),
            self.coords_to_point((ax), graph.underlying_function(ax)),
            stroke_width = 5, stroke_color = color)

        #vertical line
        def get_vertical_line(ay, color):
            return DashedLine(
                self.coords_to_point(ay,0),
                self.coords_to_point(ay, graph.underlying_function(ay)),
                stroke_width = 5,
                stroke_color = color
            )

        #circle to follow
        def get_circle_on_graph(value):
            return Circle(
                radius = 0.05,
                stroke_color = YELLOW,
                fill_color=YELLOW
            ).move_to(self.coords_to_point(value, graph.underlying_function(value)))

        #triangle shape point tracker
        def  get_point_tracker(pt):
            tri = Triangle(color='#FF0000', fill_opacity = 1).scale(0.1)
            tri.shift(self.coords_to_point(pt, -0.5))
            return tri
        
        #values to track
        p = ValueTracker(-2)
        k = ValueTracker(4)

        #horizontal and vertical lines at undefined point
        h_line1 = get_horizontal_line(1.99, BLUE_C)
        v_line1= get_vertical_line(1.99, BLUE_C)

        #horizontal and vertical lines and dot from left
        h_line2 = always_redraw(lambda : get_horizontal_line(p.get_value(), RED_C))
        v_line2 = always_redraw(lambda : get_vertical_line(p.get_value(), RED_C))

        dotcirc2 = always_redraw(lambda : get_circle_on_graph(p.get_value()))

        #horizontal and vertical lines and dot from right
        h_line3 = always_redraw(lambda : get_horizontal_line(k.get_value(), RED_C))
        v_line3 = always_redraw(lambda : get_vertical_line(k.get_value(), RED_C))

        dotcirc3 = always_redraw(lambda : get_circle_on_graph(k.get_value()))

        #triangle pointer
        ptr1 = always_redraw(lambda : get_point_tracker(p.get_value()))
        ptr2 = always_redraw(lambda : get_point_tracker(k.get_value()))

        #LHL function text and value
        ftext1 = MathTex("f(","x", ")", "=").move_to(equ, aligned_edge=LEFT).shift(2*DOWN)
        ftext1_value = always_redraw(lambda : DecimalNumber(num_decimal_places=2).next_to(ftext1, RIGHT).set_value(graph.underlying_function(p.get_value())))

        #RHL function text and value
        ftext2 = MathTex("f(","x", ")", "=").next_to(ftext1, DOWN, buff = 0.5)
        ftext2_value = always_redraw(lambda : DecimalNumber(num_decimal_places=2).next_to(ftext2, RIGHT).set_value(graph.underlying_function(k.get_value())))

        #LH ext and value
        xtext1 = always_redraw(lambda : MathTex(r"x", r"=").next_to(ptr1, 1.1*DOWN+LEFT))
        xtext1_value = always_redraw(lambda : DecimalNumber(num_decimal_places=2).scale(0.7).next_to(xtext1, RIGHT).set_value(p.get_value()))
        
        #RH text and value
        xtext2 = always_redraw(lambda : MathTex(r"x", r"=").next_to(ptr2, 1.1*DOWN+LEFT))
        xtext2_value = always_redraw(lambda : DecimalNumber(num_decimal_places=2).scale(0.7).next_to(xtext2, RIGHT).set_value(k.get_value()))


        self.play(Create(graph), Write(equ))
        self.wait()
        
        self.play(Create(v_line1))
        self.wait()

        self.play(Create(h_line1))
        self.wait()

        self.play(FadeTransform(equ[1], equ_xvalue))
        self.wait()

        self.play(FadeTransform(equ[3], equ_yvalue))
        self.wait()

        self.play(Create(dotcirc), run_time = 3)
        self.wait()

        self.play(Create(cross), run_time = 3)
        self.wait(5)

        self.play(FadeTransform(VGroup(equ_xvalue, equ_yvalue, cross), equ), run_time = 3)
        self.wait()

        #for updated animation
        self.play(Create(h_line2), Create(v_line2), Create(dotcirc2), Create(ptr1))
        self.wait()

        self.play(Write(xtext1), Write(xtext1_value), Write(ftext1), Write(ftext1_value))
        self.wait()

        self.play(p.animate.set_value(1.97), run_time=4)
        self.wait(5)

        self.play(Create(h_line3), Create(v_line3), Create(dotcirc3), Create(ptr2), FadeOut(VGroup(xtext1, xtext1_value)))
        self.wait()

        self.play(Write(xtext2), Write(xtext2_value), Write(ftext2), Write(ftext2_value))
        self.wait()

        self.play(k.animate.set_value(2.01), run_time=4)
        self.wait(5)

        self.play(FadeOut(VGroup(xtext2, xtext2_value)))
        self.wait()

        self.play(CircleIndicate(ftext1[1]), CircleIndicate(ftext2[1]), run_time = 3)
        self.wait(5)

        self.play(ShowPassingFlashAround(ftext1_value), ShowPassingFlashAround(ftext2_value), run_time = 3)
        self.wait(5)

        #left and right x values
        x_at_pointl = MathTex("2").move_to(ftext1[1])
        x_at_pointr = MathTex("2").move_to(ftext2[1])

        #left and right function values
        f_at_xl = MathTex("4").move_to(ftext1_value, aligned_edge=LEFT)
        f_at_xr = MathTex("4").move_to(ftext2_value, aligned_edge=LEFT)

        #LHL and RHL
        lhl = MathTex(r"\lim_{x \to 2^-} f(x)").move_to(ftext1[0], aligned_edge=RIGHT).shift(0.3*RIGHT)
        rhl = MathTex(r"\lim_{x \to 2^+} f(x)").move_to(ftext2[0], aligned_edge=RIGHT).shift(0.3*RIGHT)

        brace_btn_limit = Brace(VGroup(f_at_xl, f_at_xr), direction=RIGHT, color = YELLOW)

        limit = MathTex(r'\lim_{x \to 2}f(x)=4').next_to(brace_btn_limit, RIGHT)

        self.play(
            Transform(VGroup(ftext1[1], ftext2[1]), VGroup(x_at_pointl, x_at_pointr)),
            ReplacementTransform(VGroup(ftext1_value, ftext2_value), VGroup(f_at_xl, f_at_xr))
        )
        self.wait(10)

        self.play(FadeTransform(ftext1[0:3], lhl), run_time = 3)
        self.wait(5)

        self.play(FadeTransform(ftext2[0:3], rhl), run_time = 3)
        self.wait(5)

        self.play(FadeIn(brace_btn_limit))
        self.wait(5)

        self.play(Write(limit), run_time = 2)
        self.wait(5)

        display_out = Rectangle(BLACK, config["frame_height"], config["frame_width"], fill_opacity=1)

        self.play(FadeIn(display_out), run_time = 2)
        self.wait(2)

class Limit2(GraphScene):
    def construct(self):
        self.x_min = -1
        self.x_max = 4
        self.y_min = -1
        self.y_max = 3
        self.x_axis_width = 9
        self.y_axis_height = 6
        self.axes_color = WHITE
        self.graph_origin = DOWN*2 + LEFT*4.5
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        # self.x_labeled_nums = list(range(-1,5,1))
        # self.y_labeled_nums = list(range(-1,4,1))

        self.setup_axes(animate=True)

        func = lambda x : 2*(x-1)**3-3*(x-1)**2+2.5
        graph = self.get_graph(func, color = GREEN, x_min = 0, x_max = 2.68)
        f = MathTex("f(x)").shift(self.coords_to_point(2.25, 3))

        #horizontal line
        def get_horizontal_line(ax, color):
            return DashedLine(
                self.coords_to_point(0, graph.underlying_function(ax)),
                self.coords_to_point((ax), graph.underlying_function(ax)),
                stroke_width = 5,
                stroke_color = color,
                dash_length = 0.1
            )

        #vertical line
        def get_vertical_line(ay, color):
            return DashedLine(
                self.coords_to_point(ay,0),
                self.coords_to_point(ay, graph.underlying_function(ay)),
                stroke_width = 5,
                stroke_color = color,
                dash_length = 0.1
            )

        #brace
        def get_brace(p1, p2, dir):
            return BraceBetweenPoints(p1, p2, direction=dir, color=YELLOW, buff = 0)

        p = ValueTracker(1.25)
        k = ValueTracker(1.75)

        #horizontal and vertical lines at target point
        h_line1 = get_horizontal_line(1.5, BLUE_C)
        v_line1= get_vertical_line(1.5, BLUE_C)

        c = MathTex("c").scale(0.7).shift(self.coords_to_point(1.5, -0.2))
        l = MathTex("L").scale(0.7).shift(self.coords_to_point(-0.2,2))

        #horizontal and vertical lines from left
        h_line2 = always_redraw(lambda : get_horizontal_line(p.get_value(), RED_C))
        v_line2 = always_redraw(lambda : get_vertical_line(p.get_value(), RED_C))

        #horizontal and vertical lines from right
        h_line3 = always_redraw(lambda : get_horizontal_line(k.get_value(), RED_C))
        v_line3 = always_redraw(lambda : get_vertical_line(k.get_value(), RED_C))

        #brace at x left
        x_brace1 = always_redraw(
            lambda : get_brace(
                self.coords_to_point(p.get_value(), 0),
                self.coords_to_point(1.5,0),
                dir = DOWN
            )
        )
        #delta 1
        x_brt1 = x_brace1.get_tex("\delta").scale(0.8).shift(0.1*UP).set_color(RED)

        #delta greter than zero
        delta_gt1 = MathTex(r"0","<").scale(0.6).next_to(x_brt1, LEFT, buff = 0.1)
        delta_gt1[1].set_color(YELLOW)
        delta_gt1[0].set_color(RED)
        
        #brace at x right
        x_brace2 = always_redraw(
            lambda : get_brace(
                self.coords_to_point(k.get_value(), 0),
                self.coords_to_point(1.5,0),
                dir = DOWN
            )
        )
        #delta 2
        x_brt2 = x_brace2.get_tex("\delta").scale(0.8).shift(0.1*UP).set_color(RED)

        #delta greter than zero
        delta_gt2 = MathTex(">", "0").scale(0.6).next_to(x_brt2, RIGHT, buff = 0.1)
        delta_gt2[0].set_color(YELLOW)
        delta_gt2[1].set_color(RED)

        #brace at y above
        y_brace1 = always_redraw(
            lambda : get_brace(
                self.coords_to_point(0, graph.underlying_function(p.get_value())),
                self.coords_to_point(0, graph.underlying_function(1.5)),
                dir = LEFT
            )
        )
        #epsilon 1
        y_brt1 = y_brace1.get_tex("\epsilon").scale(0.8).shift(0.1*RIGHT).set_color(RED)

        #epsilon greter than zero
        epsolon_gt1 = MathTex("0", "<").scale(0.6).next_to(y_brt1, LEFT, buff = 0.1)
        epsolon_gt1[0].set_color(RED)
        epsolon_gt1[1].set_color(YELLOW)

        #brace at y below
        y_brace2 = always_redraw(
            lambda : get_brace(
                self.coords_to_point(0, graph.underlying_function(1.5)),
                self.coords_to_point(0, graph.underlying_function(k.get_value())),
                dir = LEFT
            )
        )
        y_brt2 = y_brace2.get_tex("\epsilon").scale(0.8).shift(0.1*RIGHT).set_color(RED)

        #epsilon greter than zero
        epsolon_gt2 = MathTex("0", "<").scale(0.6).next_to(y_brt2, LEFT, buff = 0.1)
        epsolon_gt2[0].set_color(RED)
        epsolon_gt2[1].set_color(YELLOW)


        self.play(Create(graph), Write(f), run_time = 3)
        self.wait(5)

        self.play(Create(v_line1), run_time = 2)
        self.wait()

        self.play(FadeIn(c))
        self.wait(5)

        self.play(Create(h_line1), run_time = 2)
        self.wait(5)

        self.play(FadeIn(l))
        self.wait(5)

        self.play(
            Create(v_line2),
            Create(h_line2),
            Create(v_line3),
            Create(h_line3),
            run_time = 3
        )
        # self.wait()

        # self.play(
        #     Create(v_line3),
        #     Create(h_line3),
        #     run_time = 3
        # )
        self.wait(5)

        self.play(Create(x_brace1), Create(x_brace2), Create(x_brt1), Create(x_brt2))
        self.wait(5)

        self.play(Create(y_brace1), Create(y_brace2))
        self.wait(5)

        self.play(Create(y_brt1), Create(y_brt2))
        self.wait(5)

        self.play(WiggleOutThenIn(VGroup(x_brt1, x_brt2, y_brt1, y_brt2)), run_time = 4)
        self.wait(5)

        self.play(FadeIn(VGroup(delta_gt1, delta_gt2, epsolon_gt1, epsolon_gt2)))
        self.wait(5)

        self.play(p.animate.set_value(1.5), k.animate.set_value(1.5), run_time = 4)
        self.wait(5)

        self.play(p.animate.set_value(1.25), k.animate.set_value(1.75), run_time = 2)
        self.wait(5)

        ## animation for line at x

        #double arrow between interval
        double_arrow = DoubleArrow(
            self.coords_to_point(1.25, 0),
            self.coords_to_point(1.75, 0),
            buff = 0
        ).shift(0.25*UP)

        t = ValueTracker(0.25)
        u = ValueTracker(1.35)

        #horizontal and vertical line at x
        h_line_at_x = always_redraw(lambda : get_horizontal_line(t.get_value(), "#FF0000"))
        v_line_at_x = always_redraw(lambda : get_vertical_line(t.get_value(), "#FF0000"))

        fx = always_redraw(
            lambda : MathTex(r'f(x)').scale(0.6).set_color('#99ff00').next_to(h_line_at_x,LEFT, buff = -0.55)
        )

        xt = always_redraw(
            lambda : MathTex(r'x').scale(0.6).set_color('#99ff00').next_to(v_line_at_x,DOWN, buff = -0.2)
        )

        # xtext1 = always_redraw(lambda : MathTex(r"x", r"=").next_to(ptr1, 1.1*DOWN+LEFT))

        brace_x = always_redraw(
            lambda : get_brace(
                self.coords_to_point(1.5, 0),
                self.coords_to_point(u.get_value(), 0),
                dir = UP
            )
        )

        dist_x = MathTex("0","<","|","x","-c|","<",r"\delta").shift(self.coords_to_point(4,2.5))
        dist_x[3].set_color('#99ff00')
        dist_x[0].set_color(RED)
        dist_x[1].set_color(YELLOW)
        dist_x[5].set_color(YELLOW)
        dist_x[6].set_color(RED)

        brace_y = always_redraw(
            lambda : get_brace(
                self.coords_to_point(0, graph.underlying_function(1.5)),
                self.coords_to_point(0, graph.underlying_function(u.get_value())),
                dir = RIGHT
            )
        )

        dist_y = MathTex("|","f(x)","-L|","<",r"\epsilon").next_to(dist_x, DOWN)
        dist_y[1].set_color('#99ff00')
        dist_y[3].set_color(YELLOW)
        dist_y[4].set_color(RED).scale(1.2)

        rect = Rectangle(color = BLUE, height=1.5, width=3, fill_opacity = 1).next_to(dist_y, DOWN)
        rect.set_fill("#343434")

        xc = MathTex("x=c").move_to(rect, UL).shift(0.2*DOWN+0.2*RIGHT)
        xmc = MathTex("|x-c|=0").next_to(xc, DOWN, aligned_edge=LEFT)

        self.play(FadeIn(double_arrow), run_time = 2)
        self.wait()

        self.play(FadeOut(double_arrow))
        self.wait()

        self.play(Create(h_line_at_x), Create(v_line_at_x), Write(xt), Write(fx))
        self.wait()
        

        self.play(t.animate.set_value(1.35), run_time = 4)
        self.wait(5)

        self.play(Create(brace_x), run_time = 2)
        self.wait(4)

        self.play(TransformFromCopy(brace_x, dist_x[2:]), run_time = 3)
        self.wait(5)

        self.play(ShowPassingFlashAround(dist_x[2]), run_time = 2)
        self.wait(3)

        self.play(Create(brace_y), run_time = 2)
        self.wait(5)

        self.play(TransformFromCopy(brace_y, dist_y), run_time = 3)
        self.wait(5)

        self.play(t.animate.set_value(1.65), u.animate.set_value(1.65), run_time = 3)
        self.play(t.animate.set_value(1.3), u.animate.set_value(1.3), run_time = 3)
        self.wait(5)

        self.play(
            t.animate.set_value(1.5),
            u.animate.set_value(1.5),
            DrawBorderThenFill(rect),
            Write(xc),
            run_time = 3
        )
        self.wait(5)

        self.play(Write(xmc), run_time = 2)
        self.wait(5)

        self.play(
            FadeTransform(VGroup(rect, xc, xmc), dist_x[0:2]),
            t.animate.set_value(1.32),
            u.animate.set_value(1.32),
            run_time = 3
        )
        self.wait(5)

        self.play(t.animate.set_value(1.4), u.animate.set_value(1.4), run_time = 4)
        self.wait(5)

        #definition of limit
        display = Rectangle(color = BLUE, height = 3, width=5, fill_opacity = 1).next_to(dist_y, DOWN, buff = 0.6).shift(0.5*RIGHT)
        display.set_fill("#343434")

        limit = MathTex(r"\lim_{x \to c}f(x) = L").move_to(display, UL).shift(0.2*DOWN+0.2*RIGHT)

        c1 = MathTex(r"1.\ \text{if}\ ", r"\epsilon", ">", "0", "\ \Rightarrow \ ", r"\delta", ">", "0").scale(0.8).next_to(limit, DOWN, aligned_edge=LEFT)

        c1[1].set_color(RED)
        c1[2].set_color(YELLOW)
        c1[3].set_color(RED)
        c1[5].set_color(RED)
        c1[6].set_color(YELLOW)
        c1[7].set_color(RED)

        c2 = MathTex(r"2.\ \text{if}\ ", "0", "<", "|x-c|","<", r"\delta").scale(0.8).next_to(c1, DOWN, aligned_edge=LEFT)

        c2[1].set_color(RED)
        c2[2].set_color(YELLOW)
        c2[4].set_color(YELLOW)
        c2[5].set_color(RED)

        c3 = MathTex(r"\text{then}\ ", "|f(x)-L|", "<", r"\epsilon").scale(0.8).next_to(c2, DOWN, aligned_edge=LEFT)
        c3.shift(0.6*RIGHT)

        c3[2].set_color(YELLOW)
        c3[3].set_color(RED)


        self.play(DrawBorderThenFill(display), run_time = 2)
        self.wait(5)

        self.play(Write(limit), run_time = 2)
        self.wait(2)

        self.play(FadeIn(c1), run_time = 2)
        self.wait(5)

        self.play(FadeIn(c2), run_time = 2)
        self.wait(5)

        self.play(FadeIn(c3), run_time = 2)
        self.wait(5)

        frame_rect = Rectangle(BLACK, config["frame_height"], config["frame_width"], fill_opacity=0.9)

        #definition of limit
        def1 = Tex(r"Let $f(x)$ be a function defined on the interval that contains $x = c$.").scale(0.7)

        def2 = Tex(r"Then $\displaystyle\lim_{x \to c}f(x)=L$ if for every number ", r"$\epsilon$", r"$>$", r"$0$", r" there exists some real number ", r"$\delta$", r"$>$", r"$0$", r" so that if").scale(0.7).next_to(def1, DOWN)

        def2[1].set_color(RED)
        def2[2].set_color(YELLOW)
        def2[3].set_color(RED)
        def2[5].set_color(RED)
        def2[6].set_color(YELLOW)
        def2[7].set_color(RED)

        def3 = Tex(r"$0$", r"$<$", r"$|x-c|$",r"$<$", r"$\delta$", r" then ", r"$|f(x)-L|$", r"$<$", r"$\epsilon$").scale(0.7).next_to(def2, DOWN)

        def3[0].set_color(RED)
        def3[1].set_color(YELLOW)
        def3[3].set_color(YELLOW)
        def3[4].set_color(RED)

        def3[7].set_color(YELLOW)
        def3[8].set_color(RED)

        def_group = VGroup(def1, def2, def3).move_to(frame_rect)

        self.play(FadeIn(frame_rect), FadeIn(def_group), run_time = 3)
        self.wait(5)

        # display_out = Rectangle(BLACK, config["frame_height"], config["frame_width"], fill_opacity=1)

        # self.play(FadeIn(display_out), run_time = 2)
        # self.wait(2)


# class Indicator(GraphScene):
#     def construct(self):
#         t1 = MathTex("3.97")
#         t2 = MathTex("4.01").next_to(t1, DOWN)

#         self.add(t1,t2)
#         self.play(WiggleOutThenIn(t1), WiggleOutThenIn(t2), run_time = 5)
#         self.wait()

# class Test(Scene):
#     def construct(self):
#         text = Text("Hello, World!")
#         rect = Rectangle(
#             BLACK, config["frame_height"], config["frame_width"], fill_opacity=0.8
#         )
#         text2 = Text("o").move_to(text.chars[4])
#         self.add(text)
#         self.play(FadeIn(rect), FadeIn(text2))

# class TestC(GraphScene):
#     def construct(self):
#         frame_rect = Rectangle(BLACK, config["frame_height"], config["frame_width"], fill_opacity=0.9)

#         def1 = Tex(r"Let $f(x)$ be a function defined on the interval that contains $x = c$.").scale(0.7)

#         def2 = Tex(r"Then $\displaystyle\lim_{x \to c}f(x)=L$ if for every number ", r"$\epsilon$", r"$>$", r"$0$", r" there exists some real number ", r"$\delta$", r"$>$", r"$0$", r" so that if").scale(0.7).next_to(def1, DOWN)

#         def2[1].set_color(RED)
#         def2[2].set_color(YELLOW)
#         def2[3].set_color(RED)
#         def2[5].set_color(RED)
#         def2[6].set_color(YELLOW)
#         def2[7].set_color(RED)

#         def3 = Tex(r"$0$", r"$<$", r"$|x-c|$",r"$<$", r"$\delta$", r" then ", r"$|f(x)-L|$", r"$<$", r"$\epsilon$").scale(0.7).next_to(def2, DOWN)

#         def3[0].set_color(RED)
#         def3[1].set_color(YELLOW)
#         def3[3].set_color(YELLOW)
#         def3[4].set_color(RED)

#         def3[7].set_color(YELLOW)
#         def3[8].set_color(RED)

#         def_group = VGroup(def1, def2, def3).move_to(frame_rect)


#         self.play(FadeIn(frame_rect), run_time = 3)
#         self.wait()

#         self.add(def_group)
#         self.wait()
        


