# coding=utf-8
import numpy as np
import os
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import ParagraphStyle
import time


class ReportGenerator(object):
    """
    Class which generating report in PDF format, and saving this report in the same directory with
    program.
    """

    def __init__(self, task):
        """
        Constructor of class with one parameter
        :param task: object which contains information needed for PDF document generating
        :return: object of class
        """
        self.task = task
        self.pageMarkup = []
        self.styles = []
        self.imagesNumber = 0
        self.tablesNumber = 0

    def generateReport(self):
        """
        Generating report from given Task object into PDF-document and save it to the same with program file
        directory
        :return: nothing
        """
        from reportlab.platypus import Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.platypus import SimpleDocTemplate
        from reportlab.rl_config import defaultPageSize
        import getpass

        # parameters of images for report
        extension = '.png'
        path = 'Temporal Images/'

        PAGE_HEIGHT = defaultPageSize[1]
        self.styles = getSampleStyleSheet()
        space = Spacer(0, 15)
        bodyStyle = ParagraphStyle('picture', alignment=TA_CENTER)

        # Title
        self.insertParagraph("Calculation and graphic work on the theory of decision-making ",
                             self.styles["title"], space)
        # "(Variant :"+ str(self.task.variant) + ")"
        self.insertParagraph("<strong>Author  : </strong>" + getpass.getuser(), self.styles["Normal"], Spacer(0, 5))
        self.insertParagraph("<strong>Variant : </strong>" + str(self.task.variant), self.styles["Normal"],
                             Spacer(0, 5))
        self.insertParagraph("<strong>Created : </strong>" + time.strftime("%c"), self.styles["Normal"], space)

        # Common data


        # Abstract with task matrix
        self.insertParagraph("<strong>Abstract. </strong>On the set of alternatives Omega given ratio"
                             " of benefits R presented by adjacency matrix", self.styles["Normal"], space)
        self.insertTable(map(list, list(self.task.relation.getMatrix().A)))
        self.insertParagraph(self.tableSignature("Adjacency matrix of relation R"), bodyStyle, space)

        # Exercise one
        self.insertParagraph(self.task.tasksText[0], self.styles["Normal"], space)
        self.insertImage(self.task.relation.getImageName())
        self.insertParagraph(self.imageSignature("Graph of ratio R"), bodyStyle, space)

        # Exercise two
        self.insertParagraph(self.task.tasksText[1], self.styles["Normal"], space)
        self.insertTable(self.generateAnalyzeView(self.task.relation))
        self.insertParagraph(self.tableSignature("Analysis of relation R "), bodyStyle, space)
        self.insertParagraph(self.relationSignature(self.task.relation.getName(), self.task.relation.getType()),
                             self.styles["Normal"], space)

        # Exercise three
        self.insertParagraph(self.task.tasksText[2], self.styles["Normal"], space)
        self.insertTable(map(list, list(self.task.symmetricPart.getMatrix().A)))
        self.insertParagraph(self.tableSignature("Adjacency matrix of Symmetric part of relation R"), bodyStyle, space)
        self.insertImage(self.task.symmetricPart.getImageName())
        self.insertParagraph("<strong>Pic 2.</strong> Symmetric part of R ratio ", bodyStyle, space)
        self.insertTable(self.generateAnalyzeView(self.task.symmetricPart))
        self.insertParagraph(self.tableSignature("Analysis of Symmetric part of relation R "), bodyStyle, space)
        self.insertParagraph(
            self.relationSignature(self.task.symmetricPart.getName(), self.task.symmetricPart.getType()),
            self.styles["Normal"], space)

        self.insertTable(map(list, list(self.task.asymmetricPart.getMatrix().A)))
        self.insertParagraph(self.tableSignature("Adjacency matrix of Asymmetric part of relation R"), bodyStyle, space)
        self.insertImage(self.task.asymmetricPart.getImageName())
        self.insertParagraph("<strong>Pic 3.</strong> Asymmetric part of R ratio ", bodyStyle, space)
        self.insertTable(self.generateAnalyzeView(self.task.asymmetricPart))
        self.insertParagraph(self.tableSignature("Analysis of Asymmetric part of relation R "), bodyStyle, space)
        self.insertParagraph(
            self.relationSignature(self.task.asymmetricPart.getName(), self.task.asymmetricPart.getType()),
            self.styles["Normal"], space)

        self.insertTable(map(list, list(self.task.nonComparablePart.getMatrix().A)))
        self.insertParagraph(self.tableSignature("Adjacency matrix of non-Comparable relation built on R"), bodyStyle,
                             space)
        self.insertImage(self.task.nonComparablePart.getImageName())
        self.insertParagraph("<strong>Pic 4.</strong> Relation of non-comparability built on R ", bodyStyle, space)
        self.insertTable(self.generateAnalyzeView(self.task.nonComparablePart))
        self.insertParagraph(self.tableSignature("Relation of non-comparability built on R "), bodyStyle, space)
        self.insertParagraph(self.relationSignature(self.task.nonComparablePart.getName(),
                                                    self.task.nonComparablePart.getType()),
                             self.styles["Normal"], space)
        # Exercise four
        self.insertParagraph(self.task.tasksText[3], self.styles["Normal"], space)
        self.insertTable(self.generateOptmizationView(self.task.relation, False))
        self.insertParagraph(self.tableSignature("Optimal sets( blocking principle) "), bodyStyle, space)

        # Exercise five
        self.insertParagraph(self.task.tasksText[4], self.styles["Normal"], space)
        self.insertTable(self.generateOptmizationView(self.task.relation, True))
        self.insertParagraph(self.tableSignature("Optimal sets( dominating principle) "), bodyStyle, space)

        # Exercise six
        self.insertParagraph(self.task.tasksText[5], self.styles["Normal"], space)

        # Exercise seven
        self.insertParagraph(self.task.tasksText[6], self.styles["Normal"], space)

        # Exercise eight
        self.insertParagraph(self.task.tasksText[7], self.styles["Normal"], space)

        if os._exists(getpass.getuser() + "_" + str(self.task.variant) + '.pdf'):
            os.remove(getpass.getuser() + "_" + str(self.task.variant) + '.pdf')
            print "File " + getpass.getuser() + "_" + str(self.task.variant) + '.pdf' + " deleted successfully"
        doc = SimpleDocTemplate(getpass.getuser() + "_" + str(self.task.variant) + '.pdf')
        print "File " + getpass.getuser() + "_" + str(self.task.variant) + '.pdf' + " created successfully"
        doc.build(self.pageMarkup)
        return

    def generateAnalyzeView(self, relation):
        """

        :param relation:
        :return:
        """

        temp = relation.getAnalyze()
        tempSet = []
        for i in range(0, np.shape(temp)[0]):
            if bool(temp[i]):
                tempSet.append([self.task.analyzeRules[i], "True"])
            else:
                tempSet.append([self.task.analyzeRules[i], "False"])
        return tempSet

    def generateOptmizationView(self, relation, isBlocking):
        """

        :param relation:
        :param isBlocking:
        :return:
        """

        if not isBlocking:
            counter = 3
        else:
            counter = 0
        temp = relation.getOptimization()
        tempSet = []
        for i in range(counter, np.shape(temp)[0] - (3 - counter)):
            tempSet.append([self.task.optimizationRules[i], str(np.asarray(temp[i]))])
        return tempSet

    def insertParagraph(self, text, paragraphStyle, space):
        """

        :param text:
        :param paragraphStyle:
        :param space:
        :return:
        """
        from reportlab.platypus import Paragraph

        self.pageMarkup.append(Paragraph(text, paragraphStyle))
        self.pageMarkup.append(space)

    def insertTable(self, table):
        """

        :param table:
        :return:
        """
        from reportlab.lib import colors
        from reportlab.platypus import Table, TableStyle, Spacer
        from reportlab.platypus.flowables import KeepTogether
        element = Table(table)
        element.setStyle(TableStyle([
            ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
            ('BOX', (0, 0), (-1, -1), 0.25, colors.black),
        ]))
        for i in range(0, len(table)):
            temp = table[i]
            for j in range(0, len(temp)):
                if temp[j] == 1:
                    element.setStyle(TableStyle([('BACKGROUND', (j, i), (j, i), colors.yellowgreen)]))
                if temp[j] == "True":
                    element.setStyle(TableStyle([('BACKGROUND', (j, i), (j, i), colors.yellowgreen)]))
                if temp[j] == "False":
                    element.setStyle(TableStyle([('BACKGROUND', (j, i), (j, i), colors.fidred)]))
                if temp[j] == "[]":
                    element.setStyle(TableStyle([('BACKGROUND', (j, i), (j, i), colors.fidred)]))

        self.pageMarkup.append(KeepTogether(element))
        self.pageMarkup.append(Spacer(0, 15))

    def insertImage(self, imageName):
        """

        :param name:
        :param path:
        :param extension:
        :return:
        """

        from reportlab.platypus import Image, Spacer
        self.pageMarkup.append(Image(imageName, 340, 253))
        self.pageMarkup.append(Spacer(0, 15))

    def imageSignature(self, description):
        """

        :param description:
        :return:
        """
        self.imagesNumber += 1
        return "<strong>Picture " + str(self.imagesNumber) + ".</strong> " + description

    def tableSignature(self, description):
        """

        :param description:
        :return:
        """
        self.tablesNumber += 1
        return "<strong>Table " + str(self.tablesNumber) + ".</strong> " + description

    def relationSignature(self, name, description):
        """

        :param name:
        :param description:
        :return:
        """
        return "<strong>Ratio type :</strong> Given " + name + " is of type " + "<strong><i>" + description + "</i></strong>"
