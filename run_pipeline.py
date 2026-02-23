import pandas as pd

def run_pipeline(region="austin"):
    df = pd.read_csv("example/example_data.csv")
    df["forward_return"] = df["price"].pct_change(4)
    df["regime"] = df["income"] < 72
    return df

if __name__ == "__main__":
    df = run_pipeline()
    print(df.head())
