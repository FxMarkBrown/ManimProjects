from manim import *


class rotatingSurfaces(ThreeDScene):
    def construct(self):
        self.move_camera(phi=70 * DEGREES, theta=-37 * DEGREES, zoom=0.8)
        axes = ThreeDAxes()
        self.add(axes)
        self.theta = 1e-6
        #   待旋转函数z=2-lny (yoz面上)(f(y,z)=z+lny-2=0)
        line_func = lambda y: np.array([
            0,
            y,
            2 - np.log(y)
        ])
        line_rotate = ParametricFunction(line_func, t_range=(1, 3), stroke_color=PINK,
                                         stroke_width=8, stroke_opacity=0.5)
        #   施加旋转矩阵后获得的函数z=f(u,v)
        surface_func = lambda u, v: np.dot(
            line_func(v),  # 传入y到待旋转函数，获得所有z=2-lny的点
            rotation_matrix(u, OUT).T  # 将x沿z轴(OUT表示z轴正向np.array[0,0,1])旋转x度,转为tuple
        )
        #   绘图，先转1度
        surface_rotate = Surface(surface_func, u_range=(0, self.theta), v_range=(1, 3))
        #   dθ
        dtheta = 1 * DEGREES

        #   更新旋转
        def update_surface(s, dt):
            if self.theta <= 360 * DEGREES:
                s.become(Surface(surface_func,
                                 u_range=(0, self.theta),
                                 v_range=(1, 3),
                                 fill_color=BLUE, fill_opacity=0.8,
                                 stroke_color=WHITE, stroke_width=1.6
                                 ))
                self.theta += dtheta

        self.add(line_rotate)
        dot1 = Dot((0, 0, 2 - np.log(1)))
        dot2 = Dot((0, 1, 2 - np.log(1))).scale(0.9).set_color(RED)
        tex = (MathTex("f(y,z)=0")
               .scale(0.7)
               .next_to(dot2).shift(2 * Z_AXIS)
               .rotate(PI / 2, axis=X_AXIS).rotate(PI / 3, axis=Z_AXIS))
        self.play(Write(tex))
        self.wait(2)
        self.play(FadeOut(tex))
        self.play(FadeIn(dot2, scale=2))
        dashedline = DashedLine(
            dot1,
            dot2
        ).set_color(YELLOW)
        self.play(Create(dashedline))
        brace = Brace(mobject=VGroup(dot1, dot2), direction=RIGHT, buff=0)
        bracetext = brace.get_tex("|y_1|")
        tex2 = (MathTex("f(y_1,z_1)=0")
                .scale(0.7)
                .next_to(dot2).shift(1 * Y_AXIS)
                .rotate(PI / 2, axis=X_AXIS).rotate(PI / 3, axis=Z_AXIS))
        tex2[0][2:4].set_color(RED)
        tex2[0][5:7].set_color(RED)
        self.play(GrowFromCenter(brace), FadeIn(bracetext))
        self.move_camera(phi=0, theta=0)
        self.wait(1)
        self.move_camera(phi=70 * DEGREES, theta=-37 * DEGREES)
        self.play(Write(tex2))
        self.wait(2)
        self.play(FadeOut(brace, bracetext))
        #   旋转原函数
        line_rotate.add_updater(lambda l, dt: l.rotate(dtheta, about_point=ORIGIN))
        surface_rotate.add_updater(update_surface)
        dashedline.add_updater(lambda l, dt: l.rotate(dtheta, about_point=ORIGIN))
        dot2.add_updater(lambda l, dt: l.rotate(dtheta, about_point=ORIGIN))
        self.begin_ambient_camera_rotation()
        self.add(surface_rotate)
        tex3 = (MathTex(r"|y_1|=\sqrt{x^2+y^2}")
                .scale(0.7)
                .next_to(line_rotate).shift(2 * X_AXIS)
                .rotate(PI / 2, axis=X_AXIS).rotate(PI / 3, axis=Z_AXIS))
        tex3[0][1:3].set_color(RED)
        self.wait(2)
        self.play(Write(tex3))
        tex4 = (MathTex(r"y_1=\pm\sqrt{x^2+y^2}")
                .scale(0.7)
                .next_to(dot2).shift(3.5 * Y_AXIS)
                .rotate(PI / 2, axis=X_AXIS).rotate(PI / 3, axis=Z_AXIS))
        tex4[0][0:2].set_color(RED)
        self.wait(1)
        self.play(ReplacementTransform(tex3, tex4))
        self.wait(1)
        self.play(TransformFromCopy(tex4, tex2))
        self.play(FadeOut(tex4))
        tex5 = (MathTex(r"f(\pm\sqrt{x^2+y^2},z)=0")
                .scale(0.7)
                .next_to(dot2).shift(3.5 * Y_AXIS)
                .rotate(PI / 2, axis=X_AXIS).rotate(PI / 3, axis=Z_AXIS))
        self.play(ReplacementTransform(tex2, tex5))
        self.wait(10)
