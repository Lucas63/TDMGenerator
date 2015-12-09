import numpy as np


class RelationOptimizer(object):
    """

    """

    @staticmethod
    def optimizeRelation(matrix):
        """

        :param matrix:
        :return:
        """
        tempSet = []
        tempSet.append(RelationOptimizer.blockingMaxROnOmega(matrix))
        tempSet.append(RelationOptimizer.blockingMaxPOnOmega(matrix))
        tempSet.append(RelationOptimizer.blockingStriclyMaxROnOmega(matrix))
        tempSet.append(RelationOptimizer.dominatingMaxROnOmega(matrix))
        tempSet.append(RelationOptimizer.dominatingMaxPOnOmega(matrix))
        tempSet.append(RelationOptimizer.dominatingStriclyMaxROnOmega(matrix))

        return tempSet

    @staticmethod
    def blockingMaxROnOmega(matrix):
        """

        :param matrix:
        :return:
        """
        tempSet = []
        for i in range(0, np.shape(matrix)[0]):
            lowSet = set((np.where(matrix[i, :] == 1)[1]).A1.flat)
            highSet = set((np.where(matrix.transpose()[i, :] == 1)[1]).A1.flat)

            if highSet.issubset(lowSet):
                tempSet.append(i + 1)
        return tempSet

    @staticmethod
    def blockingMaxPOnOmega(matrix):
        """

        :param matrix:
        :return:
        """
        temp = RelationOptimizer.blockingMaxROnOmega(matrix)
        tempSet = []
        for i in range(0, np.shape(temp)[0]):
            highSet = set((np.where(matrix.transpose()[temp[i] - 1, :] == 1)[1]).A1.flat)
            if not bool(highSet):
                tempSet.append(temp[i])
        return tempSet

    @staticmethod
    def blockingStriclyMaxROnOmega(matrix):
        """

        :param matrix:
        :return:
        """
        tempSet = []
        for i in range(0, np.shape(matrix)[1]):
            high = (np.where(matrix.transpose()[i, :] == 1)[1]).A1
            highSet = set(high.flat)
            if not bool(highSet) or highSet == {i}:
                tempSet.append(i + 1)

        return tempSet

    @staticmethod
    def dominatingMaxROnOmega(matrix):
        """

        :param matrix:
        :return:
        """
        omega = set(range(1, np.shape(matrix)[1]))
        tempSet = []
        for i in range(0, np.shape(matrix)[1]):
            lowSet = set((np.where(matrix[i, :] == 1)[1]).A1.flat)
            if lowSet == omega:
                tempSet.append(i + 1)

        return tempSet

    @staticmethod
    def dominatingMaxPOnOmega(matrix):
        """

        :param matrix:
        :return:
        """
        omega = set(range(0, np.shape(matrix)[1]))
        tempSet = []
        for i in range(0, np.shape(matrix)[1]):
            lowSet = set((np.where(matrix[i, :] == 1)[1]).A1.flat)
            if lowSet == (omega - {i}):
                tempSet.append(i + 1)

        return tempSet

    @staticmethod
    def dominatingStriclyMaxROnOmega(matrix):
        """

        :param matrix:
        :return:
        """
        omega = set(range(0, np.shape(matrix)[1]))
        tempSet = []
        for i in range(0, np.shape(matrix)[1]):
            lowSet = set((np.where(matrix[i, :] == 1)[1]).A1.flat)
            highSet = set((np.where(matrix.transpose()[i, :] == 1)[1]).A1.flat)
            if (lowSet == omega and highSet == {i}) or not bool(highSet):
                tempSet.append(i + 1)
        return tempSet

    @staticmethod
    def isInnerStable(matrix):
        return True

    @staticmethod
    def isOuterStable(matrix):
        return True
