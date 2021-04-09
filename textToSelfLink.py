# this file is for making a self contained link
# you can generate self indicated markdown link from any string

def stringToLink(convertableString):
    convertableString = convertableString.replace(" ", "-")
    if convertableString[0]=='-':
        list1 = list(convertableString)
        list1[0]='#'
        return ''.join(list1).lower()
    else:
        return '#'+convertableString.lower()
    
if __name__ == "__main__":
    while True:
        convertableString = input("Enter the string: ")
        print(stringToLink(convertableString))