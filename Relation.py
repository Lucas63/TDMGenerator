import RelationAnalyzer as Analyzer
import RelationOptimizer as Optimizer
import RelationVisualizer as Visualizer


class Relation:
    """
    Class of relation
    """

    def __init__(self, matrix, name):
        """
        Constructor of class with two parameters

        :param matrix: numpy.matrix - adjacency matrix of Relation
        :param name: String - name of Relation
        :return: new Relation object
        """
        self.inputMatrix = matrix
        self.name = name
        self.analyze = []
        self.optimization = []
        self.relationType = self.setType()
        self.imageName = ""

    def runAnalyze(self):
        """

        :return: nothing
        """
        self.analyze = Analyzer.RelationAnalyzer.analyzeRelation(self.inputMatrix)

    def runOptimization(self):
        """

        :return:
        """
        self.optimization = Optimizer.RelationOptimizer.optimizeRelation(self.inputMatrix)

    def getAnalyze(self):
        """

        :return:
        """
        if not bool(self.analyze):
            self.runAnalyze()
        return self.analyze

    def getOptimization(self):
        """

        :return:
        """
        if not bool(self.optimization):
            self.runOptimization()
        return self.optimization

    def getMatrix(self):
        """
        getter for adjacency matrix
        :return: numpy.matrix - adjacency matrix
        """
        import numpy as np
        return np.asmatrix(self.inputMatrix)

    def getName(self):
        """
        getter for relation name

        :return: String - name of relation
        """
        return self.name

    def setType(self):
        type = "Unknown"
        temp = self.getAnalyze()
        if temp[0]:  # isReflective
            if temp[5]:  # isTransitive
                type = "Quasi-order"
                if temp[2]:  # isSymmetric
                    type = "Equality"
                if temp[4]:
                    type = "Non-strict order"
        else:  # Antireflective
            if temp[5]:
                type = "Strict order"
                if temp[6]:
                    type = "Strict ordering"
        return type

    def getType(self):
        return self.relationType

    def getImageName(self):
        if self.imageName == "":
            self.imageName = Visualizer.RelationVisualizer.saveRelatioGraph(self.getMatrix(), self.name)
        return self.imageName
