# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 17:50:04 2022

@author: Anukool
"""

class Huffman:
    
    __symbols = dict()
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

    def __calculateCodes(self, node, val=''):
        # huffman code for current node
        newVal = val + str(node.code)

        if(node.left):
            self.__calculateCodes(node.left, newVal)
        if(node.right):
            self.__calculateCodes(node.right, newVal)

        if(not node.left and not node.right):
            self.codes[node.symbol] = newVal
            
        return self.codes        
    
    """ A helper function to calculate the probabilities of symbols in given data"""
    def __calculateProbability(self, data):
        
        for element in data:
            if self.__symbols.get(element) == None:
                self.__symbols[element] = 1
            else: 
                self.__symbols[element] += 1     
        return self.__symbols

    """ A helper function to obtain the encoded output"""
    def __outputEncoded(self, data, coding):
        encoding_output = []
        for c in data:
        #  print(coding[c], end = '')
            encoding_output.append(coding[c])
            
        string = ''.join([str(item) for item in encoding_output])    
        return string
            
    """ A helper function to calculate the space difference between compressed and non compressed data"""    
    def __totalGain(self, data, coding):
        before_compression = len(data) * 8 # total bit space to stor the data before compression
        after_compression = 0
        symbols = coding.keys()
        for symbol in symbols:
            count = data.count(symbol)
            after_compression += count * len(coding[symbol]) #calculate how many bit is required for that symbol in total
        print("\n============:: Space usage before compression (in bits) ::============", before_compression, sep='\n')    
        print("\n============:: Space usage after compression (in bits) ::============",  after_compression, sep='\n')           

    def __huffmanEncoding(self, data):
        symbol_with_probs = self.__calculateProbability(data)
        symbols = symbol_with_probs.keys()
        probabilities = symbol_with_probs.values()
        print("\n============:: List of Symbols in the input ::============", list(symbols), sep='\n')
        print("\n============:: Respective occurence of each symbol ::============", list(probabilities), sep='\n')
        
        nodes = []
        
        # converting symbols and probabilities into huffman tree nodes
        for symbol in symbols:
            outer = Huffman()
            nodes.append(outer.Node(symbol_with_probs.get(symbol), symbol))
        
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
            newOuter = Huffman()
            newNode = newOuter.Node(left.prob+right.prob, left.symbol+right.symbol, left, right)
        
            nodes.remove(left)
            nodes.remove(right)
            nodes.append(newNode)
                
        huffman_encoding = self.__calculateCodes(nodes[0])
        print("\n============:: Symbol and it's Code ::============", huffman_encoding, sep='\n')
        self.__totalGain(data, huffman_encoding)
        encoded_output = self.__outputEncoded(data,huffman_encoding)
        return encoded_output, nodes[0]  
        
    
    def __huffmanDecoding(self, encoded_data, huffman_tree):
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

    def startHuffman(self):
        data = input("Enter the String to encode using Huffman Algorithm\n")
        encoding, tree = self.__huffmanEncoding(data)
        print("\n============:: Encoded Output ::============", encoding, sep='\n')
        print("\n============:: Decoded Output:: ============", self.__huffmanDecoding(encoding,tree),"\n", sep='\n')
        
    def fileHuffman(self):
        f = open("HuffmanFile.txt", "r")
        data = f.read()
        encoding, tree = self.__huffmanEncoding(data)
        print("\n============:: Encoded Output ::============",encoding, sep='\n')
        print("\n============:: Decoded Output ::============",self.__huffmanDecoding(encoding,tree),"\n", sep='\n')
        
