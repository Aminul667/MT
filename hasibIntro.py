from manimlib.imports import *

class IntroHasib(Scene):
    def construct(self):
        # back_rect = Rectangle(width = FRAME_WIDTH, height = FRAME_HEIGHT, stroke_width = 0, fill_color = LIGHT_GREY, fill_opacity = 1)
        # self.add(back_rect)

        t = TexMobject(r'Thank\ You')
        # t.set_color(BLUE)

        t.set_color_by_gradient(PINK, YELLOW, ORANGE).to_edge(UP)

        self.play(Write(t), run_time = 2.5)
        self.wait()

        # self.play(ApplyMethod(t.shift, UP))
        # self.wait()

        # picture = Group(*self.mobjects)

        img = SVGMobject(
            'isac.svg',
            height = 5
        )
        img.next_to(t, DOWN, buff = 0.25)

        self.play(Write(img))
        self.wait()

        # group = Group(t, img)

        # self.play(FadeOut(group))
        # self.wait()

        # img2 = ImageMobject(
        #     'hasib3.png',
        #     color = BLUE,
        #     height = 1
        # )

        # self.play(FadeIn(img2))
        # self.wait()

        # self.play(FadeOut(img2))
        # self.wait()

        # # picture = Group(*self.mobjects)

        # back_rect = Rectangle(width = FRAME_WIDTH, height = FRAME_HEIGHT, stroke_width = 0, fill_color = LIGHT_GREY, fill_opacity = 1)
        # self.add(back_rect)

        # self.play(Transform(picture, back_rect), run_time = 2)
        # self.wait()

        # img1 = ImageMobject(
        #     'hasib2.png',
        #     color = BLUE,
        #     height = FRAME_HEIGHT
        # )

        # self.play(FadeIn(img1))
        # self.wait(3)