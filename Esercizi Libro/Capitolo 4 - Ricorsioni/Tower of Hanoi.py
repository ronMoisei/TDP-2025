# Initial towers: peg A has disks [5,4,3,2,1], B and C are empty
towers = [
    [5, 4, 3, 2, 1],  # A
    [],               # B
    []                # C
]
pegs = ['A', 'B', 'C']

def print_towers():
    print(' | '.join(f"{pegs[i]}: {towers[i]}" for i in range(3)))

def hanoi(n: int, src: int, dst: int, aux: int) -> None:
    if n == 0:
        return
    # move n-1 disks from src to aux
    hanoi(n - 1, src, aux, dst)
    # move disk
    disk = towers[src].pop()
    towers[dst].append(disk)
    print(f"Move disk {disk} from {pegs[src]} to {pegs[dst]}")
    print_towers()
    # move n-1 disks from aux to dst
    hanoi(n - 1, aux, dst, src)

# Demonstration
print("Initial state:")
print_towers()
hanoi(5, 0, 2, 1)  # move 5 disks from A(0) → C(2) using B(1)
