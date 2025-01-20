from manim import *

class Scn(Scene):
    def construct(self):
        title = Text("Computação Gráfica ♥ Álgebra Linear", weight=BOLD)
        subtitle = Text("Criado por Paulo Artur")
        subtitle.next_to(title, DOWN)
        tGroup = VGroup(title, subtitle)
        tGroup.move_to(ORIGIN)
        self.play(Write(title))
        self.wait()
        self.play(Write(subtitle))
        self.wait(2)

        self.play(FadeOut(tGroup))

        title = Text("Conteúdo explorado:")
        title.to_edge(UL)

        self.play(Write(title))

        indice = BulletedList(
            "Representação das cores \\\\ em computadores.",
            "Computação gráfica 101.",
            "O que é um shader?",
            "Exemplos de shaders."
        )

        for x in indice: 
            self.play(Write(x))
            self.wait()

        self.wait()
        self.play(FadeOut(indice))
