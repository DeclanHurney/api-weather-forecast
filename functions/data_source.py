def get_local_data(days):
    dates_list = ["2025-10-09", "2025-10-10", "2025-10-11"]
    temperatures_list = [10, 11, 15]
    temperatures_list = [days * i for i in temperatures_list]
    return dates_list, temperatures_list