def numComperor(num1, num2):
    return abs(num2-num1)

def collectionComperor(col1, col2):
    return len(col1 & col2) / len(col1 | col2)