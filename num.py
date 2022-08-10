class ProcessNumbers:
  
    def readFileReplace(filename):
        newnumber = []

        with open(filename , "r") as fin:
            for numbers in fin:
                newnumber.append(numbers.replace("123", "321"))

        return newnumber

    def convertAndSort(array):
        for i in range(0, len(array)):
            array[i] = int(array[i])
        
        array.sort()
        return array

    def writeInFile(filename, contents):
        with open(filename, "w") as fout:
            for items in contents:
                fout.write("%i\n" % items)
    
    
    result = readFileReplace("in.txt")
    convertAndSort(result)
    writeInFile("out.txt", result)
