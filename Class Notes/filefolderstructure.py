import os
'''
>>> os.listdir('test')
['fileA.txt', 'folder1', 'folder2']
>>> os.path.join('test', 'folder1')
'test\\folder1'
'''

def printFiles(path):
    '''recursivly print all files'''
    try: #treat path as a folder
        for item in os.listdir(path):
            fullPath = os.path.join(path, item)
            printFiles(fullPath)
    except NotADirectoryError: #treat path as a file
        print(path)

def search(path, target):
    '''recursivly search path and print all files with the text target'''
    try:
        for item in os.listdir(path):
            fullPath = os.path.join(path, item)
            search(fullPath, target)
    except NotADirectoryError:
        if target in open(path).read():
            print(path)

def getFiles(path, target):
    '''recursivly search path and return list of file with the text target'''
    try:
        ans = []
        for item in os.listdir(path):
            pullPath = os.path.join(path, item)
            ans += getFiles(fullPath, target)
        return ans 
        except NotADirectoryError:
            if target in open(path).read():
                return [path]
            else:
                return []
