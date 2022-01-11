def replaceElements(arr):
    output =[]

    for i in range(len(arr)-1):
        output.append(max(arr[i+1:]))

    output +=[-1]


    return output