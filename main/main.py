def hanoi(n, source, target, auxiliary):
    if n == 1:
        print(f"Mover disco de {source} a {target}")
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Mover disco de {source} a {target}")
    hanoi(n - 1, auxiliary, target, source)

def main():
    n = 3  # Número de discos
    hanoi(n, 'A', 'C', 'B')

if __name__ == "__main__":
    main()