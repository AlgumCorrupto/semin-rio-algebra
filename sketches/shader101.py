from manim import *

class Scn(Scene):
    def construct(self):
        title = Text("Computação Gráfica 101")
        title.to_edge(UL)

        self.play(Write(title))

        points = BulletedList(
            "Pixel é algo atômico.", 
            "Viewport é uma matriz de pixels.",
            "Shader é um termo genérico para programas que rodam na GPU.",
            "Vamos falar especificamente sobre Fragment Shaders."
        )
        
        for point in points:
            self.play(Write(point))
            self.wait()

        self.wait()
        self.play(FadeOut(points))

        title2 = Text("X equivale a X")
        title2.to_edge(UL)
        self.play(ReplacementTransform(title, title2))
        points = BulletedList(
            "Pixel, membro da matriz.",
            "Viewport, matriz.",
            "Fragment shader, função geradora da matriz."
        )
         
        for point in points:
            self.play(Write(point))
            self.wait()
        self.wait()
        self.play(FadeOut(*self.mobjects))
