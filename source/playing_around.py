from manim import *
from math import log as ln
from math import sin,cos,pi,e
i

def func1(x):
    return sin(cos(e**x))
    
class Stuff(Scene):
    def construct(self):
        name = Tex('Praneeth').to_edge(LEFT, buff = 3).to_edge(DOWN)
        square = Square(side_length=3)
        square.set_fill(PINK,opacity=0.5)
        circle = Circle(radius= 3).scale(0.5)
        circle.set_fill(BLUE,opacity=0.5)
        square.shift(LEFT * 3)
        self.play(DrawBorderThenFill(square), run_time=2)
        self.play(Write(name))
        self.play(ReplacementTransform(square,circle), name.animate.shift(RIGHT * 3))
        self.play(FadeToColor(circle,color=GREEN))
        self.play(circle.animate.scale(0),name.animate.to_edge(DR))
        self.wait(3)
        
class Plot(Scene):
        def construct(self):
            axes = Axes(
                x_range=[-10,10,1],
                y_range=[-10,10,1],
                x_length=15,
                y_length=15,
                axis_config={
                    'color':GREEN
                },
                x_axis_config={
                    'numbers_to_include':np.arange(-10,10.1,2),
                    'numbers_with_elongated_ticks':np.arange(-10,10.1,2)
                },
                y_axis_config={
                    'numbers_to_include':np.arange(-10,10.1,2),
                    'numbers_with_elongated_ticks':np.arange(-10,10.1,2)
                },
                tips = False
            )
            axes_labels=axes.get_axis_labels()
            f_label = MathTex('f(x)=sin(cos(e^{x}))}',color=PURPLE).scale(2.5)
            self.play(Write(f_label))
            self.wait()
            self.play(f_label.animate.scale(0.25).to_edge(DL))
            f1=axes.plot(func1,color=BLUE)
            self.play(Create(axes),run_time=2)
            self.play(Create(axes_labels))
            self.play(Create(f1),run_time=3)
            dot=Dot()
            self.play(MoveAlongPath(dot,f1),run_time=2,rate_func=linear)
