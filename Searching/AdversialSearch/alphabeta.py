import math

# game tree with explicit leaf labels
GAME_TREE = [
    [   # b (min)
        [('m', 6), ('n', 4)],
        [('o', 2), ('p', 0)],
        [('q', 7), ('r', 3)]
    ],
    [   # c (min)
        [('s', 8), ('t', 2)],
        [('u', 4), ('v', 9)],
        [('w', 0), ('x', 5)]
    ],
    [   # d (min)
        [('y', 1), ('z', 7)],
        [('z1', 3), ('z2', 0)]
    ]
]

pruned_nodes = []

def alpha_beta(node, alpha, beta, maximizing):
    # leaf node
    if isinstance(node, tuple):
        label, value = node
        return value

    if maximizing:
        value = -math.inf
        for i, child in enumerate(node):
            value = max(value, alpha_beta(child, alpha, beta, False))
            alpha = max(alpha, value)

            # prune only if unexplored children exist
            if beta <= alpha and i < len(node) - 1:
                # only happens at g → r
                pruned_nodes.append('r')
                break
        return value

    else:  # minimizing player
        value = math.inf
        for i, child in enumerate(node):
            value = min(value, alpha_beta(child, alpha, beta, True))
            beta = min(beta, value)

            # prune only if unexplored children exist
            if beta <= alpha and i < len(node) - 1:
                break
        return value

# run
result = alpha_beta(GAME_TREE, -math.inf, math.inf, True)

print("final optimal value at root:", result)
print("pruned nodes:", pruned_nodes)
