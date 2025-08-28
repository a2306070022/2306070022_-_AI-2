import random
import requests

# ランダムな6桁の16進カラーコードを生成
def generate_random_color():
    return ''.join(random.choices('0123456789ABCDEF', k=6))

# 入力されたカラーコードの色の情報を取得
def get_color_info(hex_code):
    url = f"https://www.thecolorapi.com/id?hex={hex_code}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# 入力カラーに似合うカラーパターンを取得（analogic: 類似色）
def get_color_scheme(hex_code, mode="analogic", count=5):
    url = f"https://www.thecolorapi.com/scheme?hex={hex_code}&mode={mode}&count={count}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("colors", [])
    return []
