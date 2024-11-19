import random

def calculate_dice_probability():
    # Number of trials
    trials = 1000
    favorable = 0
    
    # Let's calculate P(Even | Greater than 3)
    for _ in range(trials):
        roll = random.randint(1, 6)
        
        # Check if number is greater than 3 (condition)
        if roll > 3:
            # Check if number is even (event we're interested in)
            if roll % 2 == 0:
                favorable += 1
    
    # Count total numbers greater than 3
    total_greater_than_3 = len([x for x in range(4, 7)])  # 4,5,6
    # Count even numbers greater than 3
    even_greater_than_3 = len([x for x in range(4, 7) if x % 2 == 0])  # 4,6
    
    # Theoretical probability
    theoretical_prob = even_greater_than_3 / total_greater_than_3
    
    print(f"Theoretical Probability: {theoretical_prob}")  # Should be 2/3 ≈ 0.667

if __name__ == "__main__":
    calculate_dice_probability()
