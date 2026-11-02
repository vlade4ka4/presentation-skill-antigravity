import os
from PIL import Image, ImageDraw, ImageFont

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', '..'))
OUTPUT_PATH = os.path.join(PROJECT_ROOT, 'assets', 'peleng_colors_palette.png')
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

def generate_palette():
    W, H = 1920, 1080
    img = Image.new('RGB', (W, H), color='#0F131C')
    draw = ImageDraw.Draw(img)

    try:
        font_title = ImageFont.truetype('segoeuib.ttf', 44)
        font_subtitle = ImageFont.truetype('segoeui.ttf', 20)
        font_cat = ImageFont.truetype('segoeuib.ttf', 24)
        font_cname = ImageFont.truetype('segoeuib.ttf', 26)
        font_spec_b = ImageFont.truetype('segoeuib.ttf', 16)
        font_spec = ImageFont.truetype('segoeui.ttf', 15)
        font_desc = ImageFont.truetype('segoeuii.ttf', 14)
    except Exception:
        font_title = font_subtitle = font_cat = font_cname = font_spec_b = font_spec = font_desc = ImageFont.load_default()

    # Header
    draw.rectangle([0, 0, W, 120], fill='#161B26')
    draw.rectangle([0, 118, W, 120], fill='#CC0000')
    draw.text((80, 28), "ОАО «ПЕЛЕНГ» — ОФИЦИАЛЬНАЯ ПАЛИТРА ЦВЕТОВ", fill='#FFFFFF', font=font_title)
    draw.text((80, 80), "Спецификация для дизайн-системы и фронтенд-разработки (HEX, RGB, CMYK, RAL, Web-оттенки)", fill='#94A3B8', font=font_subtitle)

    primary_colors = [
        {"name": "Лазер (Laser)", "hex": "#CC0000", "rgb": "204, 0, 0", "cmyk": "0, 100, 100, 20", "ral": "RAL 3020 Traffic red", "role": "Основной цвет логотипа. Лидерство, акценты, CTA"},
        {"name": "Графит (Graphite)", "hex": "#232328", "rgb": "35, 35, 40", "cmyk": "13, 13, 0, 84", "ral": "RAL 7021 Black grey", "role": "Основа чертежей, шрифты, тёмный фон интерфейса"},
        {"name": "Металл (Metal)", "hex": "#7F8081", "rgb": "127, 128, 129", "cmyk": "2, 1, 0, 49", "ral": "RAL 7040 Window grey", "role": "Металлические детали, нейтральные рамки, иконки"},
        {"name": "Стекло (Glass)", "hex": "#EFEFEF", "rgb": "239, 239, 239", "cmyk": "0, 0, 0, 2", "ral": "RAL 9003 Signal white", "role": "Светлый фон, контраст на тёмном, прозрачные слои"}
    ]

    additional_colors = [
        {"name": "Ночь (Night)", "hex": "#192241", "rgb": "25, 34, 65", "cmyk": "90, 77, 27, 60", "ral": "Космическое направление", "role": "Глубина космоса, фундаментальные открытия"},
        {"name": "Воздух (Air)", "hex": "#A1C8DB", "rgb": "161, 200, 219", "cmyk": "41, 10, 10, 1", "ral": "Гражданская продукция", "role": "Доверие, чистота, небесные технологии"},
        {"name": "Защита (Protect)", "hex": "#ABB385", "rgb": "171, 179, 133", "cmyk": "35, 16, 53, 9", "ral": "Специальное / военное", "role": "Функциональность, надежность, интеграция"}
    ]

    def draw_card(c, x, y, w, h):
        draw.rounded_rectangle([x, y, x + w, y + h], radius=16, fill='#161B26', outline='#283245', width=1)
        draw.rounded_rectangle([x + 12, y + 12, x + w - 12, y + 150], radius=10, fill=c['hex'])
        if c['hex'] in ['#EFEFEF', '#A1C8DB', '#ABB385']:
            draw.rounded_rectangle([x + 12, y + 12, x + w - 12, y + 150], radius=10, outline='#64748B', width=1)
        draw.rounded_rectangle([x + 24, y + 104, x + 130, y + 138], radius=6, fill='#000000B0')
        draw.text((x + 34, y + 110), c['hex'], fill='#FFFFFF', font=font_spec_b)
        ty = y + 165
        draw.text((x + 20, ty), c['name'], fill='#FFFFFF', font=font_cname)
        ty += 38
        draw.text((x + 20, ty), f"RGB:   {c['rgb']}", fill='#CBD5E1', font=font_spec)
        ty += 24
        draw.text((x + 20, ty), f"CMYK: {c['cmyk']}", fill='#94A3B8', font=font_spec)
        ty += 24
        draw.text((x + 20, ty), f"{c['ral']}", fill='#38BDF8', font=font_spec_b)
        ty += 28
        draw.text((x + 20, ty), f"Назначение: {c['role']}", fill='#94A3B8', font=font_desc)

    draw.text((80, 150), "1. ОСНОВНЫЕ ЦВЕТА БРЕНДА (PRIMARY PALETTE)", fill='#38BDF8', font=font_cat)
    for i, col in enumerate(primary_colors):
        draw_card(col, 80 + i * (410 + 30), 195, 410, 360)

    draw.text((80, 590), "2. ДОПОЛНИТЕЛЬНЫЕ ЦВЕТА ПО НАПРАВЛЕНИЯМ (ADDITIONAL / DOMAINS)", fill='#38BDF8', font=font_cat)
    for i, col in enumerate(additional_colors):
        draw_card(col, 80 + i * (560 + 30), 635, 560, 360)

    draw.rectangle([0, H - 40, W, H], fill='#10141E')
    draw.text((80, H - 30), "Источник: peleng.by/brandbook#colors | Сформировано для команды разработки", fill='#64748B', font=font_desc)

    img.save(OUTPUT_PATH, "PNG", quality=95)
    print(f"Image saved to: {OUTPUT_PATH}")

if __name__ == '__main__':
    generate_palette()
