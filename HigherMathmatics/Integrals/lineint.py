import numpy as np
from manim import *

class lineInt_scalar(ThreeDScene):
    def construct(self):
        self.begin_ambient_camera_rotation(rate=0.01)
        self.move_camera(phi=70 * DEGREES, theta=-37 * DEGREES, zoom=0.75)
        axes = ThreeDAxes()
        self.play(Create(axes))

        fxy_graph3d = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.cos(u) + np.sin(v) + 2
            ]), v_range=(-7, 7), u_range=(-7, 7), checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(30, 63)).fade(.7).set_z_index(2)
        self.play(Create(fxy_graph3d))
        self.wait()

        def l_func(u):
            return 0.4 * (u ** 3 + u ** 2 - 6 * u)
        l_graph = ParametricFunction(
            lambda u: np.array([
                u,
                0.4 * (u ** 3 + u ** 2 - 6 * u),
                0
            ]), color=RED, t_range=(-2, 2),
        ).set_z_index(1)

        self.play(Create(l_graph))
        self.wait(5)

        # ds
        self.move_camera(phi=0,theta=0)
        self.wait(1)
        #   获取二维点集数学物件列表，用于显示函数上的点，步长n将从1到4逐渐变密（步长变短）
        #   1/5步长
        func_dot = VGroup(*list(
            Dot((i / 5, l_func(i/5), 0))
            .scale(.5)
            .set_color(GREEN)
            .set_z_index(3)
            for i in range(-10, 10)))
        #   1/10步长
        func_dot2 = VGroup(*list(
            Dot((i / 10, l_func(i/10), 0))
            .scale(.5)
            .set_color(GREEN)
            .set_z_index(3)
            for i in range(-20, 20)))
        #   1/20步长
        func_dot3 = VGroup(*list(
            Dot((i / 20, l_func(i/20), 0))
            .scale(.5)
            .set_color(GREEN)
            .set_z_index(3)
            for i in range(-40, 40)))
        lines = VGroup(*list(
            Line(func_dot[i],func_dot[i+1])
            for i in range(0,19)
        )).set_color(BLUE).set_z_index(4)
        lines2 = VGroup(*list(
            Line(func_dot2[i],func_dot2[i+1])
            for i in range(0,39)
        )).set_color(BLUE).set_z_index(4)
        lines3 = VGroup(*list(
            Line(func_dot3[i],func_dot3[i+1])
            for i in range(0,79)
        )).set_color(BLUE).set_z_index(4)

        self.play(Create(func_dot))
        self.play(FadeOut(l_graph))
        self.wait(2)
        self.play(Create(lines))
        self.wait(3)
        self.play(ReplacementTransform(func_dot,func_dot2))
        self.play(ReplacementTransform(lines,lines2))
        self.play(ReplacementTransform(func_dot2,func_dot3))
        self.play(ReplacementTransform(lines2,lines3))
        self.wait(5)
