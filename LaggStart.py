from manim import *

class Lagg(Scene):
    def construct(self):
        text = MathTex("a^2+b^2 = c^2").scale(1.5)
        circle = Circle(color=RED, fill_opacity = 1, fill_color = ORANGE).next_to(text, DOWN)
        hello = Text("Hello").next_to(text, UP)

        self.add(hello)

        self.play(
            LaggedStart(
                hello.animate(run_time=5).shift(3*RIGHT),
                DrawBorderThenFill(circle, run_time=3),
                Write(text, run_time=3),
                lag_ratio=0.5
            )
        )

        self.wait()

        # self.play(Write(text))
        # self.wait()

        # self.play(DrawBorderThenFill(circle))
        # self.wait()

        # self.play(
        #     AnimationGroup(
        #         Write(text, run_time=4),
        #         DrawBorderThenFill(circle, run_time=2),
        #         lag_ratio=0.5
        #     )
        # )

        # self.wait()