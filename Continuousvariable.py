import random
from datetime import datetime, timedelta

# Starting temperature
current_temp = 20  # Start at 20°C

# Generate 24 hourly readings (one full day)
times = [datetime.now() + timedelta(hours=i) for i in range(24)]
temperatures = []

# Generate temperatures with smooth transitions
for i in range(24):
    # Change temperature by small random amount (between -1 and +1)
    change = random.uniform(-1, 1)
    current_temp = current_temp + change
    
    # Keep temperature within realistic range (15-30°C)
    if current_temp > 30:
        current_temp = 30
    if current_temp < 15:
        current_temp = 15
        
    temperatures.append(round(current_temp, 1))

# Print the weather report
print("24-Hour Weather Report:")
print("-" * 40)
for time, temp in zip(times, temperatures):
    print(f"Time: {time.strftime('%H:%M')} - Temperature: {temp}°C")

print(f"\nSummary:")
print(f"Highest Temperature: {max(temperatures)}°C")
print(f"Lowest Temperature: {min(temperatures)}°C")
print(f"Average Temperature: {sum(temperatures)/len(temperatures):.1f}°C")
