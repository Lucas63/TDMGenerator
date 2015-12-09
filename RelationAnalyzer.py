import numpy as np
import random


class RelationAnalyzer(object):
    """

    """

    @staticmethod
    def analyzeRelation(matrix):
        """

        :param matrix:
        :return:
        """
        tempSet = []
        tempSet.append(RelationAnalyzer.isReflective(matrix))
        tempSet.append(RelationAnalyzer.isAntiReflective(matrix))
        tempSet.append(RelationAnalyzer.isSymmetric(matrix))
        tempSet.append(RelationAnalyzer.isAsymmetric(matrix))
        tempSet.append(RelationAnalyzer.isAntiSymmetric(matrix))
        tempSet.append(RelationAnalyzer.isTransitive(matrix))
        tempSet.append(RelationAnalyzer.isAntiTransitive(matrix))
        tempSet.append(RelationAnalyzer.isAcyclic(matrix))
        tempSet.append(RelationAnalyzer.isConnected(matrix))
        tempSet.append(RelationAnalyzer.isWeakConnected(matrix))
        return tempSet

    @staticmethod
    def isReflective(matrix):
        """

        :param matrix:
        :return:
        """
        return (matrix.diagonal() == 1).all()

    @staticmethod
    def isAntiReflective(matrix):
        """

        :param matrix:
        :return:
        """
        return (matrix.diagonal() == 0).all()

    @staticmethod
    def isSymmetric(matrix):
        """

        :param matrix:
        :return:
        """
        return (matrix == matrix.transpose()).all()

    @staticmethod
    def isAsymmetric(matrix):
        """

        :param matrix:
        :return:
        """
        return not (matrix == matrix.transpose()).any()

    @staticmethod
    def isAntiSymmetric(matrix):
        """

        :param matrix:
        :return:
        """
        return RelationAnalyzer.isReflective(matrix) and not \
            RelationAnalyzer.isSymmetric(matrix) and not \
                   RelationAnalyzer.isAsymmetric(matrix)

    @staticmethod
    def isTransitive(matrix):
        """

        :param matrix:
        :return:
        """
        matrix = np.asmatrix(matrix)
        for i in range(0, np.shape(matrix)[0]):

            x = (np.where(matrix[i, :] == 1)[1]).A1
            xSet = set(x.flat)
            # print "P(",i+1,")_",x+1
            for j in range(0, len(x)):
                z = (np.where(matrix[x[j], :] == 1)[1]).A1
                zSet = set(z.flat)
                if not zSet.issubset(xSet):
                    return False
                    # print "---P(",j+1,")_",z+1,"is NOT subset of","P(",i+1,")_"
                    # else:
                    # print "---P(",x[j]+1,")_",z+1,"is subset of","P(",i+1,")_"
        return True

    @staticmethod
    def isAntiTransitive(matrix):
        """

        :param matrix:
        :return:
        """
        matrix = np.asmatrix(matrix)
        for i in range(0, np.shape(matrix)[0]):
            x = (np.where(matrix[i, :] == 0)[1]).A1
            xSet = set(x.flat)
            # print "P(",i+1,")_",x+1
            for j in range(0, len(x)):
                z = (np.where(matrix[x[j], :] == 0)[1]).A1
                zSet = set(z.flat)
                if not zSet.issubset(xSet):
                    return False
                    # print "---P(",j+1,")_",z+1,"is NOT subset of","P(",i+1,")_"
                    # else:
                    # print "---P(",x[j]+1,")_",z+1,"is subset of","P(",i+1,")_"

        return True

    @staticmethod
    def isAcyclic(matrix):
        """

        :param matrix:
        :return:
        """

        return (not RelationAnalyzer.isReflective(matrix)) & (not RelationAnalyzer.isSymmetric(matrix))

    @staticmethod
    def isConnected(matrix):
        """

        :param matrix:
        :return:
        """
        return np.logical_or(matrix == 1, matrix.transpose() == 1).all()

    @staticmethod
    def isWeakConnected(matrix):
        """

        :param matrix:
        :return:
        """
        temp = (np.logical_or(matrix == 1, matrix.transpose() == 1))
        np.fill_diagonal(temp, True)
        return (temp == True).all()

    @staticmethod
    def buildSymmetricPart(matrix):
        """

        :param matrix:
        :return:
        """
        tempMatrix = np.zeros(np.shape(matrix))
        tempMatrix[(matrix == 1) & (matrix.transpose() == 1)] = 1
        return tempMatrix

    @staticmethod
    def buildAsymmetricPart(matrix):
        """

        :param matrix:
        :return:
        """
        tempMatrix = np.zeros(np.shape(matrix))
        tempMatrix[(matrix == 1) & (matrix.transpose() == 0)] = 1
        return tempMatrix

    @staticmethod
    def buildNonComparablePart(matrix):
        """

        :param matrix:
        :return:
        """
        tempMatrix = np.zeros(np.shape(matrix))
        tempMatrix[(matrix == 0) & (matrix.transpose() == 0)] = 1

        return np.asmatrix(tempMatrix)
