def clean_data(data):
    data_clean = [x.split("\n")[0] for x in data]
    return data_clean