from manimlib.imports import *
from sanim.anim_tools.tables import *

class Derivative(GraphScene,ZoomedScene):
    CONFIG = {
        'x_min': -2,
        'x_max': 2,
        'y_min': -2,
        'y_max': 10,
        "axes_color": GREY,
        "graph_origin": 2.5* DOWN,
        "line_config": {}

    }

    def setup(self):            
        GraphScene.setup(self)
        MovingCameraScene.setup(self)

    def construct(self):
        self.setup_axes(animate = True)
        self.wait(5)

        #graph function
        def graph_to_be_drawn(x):
            return x**3-x**2-4*x+4

        func = self.get_graph(graph_to_be_drawn, x_min = -2.6, x_max = 3.1, color = RED)

        self.play(ShowCreation(func), run_time = 2)
        self.wait(5)

        #writing function
        f = TexMobject(r'y=f(x)=x^3-x^2-4x+4').scale(0.7)
        f.move_to(self.coords_to_point(-1.1,-1.5))

        self.play(Write(f), run_time = 2)
        self.wait(5)

        #making 1st point
        dot_start = Dot(self.coords_to_point(-1, graph_to_be_drawn(-1)))

        self.play(GrowFromCenter(dot_start))

        text_start = TexMobject(r'(-1,6)').next_to(dot_start, UP, buff = 0).scale(0.5)
        self.play(Write(text_start))
        self.wait(5)

        #slope formula
        slope = TexMobject(r'slope = \frac{\Delta y}{\Delta x}').move_to(self.coords_to_point(-2.65,7))
        slope.scale(0.7)

        self.play(Write(slope))
        self.wait(5)

        #making 2nd point
        dot_end = Dot(self.coords_to_point(-0.5, graph_to_be_drawn(-0.5)))

        self.play(GrowFromCenter(dot_end))

        text_end = TexMobject(r'(-0.5, 5.625)').next_to(dot_end, DOWN, buff = 0).scale(0.5)
        self.play(Write(text_end))
        self.wait(5)

        # self.play(
        #     self.camera_frame.scale, 0.3,
        #     self.camera_frame.move_to, dot_end
        # )
        # self.wait()

        line = VMobject()
        line.add_updater(self.get_line_updater(dot_start,dot_end))

        self.play(ShowCreation(line))
        self.wait(5)

        #table making
        tabledict={
            TexMobject(r'x'):[ ],
            TexMobject(r'y'):[ ],
            TexMobject(r'slope'):[ ],
        }

        #table moving point
        tp = self.coords_to_point(1.5, 11)
        table=Table(tabledict=tabledict, buff_length=0.1, hbuff_length = 0.2, line_color=GRAY).move_to(tp)
        self.play(FadeIn(table), run_time = 2)

        x1 = TexMobject(r'-0.5').scale(0.7)
        y1 = TexMobject(r'5.625').scale(0.7)
        m1 = TexMobject(r'-0.75').scale(0.7)

        self.play(
            Write(table.add_record(record = x1, field_num=0).shift(0.2*DOWN)),
            Write(table.add_record(record = y1, field_num=1).shift(0.2*DOWN)),
            Write(table.add_record(record = m1, field_num=2).shift(0.2*DOWN))
        )

        self.play(table.adjust_lines())
        self.wait(5)

        self.play(FadeOut(text_end))
        
        #moving dot
        vt = ValueTracker(-0.5)
        def moving_dot():
            x = vt.get_value()
            d = dot_end.move_to(self.coords_to_point(x, graph_to_be_drawn(x)))
            return d

        dd = always_redraw(moving_dot)

        self.add(dd)
        self.play(vt.set_value, -0.8, rate_func=linear, run_time=5)
        self.wait(5)

        text_end = TexMobject(r'(-0.8, 6.048)').next_to(dot_end, DOWN, buff = 0).scale(0.5)
        self.play(Write(text_end))
        self.wait(5)

        #table update
        x2 = TexMobject(r'-0.8').scale(0.7)
        y2 = TexMobject(r'6.048').scale(0.7)
        m2 = TexMobject(r'0.24').scale(0.7)

        self.play(
            Write(table.add_record(record = x2, field_num=0).shift(0.2*DOWN)),
            Write(table.add_record(record = y2, field_num=1).shift(0.2*DOWN)),
            Write(table.add_record(record = m2, field_num=2).shift(0.2*DOWN))
        )

        self.play(table.adjust_lines())
        self.wait(5)

        self.play(FadeOut(text_end))

        
        #point update
        vt = ValueTracker(-0.8)
        def moving_dot():
            x = vt.get_value()
            d = dot_end.move_to(self.coords_to_point(x, graph_to_be_drawn(x)))
            return d

        dd = always_redraw(moving_dot)

        self.add(dd)
        self.play(vt.set_value, -0.9, rate_func=linear, run_time=3)
        self.wait(5)

        text_end = TexMobject(r'(-0.9, 6.061)').next_to(dot_end, DOWN, buff = 0).scale(0.5)
        self.play(Write(text_end))
        self.wait(5)

        #table update
        x3 = TexMobject(r'-0.9').scale(0.7)
        y3 = TexMobject(r'6.061').scale(0.7)
        m3 = TexMobject(r'0.61').scale(0.7)

        self.play(
            Write(table.add_record(record = x3, field_num=0).shift(0.2*DOWN)),
            Write(table.add_record(record = y3, field_num=1).shift(0.2*DOWN)),
            Write(table.add_record(record = m3, field_num=2).shift(0.2*DOWN))
        )

        self.play(table.adjust_lines())
        self.wait(5)

        self.play(FadeOut(text_end))

        #update point
        vt = ValueTracker(-0.9)
        def moving_dot():
            x = vt.get_value()
            d = dot_end.move_to(self.coords_to_point(x, graph_to_be_drawn(x)))
            return d

        dd = always_redraw(moving_dot)

        self.add(dd)
        self.play(vt.set_value, -0.99, rate_func=linear, run_time=1)
        self.wait(5)

        text_end = TexMobject(r'(-0.99, 6.0096)').next_to(dot_end, DOWN, buff = 0).scale(0.5)
        self.play(Write(text_end))
        self.wait(5)

        #update table
        x4 = TexMobject(r'-0.99').scale(0.7)
        y4 = TexMobject(r'6.0096').scale(0.7)
        m4 = TexMobject(r'0.9601').scale(0.7)

        self.play(
            Write(table.add_record(record = x4, field_num=0).shift(0.2*DOWN)),
            Write(table.add_record(record = y4, field_num=1).shift(0.2*DOWN)),
            Write(table.add_record(record = m4, field_num=2).shift(0.2*DOWN))
        )

        self.play(table.adjust_lines())
        self.wait(5)

        #camera zoomin
        self.camera_frame.save_state()
        self.play(
            self.camera_frame.scale, 0.2,
            self.camera_frame.move_to, dot_end
        )
        # self.wait()

        self.play(FadeOut(text_end))

        vt = ValueTracker(-0.99)
        def moving_dot():
            x = vt.get_value()
            d = dot_end.move_to(self.coords_to_point(x, graph_to_be_drawn(x)))
            return d

        dd = always_redraw(moving_dot)

        self.add(dd)
        self.play(vt.set_value, -0.999, rate_func=linear, run_time=1)
        self.wait()

        text_end = TexMobject(r'(-0.999, 6.001)').next_to(dot_end, DOWN, buff = 0).scale(0.5)
        self.play(Write(text_end))
        # self.wait(5)

        #camera zoomout
        self.play(Restore(self.camera_frame))
        self.wait()

        #text update
        x5 = TexMobject(r'-0.999').scale(0.7)
        y5 = TexMobject(r'6.001').scale(0.7)
        m5 = TexMobject(r'0.996001').scale(0.7)

        self.play(
            Write(table.add_record(record = x5, field_num=0).shift(0.2*DOWN)),
            Write(table.add_record(record = y5, field_num=1).shift(0.2*DOWN)),
            Write(table.add_record(record = m5, field_num=2).shift(0.2*DOWN))
        )

        self.play(table.adjust_lines())
        self.wait(5)

        self.play(FadeOut(text_end))

        #text updat 
        x6 = TexMobject(r'-0.9999').scale(0.7)
        y6 = TexMobject(r'6.0001').scale(0.7)
        m6 = TexMobject(r'0.9996').scale(0.7)

        self.play(
            Write(table.add_record(record = x6, field_num=0).shift(0.2*DOWN)),
            Write(table.add_record(record = y6, field_num=1).shift(0.2*DOWN)),
            Write(table.add_record(record = m6, field_num=2).shift(0.2*DOWN))
        )

        self.play(table.adjust_lines())
        self.wait(5)

        #final text update
        x7 = TexMobject(r'-1').scale(0.7)
        y7 = TexMobject(r'6').scale(0.7)
        m7 = TexMobject(r'1').scale(0.7)

        table.add_record(record = x7, field_num=0).shift(0.2*DOWN)
        table.add_record(record = y7, field_num=1).shift(0.2*DOWN)
        table.add_record(record = m7, field_num=2).shift(0.2*DOWN)

        #creating rectangle for record
        rect1 = Rectangle(width = table.get_record(0,5).get_width(), height = table.get_record(0,5).get_height(), color = RED)
        rect1.move_to(table.get_record(0,5))

        rect2 = Rectangle(width = table.get_record(1,5).get_width(), height = table.get_record(1,5).get_height(), color = RED)
        rect2.move_to(table.get_record(1,5))

        rect3 = Rectangle(width = table.get_record(2,5).get_width(), height = table.get_record(2,5).get_height(), color = RED)
        rect3.move_to(table.get_record(2,5))

        self.play(ShowCreation(rect1))
        self.wait(5)

        self.play(Transform(rect1, x7))
        self.wait(5)

        self.play(ShowCreation(rect2))
        self.wait(5)

        self.play(Transform(rect2, y7))
        self.wait(5)

        self.play(ShowCreation(rect3))
        self.wait(5)

        self.play(Transform(rect3, m7))
        self.wait(5)

        self.play(table.adjust_lines())
        self.wait(5)

        #Derivative definition
        text_dri = TextMobject('The Derivative').move_to(self.coords_to_point(-2.3,12))
        self.play(FadeIn(text_dri))
        self.wait(5)

        text_d1 = TextMobject('Slope of the curve at $(-1,6)$ is $1$').next_to(text_dri, DOWN, buff = 0.35).scale(0.7)
        text_d1.align_to(text_dri, LEFT)

        self.play(Write(text_d1))
        self.wait(5)

        text_d2 = TextMobject('Derivative of $f(x)$ at $x = -1$ is $1$').next_to(text_d1, DOWN, buff = 0.15).scale(0.7)
        text_d2.align_to(text_dri, LEFT)

        self.play(Write(text_d2))
        self.wait(5)

        #picture group
        picture = Group(*self.mobjects)
        self.play(FadeOut(picture), run_time = 2)
        self.wait(5)





    #out of construct
    def get_line_updater(self,d1,d2,buff=3,**kwargs):
        def updater(mob):
            mob.become(
                self.get_line_across_points(d1,d2,buff)
            )
        return updater

    def get_line_across_points(self,d1,d2,buff):
        reference_line = Line(d1.get_center(),d2.get_center())
        vector = reference_line.get_unit_vector()
        return Line(
            d1.get_center() - vector * buff,
            d2.get_center() + vector * buff,
            **self.line_config
        )