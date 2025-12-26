import pandas as pd
from .loader import normalize_chuyentien


def bang_1_ct_trong_nuoc(df, dvkd):
    df = normalize_chuyentien(df)
    df =ư= df[df["DVKD"].astype(str) == str(dvkd)]
    df = df[df["KENH"].str.upper() != "SWIFT"]

    return (
        df.groupby(["KENH", "NAM"])
        .agg(
            TONG_TIEN=("SOTIEN", "sum"),
            SO_GD=("SOTIEN", "count")
        )
        .reset_index()
    )


def bang_2_ct_giao_dich_lon(df, dvkd, nguong):
    df = normalize_chuyentien(df)
    df = df[
        (df["DVKD"].astype(str) == str(dvkd)) &
        (df["KENH"].str.upper() != "SWIFT")
    ]

    rows = []
    for nam in sorted(df["NAM"].unique()):
        df_nam = df[df["NAM"] == nam]
        tong_kh = df_nam["CIF"].nunique()

        gd_kh = df_nam.groupby("CIF")["SOTIEN"].sum()
        gd_lon = gd_kh[gd_kh >= nguong]

        rows.append({
            "NAM": nam,
            "TONG_SO_KH": tong_kh,
            "SO_KH_GD_LON": gd_lon.count(),
            "TONG_TIEN_GD_LON": gd_lon.sum() / 1e9,
            "TY_LE": gd_lon.count() / tong_kh if tong_kh else 0
        })

    return pd.DataFrame(rows)


def bang_3_ct_nuoc_ngoai(df, dvkd):
    df = normalize_chuyentien(df)
    df = df[
        (df["DVKD"].astype(str) == str(dvkd)) &
        (df["KENH"].str.upper() == "SWIFT")
    ]

    return (
        df.groupby("NAM")
        .agg(
            TONG_TIEN=("SOTIEN", "sum"),
            SO_GD=("SOTIEN", "count")
        )
        .reset_index()
    )

