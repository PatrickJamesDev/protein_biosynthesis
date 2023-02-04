from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QColor, QPainter, QFont



class NucleotideGraphics(QtWidgets.QGraphicsPolygonItem):

    def __init__(self, nucleotide,sf,position ):
        super(NucleotideGraphics, self).__init__()
        self.nucleotide = nucleotide
        self.sf=sf
        self.constructPolygon(self.sf)
        self.color()
        self.add_label()
        self.position=position

    def constructPolygon(self,sf):

        polygon = QtGui.QPolygonF()
        "the nucleotides will graphically be like a lock and key." \
        "A and T/U will fit graphically and G and C"

        match self.nucleotide:  # python equivalent to switch
            case "A":
                polygon.append(QtCore.QPointF(0, 0))  # bottom left
                polygon.append(QtCore.QPointF(self.sf, 0))  # bottom right
                polygon.append(QtCore.QPointF(self.sf, self.sf))  # Top right
                polygon.append(QtCore.QPointF(self.sf / 2, 2 * self.sf))  # tip
                polygon.append(QtCore.QPointF(0, self.sf))  # top left

                # this should look like a house

            case "G":


                polygon.append(QtCore.QPointF(0, 0))  # bottom left
                polygon.append(QtCore.QPointF(self.sf, 0))  # bottom right
                polygon.append(QtCore.QPointF(self.sf, 2*self.sf))  #  right tip
                polygon.append(QtCore.QPointF(2*self.sf / 3, self.sf / 2))  # right middle
                polygon.append(QtCore.QPointF(self.sf/2, 2 * self.sf))  # tip
                polygon.append(QtCore.QPointF(self.sf / 3, self.sf / 2))  # left middle
                polygon.append(QtCore.QPointF(0, 2 * self.sf))  # tip
                polygon.append(QtCore.QPointF(0, 2*self.sf))  # left tip

            case "T":

                polygon.append(QtCore.QPointF(0, 0))  # bottom left
                polygon.append(QtCore.QPointF(self.sf, 0))  # bottom right
                polygon.append(QtCore.QPointF(self.sf, self.sf))  # Top right
                polygon.append(QtCore.QPointF(self.sf, 2 * self.sf))  # tip
                polygon.append(QtCore.QPointF(self.sf / 2, self.sf / 2))  # middle
                polygon.append(QtCore.QPointF(0, 2 * self.sf))  # tip
                polygon.append(QtCore.QPointF(0, self.sf))  # top left

            case "U":
                polygon.append(QtCore.QPointF(0, 0))  # bottom left
                polygon.append(QtCore.QPointF(self.sf, 0))  # bottom right
                polygon.append(QtCore.QPointF(self.sf, self.sf))  # Top right
                polygon.append(QtCore.QPointF(self.sf, 2 * self.sf))  # tip
                polygon.append(QtCore.QPointF(self.sf / 2, self.sf / 2))  # middle
                polygon.append(QtCore.QPointF(0, 2 * self.sf))  # tip
                polygon.append(QtCore.QPointF(0, self.sf))  # top lef

            case "C":
                polygon.append(QtCore.QPointF(0, 0))  # bottom left
                polygon.append(QtCore.QPointF(self.sf, 0))  # bottom right
                polygon.append(QtCore.QPointF(self.sf, self.sf))  # top right
                polygon.append(QtCore.QPointF(2*self.sf / 3, 2 * self.sf))  # right tip
                polygon.append(QtCore.QPointF(self.sf / 2, self.sf / 2))  # middle
                polygon.append(QtCore.QPointF(self.sf / 3, 2 * self.sf))  # left tip
                polygon.append(QtCore.QPointF(0,  self.sf))  # tip
            case " ": #for blank spots, after removing tata etc
                pass


        self.setPolygon(polygon)

    def add_label(self):

        match self.nucleotide:  # python equivalent to switch
            case "A":
                pass
                self.textItem = QtWidgets.QGraphicsSimpleTextItem('A', self)
                self.textItem.setFont(QFont("Arial", 20))
            case "T":
                self.textItem = QtWidgets.QGraphicsSimpleTextItem('T', self)
                self.textItem.setFont(QFont("Arial", 20))
            case "U":
                self.textItem = QtWidgets.QGraphicsSimpleTextItem('U', self)
                self.textItem.setFont(QFont("Arial", 20))
            case "G":
                self.textItem = QtWidgets.QGraphicsSimpleTextItem('G', self)
                self.textItem.setFont(QFont("Arial", 20))
            case "C":
                self.textItem = QtWidgets.QGraphicsSimpleTextItem('C', self)
                self.textItem.setFont(QFont("Arial", 20))

    def color(self):
        painter = QPainter()

        purple = (102, 0, 204)
        yellow = (255, 255, 0)
        pink = (255, 0, 127)
        blue = (0, 204, 204)
        orange = (255, 128, 0)
        match self.nucleotide:  # python equivalent to switch
            case "A":
                pass
                self.setBrush(QColor(*yellow))#* used to unpack tuples
            case "T":
                self.setBrush(QColor(*purple))
            case "U":
                self.setBrush(QColor(*pink))
            case "G":
                self.setBrush(QColor(*blue))
            case "C":
                self.setBrush(QColor(*orange))

        painter