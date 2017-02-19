# Contributors: Shivani
# Lab 1

def printTwoLargest():
    numbers = []

    while True:
        ans = eval(input("Please enter a number: "))
        if ans <= 0:
            break
        else:
            numbers.append(ans)

    numbers.sort()
    if len(numbers) >= 2:
        print("The largest is " + str(numbers[-1]))
        print("The second largest is " + str(numbers[-2]))
    elif len(numbers) == 1:
        print("The largest is " + str(numbers[-1]))
    else:
        print("No positive numbers were entered")

        
def printWordsLines(filename):
    infile = open(filename)
    content = infile.read()
    infile.close()
    print("The file {} contains {} words and {} lines.".format(filename, len(content.split()), content.count('\n')))


def reverseDict(dictionary):
    dic = {}
    for key in dictionary:
        dic[dictionary[key]] = key
    return dic
        










if __name__=='__main__':
    import doctest
    print( doctest.testfile( 'lab1TEST.py' ))
