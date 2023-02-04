import sys
from gui import *

def main():
    # Start the Qt event loop. (i.e. make it possible to interact with the gui)
    global app  # Use global to prevent crashing on exit
    app = QApplication(sys.argv)
    gui = GUI() #initializing the GUI


    DNA_file=gui.file_name  #gets the filename from the GUI prompt

    reader=Reader(DNA_file) #intializing the Reader class with the given file

    dna_list = reader.dna_list
    rna_list_after_introns_removed=reader.rna_list_after_splicing
    rna_list_joined=reader.rna_translation_list  #used for translation view
    codon_list=reader.codon_list


    #Top view aka transcription
    gui.add_nucleotide_graphics_items(dna_list, "top")                      #adds the unedited DNA sequence built from the chain in the file
    gui.add_nucleotide_graphics_items(rna_list_after_introns_removed,"top") #adds the edited RNA sequence, after TATA boxes located, TAC start codons located, and introns removed

    # Bot view aka translation
    gui.add_nucleotide_graphics_items(rna_list_joined, "bot")               #adds the same RNA sequence as above, but here the list is fully joined with no empty spaces
    gui.add_amino_acid_graphics_items(codon_list)                           #adds the list of codons based on the RNA sequence


    sys.exit(app.exec_())


if __name__ == "__main__":
    main()