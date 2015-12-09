import Relation as Relation
import RelationAnalyzer as Analyzer
import RelationVisualizer as Visualizer


class Task:
    """

    """

    def __init__(self, matrix, variant):
        """

        :param matrix:
        :return:
        """
        self.inputMatrix = matrix
        self.variant = variant
        self.relation = Relation.Relation(self.inputMatrix, "Ratio of advantages R")
        self.symmetricPart = Relation.Relation(Analyzer.RelationAnalyzer.buildSymmetricPart(self.inputMatrix),
                                               "Symmetric part of Ratio R")
        self.asymmetricPart = Relation.Relation(Analyzer.RelationAnalyzer.buildAsymmetricPart(self.inputMatrix),
                                                "Asymmetric part of Ratio R")
        self.nonComparablePart = Relation.Relation(Analyzer.RelationAnalyzer.buildNonComparablePart(self.inputMatrix),
                                                   "Non-comparable Ratio built on Ratio R")

        self.analyzeRules = []
        self.analyzeRules.append("Reflective      ")
        self.analyzeRules.append("Anti-reflective ")
        self.analyzeRules.append("Symmetric       ")
        self.analyzeRules.append("Asymmetric      ")
        self.analyzeRules.append("Anti-symmetric  ")
        self.analyzeRules.append("Transitive      ")
        self.analyzeRules.append("Anti-Transitive ")
        self.analyzeRules.append("Acyclic         ")
        self.analyzeRules.append("Connected       ")
        self.analyzeRules.append("Weak Connected  ")

        self.optimizationRules = []
        self.optimizationRules.append("        Max R on Omega(blocking principle)  ")
        self.optimizationRules.append("        Max P on Omega(blocking principle)  ")
        self.optimizationRules.append("Stricly Max R on Omega(blocking principle)  ")
        self.optimizationRules.append("        Max R on Omega(dominating principle)")
        self.optimizationRules.append("        Max P on Omega(dominating principle)")
        self.optimizationRules.append("Stricly Max R on Omega(dominating principle)")

        self.tasksText = []
        self.tasksText.append("<strong>Exercise 1. </strong> Build graph of ratio")

        self.tasksText.append("<strong>Exercise 2.</strong> Analyze given ration : set its properties "
                              "and attributed to a known class if It's possible")

        self.tasksText.append("<strong>Exercise 3.</strong> Build asymmetric P(R), symmetric I(R) parts of ratio, "
                              "ratio of non-comparability N(R) from R, analyze given ratios")

        self.tasksText.append("<strong>Exercise 4.</strong> Find sets of optimal solves, using dominating principle"
                              "(build sets of max on R elements,max on P elements"
                              ", stricly max on R")

        self.tasksText.append("<strong>Exercise 5.</strong> Find sets of optimal solves, using blocking principle"
                              "(build sets of max on R elements,max on P elements"
                              ", stricly max on R")

        self.tasksText.append("<strong>Exercise 6.</strong> Find sets of solves optimal by Neiman-Morgenstein;"
                              " If R or P(R) acyclic, use specific algorithm given for building this sets")

        self.tasksText.append("<strong>Exercise 7.</strong> Find sets of 1-,2-,3-,4- max elements")

        self.tasksText.append("<strong>Exercise 8.</strong> Make conclusion(decide, which alternatives"
                              "to choose according to taken results)")
        print "Task created"

    def printReport(self):
        """

        :return:
        """
        Visualizer.RelationVisualizer.printMatrix(self.relation.getMatrix(),
                                                  self.relation.getName())

        Visualizer.RelationVisualizer.printAnalyze(self.relation.getAnalyze(),
                                                   self.relation.getName())

        Visualizer.RelationVisualizer.printMatrix(self.symmetricPart.getMatrix(),
                                                  self.symmetricPart.getName())
        Visualizer.RelationVisualizer.printAnalyze(self.symmetricPart.getAnalyze(),
                                                   self.symmetricPart.getName())

        Visualizer.RelationVisualizer.printMatrix(self.asymmetricPart.getMatrix(),
                                                  self.asymmetricPart.getName())
        Visualizer.RelationVisualizer.printAnalyze(self.asymmetricPart.getAnalyze(),
                                                   self.asymmetricPart.getName())

        Visualizer.RelationVisualizer.printMatrix(self.nonComparablePart.getMatrix(),
                                                  self.nonComparablePart.getName())
        Visualizer.RelationVisualizer.printAnalyze(self.nonComparablePart.getAnalyze(),
                                                   self.nonComparablePart.getName())

        Visualizer.RelationVisualizer.printOptimization(self.relation.getOptimization(),
                                                        self.relation.getName())
        Visualizer.RelationVisualizer.showGraph(self.relation.getMatrix(), 'first', False)
        Visualizer.RelationVisualizer.showGraph(self.symmetricPart.getMatrix(), 'second', False)
        Visualizer.RelationVisualizer.showGraph(self.asymmetricPart.getMatrix(), 'third', False)
        Visualizer.RelationVisualizer.showGraph(self.nonComparablePart.getMatrix(), 'fourth', False)
