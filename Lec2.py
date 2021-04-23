from manim import *
import numpy as np

class Graph(GraphScene):
    def construct(self):
        self.x_min= -3
        self.x_max= 3
        self.y_min = 0
        self.y_max = 10
        self.x_axis_width = 6
        self.y_axis_height = 6
        self.axes_color = WHITE
        self.graph_origin = 3*DOWN
        self.x_axis_label = '$x$'
        self.y_axis_label = '$y$'
        self.x_labeled_nums = list(range(-3, 4, 1))
        self.y_labeled_nums = list(range(0, 11, 2))

        self.setup_axes(animate = True)

        f = lambda x: x**2

        quadratic = self.get_graph(f, x_min = -3, x_max = 3, color = PURPLE)

        dot = Dot().move_to(self.coords_to_point(0,0))
        dot_lab = MathTex(r'(0,0)').next_to(dot, DOWN)

        area = self.get_riemann_rectangles(quadratic, x_min=-2, x_max=2, dx = 0.2)

        slop = self.get_secant_slope_group(1, quadratic, dx = 1, dx_line_color=RED,df_line_color=GREEN,dx_label='x',df_label='y',include_secant_line=False)

        self.play(ShowCreation(quadratic), ShowCreation(dot), run_time = 3)
        self.wait()
        self.play(Write(dot_lab))
        self.wait()
        self.play(ShowCreation(area), run_time = 3)
        self.wait()
        self.play(ShowCreation(slop), run_time = 2)
        self.play()

class Lec2NPlane(Scene):
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
                "x_min" : -3, "x_max" : 3, "unit_size": 0.5, 
                "numbers_to_show": range(-3, 4, 1),
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : 0, # not y_min
                "x_max" : 10,  # not y_max
                "unit_size": 0.5, "numbers_to_show": range(0, 11, 2),
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.75,
                "stroke_color" : GREEN_C,
            }  
        )
        plane = NumberPlane(**plane_config)

        # shift origin to desired point
        new_origin = LEFT*2+DOWN*3
        plane.shift(new_origin)

        # rotate y labels
        for label in plane.y_axis.numbers:
            label.rotate(-PI/2)

        graph = plane.get_graph(lambda x : x**2, x_min = -3, x_max = 3, color = YELLOW_D)

        self.play(Write(plane))
        self.play(ShowCreation(graph))
        self.wait()

class Lec2Act1(GraphScene):
    def construct(self):
        self.x_min = -2
        self.x_max = 6
        self.y_min = -2
        self.y_max = 8
        self.x_axis_width = 6
        self.y_axis_height = 6
        self.axes_color = BLUE
        self.graph_origin = 2*LEFT+2*DOWN
        self.x_axis_label = '$x$'
        self.y_axis_label = '$y$'
        self.x_labeled_nums = list(range(-2,7,1))
        self.y_labeled_nums = list(range(-2,9,2))

        self.setup_axes(animate=True)

        stfunc = lambda x: x - 1.5
        stline = self.get_graph(stfunc, x_min = -2, x_max = 5, color = RED)

        text = Text('This looks good mate!').move_to(2*UP)

        area = self.get_riemann_rectangles(stline, x_min = 0, x_max = 3, dx = 0.01, input_sample_type='center',start_color=BLUE, end_color=ORANGE, stroke_color=ORANGE,stroke_width=0)

        axis = Axes()

        self.play(ShowCreation(stline), run_time = 3)
        self.wait()
        self.play(Write(text), run_time = 2)
        self.wait()
        self.play(Transform(text, area), run_time = 2)
        self.wait(5)

class Lec2Act2(GraphScene):
    def construct(self):
        self.x_min = -5
        self.x_max = 5
        self.y_min = -6
        self.y_max = 10
        self.x_axis_width = 6
        self.y_axis_height = 5
        self.axes_color = WHITE
        self.graph_origin = LEFT*3
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_labeled_nums = list(range(-5,6,1))
        self.y_labeled_nums = list(range(-6,11,2))

        plane_config = dict(
            axis_config = { 
                "include_tip": False, "include_numbers" : True,
                "include_ticks" : True, "line_to_number_buff" : 0.05,
                "stroke_color" : WHITE, "stroke_width": 0.5,
                "number_scale_val" : 0.4,
                "tip_scale": 0.1,
            },
            x_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : DOWN, "stroke_color" : WHITE,
                "x_min" : -5, "x_max" : 5, "unit_size": 0.3, 
                "numbers_to_show": range(-5, 6, 1),
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : -10, # not y_min
                "x_max" : 10,  # not y_max
                "unit_size": 0.3, "numbers_to_show": range(-10, 11, 2),
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.75,
                "stroke_color" : GREEN_C,
            }  
        )

        self.setup_axes(animate=True)

        pfunc = lambda x:(x+1.5)**2-6

        pgraph = self.get_graph(pfunc,color = GREEN, x_min = -5, x_max = 2)


        plane = NumberPlane(**plane_config)

        # shift origin to desired point
        new_origin = 3*RIGHT
        plane.shift(new_origin)

        # rotate y labels
        # for label in plane.y_axis.numbers:
        #     label.rotate(-PI/2)

        lgraph = plane.get_graph(lambda x : x, x_min = -5, x_max = 3, color = YELLOW_D)

        text = Text('I am keen for some derivatives......Maaaaate!!').scale(0.7).to_edge(DOWN)


        self.play(ShowCreation(pgraph), run_time = 2)
        self.wait()

        self.play(Write(plane))
        self.play(ShowCreation(lgraph))
        self.wait(2)
        self.play(Write(text))
        self.wait()
