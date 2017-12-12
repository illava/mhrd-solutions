import bisect  # insert an element to an sorted list.
import tqdm  # progress bar on line 17 enumerate(tqdm.tqdm(now)) and line 71


"""
    return all the possible numbers set after one iteration.
    insts:list of tuple, list of instructions
    now: list of tuple
    commom: list object to save memory
"""


def generateNext(now, insts, commom):
    newnow = []
    newnowset = set()
    newinsts = []
    for index, items in enumerate(tqdm.tqdm(now)):
        ran = list(items) + commom
        for i in ran:
            for j in ran:
                if i <= j:
                    continue
                temp = ~(i & j) + shift
                if temp in commom:
                    continue
                if temp in items:
                    continue
                newlist = list(items)
                bisect.insort(newlist, temp)
                tuplenewset = hash(tuple(newlist))
                if tuplenewset in newnowset:
                    continue
                newnow.append(tuple(newlist))
                newnowset.add(tuplenewset)
                newinsts.append(insts[index] + (i, j))
    return newnow, newinsts


if __name__ == '__main__':
    print("start: find all shortest nand operations to single output 0-255")
    now = (0, 1010101, 110011, 1111, 11111111)
    digit = max((len(str(x)) for x in now))
    shift = 2 ** digit
    nows = [int(str(x), 2) for x in now]
    nows.sort()
    goal = set(nows)
    commom = list(nows)
    for i in goal:
        print(i, 0)
    now = [[]]
    insts = [tuple()]
    goal = set(range(256)) - goal
    for j in range(9):
        now, insts = generateNext(now, insts, commom)
        for index, items in enumerate(now):
            for i in goal:  # TODO change here to meet your request
                if i in items:  # such as multi number match
                    print("%3d" % i, end=" ")
                    it = iter(insts[index])
                    for n in it:
                        m = next(it)
                        print("(%3d,%3d,%3d)" %
                              (n, m, ~(n & m) + shift), end=' ')
                    print()
                    goal.remove(i)
                    # continue
                    break
        print(256 - len(goal), "/", 256)
        if len(goal) < 50:
            print("left:", goal)
    for index, items in enumerate(tqdm.tqdm(now)):
        newlist = list(items)
        for i in newlist + commom:
            for j in newlist + commom:
                if i <= j:
                    continue
                temp = ~(i & j) + shift
                if temp in goal:  # TODO change here to meet your request
                    print("%3d" % i, end=" ")
                    it = iter(insts[index])
                    for n in it:
                        m = next(it)
                        print("(%3d,%3d,%3d)" %
                              (n, m, ~(n & m) + shift), end=' ')
                    print("(%3d,%3d,%3d)" %
                          (i, j, ~(i & j) + shift), end=' ')
                    print()
                    goal.remove(temp)
                    exit(0)
