import os
import subprocess
import json
from bs4 import BeautifulSoup

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RAW_DIR = os.path.join(BASE_DIR, 'raw')
os.makedirs(RAW_DIR, exist_ok=True)

HTML_PATH = os.path.join(RAW_DIR, 'peleng_full.html')
JSON_PATH = os.path.join(RAW_DIR, 'parsed_brandbook.json')

def fetch_html():
    print("Downloading peleng.by/brandbook...")
    cmd = ['curl.exe', '-k', '-s', '--compressed', 'https://peleng.by/brandbook', '-o', HTML_PATH]
    subprocess.run(cmd, check=True)
    print(f"Downloaded HTML to: {HTML_PATH}")

def parse_html():
    if not os.path.exists(HTML_PATH):
        fetch_html()

    with open(HTML_PATH, encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    data = {'primary_colors': [], 'additional_colors': []}

    # Primary colors
    colors_div = soup.find(id='colors')
    if colors_div:
        for cb in colors_div.find_all('div', class_=lambda c: c and 'brandbook-colors__color' in c):
            title = cb.find('h3')
            if not title:
                continue
            name = title.get_text(strip=True)
            specs = [s.get_text(strip=True) for s in cb.find_all('span')]
            desc_p = cb.find('div', class_='brandbook-colors__color__text')
            desc = ' '.join([p.get_text(strip=True) for p in desc_p.find_all('p') if not p.find('span')]) if desc_p else ""
            data['primary_colors'].append({'name': name, 'specs': specs, 'desc': desc})

    with open(JSON_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"Parsed data saved to: {JSON_PATH}")

if __name__ == '__main__':
    parse_html()
