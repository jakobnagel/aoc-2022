import functools

f = open('input.txt')

# Load trees
trees = []  # [row, column]
for line in f:
    row = []
    for tree in line:
        if (tree == '\n'):
            break
        row.append(int(tree))
    trees.append(row)


# Part 1
visible_trees = 0
for row_num in range(len(trees)):
    for col_num in range(len(trees[row_num])):
        tree_height = trees[row_num][col_num]
        # Checks left visibility
        for col2 in range(col_num):
            left_tree_height = trees[row_num][col2]

            if tree_height <= left_tree_height:
                break
        else:
            visible_trees += 1
            continue

        # Checks right visibility
        for col2 in range(col_num + 1, len(trees[row_num])):
            right_tree_height = trees[row_num][col2]

            if tree_height <= right_tree_height:
                break
        else:
            visible_trees += 1
            continue

        # Checks up visibility
        for row2 in range(row_num):
            top_tree_height = trees[row2][col_num]

            if tree_height <= top_tree_height:
                break
        else:
            visible_trees += 1
            continue

        # Checks down visibility
        for row2 in range(row_num + 1, len(trees)):
            bottom_tree_height = trees[row2][col_num]

            if tree_height <= bottom_tree_height:
                break
        else:
            visible_trees += 1
            continue
    else:
        tree_visible = False

print(visible_trees)

# Part 2
highest_score = 0
for row_num in range(len(trees)):
    for col_num in range(len(trees[row_num])):
        tree_height = trees[row_num][col_num]
        trees_seen = [0] * 4
        # Checks left visibility
        for col2 in range(col_num - 1, -1, -1):
            left_tree_height = trees[row_num][col2]

            trees_seen[0] += 1
            if tree_height <= left_tree_height:
                break

        # Checks right visibility
        for col2 in range(col_num + 1, len(trees[row_num])):
            right_tree_height = trees[row_num][col2]

            trees_seen[1] += 1
            if tree_height <= right_tree_height:
                break

        # Checks up visibility
        for row2 in range(row_num - 1, -1, -1):
            top_tree_height = trees[row2][col_num]

            trees_seen[2] += 1
            if tree_height <= top_tree_height:
                break

        # Checks down visibility
        for row2 in range(row_num + 1, len(trees)):
            bottom_tree_height = trees[row2][col_num]

            trees_seen[3] += 1

            if tree_height <= bottom_tree_height:
                break

        tree_score = functools.reduce(lambda a, b: a * b, trees_seen)

        if tree_score > highest_score:
            highest_score = tree_score

print(highest_score)
