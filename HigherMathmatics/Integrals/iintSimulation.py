from manim import *


#   二重积分模拟
class iintSimulation(ThreeDScene):

    #   与上方相同
    def construct(self):
        #   建系建轴
        axes = ThreeDAxes()
        grid = NumberPlane().set_stroke(WHITE, 0.1)
        #   建立网格线
        grid2 = grid.copy().next_to(grid, UP, buff=0)
        grid3 = grid.copy().next_to(grid, DOWN, buff=0)
        grid4 = grid.copy().next_to(grid, LEFT + UP, buff=0)
        grid5 = grid.copy().next_to(grid, LEFT + DOWN, buff=0)
        grid6 = grid.copy().next_to(grid, LEFT, buff=0)
        grid7 = grid.copy().next_to(grid, RIGHT, buff=0)
        #   渲染系，轴，网格线
        self.add(grid2, grid3, grid4, grid5, grid6, grid7)
        self.play(Write(axes), Write(grid))

        #   要模拟的函数f(x)（三次函数）
        def f(u):
            return 0.4 * (u ** 3 + u ** 2 - 6 * u)

        #   函数绘图
        func_graph = ParametricFunction(
            lambda u: np.array([
                u,
                0.4 * (u ** 3 + u ** 2 - 6 * u),
                0
            ]), color=RED, t_range=(-4, 4),
        )
        #   获取二维点集数学物件列表，用于显示函数上的点，步长n将从1到4逐渐变密（步长变短）
        #   1/5步长
        func_dot = VGroup(*list(
            Dot((i / 5, f(i/5), 0))
            .scale(.5)
            .set_color(RED)
            for i in range(-20, 20)))
        #   1/10步长
        func_dot2 = VGroup(*list(
            Dot((i / 10, f(i/10), 0))
            .scale(.5)
            .set_color(RED)
            for i in range(-40, 40)))
        #   1/20步长
        func_dot3 = VGroup(*list(
            Dot((i / 20, f(i/20), 0))
            .scale(.5)
            .set_color(RED)
            for i in range(-80, 80)))
        #   1/40步长
        func_dot4 = VGroup(*list(
            Dot((i / 40, f(i/40), 0))
            .scale(.5)
            .set_color(RED)
            for i in range(-160, 160)))
        #   绘制Latex函数文字 y=f(x)
        y = Tex(r"y=f(x)").scale(2).to_corner(UL)

        #   渲染
        self.play(Write(y))
        self.wait(1)
        self.play(Create(func_dot, run_time=2))
        self.wait(1)
        #   变换点集，展示步长变短时，无数的点最终会变为函数的图像
        self.play(ReplacementTransform(func_dot, func_dot2))
        self.play(ReplacementTransform(func_dot2, func_dot3))
        self.play(ReplacementTransform(func_dot3, func_dot4))
        self.wait(2)
        self.play(FadeIn(func_graph), FadeOut(func_dot4))
        self.wait(2)
        #   创建一个点，沿函数路径到达指定位置
        dot = (Dot((-3, 0.4 * ((-4) ** 3 + (-4) ** 2 - 6 * (-4)), 0))
               .set_color(RED)
               .scale(.7))
        self.play(MoveAlongPath(dot, func_graph, run_time=4))
        #   创建平行于y轴的虚线，从(2.2,0,0)点到（2.2,f(2.2))
        dashedline_y = (DashedLine(
            (2.2, 0, 0),
            (2.2, f(2.2), 0))
                        .set_color(YELLOW))
        #   创建平行于x轴的虚线，从(2.2,f(2,2))到(0,f(2.2))
        dashedline_x = (DashedLine(
            (2.2, f(2.2), 0),
            (0, f(2.2), 0))
                        .set_color(YELLOW))
        #   给虚线加上Latex文字
        fx = (Tex(r"f(x)")
              .next_to(dashedline_y, RIGHT)
              .scale(.7))
        x = (Tex(r"x")
             .next_to(dashedline_x, UP)
             .scale(.7))
        #   淡入效果渲染虚线和文字，然后淡出
        self.play(Create(dashedline_x), FadeIn(x))
        self.play(Create(dashedline_y), FadeIn(fx))
        self.wait(1)
        self.play(FadeOut(dashedline_y), FadeOut(dashedline_x), FadeOut(dot), FadeOut(x), FadeOut(fx))
        self.wait(5)

        #   新增部分
        #   生成一个一元定积分公式
        integral = MathTex(r"\int_a^bf(x)dx").move_to(y)
        integral[0][1].set_color(GREEN)
        integral[0][2].set_color(PURPLE)

        #   预先构建的逼近一元定积分(实际上积分区域大致为x从-3到0)的函数下方面积的小矩形intRectangle1到4
        #   每个小矩形宽为 3/n(不取3/n的原因是矩形太窄)，高为f(i/n)，构建完成后放入列表
        #   构建完毕后将列表内的这些小矩形填充在函数下方(填充时移动矩形到函数下方(移动时以矩形中心即高/2为参考))，(-3,0的区间内)
        #   之后让n分别取7,14,29,59，模拟n趋于无穷时矩形变的无限窄的效果
        intRectangle = VGroup(*list(
            Rectangle(width=3 / 7, height=f(-3 * i/7),
                      color=BLUE, stroke_width=0) for i in range(0, 8)))
        for i in range(0, 8):
            intRectangle[i].move_to(
                (-3 * i / 7, f(-3 * i/7)/2, 0))
            intRectangle[i].set_fill(BLUE, opacity=0.5)

        intRectangle2 = VGroup(*list(
            Rectangle(width=3 / 14, height=f(-3 * i/14),
                      color=BLUE, stroke_width=0) for i in range(0, 15)))
        for i in range(0, 15):
            intRectangle2[i].move_to(
                (-3 * i / 14, f(-3 * i/14)/2, 0))
            intRectangle2[i].set_fill(BLUE, opacity=0.5)

        intRectangle3 = VGroup(*list(
            Rectangle(width=3 / 29, height=f(-3 * i/29),
                      color=BLUE, stroke_width=0) for i in range(0, 30)))
        for i in range(0, 30):
            intRectangle3[i].move_to(
                (-3 * i / 29, f(-3 * i/29)/2, 0))
            intRectangle3[i].set_fill(BLUE, opacity=0.5)

        intRectangle4 = VGroup(*list(
            Rectangle(width=3 / 59, height=f(-3 * i/59),
                      color=BLUE, stroke_width=0) for i in range(0, 60)))
        for i in range(0, 60):
            intRectangle4[i].move_to(
                (-3 * i / 59, f(-3 * i/59)/2, 0))
            intRectangle4[i].set_fill(BLUE, opacity=0.5)

        #   下面开始演示
        #   往后我们会生成一个小矩形们从坐标轴上升起的动画
        #   首先创建7个宽度为3/n但高度几乎为0的矩形r0
        r0 = VGroup(*list(
            Rectangle(width=3 / 7, height=0.01 + 0 * i,
                      color=BLUE, stroke_width=0)
            for i in range(0, 8)))
        #   然后将r0填充在函数下方的区域
        for i in range(0, 8):
            r0[i].move_to((-3 * i / 7, 0.005, 0))
            r0[i].set_fill(BLUE, opacity=0.5)
        #   设置颜色
        intRectangle.set_color_by_gradient(ORANGE, PURPLE)
        intRectangle2.set_color_by_gradient(ORANGE, PURPLE)
        intRectangle3.set_color_by_gradient(ORANGE, PURPLE)
        intRectangle4.set_color_by_gradient(ORANGE, PURPLE)
        r0.set_color_by_gradient(ORANGE, PURPLE)
        #   渲染，首先展示要测量函数下方的面积，函数下方的面积用intRectangle4表示，因为此时已经非常趋近面积
        self.play(FadeIn(intRectangle4))
        self.wait(1)
        self.play(FadeOut(intRectangle4))
        self.wait(1)
        #   之后展示一个动画，从r0变换到intRectangle，因为r0的高度是几乎为0，所以此时会出现上升的动画
        self.play(ReplacementTransform(r0, intRectangle))
        self.wait(1)
        #   创建底部和左部括号，描述n取7时的小矩形的宽，并展示出来
        brace2d = Brace(mobject=intRectangle[4], direction=DOWN, buff=0)
        text2d = brace2d.get_tex(r"\Delta x")
        brace2d2 = Brace(mobject=intRectangle[4], direction=LEFT, buff=0.1)
        text2d2 = brace2d2.get_tex(r"f(x)")
        self.play(GrowFromCenter(brace2d), FadeIn(text2d))
        self.wait(1)
        self.play(GrowFromCenter(brace2d2), FadeIn(text2d2))
        #   创建底部和左部括号，描述n取14时的小矩形的宽，并展示出来
        brace2d3 = Brace(mobject=intRectangle2[8], direction=DOWN, buff=0)
        text2d3 = brace2d3.get_tex(r"\Delta x")
        self.wait(1)
        self.play(FadeOut(brace2d2), FadeOut(text2d2))
        self.play(ReplacementTransform(intRectangle, intRectangle2), ReplacementTransform(brace2d, brace2d3),
                  ReplacementTransform(text2d, text2d3))
        #   创建底部和左部括号，描述n取29时的小矩形的宽，并展示出来
        brace2d5 = Brace(mobject=intRectangle3[16], direction=DOWN, buff=0)
        text2d5 = brace2d5.get_tex(r"\Delta x")
        self.play(ReplacementTransform(intRectangle2, intRectangle3), ReplacementTransform(brace2d3, brace2d5),
                  ReplacementTransform(text2d3, text2d5))
        #   创建底部和左部括号，描述n取59时的小矩形的宽，并展示出来
        brace2d7 = Brace(mobject=intRectangle4[32], direction=DOWN, buff=0)
        text2d7 = brace2d7.get_tex(r"\Delta x")
        self.play(ReplacementTransform(intRectangle3, intRectangle4), ReplacementTransform(brace2d5, brace2d7),
                  ReplacementTransform(text2d5, text2d7))
        self.wait(1)
        #   此时将Δx变为dx
        text2d9 = Tex(r"dx").move_to(text2d7)
        self.play(ReplacementTransform(text2d7, text2d9))
        self.wait(1)
        #   染色坐标轴：创建一条粉色的线，从-3到0
        pinkline = Line((-3, 0, 0), (0, 0, 0)).set_color(PINK)
        section_a = Tex(r"a").move_to((-2.9, -0.2, 0)).set_color(PURPLE)
        section_b = Tex(r"b").move_to((-0.1, -0.2, 0)).set_color(GREEN)
        self.play(Create(pinkline, run_time=3))
        self.play(FadeIn(section_a, scale=5))
        self.play(FadeIn(section_b, scale=5))
        #   将左上角的表达式淡出，换位积分表达式
        self.play(FadeOut(y))
        self.play(FadeIn(integral, shift=DOWN))
        self.wait(1)
        #   淡出大括号和文字
        self.play(FadeOut(text2d9), FadeOut(text2d7), FadeOut(brace2d7))
        self.play(integral[0].animate.scale(1.5))
        self.play(integral[0].animate.scale(0.7))
        self.wait(1)
        #   使用save_state()函数复制每个小矩形的属性存为一份副本，后用Restore函数恢复现在的状态
        for i in range(0, 60):
            intRectangle4[i].save_state()
        #   枚举每一个小矩形依次将它们染成黄色并恢复原颜色
        for i in range(0, 60):
            self.play(intRectangle4[59 - i].animate.set_color(YELLOW), run_time=0.004)
            self.play(Restore(intRectangle4[59 - i], run_time=0.004))
        self.wait(1)

        #   下面开始旋转摄像机，因为创建的是3D场景，默认摄像机看向的是xoy平面，但旋转摄像机后就可以看到z轴

        #   构建二重积分的被积函数
        fxy_graph3d = Surface(
            lambda u, v: np.array([
                u,
                v,
                np.cos(u) + np.sin(v) + 2
            ]), v_range=(-7, 7), u_range=(-7, 7), checkerboard_colors=[BLUE_D, BLUE_E],
            resolution=(30, 63)).fade(.7)

        #   移动摄像机位置（球面坐标），φ取70度，θ取37度
        self.move_camera(phi=70 * DEGREES, theta=-37 * DEGREES)
        #   旋转视角，并让之前的符号淡出
        self.begin_ambient_camera_rotation(rate=0.007)
        self.play(FadeOut(func_graph), FadeOut(intRectangle4), FadeOut(integral), FadeOut(section_a), FadeOut(section_b),
                  FadeOut(pinkline))

        #   预先构建的逼近二重积分(实际上积分区域大致为x从-3到0)的函数下方面积的小长方体intRectangle1到4
        #   每个小矩形长宽为 1/n，高为f(i/n)，构建完成后放入列表
        #   构建完毕后将列表内的这些小矩形填充在函数下方，([1,2]x[1,2]的区间内)
        #   之后让n分别取5,10,20,40，模拟n趋于无穷时矩形变的无限窄的效果
        iintPrism = VGroup(*list(
            VGroup(*list(
                Prism(dimensions=(1 / 5, -(1 / 5), np.cos(1 + i / 5) * np.sin(1 + j / 5) + 2), stroke_width=0)
                for i in range(0, 11))) for j in range(0, 11)))
        for i in range(0, 11):
            for j in range(0, 11):
                iintPrism[j][i].move_to((1 + i / 5, -(1 + j / 5), (np.cos(1 + i / 5) * np.sin(1 + j / 5) + 2) / 2))
        iintPrism.set_color_by_gradient(ORANGE, PURPLE)

        iintPrism2 = VGroup(*list(VGroup(*list(
            Prism(dimensions=(1 / 10, -(1 / 10), np.cos(1 + i / 10) * np.sin(1 + j / 10) + 2),
                  stroke_width=0)
            for i in range(0, 21))) for j in range(0, 21)))
        for i in range(0, 21):
            for j in range(0, 21):
                iintPrism2[j][i].move_to((1 + i / 10, -(1 + j / 10), (np.cos(1 + i / 10) * np.sin(1 + j / 10) + 2) / 2))
        iintPrism2.set_color_by_gradient(ORANGE, PURPLE)

        iintPrism3 = VGroup(*list(
            VGroup(*list(
                Prism(dimensions=(1 / 20, -(1 / 20), np.cos(1 + i / 20) * np.sin(1 + j / 20) + 2), stroke_width=0)
                for i in range(0, 41))) for j in range(0, 41)))
        for i in range(0, 41):
            for j in range(0, 41):
                iintPrism3[j][i].move_to((1 + i / 20, -(1 + j / 20), (np.cos(1 + i / 20) * np.sin(1 + j / 20) + 2) / 2))
        iintPrism3.set_color_by_gradient(ORANGE, PURPLE)

        iintPrism4 = VGroup(*list(
            VGroup(*list(
                Prism(dimensions=(1 / 40, -(1 / 40), np.cos(1 + i / 40) * np.sin(1 + j / 40) + 2),
                      stroke_width=0)
                for i in range(0, 81))) for j in range(0, 81)))
        for i in range(0, 81):
            for j in range(0, 81):
                iintPrism4[j][i].move_to((1 + i / 40, -(1 + j / 40), (np.cos(1 + i / 40) * np.sin(1 + j / 40) + 2) / 2))
        iintPrism4.set_color_by_gradient(ORANGE, PURPLE)

        #   预构建小长方体升起的效果
        p0 = VGroup(*list(
            VGroup(*list(
                Prism(dimensions=(1 / 5, -(1 / 5), .01 + 0 * i * j),
                      stroke_width=0)
                for i in range(0, 11))) for j in range(0, 11)))
        for i in range(0, 11):
            for j in range(0, 11):
                p0[j][i].move_to((1 + i / 5, -(1 + j / 5), .005))
        p0.set_color_by_gradient(ORANGE, PURPLE)
        self.wait(1)

        #   现在开始模拟二元函数，首先画出xoy平面上的一些点
        #   点集从(1,1)开始，xy公差为1/3增加，画10x10=100个点
        planedot = VGroup(*list(
            VGroup(*list(
                Dot((1 + i / 3, 1 + j / 3, 0)).scale(.2)
                for i in range(0, 11))) for j in range(0, 11))).set_color(BLUE)
        #   创建平行于z轴的虚线，并加文字
        dashedline3d_z = (DashedLine((1 + 5 / 3, 1 + 5 / 3 - 3.5, 0),
                                     (1 + 5 / 3, -(1 + 5 / 3), np.cos(1 + 5 / 3) * np.sin(1 + 5 / 3) + 2))
                          .set_color(YELLOW))
        fxy3d = (Tex(r"f(x,y)")
                 .scale(.5)
                 .next_to(dashedline3d_z, LEFT)
                 .rotate(PI / 2, axis=Y_AXIS))
        fxy3d.rotate(PI / 2, axis=X_AXIS)
        fxy3d.shift(.2 * Z_AXIS + 0.2 * DOWN)
        #   下方创建平行于y，x的，同理
        dashedline3d_y = (DashedLine(
            (2 + 5 / 3, 0, 0),
            (2 + 5 / 3, 1 + 5 / 3 - 3.5, 0))
                          .set_color(YELLOW))
        y3d = Tex(r"y").next_to(dashedline3d_y).scale(.7)
        dashedline3d_x = (DashedLine((0, 1 + 5 / 3 - 3.5, 0),
                                     (1 + 5 / 3 + 1, 1 + 5 / 3 - 3.5, 0))
                          .set_color(YELLOW))
        x3d = Tex(r"x").next_to(dashedline3d_x, DOWN).scale(.7)
        x3d.shift(.7 * RIGHT)
        #   积分区域D文字
        iintD = Tex(r"D").next_to(p0)
        #   预创建dx，dy文字，调整方向及位置
        dx = (Tex(r"dx")
              .move_to(iintPrism[5][5]
                       .get_center()
                       + (np.cos(1 + 5 / 3) * np.sin(1 + 5 / 2) + 2.4) * Z_AXIS / 3 + (1 / 3 + .1) * DOWN)
              .rotate(PI / 2, axis=X_AXIS)
              .scale(.5))
        dx.rotate(PI / 2, axis=Z_AXIS)
        dy = (Tex(r"dy").move_to(iintPrism[5][5]
                                 .get_center()
                                 + (np.cos(1 + 5 / 3) * np.sin(1 + 5 / 2) + 2.5) * Z_AXIS / 3 + 1 / 3 * RIGHT)
              .rotate(PI / 2, axis=X_AXIS)
              .scale(.5))

        #   开始渲染
        #   首先渲染xoy平面上的点集
        self.play(FadeIn(planedot))

        #   下面开始将xoy平面内的点按z=f(x,y)升起一定高度
        for i in range(0, 11):
            for j in range(0, 11):
                self.play(planedot[j][i]
                          .animate.shift((np.cos(1 + i / 3) * np.sin(1 + j / 3) + 2) * Z_AXIS),
                          run_time=.05)
        self.wait(3)
        #   创建f(x,y)曲面
        self.play(Create(fxy_graph3d, run_time=2))
        self.wait(1)
        #   淡入虚线和虚线上的文字
        self.play(Create(dashedline3d_y), Create(dashedline3d_x))
        self.play(FadeIn(x3d), FadeIn(y3d))
        self.play(Create(dashedline3d_z))
        self.play(FadeIn(fxy3d))
        self.wait(3)
        #   淡出虚线和文字
        self.play(FadeOut(planedot), FadeOut(fxy3d), FadeOut(dashedline3d_z), FadeOut(x3d), FadeOut(y3d),
                  FadeOut(dashedline3d_y),
                  FadeOut(dashedline3d_x))
        #   停止摄像机旋转
        self.stop_ambient_camera_rotation()
        #   展示积分区域D（用p0表示）和文字
        self.play(FadeIn(p0))
        self.wait(1)
        self.play(FadeIn(iintD))
        #   将p0[5][5]变换为iintPrism[5][5]模拟一个小长方体升起
        self.play(ReplacementTransform(p0[5][5], iintPrism[5][5], run_time=3))
        #   创建大括号和文字
        brace_refdot = Dot((0, 0, 0))
        brace_refdot2 = Dot((np.cos(1 + 5 / 10) * np.sin(1 + 5 / 10) + 2, 0, 0))
        brace_ref = VGroup(brace_refdot, brace_refdot2)
        brace = (Brace(mobject=brace_ref, direction=DOWN, buff=0)
                 .rotate(PI / 2, axis=Y_AXIS)
                 .move_to(iintPrism[5][5]
                          .get_center() + 0.13 * LEFT + 0.2 * DOWN)
                 .scale(.7))
        text = (brace.get_tex(r"f(x,y)")
                .scale(.4)
                .next_to(brace, LEFT)
                .rotate(PI / 2, axis=Y_AXIS))
        text.shift(-.2 * Z_AXIS + 0.2 * DOWN)
        text.rotate(PI / 2, axis=X_AXIS)
        #   淡入大括号和文字
        self.play(GrowFromCenter(brace))
        self.play(FadeIn(text))
        #   淡入文字dx,dy
        self.play(FadeIn(dx), FadeIn(dy))
        self.wait(1)
        #   淡出曲边梯形，dx，dy，D文字，和大括号，将p0变换到iintPrism（升起所有小长方体）
        self.play(FadeOut(iintD), FadeOut(dx), FadeOut(dy), FadeOut(brace), FadeOut(text),
                  ReplacementTransform(p0, iintPrism, run_time=3))
        self.wait(1)
        #   淡出曲面
        self.play(FadeOut(fxy_graph3d))
        #   模拟n趋近无穷
        self.play(ReplacementTransform(iintPrism, iintPrism2))
        self.play(ReplacementTransform(iintPrism2, iintPrism3))
        self.play(ReplacementTransform(iintPrism3, iintPrism4))
        #   展示公式
        iintTex = MathTex(r"\iint_D f(x,y)dxdy")
        iintTex[0].shift(.23 * RIGHT)
        self.add_fixed_in_frame_mobjects(iintTex)
        iintTex.to_corner(UL)
        self.play(FadeIn(iintTex, shift=DOWN))
        self.begin_ambient_camera_rotation(rate=0.01)
        self.wait(5)
