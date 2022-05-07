'''
User-defined Class imported by main program
'''
class RunLength:
    encodedSequence = ""
    decodedSequence = ""
    __decodedList = []
    __encodedList = []
    #usage of init method
    def __init__(self, sequence):
        #DO Nothing
        self.__sequence = sequence 
        
    #usage of private method that takes argument and returns value
    def encode(self):
        count = 1
        for x,item in enumerate(self.__sequence):
            if x == 0:
                continue
            elif item == self.__sequence[x - 1]:
                count += 1
            else:
                self.__encodedList.append((self.__sequence[x - 1], count))
                count = 1
                
        self.__encodedList.append((self.__sequence[len(self.__sequence) - 1], count))
        self.encodedSequence = self.__formatOutput(self.__encodedList)     
        return self.encodedSequence   

    def decode(self):
        for item in self.__encodedList:
            self.__decodedList.append(item[0] * item[1])
        self.decodedSequence = "".join(self.__decodedList)
        return self.decodedSequence

    def __formatOutput(self, sequence):
        result = []
        for item in sequence:
            if (item[1] == 1):
                result.append(item[0])
            else:
                result.append(item[0] + str(item[1]))
        return "".join(result)
    
    def __repr__(self):
        return f'RunLength('+self.__sequence+','+self.encodedSequence+','+self.decodedSequence+')'
        