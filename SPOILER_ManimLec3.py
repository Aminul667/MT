from manim import *
import numpy as np

##LECTURE 3 - Basic Calculus Animations##

class Lec3Calculus(GraphScene):
    def construct(self):
        self.x_min = -3
        self.x_max = 5
        self.y_min = -10
        self.y_max = 10
        self.x_axis_width = 6
        self.y_axis_height = 7
        self.axes_color = WHITE
        self.graph_origin = LEFT*3+DOWN
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_labeled_nums = list(range(-3,6,1))
        self.y_labeled_nums = list(range(-10,11,2))

        self.setup_axes(animate=True)

        graph = self.get_graph(lambda x : 0.1*(x-3)*(x-1)*(x+1), color = YELLOW_C, x_min = -3, x_max = 5)
        graph_lab = self.get_graph_label(graph, label = "f(x)=0.1(x-3)(x-1)(x+1)", direction = UR).scale(0.4)

        dot = Dot().move_to(self.coords_to_point(-1,0)).set_color(PURPLE_B)
        dot_lab = TexMobject("(-1,0)").set_color(PURPLE).scale(0.7).next_to(dot, UP, buff=0.3)

        deriv = self.get_derivative_graph(graph, color = BLUE)
        deriv_lab = TexMobject("f'(x)").scale(0.4).next_to(deriv, UL).set_color(BLUE)

        slope = self.get_secant_slope_group(-1, graph, dx=0.01, secant_line_length = 4, secant_line_color= GREEN)
        dot2 = Dot().move_to(self.coords_to_point(-1, deriv.underlying_function(-1)))

        h_line = DashedLine(
            self.coords_to_point(0, deriv.underlying_function(-1)),
        self.coords_to_point(-1, deriv.underlying_function(-1)), 
        stroke_width = 5, stroke_color = ORANGE)        

        self.play(LaggedStart(ShowCreation(graph), Write(graph_lab), 
        DrawBorderThenFill(dot), Write(dot_lab)), run_time=3, lag_ratio = 0.75)
        self.wait()

        self.play(ShowCreation(deriv), Write(deriv_lab))
        self.wait()

        self.play(ShowCreation(VGroup(dot2, slope)))
        self.wait()
        self.play(ShowCreation(h_line))
        self.wait()

class Lec3Activity1(GraphScene):
    def construct(self):
        self.x_min = -6
        self.x_max = 3
        self.y_min = -8
        self.y_max = 14
        self.x_axis_width = 5
        self.y_axis_height = 5
        self.axes_color = WHITE
        self.graph_origin = LEFT*2+DOWN
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_labeled_nums = list(range(-6,4,2))
        self.y_labeled_nums = list(range(-8,15,2))

        self.setup_axes(animate=True)

        graph = self.get_graph(lambda x : x**2+3*x-4, x_min = -6, x_max = 3, color = RED_B)
        slope = self.get_secant_slope_group(1, graph, dx=0.01, secant_line_color=GREEN)
        area = self.get_riemann_rectangles(graph, x_min = -5,
        x_max = 2, dx = 1, input_sample_type="center", fill_opacity=0.8)

        title = TextMobject("Quadratic").next_to(self.axes, UP, buff=0.5)

        bonus_line = Line(
            self.coords_to_point(3, graph.underlying_function(3)),
            self.coords_to_point(0, graph.underlying_function(3)),
            stroke_width = 10, stroke_color = PURPLE
        )

        self.play(ShowCreation(graph), AddTextLetterByLetter(title))
        self.wait()
        self.play(GrowFromCenter(slope), run_time=2)
        self.wait()
        self.play(ShowCreation(area), run_time=4)
        self.wait()
        self.play(ShowCreation(bonus_line), run_time=3)
        self.wait()

class Lec3Activity2(Scene):
    def construct(self):
        plane_config = dict(
            axis_config = { 
                "include_tip": True, "include_numbers" : True,
                "include_ticks" : True, "line_to_number_buff" : 0.05,
                "stroke_color" : WHITE, "stroke_width": 0.5,
                "number_scale_val" : 0.4,
                "tip_scale": 0.5,
            },
            x_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : DOWN, "stroke_color" : WHITE,
                "x_min" : -3, "x_max" : 3, "unit_size": 0.4, 
                "numbers_to_show": range(-3, 4, 1),
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : 0, # not y_min
                "x_max" : 10,  # not y_max
                "unit_size": 0.4, "numbers_to_show": range(0, 11, 2),
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.75,
                "stroke_color" : GREEN_C,
            }  
        )
        plane = NumberPlane(**plane_config)

        # shift origin to desired point
        new_origin = LEFT*3+DOWN*2
        plane.shift(new_origin)

        # rotate y labels
        for label in plane.y_axis.numbers:
            label.rotate(-PI/2)

        plane2_config = dict(
            axis_config = { 
                "include_tip": True, "include_numbers" : True,
                "include_ticks" : True, "line_to_number_buff" : 0.05,
                "stroke_color" : WHITE, "stroke_width": 0.5,
                "number_scale_val" : 0.4,
                "tip_scale": 0.5,
            },
            x_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : DOWN, "stroke_color" : WHITE,
                "x_min" : -3, "x_max" : 3, "unit_size": 0.4, 
                "numbers_to_show": range(-3, 4, 1),
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : -6, # not y_min
                "x_max" : 6,  # not y_max
                "unit_size": 0.4, "numbers_to_show": range(-6, 6, 2),
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.75,
                "stroke_color" : GREEN_C,
            }  
        )
        plane2 = NumberPlane(**plane2_config)

        # shift origin to desired point
        new_origin2 = RIGHT*3
        plane2.shift(new_origin2)

        # rotate y labels
        for label in plane2.y_axis.numbers:
            label.rotate(-PI/2)

        ##DEFINING THE STUFF FOR THE SCENE##

        graph1 = plane.get_graph(lambda x : x**2, x_min = -3, x_max = 3, color = RED)
        graph2 = plane2.get_graph(lambda x : 2*x, x_min = -3, x_max = 3, color = YELLOW)

        arrow = Line(plane.get_right(), plane2.get_left()).add_tip()
        text = TextMobject("Differentiate").next_to(arrow, UP, buff=0.2)

        self.play(Write(plane), Write(plane2), run_time=3)
        self.wait()
        self.play(ShowCreation(graph1), ShowCreation(graph2), run_time=2)
        self.wait()

        self.play(GrowFromCenter(arrow), Write(text))
        self.wait()

        def get_secant_line(x):
            x = interpolate(x, x+1, 0.01)
            dx = 0.01
            p1 = plane.input_to_graph_point(x, graph1)
            p2 = plane.input_to_graph_point(x + dx, graph1)
            secant_line = Line(p1, p2, color=PURPLE_A)
            secant_line.scale_in_place(1.5 / secant_line.get_length())
            return secant_line

        def get_deriv_h_line(c):
            return DashedLine(
                plane2.c2p(0, graph2.underlying_function(c)),
                plane2.c2p(c, graph2.underlying_function(c)),
                stroke_width=4, color=WHITE)

        slope = get_secant_line(x=-2)

        h_line = get_deriv_h_line(c=-2)

        explain = TextMobject("Slope=-4 at x=-2").to_edge(UP)

        self.play(ShowCreation(slope))
        self.play(ShowCreation(h_line))
        self.wait()
        self.play(Write(explain))
        self.wait()
