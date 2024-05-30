import numpy as np
from manim import *


class HyperbolicParaboloid(ThreeDScene):
    def construct(self):
        self.move_camera(phi=70 * DEGREES, theta=-37 * DEGREES, zoom=0.8)
        axes = ThreeDAxes()
        surface_hp = Surface(lambda u, v: np.array([
            u,
            v,
            u ** 2 / 4 - v ** 2 / 4
        ]), u_range=(-2, 2), v_range=(-2, 2), color=GREEN)
        self.add(axes, surface_hp)
        tex = (MathTex(r"z=\frac{x^2}{a^2}-\frac{y^2}{b^2}")
               .scale(0.7)
               .next_to(surface_hp).shift(2 * Z_AXIS)
               .rotate(PI / 2, axis=X_AXIS).rotate(PI / 3, axis=Z_AXIS))
        self.play(Write(tex))
        self.wait(1)
        surface_toshift = Surface(lambda u, v: np.array([
            -2,
            u,
            v
        ]), u_range=(-2, 2), v_range=(-2, 2), checkerboard_colors=[BLUE_D, BLUE_E], fill_opacity=0.5)
        self.play(FadeIn(surface_toshift))
        tex2 = MathTex("x=x_0").next_to(surface_toshift).shift(2*Z_AXIS).rotate(PI / 2, axis=X_AXIS).rotate(PI / 2, axis=Z_AXIS)
        self.play(Write(tex2))
        self.wait(2)

        curve_toshift = ParametricFunction(lambda t: np.array([
            -2,
            t,
            (-2) ** 2 / 4 - t ** 2 / 4
        ]), color=RED, t_range=(-2, 2))
        self.play(Create(curve_toshift))
        self.wait(2)
        tex3 = MathTex(r"z=\frac{{x_0}^2}{a^2}-\frac{y^2}{b^2}").next_to(surface_toshift).shift(2*Z_AXIS).rotate(PI / 2, axis=X_AXIS).rotate(PI / 2, axis=Z_AXIS).set_color(RED)
        self.play(ReplacementTransform(tex2, tex3))
        tex4 = MathTex(r"y^2=\frac{b^2}{a^2}{x_0}^2-z").next_to(surface_toshift).shift(2*Z_AXIS).rotate(PI / 2, axis=X_AXIS).rotate(PI / 2, axis=Z_AXIS).set_color(RED)
        self.wait(2)
        self.play(ReplacementTransform(tex3, tex4))
        self.wait(2)
        self.play(FadeOut(tex4))
        self.wait(1)
        def curve(ddx=1.0):
            return ParametricFunction(lambda t: np.array([
                ddx,
                t,
                ddx ** 2 / 4 - t ** 2 / 4
            ]), color=RED, t_range=(-2, 2))

        def surface(dx=1.0):
            return Surface(lambda u, v: np.array([
                dx,
                u,
                v
            ]),u_range=(-2, 2), v_range=(-2, 2), checkerboard_colors=[BLUE_D, BLUE_E], fill_opacity=0.5)

        def update_curve(k, alpha):
            ddx = interpolate(-2, 2, alpha)
            k_k = curve(ddx)
            k.become(k_k)

        def update_surface(kk, alpha):
            dx = interpolate(-2, 2, alpha)
            k_kk = surface(dx)
            kk.become(k_kk)


        self.play(UpdateFromAlphaFunc(curve_toshift, update_curve),
                  UpdateFromAlphaFunc(surface_toshift, update_surface))
        self.wait(3)
