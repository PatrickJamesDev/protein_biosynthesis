from codons import Codon
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import *
from PyQt5.QtGui import QColor, QPainter



class AminoAcidGraphics(QtWidgets.QGraphicsPolygonItem):
    "create object with shape and color according to the codon specifies."
    "Amino acids will be drawn as 2D squares with text on them that says what AA (amino acid) they are."
    def __init__(self,codon,sf):
        super(AminoAcidGraphics, self).__init__()
        self.codon=codon
        self.amino_acid=self.codon.get_type() #The codon triplet determines what amino acid it codes for
        self.sf = sf #size factor
        self.color_dictionary={}
        brush = QtGui.QBrush(1)  # 1 for even fill
        self.setBrush(brush)
        self.add_label()
        self.constructPolygon(self.sf)
        self.color()


    def constructPolygon(self, sf): #having the squares drawn using the QGraphicsPolygonItem class allows me to reuse much code from the nucleotide graphics class
        polygon = QtGui.QPolygonF()
        polygon.append(QtCore.QPointF(0, 0))  # bottom left
        polygon.append(QtCore.QPointF(self.sf, 0))  # bottom right
        polygon.append(QtCore.QPointF(self.sf, self.sf))  # Top right
        polygon.append(QtCore.QPointF(0, self.sf))  # top left

        self.setPolygon(polygon)


    def add_label(self): #writes a label on each square that tells what aa it is (i.e. Leucine)
        painter = QPainter()
        self.amino_acid_label = QtWidgets.QGraphicsSimpleTextItem(self.amino_acid, self)
        self.amino_acid_label.setFont(QFont("Arial", 20))
        self.amino_acid_label.setBrush(QColor(255,255,255))#changes the color of the text on the label to white
        painter


    def color(self):
        painter = QPainter()
        i=0
        cfx=12
        cfy=8
        cfz=4


        for codon_dictionary in Codon.codon_dictionaries_list:
            for name, triplets in codon_dictionary.items():

                color_tuple=tuple([i*cfx,i*cfy,i*cfz])
                self.color_dictionary.update({name:color_tuple})
                i+=1

        color_tuple=self.color_dictionary.get((self.amino_acid)) #calling a color value from the dictionary with the given amino acid type
        self.setBrush(QColor(*color_tuple))  #* "unpacks" a tuple
        painter














