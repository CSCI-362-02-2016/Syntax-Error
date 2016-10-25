import os
import add

testCases = []
currentDir = os.getcwd()
testCaseTextDir = os.getcwd()
testCaseExecDir = os.getcwd()
testID = None
testReq = None
testComp = None
testMethod = None
testInput = None
testOutcome = None
testResult = None 
#testCaseTextDir = currentDir + '/testCases'
#testCaseExecDir = currentDir + '/testCasesExecutables'
counter = 0

class TestCase: 

    def __init__(self, testID, testReq, testComp, testMethod, testInput, testOutcome, testResult):
        self.testID = testID
        self.testReq = testReq
        self.testComp = testComp
        self.testMethod = testMethod
        self.testInput = testInput
        self.testOutcome = testOutcome
        self.testResult = testResult

#print(testCaseTextDir)
for subdir, dirs, files in os.walk(testCaseTextDir):
    for file in files:
        #print os.path.join(subdir, file)
        filepath = subdir + os.sep + file
    #testCases.append(file)
    #print('Hello!, this is inside of the file loop')
        #print(file)
        #if file.endswith('.txt'):
        if '.txt' in file:
            #print('Hello! this is inside of endsiwth loop')
            openedfile = open(file, 'r')
            #print(openedfile.readline())
            #for line in openedfile:
            for line in openedfile.readlines():
                #line = openedfile.readline()
                #print(line)        
                if "1." in line:
                    temp = line.split("1.")
                    #print(temp[0])
                    testID = temp[1] 
                if "2." in line:
                    temp = line.split("2.")
                    testReq = temp[1]
                if "3." in line:
                    temp = line.split("3.")
                    testComp = temp[1]
                if "4." in line:
                    temp = line.split("4.")
                    testMethod = temp[1] 
                if "5." in line:
                    temp = line.split("5.")
                    testInput = temp[1].strip()
                    #print('Test method should have been defined:' + testMethod)
                    #print('Test input defined here as:' + testInput)
                if "6." in line:
                    temp = line.split("6.")
                    testOutcome = temp[1]
                    #print('Test input is:' + testInput)
                    #fix this later: bug on line formatting
                    currentTest = TestCase(testID, testReq, testComp, testMethod, testInput, testOutcome, False)    
                    testCases.append(currentTest)
        else:
            continue
        openedfile.close()

#print(testCases[0].testInput)
#print(testCases[0].testOutcome)

# TODO: Add additional functionality to read multiple test cases, once our project
# is decided. Currently hard coded to look for the default value         
        
#for file in testCaseExecDir:
        #results = exec(file)

results = add.add(testCases[0].testInput)
print('The results of this method call is: ' + str(results))
testStatus = eval(testCases[0].testOutcome) == results  
testCases[0].testResult = testStatus 
counter = counter + 1

print('The result of the test was: ' + str(testCases[0].testResult))
        

