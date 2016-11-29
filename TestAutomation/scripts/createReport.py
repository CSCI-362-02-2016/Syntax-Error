import os

def reportCreate(testCases):

    headers = ['TestID: ', 'Requirement: ', 'Component: ', 'Method: ', 'Input: ', 'Expected Result: ', 'Test Result: ']
    currentDir = os.getcwd()
    reportURL = os.getcwd() + '/resultsReport.html'
    report = open(reportURL, 'w+')
    report.write('<html> <table border="1" style="width:85%"> \n')

    report.write("<tr> \n")
    for i in range(0, 7):
        report.write("<td>" + headers[i] + "</td> \n")
    report.write("</tr> \n")

    for i in range(1, 25):
        report.write('<tr> \n')
        report.write('<td> TestID: ' + testCases[i].testID + '</td>')
        report.write('<td> Requirement: ' + testCases[i].testReq + '</td>')
        report.write('<td> Component: ' + testCases[i].testComp + '</td>')
        report.write('<td> Method: ' + testCases[i].testMethod + '</td>')
        report.write('<td> Input: ' + testCases[i].testInput + '</td>')
        report.write('<td> Expected Result: ' + testCases[i].testOutcome + '</td>')
        if testCases[i].testResult == True:
            report.write('<td> Test Result: ' + 'Pass' + '</td>')
        else:
            report.write('<td> Test Result: ' + 'Fail' + '</td>')
        report.write('<tr> \n')

    report.write("</table> \n </html>")
    report.close
    return (reportURL)
