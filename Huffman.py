# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:50:04 2022

@author: Anukool
"""

# A Huffman Tree Node
class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        # probability of symbol
        self.prob = prob

        # symbol 
        self.symbol = symbol

        # left node
        self.left = left

        # right node
        self.right = right

        # tree direction (0/1)
        self.code = ''

""" A helper function to print the codes of symbols by traveling Huffman Tree"""
codes = dict()

def __calculateCodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.code)

    if(node.left):
        __calculateCodes(node.left, newVal)
    if(node.right):
        __calculateCodes(node.right, newVal)

    if(not node.left and not node.right):
        codes[node.symbol] = newVal
         
    return codes        

""" A helper function to calculate the probabilities of symbols in given data"""
def __calculateProbability(data):
    symbols = dict()
    for element in data:
        if symbols.get(element) == None:
            symbols[element] = 1
        else: 
            symbols[element] += 1     
    return symbols

""" A helper function to obtain the encoded output"""
def __outputEncoded(data, coding):
    encoding_output = []
    for c in data:
      #  print(coding[c], end = '')
        encoding_output.append(coding[c])
        
    string = ''.join([str(item) for item in encoding_output])    
    return string
        
""" A helper function to calculate the space difference between compressed and non compressed data"""    
def __totalGain(data, coding):
    before_compression = len(data) * 8 # total bit space to stor the data before compression
    after_compression = 0
    symbols = coding.keys()
    for symbol in symbols:
        count = data.count(symbol)
        after_compression += count * len(coding[symbol]) #calculate how many bit is required for that symbol in total
    print("\n============:: Space usage before compression (in bits) ::============\n", before_compression)    
    print("\n============:: Space usage after compression (in bits) ::============\n",  after_compression)           

def __huffmanEncoding(data):
    symbol_with_probs = __calculateProbability(data)
    symbols = symbol_with_probs.keys()
    probabilities = symbol_with_probs.values()
    print("\n============:: List of Symbols in the input ::============\n", list(symbols))
    print("\n============:: Respective occurence of each symbol ::============\n", list(probabilities))
    
    nodes = []
    
    # converting symbols and probabilities into huffman tree nodes
    for symbol in symbols:
        nodes.append(Node(symbol_with_probs.get(symbol), symbol))
    
    while len(nodes) > 1:
        # sort all the nodes in ascending order based on their probability
        nodes = sorted(nodes, key=lambda x: x.prob)
        # for node in nodes:  
        #      print(node.symbol, node.prob)
    
        # pick 2 smallest nodes
        right = nodes[0]
        left = nodes[1]
    
        left.code = 0
        right.code = 1
    
        # combine the 2 smallest nodes to create new node
        newNode = Node(left.prob+right.prob, left.symbol+right.symbol, left, right)
    
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)
            
    huffman_encoding = __calculateCodes(nodes[0])
    print("\n============:: Symbol and it's Code ::============\n", huffman_encoding)
    __totalGain(data, huffman_encoding)
    encoded_output = __outputEncoded(data,huffman_encoding)
    return encoded_output, nodes[0]  
    
 
def __huffmanDecoding(encoded_data, huffman_tree):
    tree_head = huffman_tree
    decoded_output = []
    for x in encoded_data:
        if x == '1':
            huffman_tree = huffman_tree.right   
        elif x == '0':
            huffman_tree = huffman_tree.left
        try:
            if huffman_tree.left.symbol == None and huffman_tree.right.symbol == None:
                pass
        except AttributeError:
            decoded_output.append(huffman_tree.symbol)
            huffman_tree = tree_head
        
    string = ''.join([str(item) for item in decoded_output])
    return string        



def startHuffman():
    data = input("Enter the String to encode using Huffman Algorithm\n")
    encoding, tree = __huffmanEncoding(data)
    print("\n============:: Encoded Output ::============\n", encoding)
    print("\n============:: Decoded Output:: ============\n", __huffmanDecoding(encoding,tree),"\n")
    
def fileHuffman():
    f = open("HuffmanFile.txt", "r")
    data = f.read()
    encoding, tree = __huffmanEncoding(data)
    print("\n============:: Encoded Output ::============\n", encoding)
    print("\n============:: Decoded Output ::============\n", __huffmanDecoding(encoding,tree),"\n")
