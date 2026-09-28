import streamlit as st
import pandas as pd

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Quản lý tình trạng phòng",
    page_icon="🏨",
    layout="wide"
)

# =========================
# DỮ LIỆU PHÒNG
# =========================
if "rooms" not in st.session_state:
    st.session_state.rooms = pd.DataFrame({
        "Số phòng": [
            "101", "102", "103", "104",
            "201", "202", "203", "204",
            "301", "302", "303", "304"
        ],
        "Loại phòng": [
            "Standard", "Standard", "Standard", "Standard",
            "Deluxe", "Deluxe", "Deluxe", "Deluxe",
            "Suite", "Suite", "Suite", "Suite"
        ],
        "Giá phòng": [
            500000, 500000, 500000, 500000,
            800000, 800000, 800000, 800000,
            1500000, 1500000, 1500000, 1500000
        ],
        "Trạng thái": [
            "Trống", "Đang sử dụng", "Đang dọn", "Trống",
            "Đang sử dụng", "Trống", "Bảo trì", "Trống",
            "Trống", "Đang sử dụng", "Đang dọn", "Trống"
        ]
    })

# =========================
# TIÊU ĐỀ
# =========================
st.title("🏨 QUẢN LÝ TÌNH TRẠNG PHÒNG KHÁCH SẠN")
st.caption("Hệ thống theo dõi và cập nhật tình trạng phòng")

st.divider()

# =========================
# THỐNG KÊ
# =========================
rooms = st.session_state.rooms

tong_phong = len(rooms)
phong_trong = len(rooms[rooms["Trạng thái"] == "Trống"])
dang_su_dung = len(rooms[rooms["Trạng thái"] == "Đang sử dụng"])
dang_don = len(rooms[rooms["Trạng thái"] == "Đang dọn"])
bao_tri = len(rooms[rooms["Trạng thái"] == "Bảo trì"])

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("🏨 Tổng phòng", tong_phong)

with col2:
    st.metric("🟢 Phòng trống", phong_trong)

with col3:
    st.metric("🔴 Đang sử dụng", dang_su_dung)

with col4:
    st.metric("🟡 Đang dọn", dang_don)

with col5:
    st.metric("🔧 Bảo trì", bao_tri)

st.divider()

# =========================
# TÌM KIẾM VÀ LỌC
# =========================
st.subheader("🔎 Tìm kiếm phòng")

col1, col2 = st.columns(2)

with col1:
    search = st.text_input(
        "Nhập số phòng",
        placeholder="Ví dụ: 101"
    )

with col2:
    filter_status = st.selectbox(
        "Lọc theo trạng thái",
        [
            "Tất cả",
            "Trống",
            "Đang sử dụng",
            "Đang dọn",
            "Bảo trì"
        ]
    )

filtered = rooms.copy()

if search:
    filtered = filtered[
        filtered["Số phòng"].str.contains(search, case=False)
    ]

if filter_status != "Tất cả":
    filtered = filtered[
        filtered["Trạng thái"] == filter_status
    ]

# =========================
# DANH SÁCH PHÒNG
# =========================
