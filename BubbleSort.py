
class BubbleSort(object):
    """
        BubbleSort
    """

    def UnitSwap(self, index, unitList):
        tempVal = unitList[index]
        unitList[index] = unitList[index + 1]
        unitList[index + 1] = tempVal
        self.flag += 1


    # sortStr = ["Most Power", "Least Power", "Highest Cost", "Lowest Cost", "Highest Rank", "Lowest Rank"]
    # BubbleSort
    def SortUnits(self, curSortNum, unitList):
        while True:
            self.flag = 0
            for x in range(len(unitList) - 1):
                if curSortNum == 0:
                    if unitList[x].getAttackPower() < unitList[x + 1].getAttackPower():
                        self.UnitSwap(x, unitList)
                elif curSortNum == 1:
                    if unitList[x].getAttackPower() > unitList[x + 1].getAttackPower():
                        self.UnitSwap(x, unitList)
                elif curSortNum == 2:
                    if unitList[x].getCost() < unitList[x + 1].getCost():
                        self.UnitSwap(x, unitList)
                elif curSortNum == 3:
                    if unitList[x].getCost() > unitList[x + 1].getCost():
                        self.UnitSwap(x, unitList)
                elif curSortNum == 4:
                    if unitList[x].getRole() > unitList[x + 1].getRole():
                        self.UnitSwap(x, unitList)
                elif curSortNum == 5:
                    if unitList[x].getRole() < unitList[x + 1].getRole():
                        self.UnitSwap(x, unitList)
            if self.flag <= 0:
                break
        return unitList

