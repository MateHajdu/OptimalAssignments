def OptimalAssignments(raw_input=["(13,4,7,6)","(1,11,5,4)","(6,7,2,8)","(1,3,5,9)"]):
    
    # function to prepare the permutations from an iterable
    def permutations(items):
        if len(items) < 1:
            yield []
        else:
            for fixed in range(len(items)):
                for perm in permutations(items[:fixed] + items[fixed+1:]):
                    yield [items[fixed]] + perm
                
    # constructing array from string input
    cost_matrix = [[int(number) for number in element[1:-1].split(',')] for element in raw_input]
    
    # initialize variables storing the winner cost and setup
    win_cost, win_setup = float('Inf'), []
    
    # try all the permutations for machine-task setups and store the best with lowest cost
    for perm in permutations(list(range(len(cost_matrix)))):
        sumy = 0
        setup = []
        for machine,task in enumerate(list(perm)):
            sumy += cost_matrix[machine][task]
            setup.append(task)
        if sumy < win_cost:
            win_cost, win_setup = sumy, setup
            
    # convert the result into desired format
    output = ''
    for machine, task in enumerate(win_setup):
        output += '('+str(machine+1)+'-'+str(task+1)+')'
    return output