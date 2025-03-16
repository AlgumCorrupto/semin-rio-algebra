from manim import *
from manim_slides import Slide

class Conc(Slide):
    def construct(self):
        title = Text("Conclusão")

        title.to_edge(UL)

        conclusao = Tex("Muitos dos conceitos\\\\que são utilizadas na\\\\Computação Gráfica, vieram\\\\diretamente de conceitos abordados\\\\pela Álgebra Linear.")
        self.play(Write(title), Write(conclusao))
        self.next_slide()

        title2 = Text("Bibliografia")
        title2.to_edge(UL)
        self.play(ReplacementTransform(title, title2), FadeOut(conclusao))

        bib1 = BulletedList(
            "https://learnopengl.com/",
            "https://thebookofshaders.com/",
            "Computação Gráfica: Teoria\\\\e Prática:Geração de Imagens",
            "https://iquilezles.org/"
        )
        self.play(Write(bib1))
        self.next_slide()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()
