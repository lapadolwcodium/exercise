def slices(series, length):
    data_list = []

    for ind in range(len(series) - length + 1):
        data_list.append([int(data) for data in series[ind:ind + length]])

    return data_list
