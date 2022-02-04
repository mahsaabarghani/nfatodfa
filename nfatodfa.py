def rang(list1):  # for finding ranges(0,number)
    appends = []
    counter_range = 0
    while list1:
        counter_range += 1
        if counter_range == list1:
            break
    return counter_range


nfa = {}
lamda = 'lambda'
number_states = int(input('enter number of states: ')
                    )  # number of states for nfa
print(f'ur nfa has {number_states} states !')
states = []
count_states = 0
range_states = rang(number_states)
while range_states:  # giving states of nfa
    new_states = list(input('enter ur states name:'))
    count_states += 1
    # states.append(new_states)
    states = states + new_states
    if count_states == number_states:
        break

print(f'ur nfa states are/is {states}')

# number of terminals for nfa
number_terminals = int(input('enter number of terminals: '))
range_terminals = rang(number_terminals)
terminals = [lamda]
count_terminals = 0
while range_terminals:  # giving states of nfa
    new_terminals = list(input('enter ur terminals name:'))
    count_terminals += 1
    # terminals.append(new_terminals)
    terminals = terminals + new_terminals
    if count_terminals == (number_terminals):
        break
# print(f'ur nfa terminals count is {number_terminals}')
print(f'ur nfa terminals are/is {terminals}')


start_states = []
final_states = []

for state in states:
    nfa[state] = {}

    is_start = input(f"is ({state}) start state(y/n)? : ")
    if is_start == "y":
        # start_states.append(state)
        start_states = start_states + [state]

    is_final = input(f"is ({state}) final state(y/n)? : ")
    if is_final == "y":
        # final_states.append(state)
        final_states = final_states + [state]

    for terminal in terminals:
        out = list(
            input(f"enter the output of δ({state},{terminal}) : ").split())
        nfa[state][terminal] = out

print(f'\n -------------------- \n you write this nfa : \n {nfa}')


dfa = {}
new_start_states = start_states
for state in new_start_states:
    if nfa[state][lamda] and nfa[state][lamda] not in new_start_states:
        new_start_states = list(set(new_start_states + nfa[state][lamda]))

new_states = [new_start_states, ]
new_final_states = []

for state in new_states:
    dfa[tuple(state)] = {}
    for terminal in terminals:
        if terminal == lamda:
            continue
        out_states = []
        for alphabet in state:
            if nfa[alphabet][terminal] and nfa[alphabet][terminal] not in out_states:
                out_states = list(set(out_states+nfa[alphabet][terminal]))

        for alphabet in out_states:
            if nfa[alphabet][lamda] and nfa[alphabet][lamda] not in out_states:
                out_states = list(set(out_states+nfa[alphabet][lamda]))
        dfa[tuple(state)][terminal] = out_states
        if out_states:
            if out_states not in new_states:
                # new_states.append(out_states)
                new_states = new_states + out_states
            for i in set(final_states):
                if i in set(out_states) and (out_states not in new_final_states):

                    # if (any(set(final_states) & set(out_states))) and (out_states not in new_final_states):
                    # new_final_states.append(out_states)
                    new_final_states = new_final_states + out_states


print(f"\n ----------------------- \n  ur dfa is \n {dfa} ")

print(f"\n ur dfa start state is {set(new_start_states)}  \n")
print(f"\n ur dfa final state is {set(new_final_states)} \n ")
