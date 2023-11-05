# %%
import pandas as pd
from pathlib import Path

#file to upload
election_path = Path("/Users/staciesauer/GitHub/Python-Challenge/PyPoll/Resources/election_data.csv")

#read csv and add data to dataframe
election_df = pd.read_csv(election_path,encoding="utf-8")

election_df.head()


# %%
# The total number of votes cast
vote_count = len(election_df["Ballot ID"].unique())

# Print the number of unique votes. 
print(vote_count)

# %%
print("_________________________________________________")

# %%
#A complete list of candidates who received votes
candidate_vote = election_df["Candidate"].unique()

#print the candidates who recieved votes
print(candidate_vote)

# %%
print("__________________________________________________")

# %%
#remove the county column
del election_df["County"]

#The total number of votes each candidate won
candidate_vote_df = election_df.groupby(["Candidate"])

#print the df
candidate_vote_df.count().head()


# %%
print("__________________________________________________") 

# %%
#The percentage of votes each candidate won
#grouping the candidate_vote dataframe by the candidate column and counting results
candidate_vote_df = election_df.groupby(["Candidate"]).count()

#totally the Ballot ID by the above dataframe sorted by candidate
candidate_total = candidate_vote_df["Ballot ID"].sum()

#added total votes to be used in dataframe below
total_votes = candidate_vote_df

#getting the percentage of the total votes by candidate divided by total number of votes.
percentage_vote_df = (candidate_vote_df / vote_count) * 100

#combining the dataframes to include all 3 columns
percentage_vote_df["Total Votes"] = total_votes

#changing column name
percentage_vote_df = percentage_vote_df.rename(columns={"Ballot ID": "Percentage Votes"})

print(percentage_vote_df)


# %%
#The winner based on popular vote
Winner = percentage_vote_df.idxmax()

print(f"The winner is:" + Winner)


# %%
#output to text file
Result = [vote_count,percentage_vote_df, Winner]
result_df = pd.DataFrame(Result)

output_file = "/Users/staciesauer/GitHub/Python-Challenge/PyPoll/Analysis/output.txt"
result_df.to_csv(output_file)

print("Election Results")
print("_______________________")
print("Total Votes :", vote_count)
print(percentage_vote_df)
print(f"The winner is:" + Winner)

# %%



