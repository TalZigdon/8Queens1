from random import randrange
import random
import time


def initialPopulation():
    pop = []
    size = 200
    for i in range(size):
        chrome = []

        for i in range(8):
            chrome.append(randrange(8))

        pop.append(chrome)

    return pop


def fitnessFunction(list):
    grade = 49
    slant = 0
    for i in range(0, 8):
        for j in range(i + 1, 8):
            slant = j - i
            if list[i] == list[j]:
                grade = grade - 2
            else:
                if list[i] + slant == list[j] or list[i] - slant == list[j]:
                    grade = grade - 2
    return grade


def mutation(list, i):
    list[i] = random.randint(0, 8)
    return list


def crossOver(list1, list2):
    randNum = random.randint(0, 10)
    if (randNum < 1):
        return list1, list2
    childrenList1 = []
    childrenList2 = []
    for j in range(0, 8):
        i = random.randint(0, 1)
        if (i == 1):
            childrenList1.append(list1[j])
            childrenList2.append(list2[j])
        else:
            childrenList1.append(list2[j])
            childrenList2.append(list1[j])

    for i in range(0, 8):
        randNum = random.randint(0, 100)
        if (randNum == 0):
            childrenList1 = mutation(childrenList1, i)
        randNum = random.randint(0, 100)
        if (randNum == 0):
            childrenList2 = mutation(childrenList2, i)
    return childrenList1, childrenList2


def createNextGen(currGen, grades):
    nextGen = []

    # elitism
    for i in range(2):
        highest = grades.index(max(grades))
        temp = currGen[highest]
        nextGen.append(temp)
        currGen.pop(highest)
        grades.pop(highest)

        lowest = grades.index(min(grades))
        currGen.pop(lowest)
        grades.pop(lowest)

    # do 100 times: select 2, crossover, mutation, add to new gen
    poll = []
    for i in range(len(grades)):
        count = grades[i]
        while count > 0:
            poll.append(currGen[i])
            count = count - 1

    for k in range(98):
        choose = randrange(len(poll))
        parent1 = poll[choose]
        choose = randrange(len(poll))
        parent2 = poll[choose]

        child1, child2 = crossOver(parent1, parent2)
        nextGen.append(child1)
        nextGen.append(child2)

    return nextGen


def main():
    start_time = time.time()
    grades = []
    currGen = initialPopulation()
    for l in currGen:
        grades.append(fitnessFunction(l))
    gen = 1

    while 49 not in grades:
        currGen = createNextGen(currGen, grades)
        grades = []
        for l in currGen:
            grades.append(fitnessFunction(l))
        gen = gen + 1
        if gen % 750 == 0:
            currGen = initialPopulation()
        # print(gen)

    index = grades.index(49)

    print("Solution found after " + str(gen) + " generations.")
    print("running time: %s " % (time.time() - start_time) + "seconds")
    print("The solution is: " + str(currGen[index]))
    for i in range(8):
        for j in range(8):
            if currGen[index][i] == j:
                print("Q", end = " ")
            else:
                print("-", end = " ")
        print("")


if __name__ == "__main__":
    main()
