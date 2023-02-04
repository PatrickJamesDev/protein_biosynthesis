import unittest
from reader import Reader


class TestReader(unittest.TestCase):
    file="1"
    file4="4.txt"
    global reader
    reader=Reader(file)


    def test_rna_sequence(self): #tests to make sure no bad characters have gotten into the dna_list
        if int in reader.dna_list:
            raise TypeError("int in the file or list")
        elif float in reader.dna_list:
            raise TypeError("float in the file or list")
        elif "\n" in reader.dna_list:
            raise TypeError("newline in the file or list")
    def test_(self): #naturally there should be less tac blocks than tata blocks, this test checks for that
        if self.assertGreater(len(reader.tac_index),len(reader.tata_index),"there are less tac blocks than tata boxes, which makes sense"):
            pass
        else:
            raise ArithmeticError("There can't be more tac blocks than tata boxes")

if __name__ == "__main__":
    unittest.main()
