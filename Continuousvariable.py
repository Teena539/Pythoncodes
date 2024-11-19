import random
from datetime import datetime, timedelta

# Generate 8 temperature readings for a day
times = [datetime.now() + timedelta(hours=3*i) for i in range(8)]
temperatures = [round(random.uniform(15, 30), 1) for _ in range(8)]

print("Today's Weather Report:")
print("-" * 40)
for time, temp in zip(times, temperatures):
    print(f"Time: {time.strftime('%H:%M')} - Temperature: {temp}°C")

print(f"\nSummary:")
print(f"Highest Temperature: {max(temperatures)}°C")
print(f"Lowest Temperature: {min(temperatures)}°C")
print(f"Average Temperature: {sum(temperatures)/len(temperatures):.1f}°C")
