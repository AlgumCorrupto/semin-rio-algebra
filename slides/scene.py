from manim import *  # or: from manimlib import *
from manim_slides import Slide
from numpy import matrix


def helloShader(point):
    x, y = point
    return (x, y, 0.0, 0.0)

xMax = 4
yMax  = 4
fragWidth = 0.5
fragHeight = 0.5

class Scn(Slide):
    def construct(self):
        # PRÓLOGO ######################
        title = Text("Computação Gráfica ♥ Álgebra Linear", weight=BOLD)
        subtitle = Text("Criado por Paulo Artur")
        subtitle.next_to(title, DOWN)
        tGroup = VGroup(title, subtitle)
        tGroup.move_to(ORIGIN)
        self.play(Write(title))
        self.wait()
        self.play(Write(subtitle))
        self.wait(2)
        self.next_slide()

        self.play(FadeOut(tGroup))

        title = Text("Conteúdo explorado:")
        title.to_edge(UL)

        self.play(Write(title))
        self.next_slide()

        indice = BulletedList(
            "Representação das cores \\\\ em computadores.",
            "Computação gráfica 101.",
            "O que é um shader?",
            "Exemplos de shaders."
        )

        for x in indice: 
            self.play(Write(x))
            self.wait()
            self.next_slide()

        self.wait()
        self.play(FadeOut(*self.mobjects))
        self.next_slide()
        # REPRESENTAÇÃO DAS CORES ###################################################################
        # title
        title = Text("Representação de cores\nem computadores")
        title.to_edge(UP)
        self.play(Write(title))
        self.next_slide()
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
        self.next_slide()
        self.play(FadeIn(grayscaleGradient, sampleGrayscale, grayscaleHead, grayscaleDec))

        self.next_slide(loop=True)
        self.wait(2)
        self.play(grayscaleHead.animate.set_x(grayscaleGradient.get_right()[0]))
        self.wait()
        self.play(grayscaleHead.animate.set_x(grayscaleGradient.get_center()[0]))
        self.wait()
        self.play(grayscaleHead.animate.set_x(grayscaleGradient.get_left()[0]))
        self.wait()
        self.play(grayscaleHead.animate.set_x(grayscaleGradient.get_right()[0]))
        self.wait()
        self.play(grayscaleHead.animate.set_x(grayscaleGradient.get_center()[0]))

        self.next_slide()
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
        self.next_slide()
        rValue.add_updater(lambda d: d.set_value(sampleRect.fill_color.to_rgb()[0]))
        #rValue.add_updater(lambda d: d.set_value(sampleRect.get_center()[1]))
        gValue.add_updater(lambda d: d.set_value(sampleRect.fill_color.to_rgb()[1]))
        bValue.add_updater(lambda d: d.set_value(sampleRect.fill_color.to_rgb()[2]))
        aValue.add_updater(lambda d: d.set_value(sampleRect.get_fill_opacity()))
        
        self.next_slide(loop=True)
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
        self.play(sampleRect.animate.set_fill(color=WHITE, opacity=1.0))
        self.wait()
        self.next_slide()
        self.remove(easter_egg)
        self.play(FadeOut(*self.mobjects))
        self.next_slide()
        
        # SHADERS 101
        title = Text("Computação Gráfica 101")
        title.to_edge(UL)


        self.play(Write(title))
        self.next_slide()

        points = BulletedList(
            "Pixel é algo atômico.", 
            "Viewport é uma matriz de pixels.",
            f'Shader é um termo genérico,\\\\ para programas que rodam na GPU.',
            "Vamos falar especificamente sobre Fragment Shaders."
        )
        
        for point in points:
            self.play(Write(point))
            self.wait()
            self.next_slide()

        self.wait()
        self.play(FadeOut(points))
        self.next_slide()
        title2 = Text("X equivale a Y")
        title2.to_edge(UL)
        self.play(ReplacementTransform(title, title2))
        points = BulletedList(
            "Pixel, membro da matriz.",
            "Viewport, matriz.",
            "Fragment shader, função geradora da matriz."
        )
         
        self.next_slide()
        for point in points:
            self.play(Write(point))
            self.wait()
            self.next_slide()
        self.wait()
        self.play(FadeOut(*self.mobjects))
        
        self.next_slide()
        # ANIMAÇÃO EXEMPLO DE SHADERS ##############################################
        genFunText = Text("Lei geradora desse shader:")
        genFunText.move_to(UP)
        genFunMath = MathTex(r"A[i][j] = \left( \frac{i}{m}, \frac{j}{n}, 0.0 \right)")
        genFunMath.next_to(genFunText, DOWN)
        genFunGroup = VGroup(genFunText, genFunMath)
        genFunGroup.move_to(UP).scale(0.9)
        genFunGroup.shift(UP)
        self.play(Write(genFunGroup))
        self.next_slide()
        matrixValues = []

        for y in range(yMax):
            cols = []
            for x in range(xMax):
                red, green, blue, a = helloShader(((x+1)/xMax, (((yMax - 1) - y))/yMax))
                cols.append(r'({}, {}, {})'.format(red, green, blue))
            matrixValues.append(cols)
        matrixValues.reverse()

        unresolvedVals = []
        for y in range(yMax):
            cols = []
            for x in range(xMax):
                red, green, blue, a = helloShader(((x+1)/xMax, ((yMax - y))/yMax))
                cols.append(r'\left( \frac{' + str(x+1) + r'}{' + str(xMax) + r'}, \frac{' + str((yMax) - y) + r'}{' + str(yMax) + r'}, 0.0 \right)')
            unresolvedVals.append(cols)

        unresolvedVals.reverse()

        oldMatrixVals = [[r"\left( \frac{i}{m}, \frac{j}{n}, 0.0 \right)" for _ in range(yMax)] for _ in range(xMax)]
        
        oldMatrix = Matrix(oldMatrixVals, h_buff=4.6, v_buff=1.3,
                    element_to_mobject_config={}).scale(0.6)

        unresolvedMatrix = Matrix(unresolvedVals, h_buff=4.6, v_buff=1.3,
                    element_to_mobject_config={}).scale(0.6)

        theMatrix = Matrix(matrixValues, h_buff=3.3,
                    element_to_mobject_config={}).scale(0.6)
        theMatrix.next_to(genFunGroup, DOWN)

        matrixEntries = theMatrix.get_entries()

        # SHADER PART ------------------------------------------------------------------------------------
        # creating an array containing the colors
        colors = [[ManimColor.from_rgba((0.0, 0.0, 0.0, 0.0)) for _ in range(yMax)] for _ in range(xMax)]
        
        # construct the GUI
        shaderContainer = Rectangle(stroke_width = 1, stroke_color = WHITE,
        width=xMax * (fragWidth), height=yMax * (fragHeight))
        shaderContainer.next_to(theMatrix, RIGHT)
        msGrouping = VGroup(theMatrix, shaderContainer)
        msGrouping.next_to(genFunGroup, DOWN*4)

        oldMatrix.move_to(theMatrix.get_center())
        unresolvedMatrix.move_to(oldMatrix.get_center())

        self.play(FadeIn(oldMatrix))
        self.wait()
        self.next_slide()
        self.play(ReplacementTransform(oldMatrix, unresolvedMatrix))
        self.wait()
        self.next_slide()
        self.play(ReplacementTransform(unresolvedMatrix, theMatrix))
        self.wait()
        self.next_slide()

        print(matrixEntries[0])
        self.play(FadeIn(shaderContainer))
        # loop each member of array creating a new array containing colors
        for y in range(yMax):
            for x in range(xMax):
                # step sim
                colors[x][y] = ManimColor.from_rgb(helloShader((float((x+1)/xMax), float((yMax - y)/yMax))))
                fragTo = Rectangle(stroke_width = 1, width=fragWidth, height=fragHeight, color=colors[x][y], fill_opacity=1)
                corner = shaderContainer.get_corner(DL)
                fragTo.move_to([corner[0] + (fragWidth*0.5) + (x*fragWidth), corner[1] + (fragHeight*0.5) + (y*fragHeight), corner[2]])
                fragFrom = Rectangle(stroke_width = 1, width=0.0, height=0.0, color=colors[x][y], fill_opacity=0.0)
                fragFrom.move_to(matrixEntries[x + ((yMax - 1) - y) * xMax].get_center())
                # animate it (using self play)
                self.add(fragFrom)
                self.play(TransformFromCopy(fragFrom, fragTo))
