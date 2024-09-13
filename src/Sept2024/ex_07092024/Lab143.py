from abc import ABC, abstractmethod

class ExcelReader:

    @abstractmethod
    def readFromExcel(self):
        pass

class Browser:

    @abstractmethod
    def startBrowser(self):
        pass

    def startBrowser(self):
        pass

class TC1(Browser):

    def startBrowser(self):
        print("Starting")

    def stopBrowser(self):
        print("Stop")

    def readFromExcel(self):
        print("readFromExcel is ready")

    def runTC(self):
        self.startBrowser()
        self.readFromExcel()
        self.stopBrowser()

tc1 = TC1()
tc1.runTC()