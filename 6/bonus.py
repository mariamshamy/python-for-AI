import pandas as pd
data = {
 "name": ["Amir", "Sara", "Leo", "Nina"],
 "quiz1": [90, 70, 82, 60],
}
df = pd.DataFrame(data)

df["study_group"] = ["A", "B", "A", "B"] 
print(df.groupby("study_group")["quiz1"].mean())
print(df.groupby("study_group")["quiz1"].agg(["mean", "max", "count"]))
#df.to_csv("class_results.csv", index=False)
print("\n-----------------------------------------------------")
print(pd.read_csv("class_results.csv"))