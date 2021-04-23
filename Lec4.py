from manim import *
import numpy as np 

class Lec4Updaters(Scene):
    def construct(self):

        text = Tex('Follow Me').scale(0.8).set_color(BLUE).to_edge(UL)
        num = MathTex('ln(2) = 0.69').next_to(text, RIGHT).set_color(RED)

        #Updater

        num.add_updater(lambda x: x.next_to(text, RIGHT))

        self.play(ShowCreation(text), ShowCreation(num))
        self.wait()
        self.play(text.animate.shift(RIGHT*4), run_time = 3)
        self.wait()

        square = Square(
            stroke_color=BLUE,
            fill_color=GREY,
            fill_opacity=0.75
        ).scale(0.75)
        fol = Tex('Follower').scale(0.5).move_to(square.get_center()).set_color(PINK)
        fol.add_updater(lambda x: x.move_to(square.get_center()))

        self.play(DrawBorderThenFill(square), Write(fol))
        self.wait()
        self.play(square.animate.to_edge(DR), run_time = 3)
        self.wait()

class Lec4ValueTracker(Scene):
    def construct(self):

        k = ValueTracker(2)

        display = DecimalNumber(num_decimal_places=2).set_color(RED)
        display.set_value(k.get_value())
        display.add_updater(lambda x : x.set_value(k.get_value()))

        self.play(ShowCreation(display))
        self.wait()
        self.play(k.animate.set_value(5), display.animate.to_edge(UR), run_time = 5)
        self.wait()

class Lec4MoreUpdaters(Scene):
    def construct(self):

        circ = Circle(
            stroke_color=BLUE,
            stroke_width=4,
            fill_color = WHITE,
            fill_opacity=0.8,
            radius = 2
            )

        dot1 = Dot().move_to(circ.get_top())
        dot2 = Dot().move_to(circ.get_left())
        dot3 = Dot().move_to(circ.get_right())

        tri = Polygon(
            dot1.get_center(),
            dot2.get_center(),
            dot3.get_center(),
            stroke_color = YELLOW,
            stroke_width=5,
            fill_color = PURPLE,
            fill_opacity=0.8
            )

        self.play(DrawBorderThenFill(circ), ShowCreation(VGroup(dot1, dot2, dot3)))
        self.wait()
        self.play(DrawBorderThenFill(tri))
        self.wait()

        tri.add_updater(
            lambda x: x.become(Polygon(dot1.get_center(), dot2.get_center(), dot3.get_center(), stroke_color = YELLOW, stroke_width = 5, fill_color = RED_B, fill_opacity = 0.8))
        )

        self.play(MoveAlongPath(dot1, circ), run_time = 6)
        self.wait()

class Lec4Act1(Scene):
    def construct(self):
        
        text = TextMobject("Mate, follow me!").to_edge(UR)
        p = ValueTracker(4)
        num = DecimalNumber(num_decimal_places = 3).set_value(4).next_to(text, LEFT, buff=0.5)

        num.add_updater(lambda f : f.set_value(p.get_value()))
        num.add_updater(lambda g : g.next_to(text, LEFT, buff=0.5))

        self.play(ShowCreation(num), Write(text))
        self.wait()
        self.play(p.animate.set_value(-6), text.animate.move_to(ORIGIN),
        run_time=4)
        self.wait()

class Lec4Act2(GraphScene):
    def construct(self):
        self.x_min = -3
        self.x_max = 3
        self.y_min = -7
        self.y_max = 7
        self.x_axis_width = 5
        self.y_axis_height = 5
        self.axes_color = WHITE
        self.graph_origin = LEFT*2
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_labeled_nums = list(range(-3,4,1))
        self.y_labeled_nums = list(range(-6, 7,2))

        self.setup_axes(animate=True)

        graph = self.get_graph(lambda x : 2*x-1, x_min = -3, x_max = 3, color = BLUE)
        dot = Dot().move_to(self.coords_to_point(-3, -7))
        text = TextMobject("Dot Follower").scale(0.5).next_to(dot, UP, buff=0.5)

        text.add_updater(lambda j : j.next_to(dot, UP, buff=0.5))

        square = Square(fill_color = GREEN, fill_opacity = 0.75).scale(2).to_edge(RIGHT)
        outtext = TextMobject("Keen for Calculus Updaters").scale(0.4).move_to(square.get_center())

        self.play(ShowCreation(graph), DrawBorderThenFill(dot), Write(text))
        self.wait()
        self.play(MoveAlongPath(dot, graph), run_time=4)
        self.wait()

        self.play(ShowCreation(square), Write(outtext))
        self.wait()
        self.play(square.animate.scale(10), FadeOut(VGroup(
            graph, dot, text, outtext, self.axes)), run_time=3)