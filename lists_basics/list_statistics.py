num = int(input())
positives = list()
negatives = list()

for i in range(num):
    number = int(input())
    if number < 0:
        negatives.append(number)
    else:
        positives.append(number)
print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negatives)}")
