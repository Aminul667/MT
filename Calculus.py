from manimlib.imports import *
from sanim.anim_tools.tables import *


class First(Scene):
    def construct(self):
        img1 = ImageMobject(
            'Grece.png',
            color = BLUE,
            height = 6
        )

        self.play(FadeIn(img1), run_time = 2)
        self.wait(15)

        self.play(FadeOut(img1))
        self.wait(5)

        img2 = ImageMobject(
            'Newton.jpg',
            color = BLUE,
            height = 6
        )
        img2.shift(2.8*LEFT)

        self.play(FadeIn(img2), run_time = 2)
        self.wait(5)

        newton = Text('Isaac Newton', font = 'Informal Roman').next_to(img2, DOWN, buff = 0.25)
        newton.scale(0.9)
        
        self.play(Write(newton), run_time = 2)
        self.wait(5)

        img3 = ImageMobject(
            'Lei.jpg',
            color = BLUE,
            height = 6
        )
        img3.shift(2.8*RIGHT)

        self.play(FadeIn(img3), run_time = 2)
        self.wait(5)

        leib = Text('Gottfried Wilhelm Leibniz', font = 'Informal Roman').next_to(img3, DOWN, buff = 0.25)
        leib.scale(0.9)

        self.play(Write(leib), run_time = 2)
        self.wait(20)

        picture = Group(*self.mobjects)
        self.play(FadeOut(picture), run_time = 2)
        self.wait(5)


class Beginning(GraphScene):
    CONFIG = {
        "x_min": -6,
        "x_max": 6,
        "y_min": -3,
        "y_max": 3,
        "graph_origin": ORIGIN,
        "axes_color": LIGHT_GREY
    }

    def construct(self):
        #Make graph
        self.setup_axes(animate=True)
        
        function = self.get_graph(lambda x : -(1/14)*x*(x-1.5)*(x-3)*(x-6), x_min = -0.75, x_max = 6.2, color = RED)

        self.play(ShowCreation(function), run_time = 2)
        self.wait(5)

        #creating tangent line
        secant = self.get_secant_slope_group(
            0.3, function,
            dx = 0.0001,
            secant_line_color = YELLOW,
            secant_line_length = 7
        )

        self.play(ShowCreation(secant), run_time = 2)
        self.wait(5)

        #text_steepness
        step = TexMobject(r'Steepness\ ?').shift(0.5*UP+2*LEFT)

        self.play(TransformFromCopy(secant, step), run_time = 2)
        self.wait(5)

        #area under the curve
        area = self.get_riemann_rectangles(
            function,
            x_min = 3.5, x_max = 5.7,
            dx = 0.02,
            # stroke_color=None,
            fill_opacity = 0.75,
            stroke_width = 0.25,
            start_color = RED,
            end_color = ORANGE,
        )

        self.play(ShowCreation(area), run_time = 2)
        self.wait(5)

        #text_area
        area_text = TexMobject(r'Area\ ?').next_to(area, DOWN, buff = 0.5)
        
        self.play(TransformFromCopy(area, area_text))
        self.wait(5)

        #answering text
        text1 = TexMobject(r'Derivative').move_to(step)

        self.play(Transform(step, text1))
        self.wait(5)

        text2 = TexMobject(r'Integral').move_to(area_text)

        self.play(Transform(area_text, text2))
        self.wait(5)

        picture = Group(*self.mobjects)
        self.play(FadeOut(picture), run_time = 2)
        self.wait(5)


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


class Integral(GraphScene):
    CONFIG = {
        'x_min':-1,
        'x_max':3,
        'y_min':-1,
        'y_max':7,
        "axes_color": LIGHT_GREY,
        "graph_origin": 2.5*DOWN+3.5*LEFT,
    }

    def construct(self):
        self.setup_axes(animate = True)

        inte = TextMobject('Integral').move_to(self.coords_to_point(3,7.5))
        self.play(FadeIn(inte))

        function = self.get_graph(lambda x : x**3-4*x**2+x+6, x_min = -1.1, x_max = 3.1, color = RED)

        self.play(ShowCreation(function), run_time = 2)
        self.wait(5)

        #function
        f = TexMobject(r'g(x)=x^3-4x^2+x+6').scale(0.7)
        f.move_to(self.coords_to_point(1,-0.8))
        self.play(Write(f))
        self.wait(5)

        #point pointer for area
        ptr1 = Triangle(fill_opacity=1).scale(0.15)
        # ptr1.rotate(180*DEGREES)
        ptr1.set_color(YELLOW)
        ptr1.move_to(self.coords_to_point(0,-0.4))
        
        self.play(Write(ptr1))
        self.wait(5)

        ptr2 = Triangle(fill_opacity=1).scale(0.15)
        ptr2.set_color(YELLOW)
        ptr2.move_to(self.coords_to_point(0,-0.4))

        self.play(ApplyMethod(ptr2.move_to, self.coords_to_point(2,-0.4), rate_function = smooth, run_time = 2))
        self.wait(5)

        # self.play(TransformFromCopy(ptr1,ptr2))
        # self.wait()

        #riemann rectangles list
        riemann_rect = self.get_riemann_rectangles_list(
                                function,
                                9,
                                x_min = 0, x_max = 2,
                                max_dx=0.5,
                                power_base=2,
                                stroke_width = 0.25,
                                fill_opacity=0.75,
                                start_color = DARK_BROWN,
                                end_color = ORANGE,
        )

        self.play(DrawBorderThenFill(riemann_rect[0], run_time = 2, rate_function = smooth, lag_ratio = 0.5))
        self.wait(5)

        #table making
        tabledict={
            TexMobject(r'Slices'):[ ],
            TexMobject(r'Area'):[ ],
        }

        table=Table(tabledict=tabledict,buff_length=0.1, hbuff_length = 0.2, line_color=GRAY)
        table.next_to(inte, DOWN, buff = 0.25)

        self.play(FadeIn(table), run_time = 2)
        self.wait(5)

        #table data update
        s1 = TexMobject(r'4').scale(0.7)
        a1 = TexMobject(r'8.75').scale(0.7)

        self.play(
            Write(table.add_record(record = s1, field_num=0).shift(0.2*DOWN)),
            Write(table.add_record(record = a1, field_num=1).shift(0.2*DOWN))
        )

        self.play(table.adjust_lines())
        self.wait(5)

        #transforming riemann
        self.transform_between_riemann_rects(
            riemann_rect[0],
            riemann_rect[1],
            replace_mobject_with_target_in_scene = True
        )
        self.wait(5)

        #table data update
        s2 = TexMobject(r'8').scale(0.7)
        a2 = TexMobject(r'8.0625').scale(0.7)

        self.play(
            Write(table.add_record(record = s2, field_num=0).shift(0.2*DOWN)),
            Write(table.add_record(record = a2, field_num=1).shift(0.2*DOWN))
        )

        self.play(table.adjust_lines())
        self.wait(5)

        #transforming riemann
        self.transform_between_riemann_rects(
            riemann_rect[1],
            riemann_rect[2],
            replace_mobject_with_target_in_scene = True
        )
        self.wait(5)

        #table data update
        s3 = TexMobject(r'16').scale(0.7)
        a3 = TexMobject(r'7.70313').scale(0.7)

        self.play(
            Write(table.add_record(record = s3, field_num=0).shift(0.2*DOWN)),
            Write(table.add_record(record = a3, field_num=1).shift(0.2*DOWN))
        )

        self.play(table.adjust_lines())
        self.wait(5)

        #transforming riemann
        self.transform_between_riemann_rects(
            riemann_rect[2],
            riemann_rect[3],
            replace_mobject_with_target_in_scene = True
        )
        self.wait(5)

        #table data update
        s4 = TexMobject(r'32').scale(0.7)
        a4 = TexMobject(r'7.51953').scale(0.7)

        self.play(
            Write(table.add_record(record = s4, field_num=0).shift(0.2*DOWN)),
            Write(table.add_record(record = a4, field_num=1).shift(0.2*DOWN))
        )

        self.play(table.adjust_lines())
        self.wait(5)

        #transforming riemann
        self.transform_between_riemann_rects(
            riemann_rect[3],
            riemann_rect[4],
            replace_mobject_with_target_in_scene = True
        )
        self.wait(5)

        #table data update
        s5 = TexMobject(r'64').scale(0.7)
        a5 = TexMobject(r'7.42676').scale(0.7)

        self.play(
            Write(table.add_record(record = s5, field_num=0).shift(0.2*DOWN)),
            Write(table.add_record(record = a5, field_num=1).shift(0.2*DOWN))
        )

        self.play(table.adjust_lines())
        self.wait(5)

        #infinite data update
        s_dot = TexMobject(r'\hdots').scale(0.7)
        a_dot = TexMobject(r'\hdots').scale(0.7)

        self.play(
            Write(table.add_record(record = s_dot, field_num=0).shift(0.2*DOWN)),
            Write(table.add_record(record = a_dot, field_num=1).shift(0.2*DOWN))
        )

        self.play(table.adjust_lines())
        self.wait(5)

        # infinite rectangle transform
        for r in range(4,len(riemann_rect)):
            self.transform_between_riemann_rects(
                    riemann_rect[r-1],
                    riemann_rect[r],
                    replace_mobject_with_target_in_scene = True,
                )
        self.wait(5)

        s_inf = TexMobject(r'\infty').scale(0.7)
        a_inf = TexMobject(r'7.33333').scale(0.7)

        self.play(
            Write(table.add_record(record = s_inf, field_num=0).shift(0.2*DOWN)),
            Write(table.add_record(record = a_inf, field_num=1).shift(0.2*DOWN))
        )

        self.play(table.adjust_lines())
        self.wait(5)

        t = TextMobject('Integral of $g(x)$ from $x = 0$ to $x = 2$ is $7.33333$ ').scale(0.7)
        t.next_to(table, DOWN, buff = 0.5)

        self.play(Write(t), run_time = 2)
        self.wait(20)

        picture = Group(*self.mobjects)
        self.play(FadeOut(picture), run_time = 2)
        self.wait(5)


class LimitConcept(Scene):
    def construct(self):
        #image from derivative
        img_der = ImageMobject(
            'De.png',
            color = BLUE,
            height = 0.8*FRAME_HEIGHT
        )

        self.play(FadeIn(img_der), run_time = 2)
        self.wait(30)

        self.play(img_der.scale, 0.4)

        self.play(img_der.move_to, 4*LEFT+1.5*UP)
        self.wait(5)

        #derivative text
        text_der = TextMobject('Derivative').next_to(img_der, UP, buff = 0.25)

        self.play(Write(text_der))
        self.wait(5)

        #image from integral
        img_in = ImageMobject(
            'In.png',
            color = BLUE,
            height = 0.8*FRAME_HEIGHT
        )

        self.play(FadeIn(img_in), run_time = 2)
        self.wait(30)

        self.play(img_in.scale, 0.4)

        self.play(img_in.move_to, 4*LEFT+2*DOWN)
        self.wait(5)

        #integral text
        text_in = TextMobject('Integral').next_to(img_in, UP, buff = 0.25)

        self.play(Write(text_in))
        self.wait(5)

        tabledict={
            TextMobject('Derivative\par Approximate'):[ ],
            TextMobject('Integral\par Approximate'):[ ],
        }

        table=Table(tabledict=tabledict, buff_length=0.1, hbuff_length = 0.2, line_color=GRAY)
        table.shift(3*RIGHT+2*UP)

        r1 = [
            TexMobject(r'-0.75'), 
            TexMobject(r'0.24'),
            TexMobject(r'0.61'),
            TexMobject(r'0.9601'),
            TexMobject(r'0.996001'),
            TexMobject(r'0.9996'),
            TexMobject(r'1')
            ]
        for i in r1:
            table.add_record(record = i, field_num=0).shift(0.2*DOWN)

        r2 = [
            TexMobject(r'8.75'),
            TexMobject(r'8.0625'),
            TexMobject(r'7.70313'),
            TexMobject(r'7.51953'),
            TexMobject(r'7.42676'),
            TexMobject(r'7.35332'),
            TexMobject(r'7.33333')
            ]
        for i in r2:
            table.add_record(record = i, field_num = 1).shift(0.2*DOWN)

        
        table.scale(0.7)

        self.play(Write(table), run_time=2)
        self.play(table.adjust_lines())
        self.wait(15)

        rect1 = Rectangle(
            width = table.get_record(1,6).get_width(),
            height = table.get_record(1,6).get_height(),
            color = ORANGE
            )
        rect1.move_to(table.get_record(0,6))

        rect2 = Rectangle(
            width = table.get_record(1,6).get_width(),
            height = table.get_record(1,6).get_height(),
            color = ORANGE
            )
        rect2.move_to(table.get_record(1,6))

        group = VGroup(rect1, rect2)

        self.play(ShowCreation(group))
        self.wait(5)

        limits = TexMobject(r'Limits').next_to(table, DOWN, buff = 0.25)
        
        self.play(Transform(group, limits))
        self.wait(5)

        limit = TextMobject('Limit').scale(1.5).next_to(table, UP, buff = 0.5)

        self.play(TransformFromCopy(limits, limit))
        self.wait(5)

        picture = Group(*self.mobjects)
        self.play(FadeOut(picture), run_time = 2)
        self.wait(5)


class EndScene(Scene):
    CONFIG={
        "MyBLUE":"#3b5998",
        "MyRED":"#FF0000"
    }

    def construct(self):

        #youtube
        rect1 = RoundedRectangle(height = 1.5, width = 2, color = self.MyRED).shift(2*UP)
        tri1 = Triangle(color = WHITE).rotate(270*DEGREES).scale(0.5)
        tri1.move_to(rect1)

        group1 = VGroup(rect1, tri1)

        #facebook
        frect1 = RoundedRectangle(height = 1.5, width = 1.5, color = self.MyBLUE).shift(2*DOWN)

        ftext1 = TextMobject('f').move_to(frect1).scale(3)
        ftext1.set_stroke(color = WHITE)
        ftext1.set_fill(None)

        fgroup1 = VGroup(frect1, ftext1)

        self.play(ShowCreation(group1), ShowCreation(frect1), Write(ftext1), rate_function = linear, run_time = 2)

        #Filling youtube
        rect2 = RoundedRectangle(height = 1.5, width = 2, color = self.MyRED, fill_opacity = 1).shift(2*UP)
        tri2 = Triangle(color = WHITE, fill_opacity = 1).rotate(270*DEGREES).scale(0.5)
        tri2.move_to(rect1)

        group2 = VGroup(rect2, tri2)

        #filling facebook
        frect2 = RoundedRectangle(height = 1.5, width = 1.5, color = self.MyBLUE, fill_opacity = 1).shift(2*DOWN)
        ftext2 = TextMobject('f').move_to(frect2).scale(3)
        ftext2.set_stroke(color = WHITE)

        fgroup2 = VGroup(frect2, ftext2)

        self.play(Write(group2), Write(fgroup2), rate_function = linear, run_time = 2)

        group3 = VGroup(group1, group2)
        fgroup3 = VGroup(fgroup1, fgroup2)

        self.play(ApplyMethod(group3.shift,3*LEFT), ApplyMethod(fgroup3.shift,3*LEFT), rate_function = linear)

        # links
        yt = TexMobject(r'http://bit.ly/ProMatLit').next_to(group3, RIGHT, buff = 0.5)

        fb = TexMobject(r'https://bit.ly/PMLiterature').next_to(fgroup3, RIGHT, buff = 0.5)

        self.play(Write(yt), Write(fb))
        self.wait()



        