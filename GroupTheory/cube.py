import numpy as np
from manim import *
import random


def get_cube(color=GREEN, opacity=1, height=2):
    cube = Cube()
    cube.set_color(color)
    cube.set_opacity(opacity)
    cube.center()

    cube.set_height(height)
    return cube


class SymmetriesOfACube(ThreeDScene):
    def construct(self):
        # Setup
        self.camera.light_source.move_to(5 * LEFT + 20 * DOWN + 10 * OUT)
        axes = ThreeDAxes().set_z_index(0)
        labels = axes.get_axis_labels(
            Text("x").scale(0.7), Text("y").scale(0.45), Text("z").scale(0.45)
        )
        self.add(axes,labels)

        cube = get_cube(color=BLUE, opacity=0.5)
        cube.set_gloss(0.5)
        cube.set_shadow(0.2)
        cube.set_z_index(2)

        self.move_camera(
            phi=70 * DEGREES,
            theta=-30 * DEGREES,
        )
        self.begin_ambient_camera_rotation()

        self.add(cube)

        dotA1 = Dot3D(cube.get_corner(np.array([-1, -1, -1]))).scale(1).set_color(RED)
        dotA2 = Dot3D(cube.get_corner(np.array([-1, 1, -1]))).scale(1).set_color(PINK)
        dotA3 = Dot3D(cube.get_corner(np.array([-1, 1, 1]))).scale(1).set_color(ORANGE)
        dotA4 = Dot3D(cube.get_corner(np.array([-1, -1, 1]))).scale(1).set_color(PURPLE)
        dotA5 = Dot3D(cube.get_corner(np.array([1, -1, -1]))).scale(1).set_color(TEAL)
        dotA6 = Dot3D(cube.get_corner(np.array([1, 1, -1]))).scale(1).set_color(LIGHT_BROWN)
        dotA7 = Dot3D(cube.get_corner(np.array([1, 1, 1]))).scale(1).set_color(MAROON)
        dotA8 = Dot3D(cube.get_corner(np.array([1, -1, 1]))).scale(1).set_color(YELLOW)
        cube.add(dotA1, dotA2, dotA3, dotA4, dotA5, dotA6, dotA7, dotA8)

        tex1 = Tex("A1").next_to(dotA1).scale(0.8).set_color(RED).shift(LEFT)
        tex2 = Tex("A2").next_to(dotA2).scale(0.8).set_color(PINK).shift(LEFT)
        tex3 = Tex("A3").next_to(dotA3).scale(0.8).set_color(ORANGE).shift(LEFT)
        tex4 = Tex("A4").next_to(dotA4).scale(0.8).set_color(PURPLE).shift(LEFT)
        tex5 = Tex("A5").next_to(dotA5).scale(0.8).set_color(TEAL)
        tex6 = Tex("A6").next_to(dotA6).scale(0.8).set_color(LIGHT_BROWN)
        tex7 = Tex("A7").next_to(dotA7).scale(0.8).set_color(MAROON)
        tex8 = Tex("A8").next_to(dotA8).scale(0.8).set_color(YELLOW)
        self.play(Write(tex1), Write(tex2), Write(tex3), Write(tex4), Write(tex5), Write(tex6), Write(tex7), Write(tex8))
        self.wait(4)
        self.play(FadeOut(tex1,tex2,tex3,tex4,tex5,tex6,tex7,tex8))


        question = Title("执行怎样的行为后正方体还能保持原状?")
        question.set_height(0.7)
        question.to_edge(UP)
        self.add_fixed_in_frame_mobjects(question)

        def get_rotation(deg, axis, cube=cube):
            return Rotate(cube, deg * DEGREES, axis=axis, run_time=1.5)

        pairs = [
            (90, UP),
            (90, RIGHT),
            (90, OUT),
            (120, [1, 1, 1]),
            (120, [1, -1, 1]),
            (180, UP),
        ]

        for deg, axis in pairs:
            self.play(get_rotation(deg, axis))
            self.wait()

        # Count cube symmetries
        count_label = Tex("24 ", "种方式（旋转）")
        count_label.set_color_by_tex("24", YELLOW)
        count_label.set_height(0.7)
        count_label.to_edge(UP)
        self.add_fixed_in_frame_mobjects(count_label)

        self.play(
            FadeIn(count_label, shift=DOWN),
            FadeOut(question, shift=UP),
        )
        self.play(get_rotation(120, [1, -1, -1]))
        self.wait()
        self.play(get_rotation(90, LEFT))
        self.wait()
        self.play(get_rotation(120, [1, -1, -1]))
        self.wait()
        self.play(get_rotation(180, OUT))
        self.wait()


        reflection_plane = Square()
        reflection_plane.set_width(4)
        reflection_plane.move_to((0,0,0))
        reflection_plane.set_color(GREY)
        reflection_plane.set_opacity(0.4)
        reflection_plane.rotate(PI / 2, DOWN)
        reflection_plane.set_z_index(1)

        self.remove(count_label)
        count_label2 = Tex("48 ", "种方式（旋转+对称）")
        count_label2.set_color_by_tex("48", PINK)
        count_label2.set_height(0.7)
        count_label2.to_edge(UP)
        self.add_fixed_in_frame_mobjects(count_label2)

        self.play(FadeIn(reflection_plane, scale=LARGE_BUFF))
        self.play(
            ApplyMethod(cube.stretch, -1, 0),
        )
        self.wait()
        self.play(
            Rotate(reflection_plane, PI / 2, axis=UP)
        )
        self.play(
            ApplyMethod(cube.stretch, -1, 2),
        )
        self.wait()
        self.play(Rotate(reflection_plane, PI / 4, UP))

        matrix1 = rotation_matrix(-PI / 4, Y_AXIS)
        matrix2 = np.array([
            [1, 0, 0],
            [0, 1, 0],
            [0, 0, -1]
        ])
        matrix3 = rotation_matrix(PI / 4, Y_AXIS)
        matrix_final = matrix1 @ matrix2 @ matrix3
        self.play(
            cube.animate.apply_matrix(matrix_final)
        )
        self.wait()
        self.play(FadeOut(reflection_plane))
        self.wait()

        def explostion_transform(self=self, cube=cube):
            cube_copy = cube.copy()
            self.play(
                cube.animate.space_out_submobjects(1.5),
                cube.animate.shift(0.5 * OUT),
            )
            exploded_cube_copy = cube.copy()
            self.play(LaggedStart(*[
                Rotate(
                    face,
                    axis=face.get_center() - cube.get_center(),
                    angle=random.choice([0, PI / 2, -PI / 2, PI])
                )
                for face in cube
            ]))
            perm = list(range(6))
            random.shuffle(perm)
            globals()['perm'] = perm
            self.play(LaggedStart(*[
                Transform(face, cube_elem)
                for cube_elem, face in zip(cube, [cube[i] for i in perm] if len(cube) >= 6 else cube)
            ], lag_ratio=0.1))
            cube.become(exploded_cube_copy)
            self.play(Transform(cube, cube_copy))
            self.wait()

        self.play(FadeOut(dotA1,dotA2,dotA3,dotA4,dotA5,dotA6,dotA7,dotA8))
        for x in range(3):
            explostion_transform()


        self.remove(count_label2)
        count_label3 = Tex("188743680 ", "种方式(允许每个面旋转对称)")
        count_label3.set_color_by_tex("188743680", RED)
        count_label3.set_height(0.7)
        count_label3.to_edge(UP)
        self.add_fixed_in_frame_mobjects(count_label3)
        for x in range(3):
            explostion_transform()
        self.wait(2)
