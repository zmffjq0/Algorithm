import sys
input = sys.stdin.readline

def binarySearch(arr, start, end, value):
    if start > end:
        return 0

    mid = (start + end) // 2

    if arr[mid] < value:
        return binarySearch(arr, mid + 1, end, value)
    elif arr[mid] > value:
        return binarySearch(arr, start, mid - 1, value)
    else:
        return cardCount[value]

N = int(input())
numCards = list(map(int, input().split()))
numCards.sort()

M = int(input())
checkList = list(map(int, input().split()))

cardCount = {}
for num in numCards:
    if num in cardCount:
        cardCount[num] += 1
    else:
        cardCount[num] = 1
for card in checkList:
    print(binarySearch(numCards, 0, len(numCards) - 1, card))