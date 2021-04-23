from manim import *
import numpy as np

class Lec5Calc(GraphScene):
    def construct(self):

        self.x_min = -5
        self.x_max = 5
        self.y_min = -10
        self.y_max = 25
        self.x_axis_width = 7
        self.y_axis_height = 6
        self.axes_color = WHITE
        self.graph_origin = DOWN*2
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_labeled_nums = list(range(-5,6,1))
        self.y_labeled_nums = list(range(-10,26,5))

        self.setup_axes(animate=True)

        ##USING THE ALWAYS_REDRAW UPDATER TO Groups OF STUFF##

        k = ValueTracker(-5) #Tracking the graph end value
        r = ValueTracker(-2) #Tracking the tangent to curve
        t = ValueTracker(-3) #Tracking the end value of area under curve

        graph = always_redraw(lambda :
        self.get_graph(lambda x : x**2, x_min = -5, x_max = k.get_value(), color = PURPLE))

        slope = always_redraw(lambda :
        self.get_secant_slope_group(r.get_value(), graph, dx=0.01, secant_line_color=GREEN,
        secant_line_length=2.5))

        area = always_redraw(lambda :
        self.get_riemann_rectangles(graph, dx=0.1, x_min = -3, x_max = t.get_value(),
        input_sample_type="center"))

        self.add(graph)
        self.play(k.animate.set_value(3), run_time=3)
        self.add(slope)
        self.play(r.animate.set_value(2), run_time=2)
        self.wait()
        self.play(r.animate.set_value(-1), run_time=3)
        self.add(area)
        self.play(t.animate.set_value(1), run_time=4)

        ##ALTERNATIVELY, you can define you own shit. And use always_redraw
        #Note, the input value of your function doesn't need to be the same name as your value_tracker

        def get_horizontal_line_to_graph(penis):
            return DashedLine(self.coords_to_point(0, graph.underlying_function(penis)),
            self.coords_to_point((penis), graph.underlying_function(penis)),
            stroke_width = 5, stroke_color = BLUE_C)

        def get_dot_on_plane(koonts):
            return Circle(radius = 0.075, stroke_color = YELLOW, fill_color = BLUE, fill_opacity = 0.6
            ).move_to(self.coords_to_point(koonts, graph.underlying_function(koonts)))    
        
        p = ValueTracker(-3) #Tracking the horiz line and the dot

        h_line = always_redraw(lambda : get_horizontal_line_to_graph(p.get_value()))
        dot = always_redraw(lambda : get_dot_on_plane(p.get_value()))

        self.play(ShowCreation(h_line), DrawBorderThenFill(dot))
        self.wait()
        self.play(p.animate.set_value(2), run_time=4)
        self.wait()

class Lec5CalcOnPlane(Scene):
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

        def get_secant_slope(tuna):
            dx = 0.01
            p1 = plane.coords_to_point(tuna, graph.underlying_function(tuna))
            p2 = plane.coords_to_point(tuna + dx, graph.underlying_function(tuna + dx))
            secant = Line(p1, p2, color = GREEN_B)
            secant.scale_in_place(2 / secant.get_length())
            return secant

        j = ValueTracker(-1)

        slope = always_redraw(lambda : get_secant_slope(j.get_value()))

        self.add(slope)
        self.play(j.animate.set_value(2), run_time=4)
        self.wait()

class Lec5Activity1(GraphScene):
    def construct(self):

        def get_dot_on_plane(koonts):
            return Circle(radius = 0.075, stroke_color = YELLOW, fill_color = BLUE, fill_opacity = 0.6
            ).move_to(self.coords_to_point(koonts, graph.underlying_function(koonts))) 


        self.x_min = -5
        self.x_max = 4
        self.y_min = -50
        self.y_max = 30
        self.x_axis_width = 10
        self.y_axis_height = 6
        self.axes_color = WHITE
        self.graph_origin = UP
        self.x_axis_label = "$x$"
        self.y_axis_label = "$y$"
        self.x_labeled_nums = list(range(-5,5,1))
        self.y_labeled_nums = list(range(-50,31,10))

        self.setup_axes(animate=True)

        graph = self.get_graph(lambda x : (x+4)*(x-1)*(x-3), x_min = -5, x_max = 4, color = BLUE)

        k = ValueTracker(-4) #Tracking the slope, coord and vert_line

        slope = always_redraw(lambda :
        self.get_secant_slope_group(k.get_value(), graph, dx=0.01,
        secant_line_color = GREEN_B, secant_line_length=2))

        v_line = always_redraw(lambda : 
        self.get_vertical_line_to_graph(k.get_value(), graph))

        dot = always_redraw(lambda : get_dot_on_plane(k.get_value()))

        area = always_redraw(lambda :
        self.get_riemann_rectangles(graph, x_min = -4, x_max = k.get_value(),
        dx = 0.1, input_sample_type = "center"))

        self.play(ShowCreation(graph), run_time=3)
        self.add(dot, slope, v_line)
        self.play(k.animate.set_value(4), run_time=3)
        self.wait()
        self.play(k.animate.set_value(-4), run_time=3)
        self.wait()
        self.add(area)
        self.play(k.animate.set_value(4), run_time=5)
        self.wait()

class Lec5Activity2(Scene):
    def construct(self):

        #two number planes need to be defined, side by side. soooooo, this will look sticky.

        plane1_config = dict(
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
                "x_min" : -3, "x_max" : 3, "unit_size": 4/6, 
                "numbers_to_show": range(-3, 4, 1),
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : 0, # not y_min
                "x_max" : 15,  # not y_max
                "unit_size": 1/5, "numbers_to_show": range(0, 16, 3),
            },
            background_line_style = {
                "stroke_width" : 1, "stroke_opacity" : 0.75,
                "stroke_color" : GREEN_C,
            }  
        )
        plane1 = NumberPlane(**plane1_config)

        # shift origin to desired point
        new_origin1 = LEFT*4
        plane1.shift(new_origin1)

        # rotate y labels
        for label in plane1.y_axis.numbers:
            label.rotate(-PI/2)

        ##NOW, HERE IS PLANE NUMBER ##

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
                "x_min" : -3, "x_max" : 3, "unit_size": 4/6, 
                "numbers_to_show": range(-3, 4, 1),
            },
            y_axis_config = {
                "exclude_zero_from_default_numbers": True,
                "label_direction" : UR, "stroke_color" : WHITE,
                "x_min" : 0, # not y_min
                "x_max" : 15,  # not y_max
                "unit_size": 1/5, "numbers_to_show": range(0, 16, 3),
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

        ##DEFINING MY FUNCTIONS AND TITLES##

        graph1 = plane1.get_graph(lambda x : np.exp(x), x_min = -3, x_max = 2.5, color = BLUE)
        graph2 = plane2.get_graph(lambda x : np.exp(x), x_min = -3, x_max = 2.5, color = RED)

        title1 = Tex("Function").next_to(plane1, UP, buff=0.25)
        title2 = Tex("Derivative").next_to(plane2, UP, buff=0.25)

        #now, I am going to define my animating slopes/dot/shit for number plane#
        #note, change plane to plane1, or plane2 etc. whatever the name of your num plane is :)
        #note, same shit for graph.underlying_function. use graph1.underlying_function etc....

        w = ValueTracker(-3) #Tracking the slope, dot1, dot2 and horiz_line

        def get_secant_on_plane1(tuna):
            dx = 0.01
            p1 = plane1.coords_to_point(tuna, graph1.underlying_function(tuna))
            p2 = plane1.coords_to_point(tuna + dx, graph1.underlying_function(tuna + dx))
            secant = Line(p1, p2, color = GREEN_B)
            secant.scale_in_place(2 / secant.get_length())
            return secant

        def get_dot_on_plane1(fork):
            return Dot().move_to(plane1.coords_to_point(fork, graph1.underlying_function(fork)))

        def get_h_line_to_plane2(penis):
            return Line(plane2.coords_to_point(0, graph2.underlying_function(penis)),
            plane2.coords_to_point(penis, graph2.underlying_function(penis)),
            stroke_width = 6, stroke_color = YELLOW)
        
        def get_dot_on_plane2(fork):
            return Dot().move_to(plane2.coords_to_point(fork, graph2.underlying_function(fork)))

        slope = always_redraw(lambda : get_secant_on_plane1(w.get_value()))
        dot1 = always_redraw(lambda : get_dot_on_plane1(w.get_value()))
        dot2 = always_redraw(lambda : get_dot_on_plane2(w.get_value()))
        horiz_line = always_redraw(lambda : get_h_line_to_plane2(w.get_value()))

        self.play(LaggedStart(Write(plane1), Write(plane2),
        Write(title1), Write(title2), lag_ratio = 0.5, run_time=4))
        self.play(ShowCreation(graph1), ShowCreation(graph2))
        self.wait()
        self.add(slope, dot1, dot2, horiz_line)
        self.play(w.animate.set_value(2.5), run_time=7)
        self.wait()

        final_message = Tex("Calculus Animation by Brian Amedee").scale(0.7
        ).shift(DOWN)

        self.play(Write(final_message), run_time=3)
        self.wait()
