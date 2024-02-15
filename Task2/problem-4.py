if __name__ == '__main__':
    N = int(input())
    The_list = []
    for _ in range(N):
        arr = input().split()
        if arr[0] == "insert":
            The_list.insert(int(arr[1]), int(arr[2]))
        elif arr[0] == "print":
            print(The_list)
        elif arr[0] == "remove":
            The_list.remove(int(arr[1]))
        elif arr[0] == "append":
            The_list.append(int(arr[1]))
        elif arr[0] == "sort":
            The_list.sort()
        elif arr[0] == "pop":
            The_list.pop()
        elif arr[0] == "reverse":
            The_list.reverse()
    print(The_list)