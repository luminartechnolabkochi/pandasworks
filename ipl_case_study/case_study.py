# pandas.read_csv(file_path)
import pandas as pd

df = pd.read_csv("ipl_case_study\ipl_data.csv")

# df["match_id"].fillna(549,inplace=True)

for i in range(1,len(df)):

    if pd.isna(df.loc[i,"match_id"]):
        df.loc[i,"match_id"]=df.loc[i-1,'match_id']

print(df["match_id"])

df["season"].fillna(df["season"].mode()[0],inplace=True)

rounde_socre_mean=round(df["runs_scored"].mean())

df["runs_scored"].fillna(rounde_socre_mean,inplace=True)

df["city"].fillna(df["city"].mode()[0],inplace=True)

df["team1"].fillna("unknown",inplace=True)
df["team2"].fillna("unknown",inplace=True)
df["winning_team"].fillna("unknown",inplace=True)
df["player_of_match"].fillna("unknown",inplace=True)

df["venue"].fillna(df["venue"].mode()[0],inplace=True)
df["wickets"].fillna(df["wickets"].median(),inplace=True)
# print(df.isnull().sum())

# ANALYSIS
# matches per season

print("matches per season",df["season"].value_counts())


# top macth count season

print("topmatch count season",df["season"].value_counts().idxmax())

# total match won by each team

print("matches won by each team==================")

print(df["winning_team"].value_counts())

print("avg runs per season==============")

print(df.groupby("season")["runs_scored"].mean())

print("venu-wise match count============")

print(df["venue"].value_counts())
print("venu-wise avg runs=================")
print(df.groupby("venue")["runs_scored"].mean())

# city-wise


# joins