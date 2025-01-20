from manim import *

def helloShader(point):
    x, y = point
    return (x, y, 0.0, 0.0)

xMax = 4
yMax  = 4
fragWidth = 0.5
fragHeight = 0.5

class Scn(Scene):
    def construct(self):
        # Shaders have a generator function that maps every value of a matrix ---------------------------
        genFunText = Text("Lei geradora do Shader:")
        genFunText.move_to(UP)
        genFunMath = MathTex(r"A[i][j] = \left( \frac{i}{m}, \frac{j}{n}, 0.0 \right)")
        genFunMath.next_to(genFunText, DOWN)
        genFunGroup = VGroup(genFunText, genFunMath)
        genFunGroup.move_to(UP).scale(0.9)
        genFunGroup.shift(UP)
        self.add(genFunGroup)
        matrixValues = []

        for y in range(yMax):
            cols = []
            for x in range(xMax):
                red, green, blue, a = helloShader(((x+1)/xMax, ((yMax - y))/yMax))
                cols.append(r'({}, {}, {})'.format(red, green, blue))
            matrixValues.append(cols)

        unresolvedVals = []
        for y in range(yMax):
            cols = []
            for x in range(xMax):
                red, green, blue, a = helloShader(((x+1)/xMax, ((yMax - y))/yMax))
                cols.append(r'\left( \frac{' + str(x+1) + r'}{' + str(xMax) + r'}, \frac{' + str((yMax) - y) + r'}{' + str(yMax) + r'}, 0.0 \right)')
            unresolvedVals.append(cols)

        oldMatrixVals = [[r"\left( \frac{i}{m}, \frac{j}{n}, 0.0, 1.0 \right)" for _ in range(yMax)] for _ in range(xMax)]
        
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
        self.play(ReplacementTransform(oldMatrix, unresolvedMatrix))
        self.wait()
        self.play(ReplacementTransform(unresolvedMatrix, theMatrix))
        self.wait()

        print(matrixEntries[0])
        self.play(FadeIn(shaderContainer))
        # loop each member of array creating a new array containing colors
        for y in range(yMax):
            for x in range(xMax):
                # step sim
                colors[x][y] = ManimColor.from_rgb(helloShader((float(x+1)/xMax, float(y+1)/yMax)))
                fragTo = Rectangle(stroke_width = 1, width=fragWidth, height=fragHeight, color=colors[x][y], fill_opacity=1)
                corner = shaderContainer.get_corner(DL)
                fragTo.move_to([corner[0] + (fragWidth*0.5) + (x*fragWidth), corner[1] + (fragHeight*0.5) + (y*fragHeight), corner[2]])
                fragFrom = Rectangle(stroke_width = 1, width=0.0, height=0.0, color=colors[x][y], fill_opacity=0.0)
                fragFrom.move_to(matrixEntries[x + ((yMax - 1) - y) * xMax].get_center())
                # animate it (using self play)
                self.add(fragFrom)
                self.play(TransformFromCopy(fragFrom, fragTo))
