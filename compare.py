import re
def main():
    with open('iaml_assignment1.res') as f:
        rForest = f.readlines()
    with open('iaml_assignment.res') as f:
        sLog = f.readlines()
    rForest = rForest[22:222]
    sLog = sLog[417:617]
    line = count = 0
    for i,j in zip(rForest,sLog):
        i=i.split();j=j.split();
        if i[2] != j[2]:
            iGuess = float(filter(lambda x: re.search('^\*',x),i)[0].strip('*'))
            jGuess = float(filter(lambda x: re.search('^\*',x),j)[0].strip('*'))
            if iGuess > jGuess: guess = i[2] + '\tFOR'
            else: guess = j[2] + '\tLOG'
            count += 1
        else: guess = i[2]
        line += 1
        print '%s\t%s' % (line,guess)
if __name__ == '__main__':
    main()
