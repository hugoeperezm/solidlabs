def main():
    fruit = input("Que fruta desea validar?")
    validafruta = isRedFruit(fruit)
    print(f"La fruta {fruit} se valida como {validafruta}")

def isRedFruit_bad(fruit):
    if fruit == 'manzana' or fruit == 'cereza' or fruit == 'ciruela':
        return True
    else: 
        return False


def isRedFruit(fruit):
    redFruits = ['manzana', 'cereza', 'ciruela']
    return fruit in redFruits

if __name__ == "__main__":
    main()