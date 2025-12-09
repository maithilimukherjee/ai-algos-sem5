def depth_limited_search(problem, limit):
    """
    Depth-Limited Search (DLS).
    Returns: solution path, "failure", or "cutoff".
    """
    return recursive_dls((problem.INITIAL_STATE, [], 0), problem, limit)


def recursive_dls(node, problem, limit):
    state, path, depth = node

    # Goal test
    if problem.GOAL_TEST(state):
        return path

    # Cutoff if depth limit reached
    elif limit == 0:
        return "cutoff"

    else:
        cutoff_occurred = False
        for action in problem.ACTIONS(state):
            child_state, _ = problem.CHILD_NODE(state, action)
            child_path = path + [action]

            result = recursive_dls((child_state, child_path, depth + 1), problem, limit - 1)

            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return result

        return "cutoff" if cutoff_occurred else "failure"


def iterative_deepening_search(problem):
    """
    Iterative Deepening Search (IDS).
    Repeatedly applies DLS with increasing depth limits until a solution is found.
    """
    depth = 0
    while True:
        result = depth_limited_search(problem, depth)
        if result != "cutoff":
            return result
        depth += 1


class GraphProblem:
    def __init__(self):
        self.INITIAL_STATE = 'A'
        self.goal = 'G'
        self.graph = {
            'A': ['B', 'C'],
            'B': ['D', 'E'],
            'C': ['F'],
            'D': [],
            'E': ['G'],
            'F': [],
            'G': []
        }

    def GOAL_TEST(self, state):
        return state == self.goal
    def ACTIONS(self, state):
        return self.graph.get(state, [])
    def CHILD_NODE(self, state, action):
        return action, None  # In this simple graph, the action is the child state itself
        