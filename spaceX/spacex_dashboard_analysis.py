import pandas as pd

df = pd.read_csv("spacex_launch_dash.csv")

# Success rate by launch site
site_results = df.groupby("Launch Site")["class"].agg(
    successful="sum",
    total="count",
    success_rate="mean"
)

site_results["success_rate"] *= 100

print("SUCCESS RATE BY LAUNCH SITE")
print(site_results.round(2))

# Success rate by payload range
df["Payload Range"] = pd.cut(
    df["Payload Mass (kg)"],
    bins=[0, 2000, 4000, 6000, 8000, 10000],
    include_lowest=True
)

payload_results = df.groupby(
    "Payload Range", observed=True
)["class"].agg(
    successful="sum",
    total="count",
    success_rate="mean"
)

payload_results["success_rate"] *= 100

print("\nSUCCESS RATE BY PAYLOAD RANGE")
print(payload_results.round(2))

# Success rate by booster version
booster_results = df.groupby(
    "Booster Version Category"
)["class"].agg(
    successful="sum",
    total="count",
    success_rate="mean"
)

booster_results["success_rate"] *= 100

print("\nSUCCESS RATE BY BOOSTER VERSION")
print(booster_results.round(2))

