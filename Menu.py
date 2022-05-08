from Huffman import Huffman
from RunLength import RunLength

#DEFINE MENU ITEMS
mymenu = ("Press 1 to Huffman Encode an input String","Press 2 to Huffman Encode contents of a file",
          "Press 3 to Run Length Encode an input String", "Press 4 to Exit")

#PRINT MENU ON CONSOLE
def __printMenu():
    for i in mymenu:
        print(i)
    menuinput = input()
    return menuinput

#PROMPT USER TO CONTINUE DOING MORE OPERATIONS
def __continuePrompt():
    continueAnswer = input("Do you want to continue?(Y/N)")
    return continueAnswer

#DEFAULT ANSWER TO YES FOR FIRST RUN
continueAnswer = 'Y'

#LOOP AS LONG AS USER SAYS y OR Y
while continueAnswer == 'y' or continueAnswer == 'Y':
    menuinput = __printMenu()
    #LOOP TILL USER DOESNT PRESS 4
    while menuinput.isnumeric() == False or (int(menuinput) not in range(1,5)):
        print("Invalid Input")
        menuinput = __printMenu()
    
    #USAGE OF MATCH CASE - AVAILABLE PYTHON 3.10 OR ABOVE    
    match int(menuinput):
        case 1:
            print("****** HUFFMAN ENCODE/DECODE AN INPUT STRING   ******\n")
            data = input("Enter the String to encode using Huffman Algorithm\n")
            huffObj =  Huffman(data)       
            print("\n============:: Encoded Output ::============",huffObj.encode(), sep='\n')
            print("\n============:: Decoded Output ::============",huffObj.decode(),sep='\n')
            continueAnswer = __continuePrompt()
        case 2:
            print("****** HUFFMAN ENCODE/DECODE CONTENTS OF A FILE  ******\n")
            huffObj =  Huffman('')
            huffObj.fileHuffman()
            continueAnswer = __continuePrompt()
        case 3:
            print("****** RUN LENGTH ENCODE/DECODE AN INPUT STRING ******\n")
            data = input("Enter the String to encode using Run-Length Algorithm\n")
            rlObj = RunLength(data)
            encoded = rlObj.encode()
            decoded = rlObj.decode()
            print("\n============:: Encoded Output ::============",encoded, sep='\n')
            print("\n============:: Decoded Output ::============",decoded, sep='\n')
            continueAnswer = __continuePrompt()
        case 4:
            break