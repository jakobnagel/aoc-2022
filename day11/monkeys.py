from typing import List


class Item:
    worry: int

    def __init__(self, starting_worry):
        self.worry = starting_worry

    def relief(self):
        self.worry = self.worry % 9699690


class Monkey:
    items: List[Item]
    items_inspected = 0
    operation: lambda a: int
    test_func: lambda a: bool
    pass_monkey: 'Monkey'
    fail_monkey: 'Monkey'

    def __init__(self, starting_items, operation, test):
        self.items = starting_items
        self.operation = operation
        self.test_func = test

    def inspect(self):
        item = self.items[0]
        item.worry = self.operation(item.worry)
        self.items_inspected += 1

    def test(self):
        return self.test_func(self.items[0].worry)

    def throw(self, test):
        if test:
            self.pass_monkey.items.append(self.items.pop(0))
        else:
            self.fail_monkey.items.append(self.items.pop(0))

    def has_item(self):
        return len(self.items) >= 1


# Load
monkeys = [
    Monkey([Item(57)], lambda old: old * 13, lambda worry: worry % 11 == 0),
    Monkey([Item(58), Item(93), Item(88), Item(81), Item(72), Item(73),
           Item(65)], lambda old: old + 2, lambda worry: worry % 7 == 0),
    Monkey([Item(65), Item(95)], lambda old: old +
           6, lambda worry: worry % 13 == 0),
    Monkey([Item(58), Item(80), Item(81), Item(83)],
           lambda old: old * old, lambda worry: worry % 5 == 0),
    Monkey([Item(58), Item(89), Item(90), Item(96), Item(55)],
           lambda old: old + 3, lambda worry: worry % 3 == 0),
    Monkey([Item(66), Item(73), Item(87), Item(58), Item(62), Item(67)],
           lambda old: old * 7, lambda worry: worry % 17 == 0),
    Monkey([Item(85), Item(55), Item(89)],
           lambda old: old + 4, lambda worry: worry % 2 == 0),
    Monkey([Item(73), Item(80), Item(54), Item(94),
           Item(90), Item(52), Item(69), Item(58)], lambda old: old + 7, lambda worry: worry % 19 == 0)
]

# Test
# monkeys = [
#     Monkey([Item(57)], lambda old: old * 13, lambda worry: worry % 13 == 0),
#     Monkey([Item(1)], lambda old: old + 1, lambda worry: worry % 2 == 0)
# ]

# monkeys[0].pass_monkey = monkeys[1]
# monkeys[0].fail_monkey = monkeys[1]
# monkeys[1].pass_monkey = monkeys[0]
# monkeys[1].fail_monkey = monkeys[0]

# Load passing monkeys
monkeys[0].pass_monkey = monkeys[3]
monkeys[0].fail_monkey = monkeys[2]
monkeys[1].pass_monkey = monkeys[6]
monkeys[1].fail_monkey = monkeys[7]
monkeys[2].pass_monkey = monkeys[3]
monkeys[2].fail_monkey = monkeys[5]
monkeys[3].pass_monkey = monkeys[4]
monkeys[3].fail_monkey = monkeys[5]
monkeys[4].pass_monkey = monkeys[1]
monkeys[4].fail_monkey = monkeys[7]
monkeys[5].pass_monkey = monkeys[4]
monkeys[5].fail_monkey = monkeys[1]
monkeys[6].pass_monkey = monkeys[2]
monkeys[6].fail_monkey = monkeys[0]
monkeys[7].pass_monkey = monkeys[6]
monkeys[7].fail_monkey = monkeys[0]


for _ in range(10000):
    print(10000 - _)
    for monkey in monkeys:
        while monkey.has_item():
            monkey.inspect()
            monkey.items[0].relief()
            monkey.throw(monkey.test())


sorted_monkeys = sorted(monkeys, key=lambda m: m.items_inspected, reverse=True)
print(sorted_monkeys[0].items_inspected * sorted_monkeys[1].items_inspected)
