import time
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
        while IndexInLeftSide < len(LeftSide) and IndexInRightide < len(RightSide): #loop until the the two indexed are greater than the array's len
            if LeftSide[IndexInLeftSide] < RightSide[IndexInRightide]: #if the current left side element at left side index are smaller than the current right side element at right side index
                array[border] = LeftSide[IndexInLeftSide] #makes the array on the current border's position be the smaller element which is the left one
                IndexInLeftSide += 1
            else: #if the left side element isn't smaller than the right side element(which means that the right side is bigger)
                array[border] = RightSide[IndexInRightide] #makes the array on the current border's position be the smaller element which is the left one
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

    inputFile = open("input.txt", "r")

    arrayOfLines = list(filter(lambda element: element != "", inputFile.readlines()))

    arrayOfLines = list(map(lambda element: int(element.replace("\n", "")), arrayOfLines))

    arrayOfLines = [38, 27,43, 3, 9, 82, 10]
    print("Sorting a list with length of " + str(len(arrayOfLines)))
    merge = MainClass.merge_sort()
    merge.sort(arrayOfLines)

    afterTimerM = time.time()
    timeItTookM = (afterTimerM - startTimerM) * 1000

    outputFile = open("output.txt", "w")
    outputString = ""
    for num in arrayOfLines:
            outputString += (str(num) + "\n")

    outputFile.write(outputString)

    print("Time it took to merge algorithm: " + str(timeItTookM)[:3] + "ms")


if __name__ == '__main__':
    main()




