# Y2_2022_05325_Protein_Biosynthesis

##Final version

## File and directory structure
    
    source code directory: All program files and .txt files
    .txt files must be in the source code folder for the program to be able to use them
    documentation directory: The program plan and document are found here 



## Current properties 



    Ability to:
    Ask for a text file name in the path with a prompt
    Read a .txt file with only the letters A,T,G,C in uppercase or lowercase, and "\n"
    Create nucleotide lists from the info in the file
    Create amino acid lists from given nucleotides in the file
    Create appropriate graphics for RNA,DNA and Amino acids 
    Generate text labels for objects and views
    Generate A window with 2 separate views for the transcription and translation
    Scroll the views horizontally
    Button to view RNA modifications step by step, including TATA, tac, and exon and intron modifications
    Unittests for parts of the program, specifically the Reader methods
    Possibility for error in DNA->RNA transcription (1/10000, but this value can easily be changed)
    Splicing: Finding and separating introns from exons
    

    

## Instructions

    The program runs by running the main file. A text prompt and GUI window should open up, write the name of the DNA-sequence .txt that is found in the source code path to display it graphically. 
    For example, write "1.txt","2.txt","500k.txt" etc. and hit enter. 
    Not all graphics can be viewed on a single screen all at once, so use the scroll bar under the views to see more. 

## Prerequisites

    At least Python 3.10 (match-case was only added in this version), PyQT5


## Other

    The idea for the 3D graphics for the Amino acids was scrapped, instead the program has buttons instead to modify the RNA chain. 



