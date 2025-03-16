#!/bin/bash

set -e

manim -qh prologue.py Prol
manim -qh rgbexplanation.py Rgb
manim -qh coordspaces.py Coord
manim -qh pipelines.py Pipe
manim -qh shader101.py One
manim -qh mockshader.py Mock
manim -qh conclusao.py Conc

manim-slides Prol Rgb Coord Pipe One Mock Conc
