class Coor:
    x: int = 0
    y: int = 0

    def __str__(self):
        return f"x: {self.x} y: {self.y}"


moves = open('input.txt')
TRAIN_AMOUNT = 10

train = [Coor(), Coor(), Coor(), Coor(), Coor(),
         Coor(), Coor(), Coor(), Coor(), Coor()]
head = Coor()
tail = Coor()

tail_positions = set()
diff_pos = 1


def shift_tail():
    x_diff = head.x - tail.x
    y_diff = head.y - tail.y
    if abs(x_diff) == 2:
        tail.x += round(x_diff * 0.5)
        if abs(y_diff) == 1:
            tail.y += y_diff
    if abs(y_diff) == 2:
        tail.y += round(y_diff * 0.5)
        if abs(x_diff) == 1:
            tail.x += x_diff


def shift_tail_2():
    for i in range(1, len(train)):
        t_1 = train[i - 1]
        t_2 = train[i]

        x_diff = t_1.x - t_2.x
        y_diff = t_1.y - t_2.y
        if abs(x_diff) == 2:
            t_2.x += round(x_diff * 0.5)
            if abs(y_diff) == 1:
                t_2.y += y_diff
        if abs(y_diff) == 2:
            t_2.y += round(y_diff * 0.5)
            if abs(x_diff) == 1:
                t_2.x += x_diff


def store_pos():
    tail_positions.add((tail.x, tail.y))


def store_pos_2():
    t = train[len(train) - 1]
    tail_positions.add((t.x, t.y))


# Part 1
# for move in moves:
#     direction = move[0]
#     amount = int(move[2:])

#     for i in range(amount):
#         if direction == 'R':
#             head.x += 1
#         elif direction == 'L':
#             head.x -= 1
#         elif direction == 'U':
#             head.y += 1
#         else:
#             head.y -= 1

#         shift_tail()
#         store_pos()
# print(len(tail_positions))

# Part 2
for move in moves:
    direction = move[0]
    amount = int(move[2:])

    for i in range(amount):
        if direction == 'R':
            train[0].x += 1
        elif direction == 'L':
            train[0].x -= 1
        elif direction == 'U':
            train[0].y += 1
        else:
            train[0].y -= 1

        shift_tail_2()
        store_pos_2()

print(len(tail_positions))
