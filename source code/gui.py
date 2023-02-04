from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QLabel
from nucleotide_graphics import NucleotideGraphics
from amino_acid_graphics import AminoAcidGraphics
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import PyQt5
from codons import Codon
from reader import Reader

class GUI(QtWidgets.QMainWindow):
    #The class GUI draws the window with 2 different screens: one for the translation and the other for transcription
    #The GUI displayes an arbitrary number of nucleotides and amino acids on the screen at most at a time, 30 and 10 for example
    def __init__(self):
        super().__init__()
        self.setCentralWidget(QtWidgets.QWidget())  # QMainWindown must have a centralWidget to be able to add layouts
        self.layout = QtWidgets.QVBoxLayout()  # Vertical main layout(s)
        self.centralWidget().setLayout(self.layout) #set the main layout as the central widget
        self.vbox = QVBoxLayout()
        self.top_widget=QtWidgets.QWidget()
        self.DNA_top_layout = QtWidgets.QHBoxLayout()
        self.top_widget.setLayout(self.DNA_top_layout)
        self.RNA_bot_layout = QtWidgets.QHBoxLayout()
        self.init_window()
        self.add_text()
        self.file_name=None
        self.file_prompt() #calls the file prompt function at the init
        self.init_buttons()

    def init_window(self): #sets up the main window

        self.setGeometry(300, 300, 800, 800)

        self.show()
        # Add scenes for drawing 2d objects
        self.scene_top = QtWidgets.QGraphicsScene()
        self.scene_bot = QtWidgets.QGraphicsScene()

        #adds views for the 2 scenes in the main window
        self.view_top = QtWidgets.QGraphicsView(self.scene_top, self)
        self.view_top.setAlignment(QtCore.Qt.AlignTop)
        self.view_bot = QtWidgets.QGraphicsView(self.scene_bot, self)
        self.view_top.setAlignment(QtCore.Qt.AlignBottom)

        self.view_top.show()
        #self.view_bot.adjustSize()
        self.view_bot.show()
        self.layout.addWidget(self.view_top)
        self.layout.addWidget(self.view_bot)

    def init_buttons(self): #creates buttons that allow the RNA chain to be graphically changed when pressed

        reader = Reader(self.file_name)

        #Button that displays RNA-chain after TATA-boxes
        self.tata_button = PyQt5.QtWidgets.QPushButton("TATA")
        self.tata_button.clicked.connect(lambda: self.update_nucleotide_graphics_items(reader.rna_list_after_tata)) #normally button.clicked.connect would require a reference to a function, but not a function call.
        self.layout.addWidget(self.tata_button)
                                                                                                                    #Lambda allows for a function call
        # Button that displays RNA-chain after TATA-boxes and after first TAC-start codon is reached
        self.tac_button = PyQt5.QtWidgets.QPushButton("TAC")
        self.tac_button.clicked.connect(lambda: self.update_nucleotide_graphics_items(reader.rna_list_after_tac))
        self.layout.addWidget(self.tac_button)

        # Button that displays RNA-chain after TATA-boxes and after first TAC-start codon is reached and after exons have been removed
        self.intronexon_button = PyQt5.QtWidgets.QPushButton("Introns-Exons")
        self.intronexon_button.clicked.connect(lambda: self.update_nucleotide_graphics_items(reader.rna_list_after_splicing))
        self.layout.addWidget(self.intronexon_button)


    def add_text(self): #adds various texts to the different views and the windowtitle


        self.setWindowTitle('Protein Biosynthesis program')
        # text

        self.DNA = QLabel("DNA")
        self.DNA.move(30, 90)
        self.DNA.setFont(QFont("Arial", 20))
        self.RNA = QLabel("RNA")
        self.RNA.setFont(QFont("Arial", 20))
        self.RNA.move(30, 200)
        self.Transcription = QLabel("Transcription")
        self.Transcription.setFont(QFont("Arial", 20))
        self.Transcription.move(400, 250)
        self.Translation = QLabel("Translation")
        self.Translation.setFont(QFont("Arial", 20))
        self.Translation.move(400, 200)
        self.scene_top.addWidget(self.DNA)
        self.scene_bot.addWidget(self.RNA)
        self.scene_top.addWidget(self.Transcription)
        self.scene_bot.addWidget(self.Translation)

    def file_prompt(self):#graphically asks the user the name of the file in the directory that has the sequence

        self.file_name, valid=QInputDialog.getText(self, 'Prompt', 'Input the filename (e.g. 1.txt,2.txt etc):')
        if valid:
            return self.file_name

    def add_nucleotide_graphics_items(self,nucleotide_list,bot_or_top): #make every graphics object from the list and add them in a horizontal line to either the bottom or top scene
        i=0
        o=0
        x=0
        y=-3
        nth=0
        sf=100 #sizefactor
        self.rna_graphics_item_group_top = QGraphicsItemGroup()  # grouping graphics items to make an RNA/DNA chain of sorts
        self.rna_graphics_item_group_bot = QGraphicsItemGroup()
        self.dna_graphics_item_group_top = QGraphicsItemGroup()
        if "U" in nucleotide_list: #Only lets RNA lists through, not DNA lists

                for nucleotide in nucleotide_list: #Adds the RNA graphics items
                    if bot_or_top == "bot":

                        NucleoTideGraphicsItem = NucleotideGraphics(nucleotide,sf,nucleotide_list[i])
                        NucleoTideGraphicsItem.setPos(x*sf,y*sf)
                        numbering_label=QGraphicsTextItem(str(nth))
                        numbering_label.setPos(x * sf, (y-0.5)* sf)
                        self.rna_graphics_item_group_bot.addToGroup(NucleoTideGraphicsItem)
                        self.rna_graphics_item_group_bot.addToGroup(numbering_label)            #bottom view

                    elif bot_or_top=="top":

                        NucleoTideGraphicsItem2 = NucleotideGraphics(nucleotide, sf, nucleotide_list[i])
                        NucleoTideGraphicsItem2.setPos((x+1) * sf, 0)
                        NucleoTideGraphicsItem2.setRotation(180)
                        self.rna_graphics_item_group_top.addToGroup(NucleoTideGraphicsItem2)     #top view

                    nth+=1
                    x+=1
        else:
            for nucleotide in nucleotide_list: #Adds the DNA graphics items
                NucleoTideGraphicsItem = NucleotideGraphics(nucleotide,sf,nucleotide_list[o])
                NucleoTideGraphicsItem.setPos((x)*sf,-2.5*sf)

                numbering_label = QGraphicsTextItem(str(nth))
                numbering_label.setPos(x * sf, -3 * sf)
                self.dna_graphics_item_group_top.addToGroup(NucleoTideGraphicsItem)
                self.rna_graphics_item_group_top.addToGroup(numbering_label)
                nth+=1
                x+=1
        self.scene_bot.addItem(self.rna_graphics_item_group_bot)
        self.scene_top.addItem(self.rna_graphics_item_group_top)
        self.scene_top.addItem(self.dna_graphics_item_group_top)

    def update_nucleotide_graphics_items(self,rna_list):
        self.scene_top.removeItem(self.rna_graphics_item_group_top) #removes the item group containing the RNA graphics objects that are there
        self.add_nucleotide_graphics_items(rna_list,"top") #adds the new RNA graphics objects

    def add_amino_acid_graphics_items(self, codon_list):
        x=0
        sf = 300  # sizefactor
        y=-0.33
        self.aa_graphics_item_group_bot = QGraphicsItemGroup()
        for triplet in codon_list:
                codon=Codon(triplet[0],triplet[1],triplet[2])
                AminoAcidGraphicsItem=AminoAcidGraphics(codon,sf)#creates a codon object then creates an aminoacidgraphics object from that
                AminoAcidGraphicsItem.setPos(x * sf, y*sf)
                AminoAcidGraphicsItem.setRotation(0)
                self.aa_graphics_item_group_bot.addToGroup(AminoAcidGraphicsItem)
                x += 1

        self.scene_bot.addItem(self.aa_graphics_item_group_bot)

