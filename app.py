import streamlit as st
from modules.loader import load_excel
from modules.chuyentien import *
from modules.huydong import *
from modules.exporter import export_excel

st.set_page_config("BÁO CÁO KIỂM TOÁN", layout="wide")

dvkd = st.text_input("MÃ ĐVKD", "1205")
nguong = st.number_input("Ngưỡng GD lớn", 500_000_000)

f_ct = st.file_uploader("CHUYỂN TIỀN", ["xls", "xlsx"])
f_hd = st.file_uploader("HUY ĐỘNG", ["xls", "xlsx"])
f_code = st.file_uploader("CODE SẢN PHẨM", ["xls", "xlsx"])

if st.button("XỬ LÝ"):
    df_ct = load_excel(f_ct)
    df_hd = load_excel(f_hd)
    df_code = load_excel(f_code)

    kq = {
        "BANG_2_CT": bang_2_ct_giao_dich_lon(df_ct, dvkd, nguong),
        "BANG_1_KT": bang_1_kt(df_hd, dvkd)
    }

    file = export_excel(kq, "templates/BAO_CAO_TEMPLATE.xlsx")

    st.download_button(
        "⬇️ Tải báo cáo",
        data=file.getvalue(),
        file_name="BAO_CAO_KIEM_TOAN.xlsx"
    )
