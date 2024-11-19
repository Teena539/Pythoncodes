def calculate_set_union():
    # Define two sets
    set_A = {1, 2, 3, 4, 5}
    set_B = {4, 5, 6, 7, 8}
    
    # Calculate union using | operator
    union_set = set_A | set_B
    
    # Alternative way using union() method
    # union_set = set_A.union(set_B)
    
    # Calculate probabilities
    total_elements = len(union_set)
    prob_A = len(set_A) / total_elements
    prob_B = len(set_B) / total_elements
    prob_union = len(union_set) / total_elements
    
    # Print results
    print(f"Set A: {set_A}")
    print(f"Set B: {set_B}")
    print(f"Union of A and B: {union_set}")
    print("\nProbabilities:")
    print(f"P(A) = {prob_A:.3f}")
    print(f"P(B) = {prob_B:.3f}")
    print(f"P(A ∪ B) = {prob_union:.3f}")

if __name__ == "__main__":
    calculate_set_union()
