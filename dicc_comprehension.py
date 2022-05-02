from re import I


def run():

    # dicc1 = {}

    # for i in range(1,101):
    #     if i % 3 !=0:
    #         dicc1[i] = i**3
                    
    # dicc1 = {i: i**3 for i in range (1,101) if i % 3 !=0}
    dicc1 = {i: i**0.5 for i in range (1,1001) if i % 3 !=0}
    
    print(dicc1)


if __name__== '__main__':
    run()