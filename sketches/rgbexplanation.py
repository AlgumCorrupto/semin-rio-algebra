from manim import *

class Scn(Scene):
    def construct(self):
        # title
        title = Text("Representação de cores\nem computadores")
        title.to_edge(UP)
        self.add(title)
        # grayscale
        grayscaleGradient   =  Rectangle(stroke_width=0, fill_color=[WHITE, BLACK], fill_opacity=1.0, 
        width=4.0, height=0.3)
        sampleGrayscale      = Rectangle(stroke_width=0, fill_color=ManimColor.from_rgb((0.5, 0.5, 0.5)), fill_opacity=1.0, width=2.0, height=2.0)
        sampleGrayscale.next_to(title, DOWN)
        grayscaleGradient.next_to(sampleGrayscale, DOWN)
        grayscaleHead = Arrow(start=DOWN, end=UP)
        grayscaleHead.next_to(grayscaleGradient, DOWN)
        grayscaleDec = DecimalNumber(0.5, num_decimal_places=1)
        grayscaleDec.next_to(sampleGrayscale, RIGHT)

        sampleGrayscale.add_updater(lambda n: n.set_fill(  color=ManimColor.from_rgb((  (grayscaleHead.get_center()[0] - grayscaleGradient.get_left()[0]) / grayscaleGradient.width,
                                                                                        (grayscaleHead.get_center()[0] - grayscaleGradient.get_left()[0]) / grayscaleGradient.width,
                                                                                        (grayscaleHead.get_center()[0] - grayscaleGradient.get_left()[0]) / grayscaleGradient.width) )))

        grayscaleDec.add_updater(lambda n: n.set_value(sampleGrayscale.fill_color.to_rgb()[0]))

        self.add(grayscaleGradient, sampleGrayscale, grayscaleHead, grayscaleDec)
        self.wait(3)
        self.play(grayscaleHead.animate.set_x(grayscaleGradient.get_right()[0]))
        self.wait()
        self.play(grayscaleHead.animate.set_x(grayscaleGradient.get_center()[0]))
        self.wait()
        self.play(grayscaleHead.animate.set_x(grayscaleGradient.get_left()[0]))
        self.wait()
        self.play(grayscaleHead.animate.set_x(grayscaleGradient.get_right()[0]))
        self.wait(3)
        self.play(FadeOut(grayscaleHead, grayscaleGradient, sampleGrayscale, grayscaleDec))

        # rgb
        rgbText = MarkupText(f'(<span fgcolor="RED">r</span>, <span fgcolor="GREEN">g</span>, <span fgcolor="BLUE">b</span>, a)')
        rgbText.next_to(title, DOWN)


        sampleRect = Rectangle(stroke_width=0, width=2.0, height=2.0, color=WHITE, fill_opacity=1.0)
        sampleRect.center()

        rText = MarkupText(f'<span fgcolor="RED">r</span>:')
        #rText.to_edge(LEFT)
        rValue = DecimalNumber(
            1,
            num_decimal_places=1,
            unit_buff_per_font_unit=0.003
        )
        rValue.next_to(rText, RIGHT)

        gText =  MarkupText(f'<span fgcolor="GREEN">g</span>:')
        gText.next_to(rText, DOWN)
        gValue = DecimalNumber(
            1,
            num_decimal_places=1
        )
        gValue.next_to(gText, RIGHT)

        bText =  MarkupText(f'<span fgcolor="BLUE">b</span>:')
        bText.next_to(gText, DOWN)
        bValue = DecimalNumber(
            1,
            num_decimal_places=1
        )
        bValue.next_to(bText, RIGHT)

        aText =  MarkupText(f'a:')
        aText.next_to(bText, DOWN)
        aValue = DecimalNumber(
            1,
            num_decimal_places=1
        )
        aValue.next_to(aText, RIGHT)

        rgbGroup = VGroup(rText, rValue, 
                          gText, gValue, 
                          bText, bValue,
                          aText, aValue)
        
        rgbGroup.to_edge(LEFT)

        easter_egg = Text("Olá Mundo", font_size="24", fill_opacity=0.0)
        easter_egg.move_to(sampleRect.get_center())
        easter_egg.set_z(0.0)

        self.play(FadeIn(rgbText))
        self.wait()
        self.play(ReplacementTransform(rgbText, rgbGroup), FadeIn(easter_egg), FadeIn(sampleRect))
        self.wait()

        rValue.add_updater(lambda d: d.set_value(sampleRect.fill_color.to_rgb()[0]))
        #rValue.add_updater(lambda d: d.set_value(sampleRect.get_center()[1]))
        gValue.add_updater(lambda d: d.set_value(sampleRect.fill_color.to_rgb()[1]))
        bValue.add_updater(lambda d: d.set_value(sampleRect.fill_color.to_rgb()[2]))
        aValue.add_updater(lambda d: d.set_value(sampleRect.get_fill_opacity()))

        self.play(sampleRect.animate.set_fill(color=ManimColor.from_rgb((1.0, 0.0, 0.0)), opacity=1.0))
        self.wait()
        self.play(sampleRect.animate.set_fill(color=ManimColor.from_rgb((0.0, 1.0, 0.0)), opacity=1.0), easter_egg.animate.set_fill(WHITE, opacity=1.0))
        self.wait()
        self.play(sampleRect.animate.set_fill(color=ManimColor.from_rgb((0.0, 0.0, 1.0)), opacity=1.0))
        sampleRect.set_z(5.0)
        self.wait()
        self.play(sampleRect.animate.set_fill(color=ManimColor.from_rgba((0.0, 0.0, 1.0, 0.5)), opacity=0.3))
        self.wait()
        self.play(sampleRect.animate.set_fill(color=ManimColor.from_rgba((1.0, 1.0, 0.0, 1.0)), opacity=1.0))
        self.wait()
