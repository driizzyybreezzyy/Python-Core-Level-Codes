x = int(input("Enter the number of lists: "))
list_l = []
for i in range(x):
    leng = int(input(f"Enter the nunmber of elements for list {i+1}: "))
    list_l.append(leng)

lists = []
for i in range(x):
    ele = []
    print(f"Enter elements for list {i+1}:")
    for j in range(list_l[i]):
        ele_buf = int(input())
        ele.append(ele_buf)
    lists.append(ele)

def cal_func(*args):
    if len(args) == 1:
        print(args[0])
    elif len(args) == 2:
        concat_l = args[0] + args[1]
        print("\n",concat_l)
        print(f"Maximum element: {max(concat_l)}")
        print(f"Minimum element: {min(concat_l)}")
    elif len(args) == 3:
        concat_l = args[0] + args[1] + args[2]
        print("\n",concat_l)
        print(f"Sum of all elements: {sum(concat_l)}")
    else:
        concat_l = []
        for pt1 in args:
            concat_l += pt1
        squared_elements = list(map(lambda x: x**2, concat_l))
        odd_numbers = list(filter(lambda x: x % 2 != 0, squared_elements))
        print("\n",concat_l)
        print(f"Squared elements: {squared_elements}")
        print(f"Odd numbers: {odd_numbers}")

if x == 1:
    cal_func(lists[0])
elif x == 2:
    cal_func(lists[0], lists[1])
elif x == 3:
    cal_func(lists[0], lists[1], lists[2])
else:
    cal_func(*lists)