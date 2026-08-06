def impar_par(n):
    if n % 2 != 0:
        print("Número ímpar.")
    else:
        print("Número par.")


def main():
    n = int(input("Digite um número: "))
    
    impar_par(n)


if __name__ == "__main__":
    main()
        
