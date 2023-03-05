# A calculator to calculate how much I will earn when I invest in a Vanguard Cash Reserves Federal Money Market Fund Admiral Share (VMRXX)
monthEndReturn = 0.0035  # 0.35% as of 3March2023
compoundYield = 0.0461  # 4.61% as of 3March2023
expenseRatio = 0.001  # 0.10% as of 3March2023

initialInvestment = float (input ("Enter your initial investment: $"))

# Calculate the return after one year
oneYearReturn = (1 + monthEndReturn) * (1 + compoundYield) - 1

# Calculate the return after deducting the expense ratio
netReturn = oneYearReturn - expenseRatio

# Calculate the final balance after one year
finalBalance = initialInvestment * (1 + netReturn)

# Print the final balance
print (f"Your final balance after one year will be ${finalBalance:.2f}")
