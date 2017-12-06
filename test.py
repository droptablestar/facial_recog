def main():
    same=diff=0;
    with open('iaml_assignment.res') as f:
        f0 = f.readlines()
    with open('iaml_assignment1.res') as f:
        f1 = f.readlines()
    f0 = f0[21:221]
    f1 = f1[22:222]

    for line0,line1 in zip(f0,f1):
        line0=line0.split()
        line1=line1.split()
        print line0[2],line1[2]
        if line0[2] == line1[2]: same+=1
        else: diff +=1
    print same,diff
    
if __name__ == '__main__':
    main()
