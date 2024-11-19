import random
from collections import Counter

def coin_flip():
    flips = [random.choice(['H', 'T']) for _ in range(50)]  # Simulate 50 coin flips
    count = Counter(flips)  # Count frequencies
    
    print(f"Sequence: {flips}")
    print(f"Heads: {count['H']}, Tails: {count['T']}")
    print(f"Probabilities - Heads: {count['H']/50:.2f}, Tails: {count['T']/50:.2f}")

coin_flip()
