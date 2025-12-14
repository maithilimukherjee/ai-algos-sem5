import math

# ---------- USER INPUT ----------
num_min_nodes = int(input("enter number of min nodes (children of root): "))

GAME_TREE = []

for i in range(num_min_nodes):
    print(f"\nmin node {i+1}:")
    num_max_nodes = int(input("enter number of max nodes under this min node: "))
    min_node = []

    for j in range(num_max_nodes):
        leaf_input = input(
            f"enter leaf label-value pairs for max node {j+1} (e.g. m 6 n 4): "
        )
        tokens = leaf_input.split()
        leaf_list = []

        for k in range(0, len(tokens), 2):
            label = tokens[k]
            value = int(tokens[k + 1])
            leaf_list.append((label, value))

        min_node.append(leaf_list)

    GAME_TREE.append(min_node)

# ---------- ALPHA BETA ----------
pruned_nodes = []

def alpha_beta(node, alpha, beta, maximizing):
    # leaf
    if isinstance(node, tuple):
        return node[1]

    if maximizing:
        value = -math.inf
        for i, child in enumerate(node):
            child_value = alpha_beta(child, alpha, beta, False)
            value = max(value, child_value)
            alpha = max(alpha, value)

            # real pruning only if siblings exist
            if beta <= alpha and i < len(node) - 1:
                # children here are LEAVES
                for skipped_leaf in node[i+1:]:
                    pruned_nodes.append(skipped_leaf[0])
                break
        return value

    else:
        value = math.inf
        for i, child in enumerate(node):
            child_value = alpha_beta(child, alpha, beta, True)
            value = min(value, child_value)
            beta = min(beta, value)

            if beta <= alpha:
                break
        return value

# ---------- RUN ----------
result = alpha_beta(GAME_TREE, -math.inf, math.inf, True)

print("\nfinal optimal value at root:", result)
print("pruned nodes:", pruned_nodes)
