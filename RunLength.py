class RunLength:
    def __init__(self):
        #DO Nothing
        x = 1        
        
    def __encode(self, sequence):
        count = 1
        result = []
        for x,item in enumerate(sequence):
            if x == 0:
                continue
            elif item == sequence[x - 1]:
                count += 1
            else:
                result.append((sequence[x - 1], count))
                count = 1
                
        result.append((sequence[len(sequence) - 1], count))
        return result            

    def __decode(self, sequence):
        result = []
        for item in sequence:
            result.append(item[0] * item[1])
        return "".join(result)

    def __formatOutput(self, sequence):
        result = []
        for item in sequence:
            if (item[1] == 1):
                result.append(item[0])
            else:
                result.append(item[0] + str(item[1]))
        return "".join(result)

    def startRunlength(self):
        data = input("Enter the String to encode using Huffman Algorithm\n")
        encoded = self.__encode(data)
        print("\n============:: Encoded Output ::============\n", self.__formatOutput(encoded))
        decoded = self.__decode(encoded)
        print("\n============:: Decoded Output ::============\n", decoded)