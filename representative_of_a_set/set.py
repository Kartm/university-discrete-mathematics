class SetOperation():
    @staticmethod
    def intersection(X, Y):
        result = []
        for element in X:
            if(element in Y):
                result.append(element)
        return result

    @staticmethod
    def union(X, Y):
        result = []
        for element in X:
            if(element not in result):
                result.append(element)

        for element in Y:
            if(element not in result):
                result.append(element)

        return result

    @staticmethod
    def difference(X, Y):
        result = []
        for element in X:
            if(element not in Y):
                result.append(element)
        return result

    @staticmethod
    def symmetricDifference(X, Y):
        return SetOperation.difference(SetOperation.union(X, Y), SetOperation.intersection(X, Y))
