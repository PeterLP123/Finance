#MT322S - Assignment 4 - Question 2 
import numpy as np

payoff_matrix_game = np.array([
    [-4, 6, -4, 1],
    [5, -7, 3, 8],
    [-8, 0, 6, -2]
])

mixed_strategy_A = np.array([1/2, 0, 1/2])
mixed_strategy_B = np.array([1/4, 1/4, 1/4, 1/4])

def calculate_expected_payoff(payoff_matrix, strategy_A, strategy_B):
    return np.dot(strategy_A, np.dot(payoff_matrix, strategy_B))

expected_payoff = calculate_expected_payoff(payoff_matrix_game, mixed_strategy_A, mixed_strategy_B)

print("The expected payoff for player A is {}".format(expected_payoff))

expected_payoff_pure_strategies_A = np.dot(payoff_matrix_game, mixed_strategy_B)

print("The expected payoff for player A's pure strategies are {}".format(expected_payoff_pure_strategies_A))

best_response_A = np.argmax(expected_payoff_pure_strategies_A)

(expected_payoff, expected_payoff_pure_strategies_A, best_response_A)

print("The best response for player A is to play strategy {}".format(best_response_A))