import numpy as np

transactions = np.array([
    [120, 150, 160, 180, 200, 210],
    [100, 110, 115, 130, 140, 150],
    [90, 95, 100, 110, 120, 130],
    [200, 210, 220, 230, 250, 270]
])
print("Transaction Array:\n", transactions)

total_per_branch = transactions.sum(axis=1)
print("\nTotal per branch:", total_per_branch)

highest_branch = np.argmax(total_per_branch)
print("\nBranch with highest transactions: Branch", highest_branch + 1)

avg_monthly = transactions.mean()
print("\nAverage monthly transaction volume:", avg_monthly)

reshaped = transactions.reshape(3, 8)
print("\nReshaped array (3x8):\n", reshaped)
print("\nImplication: Reshaping changes structure, not data.")
f
