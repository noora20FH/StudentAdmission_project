import numpy as np
from scipy.stats import rankdata


def calculate_ranks(decision_matrix, criteria_types, weights):
    # Step 1: Create the decision matrix
    print("Decision Matrix:")
    print(decision_matrix)

    # Step 2: Normalize the decision matrix and get max and min values for each criterion
    max_values = np.amax(decision_matrix, axis=0)
    min_values = np.amin(decision_matrix, axis=0)

    normalized_matrix = np.zeros(decision_matrix.shape)
    for i in range(decision_matrix.shape[1]):
        if criteria_types[0, i] == "Cost":
            normalized_matrix[:, i] = (max_values[i] - decision_matrix[:, i]) / (max_values[i] - min_values[i])
        else:
            normalized_matrix[:, i] = (decision_matrix[:, i] - min_values[i]) / (max_values[i] - min_values[i])

    print("Normalized Matrix:")
    print(normalized_matrix)


    # Step 3: Calculate the weighted normalized decision matrix for the decision maker
    normalized_weights = weights / np.sum(weights)

    weighted_matrix = (normalized_matrix *
                       normalized_weights) + normalized_weights

    print("Weighted Normalized Matrix:")
    print(weighted_matrix)

    # Step 4: Calculate the approximate boundary area matrix (G)
    product = 1
    for i in range(weighted_matrix.shape[0]):
        product *= weighted_matrix[i]
    G = product ** (1 / weighted_matrix.shape[0])

    print("G:")
    print(G)

    # Step 5: Calculate the alternative distance matrix from the approximate boundary area (Q)
    Q = weighted_matrix - G.reshape(1, -1)

    print("Q:")
    print(Q)

    # Step 6: Calculate the alternative rankings
    S = np.sum(Q, axis=1)

    # Calculate the ranks using scipy.stats.rankdata with the 'min' method for ties
    ranks = rankdata(-S, method='min')

    # Create a list of alternatives with their corresponding ranks
    alternatives = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8']
    alternative_rankings = [(alt, rank)
                            for alt, rank in zip(alternatives, ranks)]

    return alternative_rankings


# Decision Matrix:
decision_matrix = np.array([
    [5, 2, 5, 1, 1],
    [4, 1, 5, 4, 2],
    [3, 3, 5, 2, 2],
    [2, 1, 5, 5, 2],
    [4, 3, 2, 5, 2],
    [5, 5, 1, 5, 3],
    [2, 4, 1, 2, 3],
    [2, 4, 5, 5, 2]
])

criteria_types = np.array(
    [["benefit", "benefit", "benefit", "benefit", "benefit"]])

weights = np.array([30, 20, 20, 15, 15])

result = calculate_ranks(decision_matrix, criteria_types, weights)

for alt, rank in result:
    print(f'{alt}: Rank {rank}')
