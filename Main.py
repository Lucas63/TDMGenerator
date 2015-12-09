import csv
import Task as TaskClass
import numpy as np
import ReportGenerator


def main():
    inputMatrix = np.matrix(list(csv.reader(open("data.csv", "rb"), delimiter=','))).astype('int')
    task = TaskClass.Task(inputMatrix, 57)
    reportGenerator = ReportGenerator.ReportGenerator(task)
    reportGenerator.generateReport()


main()
