def createTargetArray(arr, idx):
    target = list()

    for i,j in zip(arr,idx):
        target.insert(j,i)
    
    return target