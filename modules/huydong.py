import pandas as pd
from .loader import normalize_huydong


def bang_1_kt(df, dvkd):
    df = normalize_huydong(df)
    df = df[df["DVKD"].astype(str) == str(dvkd)]

    return (
        df.groupby(["NAM", "LOAI_KH", "KY_HAN"])
        .agg(
            SO_DU=("SODU", "sum"),
            SO_KH=("CIF", "nunique")
        )
        .reset_index()
    )


def bang_2_kt(df, code_df, dvkd):
    df = normalize_huydong(df)
    df = df[df["DVKD"].astype(str) == str(dvkd)]

    df = df.merge(code_df[["GL_SUB", "TEN_SP"]], on="GL_SUB", how="left")

    kq = (
        df.groupby(["NAM", "TEN_SP"])
        .agg(SO_DU=("SODU", "sum"))
        .reset_index()
    )

    kq["TY_TRONG"] = kq.groupby("NAM")["SO_DU"].apply(lambda x: x / x.sum())
    return kq


def bang_3_kt(df, dvkd):
    df = normalize_huydong(df)
    df = df[df["DVKD"].astype(str) == str(dvkd)]

    kh_sd = df.groupby(["NAM", "CIF"])["SODU"].sum().reset_index()
    return kh_sd
