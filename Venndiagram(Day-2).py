import matplotlib.pyplot as plt
from matplotlib_venn import venn2
import numpy as np

def create_venn_diagram():
    # Define two sets
    set_A = {1, 2, 3, 4, 5}
    set_B = {4, 5, 6, 7, 8}
    
    # Calculate union
    union_set = set_A | set_B
    
    # Calculate intersection
    intersection = set_A & set_B
    
    # Create Venn diagram
    plt.figure(figsize=(10, 6))
    venn2([set_A, set_B], 
          set_labels=('Set A', 'Set B'),
          set_colors=('skyblue', 'lightgreen'))
    
    # Add title
    plt.title('Venn Diagram showing Union of Two Sets\n' + 
              f'Set A = {set_A}\nSet B = {set_B}\n' +
              f'Union = {union_set}')
    
    # Print calculations
    print(f"Set A: {set_A}")
    print(f"Set B: {set_B}")
    print(f"Union: {union_set}")
    print(f"Intersection: {intersection}")
    print(f"\nNumber of elements in:")
    print(f"Set A: {len(set_A)}")
    print(f"Set B: {len(set_B)}")
    print(f"Union: {len(union_set)}")
    print(f"Intersection: {len(intersection)}")
    
    plt.show()

if __name__ == "__main__":
    create_venn_diagram()
