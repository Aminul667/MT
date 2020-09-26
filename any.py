from manimlib.imports import *
 
# class FunctionTracker(Scene):
#     def construct(self):
#         # f(x) = x**2
#         fx = lambda x: x.get_value()**2
#         # ValueTrackers definition
#         x_value = ValueTracker(0)
#         fx_value = ValueTracker(fx(x_value))
#         # DecimalNumber definition
#         x_tex = DecimalNumber(x_value.get_value()).add_updater(lambda v: v.set_value(x_value.get_value()))
#         fx_tex = DecimalNumber(fx_value.get_value()).add_updater(lambda v: v.set_value(fx(x_value)))
#         # TeX labels definition
#         x_label = TexMobject("x = ")
#         fx_label = TexMobject("x^2 = ")
#         # Grouping of labels and numbers
#         group = VGroup(x_tex,fx_tex,x_label,fx_label).scale(2.6)
#         VGroup(x_tex, fx_tex).arrange_submobjects(DOWN,buff=3)
#         # Align labels and numbers
#         x_label.next_to(x_tex,LEFT, buff=0.7,aligned_edge=x_label.get_bottom())
#         fx_label.next_to(fx_tex,LEFT, buff=0.7,aligned_edge=fx_label.get_bottom())

#         self.add(group.move_to(ORIGIN))
#         self.wait(3)
#         self.play(
#             x_value.set_value,30,
#             rate_func=linear,
#             run_time=10
#             )
#         self.wait()
#         self.play(
#             x_value.set_value,0,
#             rate_func=linear,
#             run_time=10
#             )
#         self.wait(3)


# class manim_examples(GraphScene):
#     def construct(self):
#         self.setup_axes()

#         def graph_to_be_drawn(x):
#             return (1 / 2) * x ** 2 - 3

#         vt = ValueTracker(3)

#         graph_1 = self.get_graph(graph_to_be_drawn, x_min=-2)

#         def moving_dot():
#             x = vt.get_value()
#             d = Dot().move_to(self.coords_to_point(x, graph_to_be_drawn(x)))
#             return d

#         dd = always_redraw(moving_dot)

#         self.add(dd, graph_1)
#         self.play(vt.set_value, 4, rate_func=linear, run_time=5)
#         self.wait()


# class MovingDot(GraphScene):
#     CONFIG = {
#         "x_axis_label": "",
#         "y_axis_label": "",
#         "x_min": -20,
#         "x_max": 20,
#         "x_tick_frequency": 10,
#         "x_axis_width": FRAME_WIDTH - 2.5,

#         "y_axis_height": FRAME_HEIGHT - 1,
#         "y_min": -10,
#         "y_max": 50,
#         "y_tick_frequency": 10,
#         "graph_origin": DOWN * 2,
#     }

#     def construct(self):
#         self.setup_axes()
#         graph = self.get_graph(lambda x: 0.1 * (x + 7) * (x - 2) * (x - 7), x_min=-15, x_max=15)

#         ss = self.get_secant_slope_group(
#             x = -0.5,
#             graph = func,
#             dx = -2,
#         )

#         start_x = -10
#         end_x = 10
#         tracker = ValueTracker(start_x)  # starting point of x

#         ctp = self.coords_to_point
#         dot_x = tracker.get_value
#         func = graph.underlying_function
#         moving_dot = always_redraw(lambda: Dot(ctp(dot_x(), func(dot_x())), radius=0.1, color=RED, ))

#         self.add(graph, moving_dot)
#         self.play(tracker.set_value, end_x, run_time=5)
#         self.wait()

# class ZoomedSceneExample(ZoomedScene):
#     CONFIG = {
#         "zoom_factor": 0.3,
#         "zoomed_display_height": 1,
#         "zoomed_display_width": 6,
#         "image_frame_stroke_width": 20,
#         "zoomed_camera_config": {
#             "default_frame_stroke_width": 3,
#         },
#     }

#     def construct(self):
#         # Set objects
#         dot = Dot().shift(UL*2)

#         image=ImageMobject(np.uint8([[ 0, 100,30 , 200],
#                                      [255,0,5 , 33]]))
#         image.set_height(7)
#         frame_text=TextMobject("Frame",color=PURPLE).scale(1.4)
#         zoomed_camera_text=TextMobject("Zommed camera",color=RED).scale(1.4)

#         self.add(image,dot)

#         # Set camera
#         zoomed_camera = self.zoomed_camera
#         zoomed_display = self.zoomed_display
#         frame = zoomed_camera.frame
#         zoomed_display_frame = zoomed_display.display_frame

#         frame.move_to(dot)
#         frame.set_color(PURPLE)

#         zoomed_display_frame.set_color(RED)
#         zoomed_display.shift(DOWN)

#         # brackground zoomed_display
#         zd_rect = BackgroundRectangle(
#             zoomed_display,
#             fill_opacity=0,
#             buff=MED_SMALL_BUFF,
#         )

#         self.add_foreground_mobject(zd_rect)

#         # animation of unfold camera
#         unfold_camera = UpdateFromFunc(
#             zd_rect,
#             lambda rect: rect.replace(zoomed_display)
#         )

#         frame_text.next_to(frame,DOWN)

#         self.play(
#             ShowCreation(frame),
#             FadeInFromDown(frame_text)
#         )

#         # Activate zooming
#         self.activate_zooming()

#         self.play(
#             # You have to add this line
#             self.get_zoomed_display_pop_out_animation(),
#             unfold_camera
#         )

#         zoomed_camera_text.next_to(zoomed_display_frame,DOWN)
#         self.play(FadeInFromDown(zoomed_camera_text))

#         # Scale in     x   y  z
#         scale_factor=[0.5,1.5,0]

#         # Resize the frame and zoomed camera
#         self.play(
#             frame.scale,                scale_factor,
#             zoomed_display.scale,       scale_factor,
#             FadeOut(zoomed_camera_text),
#             FadeOut(frame_text)
#         )

#         # Resize the frame
#         self.play(
#             frame.scale,3,
#             frame.shift,2.5*DOWN
#         )

#         # Resize zoomed camera
#         self.play(
#             ScaleInPlace(zoomed_display,2)
#         )


#         self.wait()

#         self.play(
#             self.get_zoomed_display_pop_out_animation(),
#             unfold_camera,
#             # -------> Inverse
#             rate_func=lambda t: smooth(1-t),
#         )
#         self.play(
#             Uncreate(zoomed_display_frame),
#             FadeOut(frame),
#         )
#         self.wait()


# class Derivative(Scene):
#     CONFIG = {
#         "x_start": 3,
#         "x_end": 7,
#         "axes_config": {
#             "center_point": [-4.5,-2.5,0],
#             "x_axis_config": {
#                 "x_min": -1,
#                 "x_max": 10,
#                 "include_numbers": True
#             },
#             "y_axis_config": {
#                 "label_direction": UP,
#                 "x_min": -1,
#                 "x_max": 6,
#                 "include_numbers": True
#             },
#         },
#         "func": lambda x: 0.1 * (x - 2) * (x - 8) * (x - 5) + 3,
#         "func_config": {
#             "color": RED,
#             "x_min": 0.8,
#             "x_max": 9,
#         },
#         "dot_radius": 0.1,
#         "line_config": {}
#     }
#     def construct(self):
#         axes = self.get_axes()
#         func = self.get_graph(self.func,**self.func_config)
#         dot_start = self.get_dot_from_x_coord(self.x_start)
#         dot_end   = self.get_dot_from_x_coord(self.x_end)
#         line = VMobject()
#         line.add_updater(self.get_line_updater(dot_start,dot_end))
#         # self.add(axes,func,dot_start,dot_end,line)
#         self.play(
#             Write(axes),
#             ShowCreation(func),
#             *list(map(GrowFromCenter,[dot_start,dot_end]))
#         )
#         self.play(ShowCreation(line))
#         self.wait()
#         self.move_dot(dot_end, self.x_end, self.x_start + 0.0001, run_time=8)
#         line.clear_updaters()
#         self.remove(dot_end)
#         line.add_updater(self.get_derivative_updater(dot_start))
#         self.add(line)
#         self.wait()
#         self.move_dot(
#             dot_start,
#             self.x_start, 8,
#             run_time=18,
#             rate_func=there_and_back
#         )
#         self.wait(3)

#     def get_axes(self):
#         self.axes = Axes(**self.axes_config)
#         # FIX Y LABELS
#         y_labels = self.axes.get_y_axis().numbers
#         for label in y_labels:
#             label.rotate(-PI/2)
#         return self.axes

#     def get_graph(self,func,**kwargs):
#         return self.axes.get_graph(
#                                     func,
#                                     **kwargs
#                                 )

#     def get_f(self,x_coord):
#         return self.axes.c2p(x_coord, self.func(x_coord))

#     def get_dot_from_x_coord(self,x_coord,**kwargs):
#         return Dot(
#             self.get_f(x_coord),
#             radius=self.dot_radius,
#             **kwargs
#         )

#     def get_dot_updater(self, start, end):
#         def updater(mob,alpha):
#             x = interpolate(start, end, alpha)
#             coord = self.get_f(x)
#             mob.move_to(coord)
#         return updater

#     def get_line_across_points(self,d1,d2,buff):
#         reference_line = Line(d1.get_center(),d2.get_center())
#         vector = reference_line.get_unit_vector()
#         return Line(
#             d1.get_center() - vector * buff,
#             d2.get_center() + vector * buff,
#             **self.line_config
#         )

#     def get_line_updater(self,d1,d2,buff=3,**kwargs):
#         def updater(mob):
#             mob.become(
#                 self.get_line_across_points(d1,d2,buff)
#             )
#         return updater

#     def move_dot(self,dot,start,end,*args,**kwargs):
#         self.play(
#             UpdateFromAlphaFunc(
#                 dot, self.get_dot_updater(start,end),
#                 *args,
#                 **kwargs
#             )
#         )

#     def get_derivative_updater(self, dot, length=6):
#         def updater(mob):
#             derivative = Line(
#                 dot.get_center(),
#                 self.get_dot_from_x_coord(
#                     self.axes.p2c(dot.get_center())[0] + 0.0001
#                 ).get_center(),
#                 **self.line_config
#             )
#             derivative.set_length(length)
#             derivative.move_to(dot)
#             mob.become(derivative)
#         return updater



from sanim.anim_tools.tables import *

# class Tables(Scene):
#     def construct(self):
#         tabledict={
#             TextMobject("TextMobject Input"):[TextMobject("Must"),TextMobject("add"),TextMobject("element"),TextMobject("retrieval.")],
#             TexMobject("TexMobject Input"):[TexMobject(r"e^{\iota\pi}+1 = 0"),TexMobject(r"Tex: \alpha\theta\epsilon")],
#             "Raw String Input":["Defaults","to","TextMobject."],
#             Text("Text input",font="Lucida Grande"):[Text("Text",font="Alys Script Bold"),Text("is",font="serif"),Text("Supported",font="serif")],

#         }

#         table=Table(tabledict=tabledict,buff_length=0.3,line_color=GRAY,raw_string_color=BLUE)
#         table.scale(0.5)

#         self.play(Write(table),run_time=2)

#         self.play(Write(table.add_record(record=Integer(123),field_num=0)))

#         self.play(table.adjust_lines())

#         self.play(Uncreate(table.remove_record(field_num=1,record_num=0)))

#         self.play(table.adjust_positions())

#         self.play(Write(table.add_field(DecimalNumber(3.14))))

#         self.play(table.adjust_lines())

#         self.play(
#             table.get_record(0,2).set_color,BLUE,
#             table.get_field(0).set_color,GREEN,

#         )

#         self.play(table.scale,0.75,
#         table.shift,LEFT)


#         self.wait(1)


# class Table1(Scene):
#     def construct(self):
#         tabledict={
#             TexMobject(r'x'):[ ],
#             TexMobject(r'y'):[ ],
#             TexMobject(r'slope'):[ ],
#         }

#         table=Table(tabledict=tabledict, buff_length=0.1, line_color=GRAY)
#         self.play(Write(table), run_time=2)

#         x1 = TexMobject(r'-0.5').scale(0.7)
#         y1 = TexMobject(r'5.625').scale(0.7)
#         m1 = TexMobject(r'0.24').scale(0.7)

#         self.play(
#             Write(table.add_record(record = x1, field_num=0).shift(0.2*DOWN)),
#             Write(table.add_record(record = y1, field_num=1).shift(0.2*DOWN)),
#             Write(table.add_record(record = m1, field_num=2).shift(0.2*DOWN))
#         )

#         self.play(table.adjust_lines())

#         self.wait()

#         x2 = TexMobject(r'-0.8').scale(0.7)
#         y2 = TexMobject(r'6.048').scale(0.7)
#         m2 = TexMobject(r'0.24').scale(0.7)

#         self.play(
#             Write(table.add_record(record = x2, field_num=0).shift(0.2*DOWN)),
#             Write(table.add_record(record = y2, field_num=1).shift(0.2*DOWN)),
#             Write(table.add_record(record = m2, field_num=2).shift(0.2*DOWN))
#         )

#         self.play(table.adjust_lines())

#         self.wait()

#         x3 = TexMobject(r'-0.9').scale(0.7)
#         y3 = TexMobject(r'6.061').scale(0.7)
#         m3 = TexMobject(r'0.61').scale(0.7)

#         self.play(
#             Write(table.add_record(record = x3, field_num=0).shift(0.2*DOWN)),
#             Write(table.add_record(record = y3, field_num=1).shift(0.2*DOWN)),
#             Write(table.add_record(record = m3, field_num=2).shift(0.2*DOWN))
#         )

#         self.play(table.adjust_lines())

#         self.wait()

#         x4 = TexMobject(r'-0.99').scale(0.7)
#         y4 = TexMobject(r'6.0096').scale(0.7)
#         m4 = TexMobject(r'0.9601').scale(0.7)

#         self.play(
#             Write(table.add_record(record = x4, field_num=0).shift(0.2*DOWN)),
#             Write(table.add_record(record = y4, field_num=1).shift(0.2*DOWN)),
#             Write(table.add_record(record = m4, field_num=2).shift(0.2*DOWN))
#         )

#         self.play(table.adjust_lines())

#         self.wait()

#         x5 = TexMobject(r'-0.999').scale(0.7)
#         y5 = TexMobject(r'6.001').scale(0.7)
#         m5 = TexMobject(r'0.996001').scale(0.7)

#         self.play(
#             Write(table.add_record(record = x5, field_num=0).shift(0.2*DOWN)),
#             Write(table.add_record(record = y5, field_num=1).shift(0.2*DOWN)),
#             Write(table.add_record(record = m5, field_num=2).shift(0.2*DOWN))
#         )

#         self.play(table.adjust_lines())

#         self.wait()

#         x6 = TexMobject(r'-0.9999').scale(0.7)
#         y6 = TexMobject(r'6.0001').scale(0.7)
#         m6 = TexMobject(r'0.9996').scale(0.7)

#         self.play(
#             Write(table.add_record(record = x6, field_num=0).shift(0.2*DOWN)),
#             Write(table.add_record(record = y6, field_num=1).shift(0.2*DOWN)),
#             Write(table.add_record(record = m6, field_num=2).shift(0.2*DOWN))
#         )

#         self.play(table.adjust_lines())

#         self.wait()

#         # rect3_f1 = Rectangle(width = f1[3].get_width(), height = f1[3].get_height(), color =RED)

#         rect1 = Rectangle(width = table.get_record(0,2).get_width(), height = table.get_record(0,2).get_height(), color = RED)
#         rect1.move_to(table.get_record(0,2))

#         self.add(rect1)

        

#         self.play(
#             table.get_record(0,2).set_color,BLUE,
#             table.get_field(0).set_color,GREEN,

#         )

class FTC(GraphScene):
    CONFIG = {
        "x_max": 4,
        "x_labeled_nums": list(range(-1, 5)),
        "y_min": 0,
        "y_max": 2,
        "y_tick_frequency": 2.5,
        "y_labeled_nums": list(range(5, 20, 5)),
        "n_rect_iterations": 1,
        "default_right_x": 3,
        "func": lambda x: 0.1*math.pow(x-2, 2) + 1,
        "y_axis_label": "",
    }

    def construct(self):
        self.setup_axes()

        graph = self.get_graph(self.func)
        self.play(ShowCreation(graph))
        self.graph = graph

        rects = VGroup()

        for dx in np.arange(0.2, 0.05, -0.05):
            rect = self.get_riemann_rectangles(
                self.graph,
                x_min=0,
                x_max=self.default_right_x,
                dx=dx,
                stroke_width=4*dx,
            )
            rects.add(rect)

        self.play(
            DrawBorderThenFill(
                rects[0],
                run_time=2,
                rate_func=smooth,
                lag_ratio=0.5,
            ),
        )
        self.wait()

        for rect in rects[1:]:
            self.play(
                Transform(
                    rects[0], rect,
                    run_time=2,
                    rate_func=smooth,
                    lag_ratio=0.5,
                ),
            )
            self.wait()

        t = TextMobject("Riemann Integration")
        t.scale(1.5)
        t.shift(3 * UP)

        self.play(FadeInFromDown(t))
        self.wait()




