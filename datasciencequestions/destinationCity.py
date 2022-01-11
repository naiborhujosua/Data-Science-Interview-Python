def destinationCity(paths):
    # if there is no outgoing path then it will be the destination city
    start =set([path[0] for path in paths])
    end = set([path[1] for path in paths])

    return list(end-start)[0]
    

