import matplotlib.pyplot as plt
import pandas as pd

# Example DataFrame (replace with your actual df)
data = {
    'Bad': [5, 10, 20, 40, 60, 80, 100],
    'Good': [10, 25, 45, 70, 85, 95, 100]
}
df = pd.DataFrame(data)
df.index = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

# KS Chart
plt.figure(figsize=(10, 5))
plt.plot(df.index.astype(str), df['Bad'], label='Cumulative Bad Rate (%)', linestyle='--', color='red')
plt.plot(df.index.astype(str), df['Good'], label='Cumulative Good Rate (%)', linestyle='--', color='blue')

plt.xlabel("Score - Buckets")
plt.ylabel("Cumulative %")
plt.title("KS")
plt.legend()
plt.grid(True)
plt.xticks(rotation=80, ha='right')
plt.show()

