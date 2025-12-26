import pandas as pd

def load_excel(file):
    return pd.read_excel(file)


# ===== CHUYỂN TIỀN =====
def normalize_chuyentien(df):
    df = df.rename(columns={
        "NGAY_GD": "NGAY_GD",
        "SOL_ID": "DVKD",
        "LOAI KH CHUYEN": "LOAI_KH",
        "CIF_KH_CHUYEN": "CIF",
        "SO_TIEN_QUY_DOI_VND": "SOTIEN",
        "LOAI_GIAO_DICH": "KENH",
        "NAM GIAO DICH": "NAM"
    })

    if "NAM" not in df:
        df["NAM"] = pd.to_datetime(df["NGAY_GD"], errors="coerce").dt.year

    df["SOTIEN"] = pd.to_numeric(df["SOTIEN"], errors="coerce").fillna(0)
    return df


# ===== HUY ĐỘNG =====
def normalize_huydong(df):
    df = df.rename(columns={
        "BRCD": "DVKD",
        "CUST_TYPE": "LOAI_KH",
        "CUSTSEQ": "CIF",
        "GL_SUB": "GL_SUB",
        "CURBAL_VND": "SODU",
        "DP_MAT": "KY_HAN",
        "NAM": "NAM"
    })

    df["SODU"] = pd.to_numeric(df["SODU"], errors="coerce").fillna(0)
    return df

