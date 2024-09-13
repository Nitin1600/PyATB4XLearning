class ExcelReader:

    @staticmethod
    def readExcelFile():
        print("Reading from Excel")

class MYSQLDBConnection:

    @staticmethod
    def readMYSQLFile():
        print("Reading from MYSQL")

class TC1:
    def runTC(self):
        ExcelReader().readExcelFile()
        MYSQLDBConnection.readMYSQLFile()

tc1 = TC1()
tc1.runTC()