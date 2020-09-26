from manimlib.imports import *

#'graph_origin': 0.5 * DOWN + 0 * LEFT,

class GraphX(GraphScene):
    CONFIG ={
        'x_min': -4,
        'x_max': 4,
        'y_min': -3.5,
        'y_max': 3.5,
        'x_axis_label': '$x$',
        'y_axis_label': '$y$',
        'graph_origin': ORIGIN,
    }

    # def show_arrow(self):
    #     arrow = Arrow()
    #     arrow.next_to(t1,RIGHT,buff = 0.25)
    #     return arrow

    def show_function_graph(self):
        self.setup_axes(animate = True)
        #text = TextMobject('$(x,y)$')
        #text.shift(2*UP+3*RIGHT)

        #arrow
        arrow = Arrow(stroke_width=4,tip_length = 0.15, stroke_color=RED)
        arrow.to_edge(UP, buff = 0.3)

        #cartesian
        t1 = TextMobject('$(x,y)$')
        t1.set_color(BLUE)
        t1.next_to(arrow,LEFT,buff = 0.25)

        #polar
        t2 = TextMobject('$(r,\\theta)$')
        t2.set_color(BLUE)
        t2.next_to(arrow,RIGHT,buff = 0.25)

        #point
        point = Dot(self.coords_to_point(2,3))
        text = TextMobject('$(x,y)$')
        text.next_to(point, RIGHT, buff = 0.25)

        #vhumi
        x3 = self.coords_to_point(0,0)
        y3 = self.coords_to_point(2,0)
        base = Line(x3,y3,color = YELLOW)

        x = TextMobject('$x$')
        x.next_to(base,DOWN,buff = 0.25)

        #lombo
        x1 = self.coords_to_point(2,3)
        y1 = self.coords_to_point(2,0)
        vl = Line(y1,x1, color=YELLOW)

        y = TextMobject('$y$')
        y.next_to(vl,RIGHT,buff = 0.25)

        #otivuj
        x2 = self.coords_to_point(2,3)
        y2 = self.coords_to_point(0,0)
        hl = Line(y2,x2,color = YELLOW)

        ro = TextMobject('$r$')
        ro.shift(0.65*RIGHT+1.3*UP)

        #writing all necessary scene

        self.play(Write(t1))
        self.play(Write(arrow))
        self.wait(5)

        #cartesian to polar transform
        self.play(TransformFromCopy(t1,t2))
        self.wait(5)

        #point writing
        self.play(Write(point))
        self.wait(5)
        
        self.play(Write(text))
        self.wait(5)

        #otivuj writing
        self.play(Write(hl))
        self.play(Write(ro))
        self.wait(5)

        #making angle for triangle
        arc = Arc(
            radius=1,
            start_angle=base.get_angle(),
            angle =hl.get_angle(),
            color=RED
        )
        angle_text = TextMobject('$\\theta$').next_to(arc,ORIGIN, buff = 2)

        self.play(Write(arc))
        self.wait(5)

        self.play(Write(angle_text))
        self.wait(5)

        #writing vuj and koti
        self.play(Write(vl))
        self.wait(3)

        self.play(Write(y))
        self.wait(5)

        self.play(Write(base))
        self.wait(3)

        self.play(Write(x))
        self.wait(5)

        #picture_frame
        picture= Group(*self.mobjects)
        picture.scale(0.6).to_edge(LEFT, buff=SMALL_BUFF)
        self.play(ShowCreation(picture))

        #group_triangle
        tri = VGroup(base,vl,hl)

        r2 = TexMobject(r'r^2 = x^2+y^2').next_to(picture,UR,buff = 0.5)
        r = TexMobject(r'r = \sqrt{x^2+y^2}').next_to(picture,UR,buff = 0.5)

        tan = TexMobject(r'tan\theta = \frac{y}{x}').next_to(r,DOWN,buff = 0.5)
        theta = TexMobject(r'\theta = tan^{-1}\frac{y}{x}').next_to(tan,DOWN,buff = 0.5)

        r_theta = VGroup(r,theta)
        r_theta_to = TexMobject(r'(r,\theta)').next_to(r,RIGHT, buff = 0.5).set_color(BLUE)

        cos = TexMobject(r'cos\theta = \frac{x}{r}').next_to(theta,DOWN,buff = 0.5)
        sin = TexMobject(r'sin\theta = \frac{y}{r}').next_to(cos,DOWN,buff = 0.5)

        x_value = TexMobject(r'\Rightarrow x = r cos\theta').next_to(cos,RIGHT)
        y_value = TexMobject(r'\Rightarrow y = r sin\theta').next_to(sin,RIGHT)
        xy_group = VGroup(x_value,y_value)

        arrow_to = Arrow(stroke_width=4,tip_length = 0.15, stroke_color=RED).next_to(r_theta_to,RIGHT)
        xy_cor = TexMobject(r'(x,y)').next_to(arrow_to,RIGHT).set_color(BLUE)
        xya_group = VGroup(arrow_to,xy_cor)

        # tan_xy0 = TexMobject(r'\Rightarrow tan\theta = \frac{r sin\theta}{r cos\theta}').next_to(tan,RIGHT)
        # tan_xy = TexMobject(r'\Rightarrow tan\theta = \frac{sin\theta}{cos\theta}').next_to(tan,RIGHT)

        self.wait(5)
        
        self.play(TransformFromCopy(tri,r2))
        self.wait(5)

        self.play(Transform(r2,r))
        self.wait(5)

        self.play(TransformFromCopy(tri,tan))
        self.wait(5)

        self.play(TransformFromCopy(tan,theta))
        self.wait(5)

        self.play(TransformFromCopy(r_theta,r_theta_to))
        self.wait(5)

        self.play(TransformFromCopy(tri,cos))
        self.wait(5)

        self.play(TransformFromCopy(tri,sin))
        self.wait(5)

        self.play(TransformFromCopy(cos,x_value))
        self.wait(5)

        self.play(TransformFromCopy(sin,y_value))
        self.wait(5)

        self.play(TransformFromCopy(xy_group,xya_group))
        self.wait(5)

    def construct(self):
        self.show_function_graph()