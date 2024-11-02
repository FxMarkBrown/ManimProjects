from manim import *


class Fourier3D(ThreeDScene):
    def construct(self):
        axes = (
            ThreeDAxes(
            x_range=[0, 5, 1],
            y_range=[0, 5, 1],
            z_range=[0, 2, 1],
            axis_config={"include_numbers": True, "include_tip": False},
            )
            .shift(2*IN)
            .set_color(GRAY)
        )
        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES, zoom=0.7)
        self.add(axes)

        #画出一个xoz面(y=0)内叠加的正弦函数
        func = (ParametricFunction(lambda t: np.array([
            t,
            0,
            np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t)
        ]), t_range=(-2, 4))
        .shift(-5*Y_AXIS)
        .set_color_by_gradient(ORANGE))

        func_1 = (ParametricFunction(lambda t: np.array([
            t,
            1,
            np.cos(t)
        ]), t_range=(-2, 4), stroke_opacity=0.3)
        .shift(-5 * Y_AXIS)
        .set_color_by_gradient(RED))

        func_2 = (ParametricFunction(lambda t: np.array([
            t,
            2,
            0.5 * np.cos(7 * t)
        ]), t_range=(-2, 4), stroke_opacity=0.3)
        .shift(-5 * Y_AXIS)
        .set_color_by_gradient(BLUE))

        func_3 = (ParametricFunction(lambda t: np.array([
            t,
            3,
            (1 / 7) * np.cos(14 * t)
        ]), t_range=(-2, 4), stroke_opacity=0.3)
        .shift(-5 * Y_AXIS)
        .set_color_by_gradient(GREEN))

        self.add(func, func_1, func_2, func_3)

        tex1 = (MathTex(r"f(x) = g(x) + h(x) + r(x)")
                .move_to(func)
                .shift(2*Z_AXIS)
                .rotate(PI/2, axis=X_AXIS))
        tex1[0][0:4].set_color(ORANGE)
        tex1[0][5:9].set_color(RED)
        tex1[0][10:14].set_color(BLUE)
        tex1[0][15:19].set_color(GREEN)
        self.add(tex1)

class Fourier(Scene):
    def construct(self):
        axes = (
            Axes(
                x_range=[0, 5, 1],
                y_range=[0, 5, 1],
                axis_config={"include_numbers": True, "include_tip": False},
            )
            .to_edge(DL)
            .set_color(GREY)
            .shift(0.5*DOWN)
        )

        self.add(axes)

        func = axes.plot(lambda t: 2 + np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t), color=RED, x_range=[1, 4.5])

        self.add(func)

        title = Title(r"y = f(x)")

        self.add(title)
