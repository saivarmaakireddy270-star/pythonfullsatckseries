numbers = tuple(map(int, input().split()))
target = int(input())
print(numbers.count(target), numbers.index(target))