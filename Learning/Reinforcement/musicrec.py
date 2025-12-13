import random

# states and actions
states = ["happy", "sad"]
actions = ["pop", "lofi"]

# initialize q-table with zeros
q_table = {
    "happy": {"pop": 0, "lofi": 0},
    "sad": {"pop": 0, "lofi": 0}
}

alpha = 0.1   # learning rate
gamma = 0.9   # discount factor
epsilon = 0.2 # exploration rate

# reward function (simulated user behavior)
def get_reward(state, action):
    if state == "happy" and action == "pop":
        return 1
    if state == "sad" and action == "lofi":
        return 1
    return -1

# training loop
for episode in range(100):
    state = random.choice(states)

    # epsilon-greedy action selection
    if random.random() < epsilon:
        action = random.choice(actions)
    else:
        action = max(q_table[state], key=q_table[state].get)

    reward = get_reward(state, action)

    # q-learning update
    old_value = q_table[state][action]
    next_max = max(q_table[state].values())
    new_value = old_value + alpha * (reward + gamma * next_max - old_value)

    q_table[state][action] = new_value

print("trained q-table:")
print(q_table)
