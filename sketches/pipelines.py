from manim import *
from manim_slides import Slide

def edgeFunction(a, b, c):
    return (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])

def AABB(aPos, aSize, bPos, bSize):
    if  aPos[0] < bPos + bSize and aPos[0] + aSize > bPos and aPos[1] < bPos[1] + bSize[1] and aPos[1] + aSize[1] > bPos[1]:
        return True
    return False

def interpolate(x1: float, x2: float, y1: float, y2: float, x: float):
    """Perform linear interpolation for x between (x1,y1) and (x2,y2) """

    return ((y2 - y1) * x + x2 * y1 - x1 * y2) / (x2 - x1)


def is_point_inside_rectangle(px, py, rx, ry, rw, rh):
    """
    Check if a point (px, py) is inside an axis-aligned rectangle.
    
    Parameters:
        px, py - Point coordinates
        rx, ry - Top-left corner of the rectangle
        rw, rh - Width and height of the rectangle
    
    Returns:
        True if the point is inside the rectangle, False otherwise
    """
    return rx <= px <= rx + rw and ry <= py <= ry + rh

VP_SIZE = 5
class Pipe(Slide):
    def construct(self):
        title = Text("Pipeline gráfica")
        title.to_edge(UL)
        # Input assembler
        subtitle = Text("Input assembler", font_size=38)
        subtitle.next_to(title, DOWN)
        subtitle.align_to(title, LEFT)
        
        self.play(Write(title))
        desc = BulletedList("Parte do processo onde\\\\são interpretados \\\\os dados, de cada vértice \\\\para renderização.\\\\Isso inclui posição,\\\\cor, vetores normais entre outros.", font_size=48)
        desc.to_edge(LEFT)

        viewport = Rectangle(WHITE, 5, 5)
        viewport.to_edge(RIGHT)
        self.next_slide()
        self.play(Write(desc), Write(subtitle), Write(viewport))

        v1 = Dot(color=RED)
        v2 = Dot(color=GREEN)
        v2.next_to(v1)
        v3 = Dot(color=BLUE)
        v3.next_to(v2)
        vgroup = Group(v1, v2, v3)

        vgroup.move_to(viewport.get_center())
        self.play(FadeIn(vgroup))
        self.next_slide()

        # Vertex shader
        subtitle2 = Text("Vertex shader", font_size=38)
        subtitle2.next_to(title, DOWN)
        subtitle2.align_to(title, LEFT)
        desc2 = BulletedList("Aqui as vértices dadas\\\\como entrada são\\\\posicionadas na tela.", font_size=48)
        desc2.to_edge(LEFT)

        self.play(ReplacementTransform(subtitle, subtitle2), ReplacementTransform(desc, desc2))
        self.play(
            v1.animate().shift(UP * 2),
            v2.animate().shift(LEFT * 2),
            v3.animate().shift(DOWN * 2)
        )
        l1 = Line(v1.get_center(), v2.get_center())
        l2 = Line(v2.get_center(), v3.get_center())
        l3 = Line(v3.get_center(), v1.get_center())
        
        lGroup = VGroup(l1, l2, l3)
        self.play(Write(lGroup))
        self.next_slide()
        self.play(Unwrite(lGroup))

        # Raster
        subtitle = Text("Rasterização", font_size=38)
        subtitle.next_to(title, DOWN)
        subtitle.align_to(title, LEFT)
        
        desc = BulletedList("A rasterização é o processo\\\\que converte\\\\uma imagem vetorial\\\\em uma máscara", font_size=48)
        desc.to_edge(LEFT)
        self.play(ReplacementTransform(subtitle2, subtitle), ReplacementTransform(desc2, desc))
        viewport2 = Rectangle(WHITE, 5, 5, grid_xstep=5/VP_SIZE, grid_ystep=5/VP_SIZE)
        viewport2.move_to(viewport.get_center())
        self.play(Write(viewport2))
        self.remove(viewport)

        # which grid position is the vertex in:
        pixels = [[0 for i in range(VP_SIZE)] for i in range(VP_SIZE)]
        vertPos = [(0, 0) for i in range(3)]
        for j in range(VP_SIZE):
            for i in range(VP_SIZE):
                pixels[i][j] = Rectangle(WHITE, width=5/VP_SIZE, height=5/VP_SIZE)
                pixels[i][j].align_to(viewport2, UL)
                pixels[i][j].shift(DOWN * j)
                pixels[i][j].shift(RIGHT * i)
                self.add(pixels[i][j])
                curr = pixels[i][j]

                if is_point_inside_rectangle(v1.get_center()[0], v1.get_center()[1], curr.get_start()[0] - curr.width, curr.get_start()[1] - curr.height, curr.width, curr.height):
                    # red
                    vertPos[1] = (i, j)

                if is_point_inside_rectangle(v2.get_center()[0], v2.get_center()[1], curr.get_start()[0] - curr.width, curr.get_start()[1] - curr.height, curr.width, curr.height):
                    # green
                    vertPos[0] = (i, j)

                if is_point_inside_rectangle(v3.get_center()[0], v3.get_center()[1], curr.get_start()[0] -  curr.width, curr.get_start()[1] - curr.height, curr.width, curr.height):
                    # blue
                        vertPos[2] = (i, j)

        for y in range(VP_SIZE):
            for x in range(VP_SIZE):
                abp = edgeFunction(list(vertPos[0]), list(vertPos[1]), [x,y])
                bcp = edgeFunction(list(vertPos[1]), list(vertPos[2]), [x,y])
                cap = edgeFunction(list(vertPos[2]), list(vertPos[0]), [x,y])
                if (abp >= 0 and cap >= 0 and bcp >= 0):
                    self.play(pixels[x][y].animate.set_fill(WHITE, opacity=1))

        self.next_slide()

        subtitle2 = Text("Fragment shader", font_size=38)
        subtitle2.next_to(title, DOWN)
        subtitle2.align_to(title, LEFT)
        desc2 = BulletedList("O fragment shader, como o\\\\vertex shader é uma parte\\\\programável da pipeline.\\\\onde é definida a\\\\cor de cada pixel da\\\\imagem rasterizada.", font_size=48)
        desc2.to_edge(LEFT)
        self.play(ReplacementTransform(subtitle, subtitle2), ReplacementTransform(desc, desc2))
        for y in range(VP_SIZE):
            for x in range(VP_SIZE):
                abp = edgeFunction(list(vertPos[0]), list(vertPos[1]), [x,y])
                bcp = edgeFunction(list(vertPos[1]), list(vertPos[2]), [x,y])
                cap = edgeFunction(list(vertPos[2]), list(vertPos[0]), [x,y])
                if (abp >= 0 and cap >= 0 and bcp >= 0):
                    color = BLACK
                    normX = (x / VP_SIZE)
                    normY = (x / VP_SIZE)
                    vRx = vertPos[1][0] / VP_SIZE
                    vRy = vertPos[1][1] / VP_SIZE
                    vGx = vertPos[2][0] / VP_SIZE
                    vGy = vertPos[2][1] / VP_SIZE
                    vBx = vertPos[0][0] / VP_SIZE
                    vBy = vertPos[0][1] / VP_SIZE

                    color = color.interpolate(RED, (((normX - vRy) ** 2) + (normY - vRy) ** 2) ** 0.5)
                    color = color.interpolate(GREEN, (((normX - vGx) ** 2) + (normY - vGy) ** 2) ** 0.5)
                    color = color.interpolate(BLUE, (((normX - vBx) ** 2) + (normY - vBx) ** 2) ** 0.5)
                    color.interpolate(RED, 1)
                    self.play(pixels[x][y].animate.set_fill(color, opacity=1))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()


