import numpy as np
import os
import networkx as nx


class RelationVisualizer(object):
    """

    """

    @staticmethod
    def saveRelatioGraph(matrix, name):
        """

        :param matrix:
        :param name:
        :return:
        """
        graph1 = nx.from_numpy_matrix(matrix, create_using=nx.MultiDiGraph())
        pos = {}
        labels = {}
        nodeColors = []
        for i in range(0, np.shape(matrix)[1]):
            pos[i] = (i * 10, np.shape(matrix)[1] * 10 - (sum(matrix[:, i]) * 10))
            labels[i] = i + 1
            if matrix.item(i, i) == 1:
                nodeColors.append('g')
            else:
                nodeColors.append('r')

        import matplotlib.pyplot as plt

        nx.draw(graph1,
                with_labels=True, pos=pos, labels=labels,
                node_color=nodeColors,
                label='Something',
                facecolor='red')

        path = 'Temporal Images/'
        extension = '.png'
        imageName = path + name + extension

        if os._exists(imageName):
            os.remove(imageName)
            print "File " + imageName + " deleted successfully"

        plt.savefig(imageName, facecolor='lightgrey')
        print "File " + imageName + " created successfully"
        plt.close()
        return imageName

    @staticmethod
    def printMatrix(matrix, name):
        """

        :param matrix:
        :param name:
        :return:
        """
        print "<------Adjacency matrix of ", name, " ------>"
        print matrix

    @staticmethod
    def printAnalyze(matrixAnalyze, name):
        """

        :param matrixAnalyze:
        :param name:
        :return:
        """
        matrixAnalyze = np.array(matrixAnalyze)

        print ""
        print "<------ " + name + " analyze------></br>"
        print "Reflective      : ", matrixAnalyze[0]
        print "Anti-reflective : ", matrixAnalyze[1]
        print "Symmetric       : ", matrixAnalyze[2]
        print "Asymmetric      : ", matrixAnalyze[3]
        print "Anti-symmetric  : ", matrixAnalyze[4]
        print "Transitive      : ", matrixAnalyze[5]
        print "Anti-Transitive : ", matrixAnalyze[6]
        print "Acyclic         : ", matrixAnalyze[7]
        print "Connected       : ", matrixAnalyze[8]
        print "Weak Connected  : ", matrixAnalyze[9]

    @staticmethod
    def printOptimization(matrixOptimization, name):
        """

        :param matrixOptimization:
        :param name:
        :return:
        """
        print "<------ ", name, " optimization------>"
        print "        Max R on Omega(blocking principle) : ", matrixOptimization[0]
        print "        Max P on Omega(blocking principle) : ", matrixOptimization[1]
        print "Stricly Max R on Omega(blocking principle) : ", matrixOptimization[2]
        print " "
        print "        Max R on Omega(dominating principle) : ", matrixOptimization[3]
        print "        Max P on Omega(dominating principle) : ", matrixOptimization[4]
        print "Stricly Max R on Omega(dominating principle) : ", matrixOptimization[5]
