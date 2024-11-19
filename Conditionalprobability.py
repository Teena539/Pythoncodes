import random

def roll_dice():
    return random.randint(1, 6)

def simulate_dice_rolls(num_trials):
    # Store results of dice rolls
    rolls = [roll_dice() for _ in range(num_trials)]
    return rolls

def calculate_conditional_probability(rolls, condition_a, condition_b):
    # Count events satisfying both conditions
    both_conditions = sum(1 for roll in rolls if condition_a(roll) and condition_b(roll))
    
    # Count events satisfying condition B
    condition_b_count = sum(1 for roll in rolls if condition_b(roll))
    
    # Calculate conditional probability: P(A|B) = P(A∩B)/P(B)
    if condition_b_count == 0:
        return 0
    return both_conditions / condition_b_count

def main():
    # Number of trials
    num_trials = 10000
    
    # Simulate dice rolls
    rolls = simulate_dice_rolls(num_trials)
    
    # Example 1: P(Even | Greater than 3)
    is_even = lambda x: x % 2 == 0
    greater_than_three = lambda x: x > 3
    
    prob_even_given_greater_than_three = calculate_conditional_probability(
        rolls, is_even, greater_than_three
    )
    
    print(f"Probability of rolling an even number given it's greater than 3: {prob_even_given_greater_than_three:.3f}")
    
    # Example 2: P(Greater than 4 | Even)
    greater_than_four = lambda x: x > 4
    
    prob_greater_than_four_given_even = calculate_conditional_probability(
        rolls, greater_than_four, is_even
    )
    
    print(f"Probability of rolling greater than 4 given it's even: {prob_greater_than_four_given_even:.3f}")

if __name__ == "__main__":
    main()
