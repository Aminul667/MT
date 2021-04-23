from manim import *
import numpy as np

##LEARNING GOAL: To understand the elements within GraphScene, such as
#get_secant_slope_group, and use get_graph method to call functions
#on the axes. Additionally, customise numberplanes to create basic
#2d animations within the self.play() function

class Lec2GraphScene(GraphScene):
    def construct(self):
        self.x_min = -3
        self.x_max = 3
        self.y_min = 0
        self.y_max = 10
        self.x_axis_width = 6
        self.y_axis_height = 6
        self.axes_color = WHITE
        self.graph_origin = LEFT*2+DOWN*3
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_labeled_nums = list(range(-3,4,1))
        self.y_labeled_nums = list(range(0,11,2))

        self.setup_axes(animate=True)
        quadratic = self.get_graph(lambda x : x**2, color = PURPLE_B, x_min = -3, x_max = 3)

        dot = LabeledDot(label = "(2,4)").move_to(self.coords_to_point(2,4))
        dot2 = Dot().move_to(self.coords_to_point(0,0))
        dot2_lab = TexMobject("(0,0)").next_to(dot2, DOWN)

        area = self.get_riemann_rectangles(quadratic, x_min = -2, x_max = 2, dx = 0.1, input_sample_type = "center",
        stroke_width = 0.5, fill_opacity = 0.75, start_color = GREEN_B, end_color = YELLOW_D)


        vert_line = self.get_vertical_line_to_graph(2.5, quadratic, line_class = DashedLine, color = RED)

        slope = self.get_secant_slope_group(-2.5, quadratic, dx = 0.5, dx_line_color=RED, df_line_color=BLUE,
        dx_label="dx", df_label="dy", secant_line_color=ORANGE, secant_line_length=3)

        self.play(ShowCreation(quadratic), Write(dot))
        self.wait()
        self.play(ShowCreation(area), run_time = 4)
        self.play(Write(vert_line))
        self.wait()
        self.play(ShowCreation(slope))
        self.wait()
        self.play(ShowCreation(VGroup(dot2, dot2_lab)))
        self.wait()
        
class Lec2NumberPlane(Scene):
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
