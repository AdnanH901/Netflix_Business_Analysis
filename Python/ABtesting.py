# Load the necessary libraries
import numpy as np
import pandas as pd
from scipy.stats import ttest_ind, chi2_contingency
import matplotlib.pyplot as plt

# Set random seed for reproducibility

# Load the consumer data
df = pd.read_csv("consumer_data.csv")

# Define Netflix's default pricing conditions and values
conditions = [
    df['subscription_plan'] == 'Standard (with adverts)',
    df['subscription_plan'] == 'Standard',
    df['subscription_plan'] == 'Premium'
]

pricing_values = [5.99, 12.99, 18.99]

df["group"] = np.random.choice(['A', 'B'], size=len(df), p=[0.5, 0.5])  # A/B groups
df['monthly_revenue'] = np.select(conditions, pricing_values, default=0) # Monthly revenue per customer
df["churn_status"] = np.where(df['subscription_end_date'].isnull(), 0, 1)

# Remove unnecessary columns.
df = df[["customer_id", "age", "country", "subscription_plan", "monthly_revenue", "group", "churn_status"]]
print(df.head())

# Define annual prices 
discount = 0.8 # Assuming a 10% discount for annual plans
annual_prices = {
    "Standard (with adverts)": pricing_values[0] * 12 * discount,
    "Standard": pricing_values[1] * 12 * discount,
    "Premium": pricing_values[2] * 12 * discount
}

# Simulate annual plan adoption (30% of Group B customers switch)
df['annual_plan'] = np.where((df['group'] == 'B') & (np.random.rand(len(df)) < 0.4), 1, 0)

# Adjust revenue for those in the annual plan (spread over 12 months)
df['simulated_revenue'] = np.where(df['annual_plan'] == 1, 
                                   df['subscription_plan'].map(annual_prices) / 12,  
                                   df['monthly_revenue'])

# Calculate churn rates per group
churn_rates = df.groupby('group')['churn_status'].mean()
print("Churn Rates:\n", churn_rates)

# Churn rate for annual vs. monthly users in Group B
churn_by_plan = df[df['group'] == 'B'].groupby('annual_plan')['churn_status'].mean()
print("\nChurn by Plan in Group B:\n", churn_by_plan)

# Calculate ARPU per group
arpu_comparison = df.groupby('group')['simulated_revenue'].mean()
print("\nARPU Comparison:\n", arpu_comparison)

# Perform T-test on revenue
t_stat, p_value = ttest_ind(df[df['group'] == 'A']['monthly_revenue'], 
                            df[df['group'] == 'B']['simulated_revenue'])
print(f"\nT-test result: t={t_stat}, p={p_value}")

# Perform Chi-square test on churn
churn_table = df.pivot_table(index='group', columns='churn_status', aggfunc='size', fill_value=0)
chi2, p, dof, expected = chi2_contingency(churn_table)
print(f"\nChi-square test: chi2={chi2}, p={p}")

# Visualization
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Bar chart for churn rates
churn_rates.plot(kind='bar', ax=axes[0], color=['blue', 'orange'])
axes[0].set_title('Churn Rate by Group')
axes[0].set_ylabel('Churn Rate')
axes[0].set_xticklabels(['Monthly Rate Group', 'Yearly Rate Group'], rotation=0)

# Bar chart for ARPU comparison
arpu_comparison.plot(kind='bar', ax=axes[1], color=['blue', 'orange'])
axes[1].set_title('ARPU by Group')
axes[1].set_ylabel('Average Revenue per User')
axes[1].set_xticklabels(['Monthly Rate Group', 'Yearly Rate Group'], rotation=0)

plt.tight_layout()
plt.show()
