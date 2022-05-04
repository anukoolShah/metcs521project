from Huffman import startHuffman, fileHuffman
from RunLength import RunLength

#USAGE OF CONTAINER TYPE - TUPLE
mymenu = ("Press 1 to Huffman Encode an input String","Press 2 to Huffman Encode contents of a file",
          "Press 3 to Run Length Encode an input String", "Press 4 to Exit")

#USAGE OF USER-DEFINED FUNCTION - PRIVATE
def __printMenu():
    for i in mymenu:
        print(i)
    menuinput = input()
    return menuinput

#USAGE OF USER-DEFINED FUNCTION - PRIVATE
def __continuePrompt():
    continueAnswer = input("Do you want to continue?(Y/N)")
    return continueAnswer

continueAnswer = 'Y'

#USAGE OF ITERATION TYPE - WHILE LOOP
while continueAnswer == 'y' or continueAnswer == 'Y':
    menuinput = __printMenu()
    while menuinput.isnumeric() == False or (int(menuinput) not in range(1,5)):
        print("Invalid Input")
        menuinput = __printMenu()
    
    #USAGE OF MATCH CASE - AVAILABLE PYTHON 3.10 OR ABOVE    
    match int(menuinput):
        case 1:
            print("****** HUFFMAN ENCODE/DECODE AN INPUT STRING   ******\n")
            startHuffman()
            continueAnswer = __continuePrompt()
        case 2:
            print("****** HUFFMAN ENCODE/DECODE CONTENTS OF A FILE  ******\n")
            fileHuffman()
            continueAnswer = __continuePrompt()
        case 3:
            print("****** RUN LENGTH ENCODE/DECODE AN INPUT STRING ******\n")
            data = input("Enter the String to encode using Run Length Algorithm\n")
            x1 = RunLength()
            encoded, decoded = x1.startRunlength(data)
            print("\n============:: Encoded Output ::============\n", encoded)
            print("\n============:: Decoded Output ::============\n", decoded)
            continueAnswer = __continuePrompt()
        case 4:
            break