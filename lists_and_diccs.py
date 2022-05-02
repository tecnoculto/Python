from multiprocessing.sharedctypes import Value


def run():
    my_list = [1, "hello", True, 5.5]
    my_dicc = {"firstname": "Ricardo", "lastname": "Velazquez"}

    super_list = [
        {"firstname": "Ricardo", "lastname": "Velazquez"},
        {"firstname": "Juan", "lastname": "Perez"},
        {"firstname": "Alicia", "lastname": "Acosta"},
        {"firstname": "Gabriel", "lastname": "Cordova"},
        {"firstname": "Mariana", "lastname": "Hernández"},
    ]

    super_dicc = {
        "natural_nums": [1, 2, 3, 4, 5,],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 3.5, 5.5, 6.43]
    }

    # for key, value in super_list.items():
    #     print(key, "-", value)

    # for values  in super_list:
    #     for key, value in values.items():
    #         print(f'{key} - {value}')

    for item in super_list:
        print(item["firstname"] , "-" , item["lastname"])

if __name__ == '__main__':
    run()