import random

# states and actions
states = ["child", "adult", "senior"]
actions = ["high_protein", "balanced", "low_carb"]

# transition model (state stays same after action)
transition_model = {
    (state, action): state
    for state in states
    for action in actions
}

# reward model
reward_model = {
    ("child", "balanced"): 1,
    ("adult", "high_protein"): 1,
    ("senior", "low_carb"): 1
}

# initialize value function
V = {state: 0 for state in states}
gamma = 0.9  # discount factor

# value iteration
for _ in range(50):
    for state in states:
        action_values = []
        for action in actions:
            next_state = transition_model[(state, action)]
            reward = reward_model.get((state, action), -1)
            action_value = reward + gamma * V[next_state]
            action_values.append(action_value)
        V[state] = max(action_values)

# derive policy
policy = {}
for state in states:
    best_action = None
    best_value = float("-inf")
    for action in actions:
        next_state = transition_model[(state, action)]
        reward = reward_model.get((state, action), -1)
        value = reward + gamma * V[next_state]
        if value > best_value:
            best_value = value
            best_action = action
    policy[state] = best_action

print("optimal diet policy:")
for state, action in policy.items():
    print(state, "->", action)
