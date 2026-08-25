import pandas as pd

print("\n----------------------- t1: table --------------------------------")
data_dic = {
    "name": ["Amir", "Sara", "hana", "mariam"],
    "quiz1": [90, 70, 82,60],
    "quiz2": [85, 60, 77,55],
}
df = pd.DataFrame(data_dic)
print(df)

print("\n----------------------- t2: details --------------------------------")
print(df.shape)
print(df.columns)
print(df.dtypes)
#print(df.describe()) 

print("\n----------------------- t3: get column--------------------------------")
print(df["quiz1"])
print("\n--------------------------- get 2 columns---------------------------")
print(df[["name", "quiz1"]])
print("\n--------------------------- indexed by name ---------------------------")
df2 = df.set_index("name")
print(df2)
print("\n--------------------------- loc by row---------------------------")

print(df2.loc["hana"])
print("\n--------------------------- loc by index of row ---------------------------")

print(df2.iloc[2]) 
print("\n--------------------------- t4: -------------------------")
top = df[df["quiz1"] >= 80]
print(top)
print("\n--------------------------- descending order by q1 ---------------------------")
print(df.sort_values("quiz1", ascending=False))
print("\n--------------------------- combining  ---------------------------")
combining_res= df[(df["quiz1"] >= 70) & (df["quiz2"] >= 70)]
print(combining_res)
print("\n--------------------------- t5: Add a Column avarege  ---------------------------")
df["average"] = (df["quiz1"] + df["quiz2"]) / 2
print(df)
print("\n--------------------------- Add a Column passed --------------------------")
df["passed"] = df["average"] >= 70

print(df[["name", "average", "passed"]])
print("\n----------------------------- add a NaN value in quiz1 col and row 1 ------------------------")

df.loc[1, "quiz2"] = None
print(df)
print("\n-----------------------------------------------------")
print(f"how many none in table:\n{df.isna().sum()}")
print("\n------------------------- fill it with nsnsn or any value ----------------------------")
filled = df.fillna("nsnsn")
print(filled)
df.dropna()
print("\n-----------------------------------------------------")
print(df)

