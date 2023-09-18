def maxmin(array):
    maxmin_array = []
    array.sort()
    maxmin_array.append(array[0])
    maxmin_array.append(array[len(array) - 1])
    print(maxmin_array)

array = [2,4,1,0,2,-1]
maxmin(array)
