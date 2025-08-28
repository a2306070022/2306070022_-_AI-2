import streamlit as st
from logic import generate_random_color, get_color_info, get_color_scheme

st.set_page_config(page_title="Color Explorer", layout="centered")
st.title(" Color Explorer - ランダムカラー＆意味解説")

# --- 色の生成ボタン ---
if st.button(" ランダムカラーを生成"):
    color_code = generate_random_color()
    st.session_state['color_code'] = color_code
else:
    color_code = st.session_state.get('color_code', '4A7FBC')

# --- 色の情報取得 ---
color_info = get_color_info(color_code)

# --- 色の表示 ---
st.markdown(f"<div style='width:150px; height:150px; background-color:#{color_code}; border-radius:12px; margin:auto'></div>", unsafe_allow_html=True)
st.markdown(f"<h3 style='text-align:center'>#{color_code}</h3>", unsafe_allow_html=True)

if color_info:
    st.write(f"🟢 **色の名前**: {color_info['name']['value']}")
    st.write(f" **近い色のコード**: {color_info['name']['closest_named_hex']}")
else:
    st.error("色情報の取得に失敗しました。")

# --- 色の調和パレット表示（analogic） ---
st.subheader(" この色に似合うカラー（調和パターン: analogic）")
scheme = get_color_scheme(color_code, mode="analogic", count=5)

if scheme:
    cols = st.columns(len(scheme))
    for i, color in enumerate(scheme):
        with cols[i]:
            hex_val = color['hex']['value']
            name = color['name']['value']
            st.markdown(f"<div style='width:60px; height:60px; background-color:{hex_val}; border-radius:8px; margin:auto'></div>", unsafe_allow_html=True)
            st.caption(f"{hex_val}\n{name}")
else:
    st.error("調和色の取得に失敗しました。")

# --- ユーザー入力で色を調べる ---
st.write("---")
st.subheader(" 好きな色コードで調べる")
user_input = st.text_input("カラーコードを入力してください（例: #FF5733）")

if user_input:
    user_code = user_input.strip().lstrip("#")
    if len(user_code) == 6 and all(c in '0123456789ABCDEFabcdef' for c in user_code):
        user_info = get_color_info(user_code)
        if user_info:
            st.markdown(f"<div style='width:100px; height:100px; background-color:#{user_code}; border-radius:10px; margin:auto'></div>", unsafe_allow_html=True)
            st.write(f"🔎 **色の名前**: {user_info['name']['value']}")
            st.write(f" **近い色のコード**: {user_info['name']['closest_named_hex']}")
        else:
            st.error("色情報の取得に失敗しました。")
    else:
        st.warning("6桁のカラーコード（例: #A1B2C3）を入力してください。")
