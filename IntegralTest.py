from manimlib.imports import *
from sanim.anim_tools.tables import *

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