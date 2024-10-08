"""
Gossip Algorithm
@H. Chakraa
"""
import numpy as np

def gossip_algorithm(scenario, max_iterations):

    # Get a random solution
    current_solution = scenario.generate_random_solution()
    
    # Compute the initial cost
    current_cost = scenario.compute_solution_cost(current_solution)
    
    # Lists to track costs over time
    improved_solution_costs = [current_cost]    # Costs when a better solution is found
    gossip_iteration_costs = [current_cost]    # Costs after each gossip iteration
    
    # Get the possible robot pairs that can exchange tasks
    robot_pairs = scenario.select_compatible_robots()
    
    iteration = 1  # Track iterations for stopping criteria
    iteration_s = 1  # Track iterations for solution equilibrium
    equilibrium = 0
        
    while iteration < max_iterations:
        # Shuffle the robot pairs randomly
        np.random.shuffle(robot_pairs)
        
        for pair in robot_pairs: 
                
            # Apply the gossip mechanism between the selected pair of robots
            new_solution = scenario.task_exchange_mechanism(current_solution, pair)
                
            # Compute the cost for the newly obtained solution
            new_cost = scenario.compute_solution_cost(new_solution)
            gossip_iteration_costs.append(new_cost)
                
            # If the new solution is worse or the same, increment the iteration count
            if new_cost >= current_cost:
                iteration += 1
                iteration_s += 1
            else:
                # If a better solution is found, reset the iteration count
                iteration = 1
                equilibrium = iteration_s
                
                # Update to the better solution
                current_solution = new_solution
                
                # Apply TSP algorithm for the pair
                #current_solution[pair[0]-1] = scenario.branch_and_bound_tsp(current_solution[pair[0]-1])
                #current_solution[pair[1]-1] = scenario.branch_and_bound_tsp(current_solution[pair[1]-1])
                
                current_cost = scenario.compute_solution_cost(current_solution)
                
                # Track the improved solution's cost
                improved_solution_costs.append(current_cost)
    
    return current_solution, improved_solution_costs, equilibrium, gossip_iteration_costs
