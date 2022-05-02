def divisors(num):
    try:
        if num < 0:
            raise ValueError("ingresa un número positvo")
        divisors =[i for i in range(1, num + 1) if num % i == 0]
        return divisors
    except ValueError as ve:
        print(ve)
        return False

    # divisors =[]
    # for i in range(1, num+1):
    #     if num % i == 0:
    #         divisors.append(i)
    # return divisors


def run():
    try: 
        num = int(input(f'Ingresa un número: '))      
        print(divisors(num))
        print("Termino mi programa")
    except ValueError:
        print("Ingresa un número")
    
if __name__ =='__main__':
    run()