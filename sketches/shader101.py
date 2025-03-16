from manim import *
from manim_slides import Slide

class One(Slide):
    def construct(self):
        title = Text("Computação Gráfica 101")
        title.to_edge(UL)

        self.play(Write(title))
        self.next_slide()

        points = BulletedList(
            "Pixel é algo atômico.", 
            "Viewport é uma matriz de pixels.",
            f"Shader é um termo genérico,\\\\ para programas que rodam na GPU.",
            "Vamos falar especificamente sobre Fragment Shaders."
        )
        
        self.play(Write(points))

        self.next_slide()

        self.wait()
        self.play(FadeOut(points))

        title2 = Text("X equivale a Y")
        title2.to_edge(UL)
        self.play(ReplacementTransform(title, title2))
        points = BulletedList(
            "Pixel -- membro da matriz.",
            "Viewport -- matriz.",
            "Fragment shader -- função geradora da matriz."
        )
         
        self.play(Write(points))
        self.next_slide()
        self.wait()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()
