from fractions import Fraction
from set import SetOperation


class Similarity():
    @staticmethod
    def jaccard(X, Y):
        numerator = len(SetOperation.intersection(X, Y))
        denominator = len(SetOperation.union(X, Y))
        ratio = Fraction(numerator, denominator).limit_denominator()
        return ratio

    @staticmethod
    def dice(X, Y):
        numerator = 2 * len(SetOperation.intersection(X, Y))
        denominator = len(X) + len(Y)
        ratio = Fraction(numerator, denominator).limit_denominator()
        return ratio

    @staticmethod
    def symmetricDifference(X, Y):
        return len(SetOperation.symmetricDifference(X, Y))
