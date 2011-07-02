#!/usr/bin/env python
# -*- coding: latin-1 -*-
import sys
import glob
import random

# has dependencies on reportlab, and pil (which should be installed with virtual env and bootstrap.py)
# api docs here: http://www.reportlab.com/apis/reportlab/2.4/pdfgen.html#
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors

class DesignShirtsFromCalifornia:
  CHICAGO_HEADLINE=["ThoughtWorks Chicago", "Bringing it since 1992", "CHICAGO", "Rainey's People"]
  ADJECTIVES=["Awesomist", "Best looking", "Happiest", "Legendary", "Transparent", "Shiny", "Dangerous", "Fastest"]
  NOUNS=["Chicagoans", "Agilistas", "Wonderlic Masters", "Bears Fans"]

  ATTRIBUTION="Designed by ThoughtWorks in California"
  GIT_REF="Fork me on Github https://github.com/jawspeak/tw-california-tshirt-generator"

  def __init__(self, output_filename):
    self.pdf = Canvas(output_filename, pagesize = LETTER)
#    self.headlines =

  def draw(self):
    for image in glob.glob('awesomeness/*.[jpg|png|gif]*'):
      self._draw_page(image)
    self.pdf.save()

  def _draw_page(self, image):
    self.pdf.setFillColor(colors.black)
    # To have a higher resolution for printing export the image as a higter resolution image which is then reduced
    self.pdf.drawImage(image, 2.25 * inch, 3.7 * inch, width=300, height=300, preserveAspectRatio=True)

    height = 8
#    print self.pdf.getAvailableFonts()
    self.pdf.setFont("Times-Bold", 28)
    random.shuffle(self.CHICAGO_HEADLINE, random.random)
    self.pdf.drawCentredString(4.25* inch, height*inch, self.CHICAGO_HEADLINE[0].encode('latin-1'))

    self.pdf.setFont("Times-Italic", 16)
    if len(image.split('=')) == 2:
      self.pdf.drawCentredString(4.25* inch, (height - 4.5)* inch, image.split('=')[1].split('.')[0].encode('latin-1'))
    else:
      random.shuffle(self.ADJECTIVES, random.random)
      random.shuffle(self.NOUNS, random.random)
      flattering_tagline = "Home of the %s %s!" % (', '.join(self.ADJECTIVES[:2]), self.NOUNS[0])
      self.pdf.drawCentredString(4.25* inch, (height - 4.5)* inch, flattering_tagline.encode('latin-1'))

    self.pdf.setFont("Times-Italic", 10)
    self.pdf.drawCentredString(4.25 * inch, (height - 4.8) * inch, self.ATTRIBUTION)
    self.pdf.drawCentredString(4.25 * inch, (height - 4.95) * inch, self.GIT_REF)

    self.pdf.showPage()

def main():
  printer = DesignShirtsFromCalifornia("tshirt-sumbissions-made-in-california.pdf")
  printer.draw()

if __name__ == '__main__':
  main()
