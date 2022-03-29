import pandas as pd
import matplotlib.pyplot as plt 
import random


df = pd.read_csv("RDINets_origin.csv")

time = df["InferenceLatency (ms)"].to_list()

time_choice = random.choices(time, k=200)

new_df = pd.DataFrame()
new_df["InferenceLatency (ms)"] = time_choice

new_df.to_csv("RDINets.csv", index=False)

plt.hist(new_df, bins=100)
plt.savefig("RDINets.png")