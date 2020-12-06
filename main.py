def merge(array):
    if len(array) > 1:

        midIndex = len(array) // 2

        LeftSide = array[:midIndex]
        merge(LeftSide)

        RightSide = array[midIndex:]
        merge(RightSide)

        IndexInLeftSide = 0
        IndexInRightide = 0
        border = 0
        while IndexInLeftSide < len(LeftSide) and IndexInRightide < len(RightSide):
            if LeftSide[IndexInLeftSide] < RightSide[IndexInRightide]:
                array[border] = LeftSide[IndexInLeftSide]
                IndexInLeftSide += 1
            else:
                array[border] = RightSide[IndexInRightide]
                IndexInRightide += 1
            border += 1


        while IndexInLeftSide < len(LeftSide):
            array[border] = LeftSide[IndexInLeftSide]
            IndexInLeftSide += 1
            border += 1

        while IndexInRightide < len(RightSide):
            array[border] = RightSide[IndexInRightide]
            IndexInRightide += 1
            border += 1


class Sort:
    def __init__(self):
        self.merge_sort = merge_sort





class merge_sort(Sort):
    def __init__(self):
        self.sort = merge



def main():
    startTimerM = time.time()
    MainClass = Sort()



    arrayOfLines = list(filter(lambda element: element != "", inputFile.readlines()))
    arrayOfLines = list(map(lambda element: int(element.replace("\n", "")), arrayOfLines))
    print("Sorting a list with length of " + str(len(arrayOfLines)))
    merge = MainClass.merge_sort()
    sortedList = merge.sort(arrayOfLines)

    afterTimerM = time.time()
    timeItTookM = (afterTimerM - startTimerM) * 1000

    outputFile = open("output.txt", "w")
    outputString = ""
    for num in sortedList:
            outputString += (str(num) + "\n")

    outputFile.write(outputString)

    print("Time it took to merge algorithm: " + str(timeItTookM)[:3] + "ms")



if __name__ == '__main__':
    main()
