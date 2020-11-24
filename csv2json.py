# convert a table to json
import pandas as pd
import json


def main():
    path = "src/assets/code_compare.csv"
    df = pd.read_csv(path)
    df.fillna("", inplace=True)
    columns = df.columns.tolist()
    rows = [value.tolist() for value in df.values]
    data = {"columns": columns, "rows": rows}

    with open("src/assets/code_compare.json", "w", encoding="utf-8") as f:
        json.dump(data, f)


if __name__ == "__main__":
    main()
