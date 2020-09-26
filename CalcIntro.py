from manimlib.imports import *

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