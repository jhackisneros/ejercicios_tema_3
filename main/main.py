def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Mover piedra de {source} a {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Mover piedra de {source} a {target}")
    hanoi(n - 1, auxiliary, target, source)

def main():
    n = 74  # Número de piedras
    hanoi(n, 'Columna A', 'Columna C', 'Columna B')

if __name__ == "__main__":
    main()