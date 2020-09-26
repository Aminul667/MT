from manimlib.imports import *

class IntroScene(Scene):
    def construct(self):
        img = ImageMobject(
            'OnlyPNG.png',
            color = BLUE,
            height = 3
        )

        self.play(FadeIn(img))
        self.wait()

        text = Text('Programming & Mathematics Literature', font = 'Brush Script MT', size = 1.2, stroke_color = GOLD_E)
        text.move_to(img)
        text.set_color_by_gradient(GOLD, GREY_BROWN, DARK_GREY)

        self.play(ApplyMethod(img.shift, 2*UP))

        self.play(Write(text), run_time = 2)
        self.wait()

        picture = Group(*self.mobjects)
        self.play(FadeOut(picture), run_time = 2)
        self.wait(5)