import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# read the CSV file
df = pd.read_csv("dataset.csv")
# print(df.head(10))




# Find total number of runs Kohli has scored
total_runs = df["Runs"].sum()
no_of_matches = len(df["Runs"])
print(f"Total no of runs scored in {no_of_matches} matches: ",total_runs)




# Average of number of runs he has scored
avg_runs = df["Runs"].mean()
print(f"Average runs of Kohli in {no_of_matches} matches: ",int(avg_runs))




# number of matches he has played at different positions
positions = df["Pos"].unique()
# print(positions)

df["Pos"] = df["Pos"].map({
    2.0: "Batting at 2",
    1.0: "Batting at 1",
    7.0: "Batting at 7",
    4.0: "Batting at 4",
    3.0: "Batting at 3",
    5.0: "Batting at 5",
    6.0: "Batting at 6"
})

# print(df[["Runs", "Pos", "Opposition"]].head())
pos_count = df["Pos"].value_counts()
print(pos_count)
print(type(pos_count))

pos_values = pos_count.values
pos_labels = pos_count.index
print(pos_values)

# fig = plt.figure(figsize=(10,7))
# plt.pie(pos_values, labels=pos_labels)
# plt.show()




# create a piechart of match played with opponents
def show_pie_plot(df, key):
    counts = df[key].value_counts()
    count_values = counts.values
    count_labels = counts.index

    fig = plt.figure(figsize=(10,7))
    plt.pie(count_values, labels=count_labels)
    plt.show()

# show_pie_plot(df, "Pos")
# show_pie_plot(df, "Opposition")
# show_pie_plot(df, "Ground")




# Total runs scored in different positions

# df["Pos"] = df["Pos"].map({
#     2.0: "Runs at 2",
#     1.0: "Runs at 1",
#     7.0: "Runs at 7",
#     4.0: "Runs at 4",
#     3.0: "Runs at 3",
#     5.0: "Runs at 5",
#     6.0: "Runs at 6"
# })

runs_at_pos = df.groupby("Pos")["Runs"].sum()
print(runs_at_pos)
runs_at_pos_values = runs_at_pos.values
runs_at_pos_labels = runs_at_pos.index

# fig = plt.figure(figsize=(10,7))
# plt.pie(runs_at_pos_values, labels=runs_at_pos_labels)
# plt.show()




# total sixes scored with different opponents
sixes_at_pos = df.groupby("Opposition")["6s"].sum()
print(sixes_at_pos)
sixes_at_pos_values = sixes_at_pos.values
sixes_at_pos_labels = sixes_at_pos.index

# fig = plt.figure(figsize=(10,7))
# plt.pie(sixes_at_pos_values, labels=sixes_at_pos_labels)
# plt.show()




# Number of centuries scored by Kohli in first 
centuries = df.query("Runs>=100")
print(centuries)

innings = centuries["Inns"]
tons = centuries["Runs"]
# tons_t = centuries.groupby("Runs")["Inns"].value_counts
# print(tons_t)

# fig = plt.figure(figsize=(10,7))
# plt.bar(innings, tons, color='blue', width=0.2)
# plt.show()




# Calculate the dismissals of Kohli
dismissals = df["Dismissal"].value_counts()
print(dismissals)

dismissals_counts = dismissals.values
dismissals_labels = dismissals.index

# show_pie_plot(df, "Dismissal")




# Against which team he has scored most runs
runs = df.groupby("Opposition")["Runs"].sum()
runs_values = runs.values
runs_labels = runs.index

fig = plt.figure(figsize=(10,7))
plt.bar(
    df["Opposition"], df["Runs"], color='red', width=0.4
)

plt.show()


# Against which team he has scored most centuries 