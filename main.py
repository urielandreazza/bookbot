def main():
    path = 'books/frankenstein.txt'
    book = readBook(path)
    charDict = countChars(book)
    printReport(path, countWords(book), sortDictionary(charDict))

def readBook(path):
    with open(path) as f:
        return f.read()

def countWords(book):
    return len(book.split())

def countChars(book):
    lowerCaseBook = book.lower()
    charDict = dict()
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    for char in alphabet:
        char_count = lowerCaseBook.count(char)
        charDict[char] = char_count
    return charDict

def sortDictionary(charDict):
    return sorted(charDict.items(), key=lambda x: x[1], reverse=True)

def printReport(path, wordCount, charDict):
    print('--- Begin report of ' + path +' ---')
    print(str(wordCount) + ' words found in the document \n')
    for item in charDict:
        print('The \'' + item[0] + '\' character was found ' + str(item[1]) +' times')
    print('--- End report ---')

if __name__ == "__main__":
    main()