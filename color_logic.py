import requests

def get_random_color():
    url = "https://www.thecolorapi.com/id?format=json"
    response = requests.get(url)
    data = response.json()
    color_hex = data['hex']['value']
    color_name = data['name']['value']
    color_meaning = data['name'].get('meaning', "意味情報なし")
    return color_hex, color_name, color_meaning

def get_color_info(color_hex):
    url = f"https://www.thecolorapi.com/id?hex={color_hex.lstrip('#')}&format=json"
    response = requests.get(url)
    data = response.json()
    color_name = data['name']['value']
    color_meaning = data['name'].get('meaning', '意味情報なし')
    return color_name, color_meaning
