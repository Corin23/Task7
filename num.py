class ProcessNumbers:
    
    def __init__(self,filein,fileout):
        self.filein = filein
        self.fileout = fileout

    def readFileReplace(self):
        newnumber = []
        rep = "123"
        wth = "321"

        with open(self.filein , "r") as fin:
            #for numbers in fin:
            #   newnumber.append(numbers.replace(what, wth))
            newnumber = [numbers.replace(rep, wth) for numbers in fin]
        return newnumber

    def convertAndSort(self, array):
        for i in range(0, len(array)):
            array[i] = int(array[i])
        
        array.sort()
        return array

    def writeInFile(self, contents):
        with open(self.fileout, "w") as fout:
            for items in contents:
                fout.write("%i\n" % items)

myProcess = ProcessNumbers("in.txt", "out.txt")
result = myProcess.readFileReplace()
myProcess.convertAndSort(result)
myProcess.writeInFile(result)
