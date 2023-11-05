# %%
import pandas as pd
from pathlib import Path

#file to upload
budget_path = Path("/Users/staciesauer/GitHub/Python-Challenge/PyBank/Resources/budget_data.csv")

#read csv and add data to dataframe
budget_df = pd.read_csv(budget_path,encoding="utf-8")

budget_df.head()


# %%
# Calculate the number of unique authors in the DataFrame
date_count = len(budget_df["Date"].unique())

# Print the number of unique dates. 
print(date_count)

# %%
print("_________________________________________________")

# %%
#The net total amount of "Profit/Losses" over the entire period
net_total = sum(budget_df["Profit/Losses"])

#print the total amount of profit and loss
print(net_total)

# %%
print("__________________________________________________")

# %%
# The changes in "Profit/Losses" over the entire period, and then the average of those changes
profit_loss_df = budget_df["Profit/Losses"]- budget_df["Profit/Losses"].shift(1)

average_change = profit_loss_df.mean()

#print the average of the changes
print(average_change)

# %%
print("__________________________________________________")

# %%
#The greatest increase in profits (date and amount) over the entire period
greatest_increase = profit_loss_df.max()
row = profit_loss_df == profit_loss_df.max()

date_increase = budget_df.loc[row,"Date"].values[0]

#print the greatest increase in profits
print(greatest_increase)
print(date_increase)

# %%
#The greatest decrease in profits (date and amount) over the entire period

greatest_decrease = profit_loss_df.min()
row = profit_loss_df == profit_loss_df.min()

date_decrease = budget_df.loc[row,"Date"].values[0]

#print the greatest increase in profits
print(greatest_decrease)
print(date_decrease)

# %%
#output to text file
Result = [date_count,net_total,average_change,greatest_increase,date_increase,greatest_decrease,date_decrease]
result_df = pd.DataFrame(Result)

output_file = "/Users/staciesauer/GitHub/Python-Challenge/PyBank/Analysis/output.txt"
result_df.to_csv(output_file)

print("Financial Analysis")
print("_______________________")
print("Total Months :", date_count)
print("Total: $" ,net_total)
print("Average Change: $" ,average_change)
print("Greatest Increase in Profits:" ,greatest_increase, date_increase)
print("Greatest Decrease in Profits:" ,greatest_decrease, date_decrease)

# %%



