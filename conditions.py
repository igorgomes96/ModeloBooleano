class Condition:

    #get intersection of the lists
    @staticmethod
    def andCondition(list1, list2):
        return [doc for doc in list1 if doc in list2]

    #get intersection of the lists
    @staticmethod
    def notCondition(listNot, listAll):
        return [doc for doc in listAll if doc not in listNot]

    #get union of the lists
    @staticmethod
    def orCondition(list1, list2):
        return list2 + [doc for doc in list1 if doc not in list2]