class Codon: #I'm combining the codon-triplet and amino acid into a single class, to make things easier to manage, and because they are so closely linked


    #source:https://teaching.healthtech.dtu.dk/22110/index.php/Codon_list

    #A dictionary with a list of codons as the value and the name of the amino acid as the key
    Isoleucine={"Isoleucine":["ATT","ATC","ATA"]}
    Leucine={"Leucine":["CTT","CTC","CTA","CTG","TTA","TTG"]}
    Valine={"Valine":["GTT","GTC","GTA","GTG"]}
    Phenylalanine={"Phenylalanine":["TTT","TTC"]}
    Methionine={"Methionine":["ATG"]}
    Cysteine={"Cysteine":["TGT","TGC"]}
    Alanine={"Alanine":["GCT","GCC","GCA","GCG"]}
    Glycine={"Glycine":["GGT","GGC","GGA","GGG"]}
    Proline={"Proline":["CCT","CCC","CCA","CCG"]}
    Threonine={"Threonine":["ACT","ACC","ACA","ACG"]}
    Serine={"Serine":["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"]}
    Tyrosine={"Tyrosine":["TAT", "TAC"]}
    Tryptophan={"Tryptophan":["TGG"]}
    Glutamine={"Glutamine":["CAA", "CAG"]}
    Asparagine={"Asparagine":["AAT", "AAC"]}
    Histidine={"Histidine":["CAT","CAC"]}
    Glutamic_acid={"Glutamic acid":["GAA","GAG"]}
    Aspartic_acid={"Aspartic acid":["GAT","GAC"]}
    Lysine={"Lysine":["AAA","AAG"]}
    Arginine={"Arginine":["CGT","CGC","CGA","CGG","AGA","AGG"]}
    Stop_codons={"Stop codons":["TAA","TAG","TGA"]} #this ends the peptide chain transcription
    Start_codons={"Start codons":["TAA","TAG","TGA"]}

    codon_dictionaries_list=[Isoleucine,Leucine,Valine,Phenylalanine,Methionine,Cysteine,Alanine,Glycine,Proline,Threonine,Serine,Tyrosine,Tryptophan,Glutamine,Asparagine,Histidine,Glutamic_acid,Aspartic_acid,Lysine,Arginine,Stop_codons]



    def __init__(self,base1,base2,base3):
        self.base1=base1
        self.base2 = base2
        self.base3 = base3
        self.triplet=base1+base2+base3
        self.type=None  #The type of amino acid, i.e. "Leucine"
        self.U_T_converter()



    def get_type(self): #Gets codon type when given nucleotide triplet, e.g. "ATT"

        for codon_dictionary in Codon.codon_dictionaries_list:
            for name,triplets in codon_dictionary.items():
                for triplet in triplets:
                    if self.triplet==triplet:
                        self.type=name
                        return self.type

    def complementary(base): #returns the complementary nucleotide when given a nucleotide
        match base:  # python equivalent to switch
            case "A":
                base="U"
            case "T":
                base = "A"
            case "G":
                base = "C"
            case "C":
                base = "G"
            case " ":
                base = " "
        return base
    def U_T_converter(self):
        if "U" in self.triplet: #Lazy but ok way of making sure the Codon class can handle both RNA and DNA
            self.triplet=self.triplet.replace("U","T")
        return self.triplet
