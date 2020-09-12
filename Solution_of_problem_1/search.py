# List Searching
# Author: Farzana Bulbul
# Date: 10 Sep 2020
def search(my_list, target):
    indx1 = 0
    indx2 = 0
    for i in range(len(my_list)):
        if int(my_list[i]) == target:
            indx1 = i
            for j in range(indx1, len(my_list)):
                if int(my_list[j]) == target:
                    indx2 = j
            break
    result = [indx1, indx2]
    print(result)


my_list = input("Enter a list elements separated by space: ")
my_list = my_list.split()

target = int(input("Enter target value: "))

search(my_list, target)
