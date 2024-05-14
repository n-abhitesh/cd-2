from collections import deque

def closure(item, grammar):
    queue = deque(item)
    closure_items = set(queue)

    while queue:
        current_item = queue.popleft()
        dot_index = current_item.index('.')
        if dot_index < len(current_item) - 1:
            next_symbol = current_item[dot_index + 1]
            if next_symbol in grammar:
                for production in grammar[next_symbol]:
                    new_item = '.' + production
                    if new_item not in closure_items:
                        closure_items.add(new_item)
                        queue.append(new_item)

    return closure_items

def goto(items, symbol, grammar):
    new_items = set()
    for item in items:
        dot_index = item.index('.')
        if dot_index < len(item) - 1 and item[dot_index + 1] == symbol:
            new_item = item[:dot_index] + symbol + '.' + item[dot_index + 2:]
            new_items.add(new_item)
    return closure(new_items, grammar)

def canonical_lr0_items(grammar):
    start_production = next(iter(grammar))
    start_item = '.' + start_production
    start_state = frozenset(closure([start_item], grammar))

    states = [start_state]
    transitions = {}

    queue = deque([(0, start_state)])
    while queue:
        state_id, state = queue.popleft()
        for symbol in grammar.keys():
            next_state = goto(state, symbol, grammar)
            if next_state:
                if next_state not in states:
                    states.append(next_state)
                    queue.append((len(states) - 1, next_state))
                transitions[(state_id, symbol)] = states.index(next_state)

    return states, transitions

# Example grammar
example_grammar = {
    'S': ['E'],
    'E': ['E + T', 'T'],
    'T': ['T * F', 'F'],
    'F': ['( E )', 'id']
}

states, transitions = canonical_lr0_items(example_grammar)

print("Canonical LR(0) Items:")
for i, state in enumerate(states):
    print(f"State {i}: {state}")

print("\nTransitions:")
for (state, symbol), next_state in transitions.items():
    print(f"State {state} --({symbol})--> State {next_state}")
