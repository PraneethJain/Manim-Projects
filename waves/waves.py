from math import exp, sin,cos,pi
from manim import *
def func(t,Ac=1,wc=2,Am=1,wm=1,phi=0):
    myu=Am/Ac
    return Ac*sin(wc*t+phi)+myu*Ac*(cos((wc-wm)*t))/2-myu*Ac*(cos((wc+wm)*t+2*phi))/2
class communication(Scene):
    def construct(self):
        graph=NumberPlane(
            x_range=[-10,10,1],
            y_range=[-10,10,1],
            x_length=15,
            y_length=10,
            axis_config={
                'color':GREEN
            },
            x_axis_config={
                'numbers_to_include':np.arange(-10,10.1,2),
            },
            y_axis_config={
                'numbers_to_include':np.arange(-10,10.1,2),
            },
        )
        self.play(Create(graph),run_time=2)
        self.wait()
        f1=graph.plot(lambda t:func(t),color=RED,stroke_width=5)
        f2=graph.plot(lambda t:func(t,Am=2,wc=5,Ac=3,wm=1.5,phi=pi),color=RED,stroke_width=5)
        self.play(Create(f1),run_time=2)
        self.wait(1)
        self.play(ReplacementTransform(f1,f2),run_time=5)
        self.wait()
        self.play(Rotate(f2,angle=100*PI),rate_func=smooth,run_time=10)
        self.wait()

