import pandas as pd

def normalize(df):
    df = df.rename(columns={
        "NGAY_GD": "NGAY",
        "CIF": "CIF",
        "SO_TIEN": "SOTIEN",
        "KENH": "KENH"
    })
    df["NAM"] = pd.to_datetime(df["NGAY"], errors="coerce").dt.year
    return df


def tong_ct_trong_nuoc(df, nam):
    return (
        df.query("KENH != 'SWIFT' and NAM == @nam")
        .groupby("KENH")
        .agg(
            TONG_TIEN=("SOTIEN", "sum"),
            SO_GD=("SOTIEN", "count")
        )
        .reset_index()
    )


def giao_dich_lon(df, nam, nguong):
    df = df.query("KENH != 'SWIFT' and NAM == @nam")
    kh = (
        df.groupby("CIF")["SOTIEN"]
        .sum()
        .reset_index()
    )
    lon = kh[kh["SOTIEN"] >= nguong]
    return {
        "tong_kh": kh["CIF"].nunique(),
        "so_kh_lon": lon["CIF"].nunique(),
        "tong_tien": lon["SOTIEN"].sum()
    }


def ct_nuoc_ngoai(df, nam):
    df = df.query("KENH == 'SWIFT' and NAM == @nam")
    return (
        df.groupby("CIF")
        .agg(
            TONG_TIEN=("SOTIEN", "sum"),
            SO_GD=("SOTIEN", "count")
        )
        .reset_index()
    )
