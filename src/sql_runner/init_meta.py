def init_meta(database_name: str) -> None:
    import os
    import pandas as pd

    meta = {
        "TABLE_NAME": "__META",
        "ATTRIBUTES": ",".join(["TABLE_NAME", "ATTRIBUTES", "PRIMARY_KEY"]),
        "PRIMARY_KEY": "TABLE_NAME",
    }
    df = pd.DataFrame(data=meta, index=["__META"])

    meta_path = os.path.join(database_name, "__META.csv")
    df.to_csv(path_or_buf=meta_path)
