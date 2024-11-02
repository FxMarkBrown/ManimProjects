from manim import *

class WallisSingle(Scene):
    def construct(self):
        axes = Axes(x_range=[0, TAU+2], y_range=[-2,2])

        sinx = axes.plot(lambda x: np.sin(x), color=RED, x_range=[0,TAU])
        area0toTAU = axes.get_area(
            sinx,
            x_range=(0,TAU),
            color=GREEN_B,
            opacity=1
        )
        area0toTAU_rieman = axes.get_riemann_rectangles(
            sinx,
            x_range=[0,TAU],
            dx=0.25,
            color=(TEAL,BLUE_B,DARK_BLUE)
        )
        TexSinx = MathTex(r"y=\sin x").move_to(3.5*UP+4*RIGHT).set_color(RED).scale(0.8)

        self.play(Create(axes),Create(sinx),Write(TexSinx))
        self.wait(2)
        self.play(Create(area0toTAU_rieman))
        self.wait(1)
        self.play(ReplacementTransform(area0toTAU_rieman,area0toTAU))

        intTex_sinx = MathTex(r"\int_{0}^{2\pi} \sin xdx").move_to(UP*3).set_color(GREEN)
        self.play(Write(intTex_sinx))
        self.wait(1)
        self.play(FadeOut(intTex_sinx))
        self.play(Uncreate(area0toTAU))


        sin3x = axes.plot(lambda x: np.sin(x) ** 3, color=LIGHT_PINK,x_range=[0,TAU])
        sin5x = axes.plot(lambda x: np.sin(x) ** 5, color=MAROON,x_range=[0,TAU])
        sin7x = axes.plot(lambda x: np.sin(x)** 7, color=PURPLE,x_range=[0,TAU])
        TexSin3x = MathTex(r"y=\sin^3 x").move_to(UR).set_color(RED).next_to(TexSinx,DOWN).set_color(LIGHT_PINK).scale(0.8)
        TexSin5x = MathTex(r"y=\sin^5 x").move_to(UR).set_color(RED).next_to(TexSin3x,DOWN).set_color(MAROON).scale(0.8)
        TexSin7x = MathTex(r"y=\sin^7 x").move_to(UR).set_color(RED).next_to(TexSin5x,DOWN).set_color(PURPLE).scale(0.8)

        sin3to7x = VGroup(sin3x,sin5x,sin7x)
        Texsin3to7x = VGroup(TexSin3x,TexSin5x,TexSin7x)

        self.wait(2)
        self.play(Create(sin3to7x),Write(Texsin3to7x))
        self.wait(2)
        self.play(Texsin3to7x.animate.set_opacity(0.5))
        self.play(FadeOut(sin3to7x))
        self.wait(1)
        self.play(TexSinx.animate.set_opacity(1))
        self.wait(1)
        self.play(ReplacementTransform(sinx,sin3x),TexSinx.animate.set_opacity(0.5),TexSin3x.animate.set_opacity(1))
        self.wait(1)
        self.play(TexSin3x.animate.set_opacity(0.5),ReplacementTransform(sin3x,sin5x),TexSin5x.animate.set_opacity(1))
        self.wait(1)
        self.play(TexSin5x.animate.set_opacity(0.5),ReplacementTransform(sin5x,sin7x),TexSin7x.animate.set_opacity(1))
        self.wait(1)
        self.play(FadeOut(sin7x),FadeOut(Texsin3to7x),FadeOut(TexSinx))

        self.wait(1)

        sin2x = axes.plot(lambda x: np.sin(x) ** 2, color=LIGHT_PINK,x_range=[0,TAU])
        sin4x = axes.plot(lambda x: np.sin(x) ** 4, color=MAROON,x_range=[0,TAU])
        sin6x = axes.plot(lambda x: np.sin(x) ** 6, color=PURPLE,x_range=[0,TAU])
        TexSin2x = MathTex(r"y=\sin^2 x").move_to(UR).set_color(RED).move_to(3.5*UP+4*RIGHT).set_color(LIGHT_PINK).scale(0.8)
        TexSin4x = MathTex(r"y=\sin^4 x").move_to(UR).set_color(RED).next_to(TexSin2x,DOWN).set_color(MAROON).scale(0.8)
        TexSin6x = MathTex(r"y=\sin^6 x").move_to(UR).set_color(RED).next_to(TexSin4x,DOWN).set_color(PURPLE).scale(0.8)

        sin2to6x = VGroup(sin2x,sin4x,sin6x)
        Texsin2to6x = VGroup(TexSin2x,TexSin4x,TexSin6x)

        self.play(Create(sin2to6x),Write(Texsin2to6x))
        self.wait(2)
        self.play(FadeOut(sin2to6x),FadeOut(Texsin2to6x))

        sinx = axes.plot(lambda x: np.sin(x), color=RED, x_range=[0, TAU])
        area0toPI = axes.get_area(
            sinx,
            x_range=(0, PI),
            color=GREEN_B,
            opacity=1
        )
        areaPItoTAU = axes.get_area(
            sinx,
            x_range=(PI, TAU),
            color=GREEN_A,
            opacity=1
        )
        areaPItoTAU_divides = VGroup(area0toPI, areaPItoTAU)

        int_sinx0toTAU = MathTex(r"\int_{0}^{2\pi} \sin xdx = 0").move_to(3*UP).set_color_by_gradient(ORANGE,PURPLE)
        self.play(Create(sinx),Create(areaPItoTAU_divides))
        self.wait(1.5)
        self.play(TransformFromCopy(area0toPI,areaPItoTAU))
        self.play(Uncreate(areaPItoTAU_divides))
        self.play(Write(int_sinx0toTAU))
        self.wait(1)


        area0toPId2 = axes.get_area(
            sinx,
            x_range=(0, PI/2),
            color=BLUE_A,
            opacity=1
        )
        areaPId2toPI = axes.get_area(
            sinx,
            x_range=(PI/2, PI),
            color=BLUE_E,
            opacity=1
        )
        area0toPI_divides = VGroup(area0toPId2,areaPId2toPI)

        int_sinx0toPI = MathTex(r"\int_{0}^{\pi} \sin xdx = 2\int_{0}^{\frac{\pi}{2}} \sin xdx").move_to(int_sinx0toTAU).set_color_by_gradient(ORANGE,PURPLE)
        self.play(Create(area0toPI_divides))
        self.play(TransformFromCopy(areaPId2toPI,area0toPId2))
        self.wait(1)
        self.play(FadeOut(areaPId2toPI))
        self.play(area0toPId2.animate.set_color(DARK_BLUE))
        self.wait(1)
        self.play(ReplacementTransform(int_sinx0toTAU,int_sinx0toPI))
        self.wait(3)


class WallisMultiple(Scene):
    def construct(self):
        axes = Axes(x_range=[0, TAU+2], y_range=[-2,2])
        self.play(Create(axes))

        sin2x = axes.plot(lambda x: np.sin(x)**2, color=RED,x_range=[0,TAU])
        cos3x = axes.plot(lambda x: np.cos(3*x)**3, color=BLUE_B,x_range=[0,TAU])

        TexSin2x = MathTex(r"y=\sin^2 x").move_to(UR).set_color(RED).move_to(3.5 * UP + 4 * RIGHT).set_color(RED).scale(0.8)
        TexCos3x = MathTex(r"y=\cos^3 x").move_to(UR).set_color(RED).next_to(TexSin2x, DOWN).set_color(BLUE_B).scale(0.8)
        Texsin2xMultiplycos3x = MathTex(r"y=\sin^2x\times\cos^3x").move_to(UR).set_color(GREEN_B).move_to(3.5 * UP + 4 * RIGHT).set_color(GREEN_B).scale(0.8)

        sin2xcos3x = VGroup(sin2x,cos3x)
        Texsin2xcos3x = VGroup(TexSin2x,TexCos3x)

        self.play(Create(sin2xcos3x,rate_func=linear),Write(Texsin2xcos3x))

        sin2xMultiplycos3x = axes.plot(lambda x: np.sin(x)**2*np.cos(x)**3, color=GREEN_B,x_range=[0,TAU])

        self.wait(2)
        self.play(ReplacementTransform(sin2xcos3x,sin2xMultiplycos3x),ReplacementTransform(Texsin2xcos3x,Texsin2xMultiplycos3x))

        area0toTAU = axes.get_area(
            sin2xMultiplycos3x,
            x_range=(0, TAU),
            color=GREEN,
            opacity=1
        )

        self.wait(2)
        self.play(FadeIn(area0toTAU, rate_func=linear))
        self.wait(3)