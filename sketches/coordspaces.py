from manim import *
from manim_slides import ThreeDSlide

class Coord(ThreeDSlide):
    def construct(self):
        # Criando um plano 3D
        plane = Surface(
            lambda u, v: np.array([u, v, 0]),  # Z é sempre 0 → plano XY
            u_range=[-16, 16], v_range=[-16, 16],  # Tamanho do plano
            resolution=(32, 32),  # Resolução da grade
            fill_opacity=0.0,  # Transparência (0.0 = invisível, 1.0 = opaco)
            checkerboard_colors=[GRAY, GRAY],
            color=GRAY,  # Cor do plano
            stroke_width=0.5  # Linhas da grade
        )
        title = Text("Sistema de coordenadas")
        subtitle = Text("Local space")
        title.to_edge(UL)
        subtitle.next_to(title, DOWN)
        subtitle.align_to(title, LEFT)

        self.play(FadeIn(plane), Write(title))
        self.next_slide()
        cameraBox = Prism(dimensions=[0.5, 0.3, 0.3])
        cameraBox.color = GRAY
        cameraLens = Cone(base_radius=0.2, height=0.1).rotate(PI/2, axis=DOWN)
        cameraLens.color = GRAY
        cameraLens.next_to(cameraBox,RIGHT, buff=0.0)
        myCamera =Group(cameraBox, cameraLens)
        myCamera.rotate(PI, RIGHT)

        cube1 = Cube(fill_opacity=0.7, side_length=1.0)
        cube1.move_to(np.array([1,2,0]))
        cube1.rotate(60 * DEGREES)
        vertex_coords = [
            [1, 1, 0],
            [1, -1, 0],
            [-1, -1, 0],
            [-1, 1, 0],
            [0, 0, 2]
        ]
        faces_list = [
            [0, 1, 4],
            [1, 2, 4],
            [2, 3, 4],
            [3, 0, 4],
            [0, 1, 2, 3]
        ]

        pyramid = Polyhedron(vertex_coords, faces_list)
        pyramid.color = YELLOW
        pyramid.fill_opacity = 0.7
        pyramid.move_to(np.array([1,-1,0])).rotate(32 * DEGREES,UP)
        cube2 = Cube(fill_opacity=0.7, side_length=1.0)
        cube2.move_to(np.array([1,-3,0]))
        cube2.color = PINK

        myCamera.move_to(cube1.get_center())
        myCamera.shift(LEFT*6)
        main_ax = ThreeDAxes()

        self.add_fixed_in_frame_mobjects(title, subtitle)
        self.remove(subtitle)
        self.move_camera(phi=60 * DEGREES, frame_center=cube1, added_anims=[FadeIn(cube1,main_ax, myCamera, pyramid, cube2), Write(subtitle)])
        arrowLen = 2
        cube_center = cube1.get_center()

        xAxes = Arrow3D(
            start=np.array(cube_center),
            end=np.array([(cube_center[0]+(arrowLen))*np.cos(30*DEGREES), cube_center[1]*np.sin(30*DEGREES), cube_center[2]]),
            color=BLUE
        )
        yAxes = Arrow3D(
            start=np.array(cube_center),
            end=np.array([cube_center[0]*np.cos(90*DEGREES), (cube_center[1]-(arrowLen))*np.sin(90*DEGREES), cube_center[2]]),
            color=RED
        )
        zAxes = Arrow3D(
            start=np.array(cube_center),
            end=np.array([cube_center[0], cube_center[1], cube_center[2]+arrowLen]),
            color=GREEN
        )

        self.play(GrowFromPoint(xAxes, cube_center), GrowFromPoint(yAxes, cube_center), GrowFromPoint(zAxes, cube_center))
        self.next_slide()
        self.play(FadeOut(xAxes, yAxes, zAxes))
        subtitle2 = Text("World space")
        subtitle2.next_to(title, DOWN)
        subtitle2.align_to(title, LEFT)

        self.add_fixed_in_frame_mobjects(subtitle2)
        self.remove(subtitle2)
        self.move_camera(frame_center=main_ax, added_anims=[ReplacementTransform(subtitle, subtitle2)])
        cube_center = main_ax.get_center()
        xAxes = Arrow3D(
            start=np.array(cube_center),
            end=np.array([cube_center[0]+arrowLen, cube_center[1], cube_center[2]]),
            color=BLUE
        )
        yAxes = Arrow3D(
            start=np.array(cube_center),
            end=np.array([cube_center[0], cube_center[1]-arrowLen, cube_center[2]]),
            color=RED
        )
        zAxes = Arrow3D(
            start=np.array(cube_center),
            end=np.array([cube_center[0], cube_center[1], cube_center[2]+arrowLen]),
            color=GREEN
        )
        self.play(GrowFromPoint(xAxes, cube_center), GrowFromPoint(yAxes, cube_center), GrowFromPoint(zAxes, cube_center))
        self.next_slide()
        self.play(FadeOut(xAxes, yAxes, zAxes))
        subtitle = Text("View space")
        subtitle.next_to(title, DOWN)
        subtitle.align_to(title, LEFT)

        self.add_fixed_in_frame_mobjects(subtitle)
        self.remove(subtitle)
        self.move_camera(phi=PI/2, theta=-PI,frame_center=cube1, added_anims=[FadeOut(plane, main_ax, myCamera), ReplacementTransform(subtitle2, subtitle)])
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
