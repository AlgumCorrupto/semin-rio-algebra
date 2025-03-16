from manim import *
from manim_slides import Slide

class Prol(Slide):
    def construct(self):
        title = Text("Computação Gráfica ♥ Álgebra Linear", weight=BOLD)
        subtitle = Text("Criado por Apolo Arêas, Paulo Artur")
        subtitle.next_to(title, DOWN)
        tGroup = VGroup(title, subtitle)
        tGroup.move_to(ORIGIN)
        self.play(Write(title))
        self.wait()
        self.play(Write(subtitle))
        self.next_slide()

        self.play(FadeOut(tGroup))

        title = Text("Conteúdo explorado:")
        title.to_edge(UL)

        self.play(Write(title))

        indice = BulletedList(
            "Representação das cores \\\\ em computadores.",
            "Espaços de coordenadas.",
            "Pipelines gráficas.",

        )
        indice2 = BulletedList(
            "Computação gráfica 101.",
            "O que é um shader?",
            "Exemplos de shaders."
        )

        self.play(Write(indice))
        self.next_slide()
        self.play(ReplacementTransform(indice, indice2))
        self.next_slide()

        self.play(FadeOut(*self.mobjects))
