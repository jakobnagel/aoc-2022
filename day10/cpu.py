X = 1

cycle_count = 0

opp_cycles = {
    "noop": 1,
    "addx": 2
}

signal_strengths = []

with open('input.txt') as file:
    for line in file.readlines():
        split_line = line.split(' ')
        opp = split_line[0].strip()
        param = int(split_line[1]) if len(split_line) >= 2 else None

        for _ in range(opp_cycles[opp]):
            cycle_count += 1

            sprite = range(X, X + 3)
            if cycle_count % 40 in sprite:
                print("#", end="")
            else:
                print(".", end="")

            if (cycle_count % 40 == 0):
                print()

            if (cycle_count + 20) % 40 == 0 and cycle_count <= 220:
                signal_strengths.append(X * cycle_count)

        if opp == 'addx':
            X += param

print(sum(signal_strengths))
