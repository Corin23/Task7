class ProcessNumbers:
    rep = "123"
    wth = "321"


    def __init__(self,filein,fileout,arr: list[str]):
        self.filein = filein

        self.fileout = fileout

        self.arr = arr


    def readFileReplace(self):

        with open(self.filein , "r") as fin:
            self.arr = [numbers.replace(ProcessNumbers.rep, ProcessNumbers.wth) for numbers in fin]
 

    def convertAndSort(self):

        for i in range(0, len(self.arr)):
            self.arr[i] = int(self.arr[i])
        
        self.arr.sort()


    def writeInFile(self):
        
        with open(self.fileout, "w") as fout:
            for items in self.arr:
                fout.write("%i\n" % items)


res = []
myProcess = ProcessNumbers("in.txt", "out.txt",res)

arr1 = myProcess.readFileReplace()
myProcess.convertAndSort()

myProcess.writeInFile()
