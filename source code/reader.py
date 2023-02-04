from codons import Codon
import random
class Reader:

    def __init__(self,file):
        self.file=file
        self.dna_list=[]#dna_list
        self.opened_file=open(self.file,"r")
        self.dna_string = ""  # dna_string
        self.nt_string = ""  # dna_string
        self.rna_string = ""  # rna_string
        #self.nt_string.strip()
        self.read_all_and_join()
        self.nt_string = self.nt_string.upper()
        self.read_all_and_split()
        self.tata_index=[]
        self.tac_index = {}
        self.intron_index={}
        self.rna_list = []  # rna_list
        self.DNA_to_RNA(10) #1 in a thousand chance for a mistake in transcription
        self.rna_list_after_tata = [" "] * len(self.rna_list)
        self.rna_list_after_tac = [" "] * len(self.rna_list)
        self.rna_list_after_splicing = [" "] * len(self.rna_list)
        self.tata_finder()
        self.tac_finder()
        self.intron_and_exon_finder()
        self.RNA_chain_builder()
        self.rna_translation_list = []
        self.join_rna(self.rna_list_after_splicing)

        self.codon_list=[]
        self.RNA_to_codons()

    def uppercase(self,string): #makes the characters uppercase and removes \n newlines
        string_upper = ""
        for character in string:
            if character != "\n":
                character = character.upper()
                string_upper+=character
        return string_upper

    def read_all_and_split(self): #splits all the characters in the file into list items one by one

        for line in self.opened_file:
            line1=Reader.uppercase(self, line)
            for character in line1:
                self.dna_list.append(character)
        self.opened_file.close()
        return self.dna_list

    def read_all_and_join(self): #joins characters into one string
        self.nt_string = open(self.file,"r").read()
        self.nt_string=self.nt_string.strip()
        return self.nt_string

    def DNA_to_RNA(self,random_constant):
        i=0
        #random constant determining how often a transcription error occurs
        while i < len(self.dna_list):
            randomizer_transcription = random.randint(1, random_constant)
            if randomizer_transcription==random_constant:
                randomizer_rna=random.randint(1, 4)
                match randomizer_rna:
                    case 1:
                        self.rna_list.append("U")
                    case 2:
                        self.rna_list.append("A")
                    case 3:
                        self.rna_list.append("G")
                    case 4:
                        self.rna_list.append("C")
                i += 1
            else:
                self.rna_list.append(Codon.complementary(self.dna_list[i]))
                i+=1
        return self.rna_list





    def tata_finder(self): #the function finds the indexes at which tata boxes occur and returns them
        i = 0
        for i in range(0,len(self.dna_list)-3):
            if self.dna_list[i]=="T":
                if self.dna_list[i+1] == "A":
                    if self.dna_list[i+2] == "T":
                        if self.dna_list[i+3] == "A":
                            self.tata_index.append(i) #the +4 makes sure the index is after the tata box is completed, and does not include the tata box
        self.tata_index.append(len(self.dna_list)) #cheeky way of deciding the final end point for the tata range
        return self.tata_index

    def tac_finder(self):

        for tata_box in range(0,len(self.tata_index)-1):#"area" between 2 tata boxes, function attempts to find the first tac in there
            start = self.tata_index[tata_box]
            end = self.tata_index[tata_box + 1]
            tac_range = self.dna_list[start:end]
            for i in range(3,len(tac_range)-2):
                if tac_range[i]=="T" and tac_range[i+1] == "A" and tac_range[i+2] == "C":
                    pair={i+self.tata_index[tata_box]:self.tata_index[tata_box+1]} #key is location of T in first TAC, value is value until the next TATA box is reached
                    self.tac_index.update(pair)
                    break


        return self.tac_index





    def intron_and_exon_finder(self):#starts with GU and ends in AG in RNA sequence,CA and TC for DNA

        for n in range(0,len(self.tac_index)):
            start = list(self.tac_index.keys())[n]  # gets the nth key
            end = self.tac_index[start]  # gets the nth value
            tac_range = self.dna_list[start:end]
            for i in range(0,len(tac_range)-1):
                if tac_range[i]=="C" and tac_range[i+1] == "A":
                    for x in range(i,len(tac_range)-2):
                        if tac_range[x] == "T" and tac_range[x+1] == "C":
                            pair={i+start-1:x+start+2}
                            self.intron_index.update(pair)


                    break


        return self.intron_index


    def RNA_chain_builder(self):

        number_of_tata_boxes=len(self.tata_index)                #this section deals with building the rna list given info about tata box locations
        for o in range(0, number_of_tata_boxes-1):
            start=self.tata_index[o]
            end=self.tata_index[o+1]
            for i in range(start, end):
                if start<i<end:
                    self.rna_list_after_tata[i] = self.rna_list[i]
                else:
                    self.rna_list_after_tata[i]=" "

        tac_index_keys = list(self.tac_index.keys()) #this section deals with building the rna list given info about tata box locations + tac locations
        for a in range(0, len(self.tac_index)):
            start=tac_index_keys[a]
            end=self.tac_index[tac_index_keys[a]]
            for i in range(start, end):
                if start<i<end:
                    self.rna_list_after_tac[i] = self.rna_list[i]
                else:
                    self.rna_list_after_tac[i]=" "

        intron_index_keys = list(self.intron_index.keys())  # this section deals with building the rna list given info about tata box locations + tac locations + intron locations
        for a in range(0, len(self.intron_index)):
            start = intron_index_keys[a]
            end = self.intron_index[intron_index_keys[a]]
            for i in range(start, end):
                if start < i < end:
                    self.rna_list_after_splicing[i] = self.rna_list[i]
                else:
                    self.rna_list_after_splicing[i] = " "


        return self.rna_list_after_tata, self.rna_list_after_tac,self.rna_list_after_splicing

    def join_rna(self,given_rna_list):  # finalizes the RNA-list after all alterations have taken place, to be used for translation view

        for character in given_rna_list:
            if character == " ":
                pass
            else:
                self.rna_translation_list.append(character)

        return self.rna_translation_list

    def RNA_to_codons(self):
        for n in range(0,len(self.rna_translation_list)-2,3):

            codon=Codon(self.rna_translation_list[n],self.rna_translation_list[n+1],self.rna_translation_list[n+2])
            self.codon_list.append(codon.triplet)

        return self.codon_list



















