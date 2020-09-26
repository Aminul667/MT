from manimlib.imports import *
from sanim.anim_tools.tables import *

class BothTest(Scene):
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
