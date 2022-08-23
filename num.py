class ProcessNumbers:
    rep = "123"
    wth = "321"


    def __init__(self,filein,fileout,arr: list[str]):
        self.filein = filein

        self.fileout = fileout

        self.arr = arr


    def readFileReplace(self):

        with open(self.filein , "r") as fin:
<<<<<<< HEAD
            self.arr = [numbers.replace(ProcessNumbers.rep, ProcessNumbers.wth) for numbers in fin]
 

    def convertAndSort(self):
=======
            #for numbers in fin:
            #   newnumber.append(numbers.replace(what, wth))
            newnumber = [numbers.replace(rep, wth) for numbers in fin]
        return newnumber
>>>>>>> 76ed639af94b83a6310ffe0803739768a3328a5c

        for i in range(0, len(self.arr)):
            self.arr[i] = int(self.arr[i])
        
        self.arr.sort()


    def writeInFile(self):
        
        with open(self.fileout, "w") as fout:
            for items in self.arr:
                fout.write("%i\n" % items)

<<<<<<< HEAD

res = []
myProcess = ProcessNumbers("in.txt", "out.txt",res)

arr1 = myProcess.readFileReplace()
myProcess.convertAndSort()

myProcess.writeInFile()
=======
myProcess = ProcessNumbers("in.txt", "out.txt")
result = myProcess.readFileReplace()
myProcess.convertAndSort(result)
myProcess.writeInFile(result)
>>>>>>> 76ed639af94b83a6310ffe0803739768a3328a5c
