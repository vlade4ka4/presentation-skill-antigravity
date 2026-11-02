import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', '..'))
OUTPUT_PATH = os.path.join(PROJECT_ROOT, 'presentations', 'peleng_brandbook_tz.pptx')
os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

def build_presentation():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    # Brand Colors
    c_laser = RGBColor(204, 0, 0)
    c_graphite = RGBColor(35, 35, 40)
    c_metal = RGBColor(127, 128, 129)
    c_glass = RGBColor(239, 239, 239)
    c_night = RGBColor(25, 34, 65)
    c_air = RGBColor(161, 200, 219)
    c_protect = RGBColor(171, 179, 133)
    c_card_bg = RGBColor(32, 33, 38)
    c_card_border = RGBColor(55, 58, 66)
    c_white = RGBColor(255, 255, 255)
    c_muted = RGBColor(160, 165, 175)

    def set_slide_bg(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
        bg.fill.solid()
        bg.fill.fore_color.rgb = c_graphite
        bg.line.fill.background()
        return bg

    def add_header(slide, badge_text, title_text):
        line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(0.08))
        line.fill.solid()
        line.fill.fore_color.rgb = c_laser
        line.line.fill.background()

        tb = slide.shapes.add_textbox(Inches(0.9), Inches(0.55), Inches(11.5), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p1 = tf.paragraphs[0]
        p1.text = badge_text.upper()
        p1.font.size = Pt(11)
        p1.font.bold = True
        p1.font.color.rgb = c_laser
        p1.font.name = "Segoe UI"
        
        p2 = tf.add_paragraph()
        p2.text = title_text
        p2.font.size = Pt(26)
        p2.font.bold = True
        p2.font.color.rgb = c_glass
        p2.font.name = "Segoe UI"
        p2.space_before = Pt(4)

    # Slide 1: Cover
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1)
    rline = s1.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.9), Inches(2.2), Inches(0.12), Inches(3.2))
    rline.fill.solid()
    rline.fill.fore_color.rgb = c_laser
    rline.line.fill.background()

    tb1 = s1.shapes.add_textbox(Inches(1.3), Inches(1.8), Inches(11), Inches(4.0))
    tf1 = tb1.text_frame
    tf1.word_wrap = True
    p = tf1.paragraphs[0]
    p.text = "✦ БРЕНДБУК ОАО «ПЕЛЕНГ» • ТЗ ДЛЯ КОМАНДЫ РАЗРАБОТКИ"
    p.font.size = Pt(13)
    p.font.bold = True
    p.font.color.rgb = c_laser
    p.font.name = "Segoe UI"

    p = tf1.add_paragraph()
    p.text = "Визуальный стиль и дизайн-система"
    p.font.size = Pt(42)
    p.font.bold = True
    p.font.color.rgb = c_glass
    p.font.name = "Segoe UI"
    p.space_before = Pt(14)

    p = tf1.add_paragraph()
    p.text = "Спецификация официальных цветов, типографика (Bebas Neue / Roboto Condensed),\nсемантические правила верстки и технические требования к фронтенду."
    p.font.size = Pt(18)
    p.font.color.rgb = c_muted
    p.font.name = "Segoe UI"
    p.space_before = Pt(16)

    # Slide 2: Primary Colors
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2)
    add_header(s2, "Раздел 1 • Основная палитра бренда", "4 базовых цвета ОАО «Пеленг»")

    primary_cards = [
        ("ЛАЗЕР", "#CC0000", "RGB: 204, 0, 0\nRAL 3020 Traffic red", "Основной цвет логотипа. Символизирует лидерство. Главный акцент интерфейса, CTA.", c_laser, c_white),
        ("ГРАФИТ", "#232328", "RGB: 35, 35, 40\nRAL 7021 Black grey", "Отождествляет чертежи карандашом, шрифт. Базовый тёмный фон интерфейсов.", c_graphite, c_glass),
        ("МЕТАЛЛ", "#7F8081", "RGB: 127, 128, 129\nRAL 7040 Window grey", "Металлические детали и структуры. Нейтральные разделители, рамки, иконки.", c_metal, c_white),
        ("СТЕКЛО", "#EFEFEF", "RGB: 239, 239, 239\nRAL 9003 Signal white", "Контраст на тёмном фоне, прозрачность. Карточки, светлый фон, основной текст.", c_glass, c_graphite)
    ]
    card_w, card_h, card_y, gap, start_x = Inches(2.65), Inches(4.9), Inches(1.9), Inches(0.28), Inches(0.9)
    for i, (name, hex_code, specs, role, col, text_col) in enumerate(primary_cards):
        cx = start_x + i * (card_w + gap)
        card = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y, card_w, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = c_card_bg
        card.line.color.rgb = c_card_border
        swatch = s2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.2), card_y + Inches(0.2), card_w - Inches(0.4), Inches(1.8))
        swatch.fill.solid()
        swatch.fill.fore_color.rgb = col
        swatch.line.color.rgb = c_card_border
        p = swatch.text_frame.paragraphs[0]
        p.text = hex_code
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = text_col
        p.alignment = PP_ALIGN.CENTER
        tb = s2.shapes.add_textbox(cx + Inches(0.2), card_y + Inches(2.1), card_w - Inches(0.4), Inches(2.6))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = name
        p.font.size = Pt(20)
        p.font.bold = True
        p.font.color.rgb = c_glass
        p = tf.add_paragraph()
        p.text = specs
        p.font.size = Pt(12)
        p.font.color.rgb = c_metal
        p.space_before = Pt(6)
        p = tf.add_paragraph()
        p.text = role
        p.font.size = Pt(12)
        p.font.color.rgb = c_muted
        p.space_before = Pt(10)

    # Slide 3: Additional Colors
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3)
    add_header(s3, "Раздел 2 • Продуктовые направления", "Дополнительные цвета приборов ОАО «Пеленг»")
    add_cards = [
        ("НОЧЬ (NIGHT)", "#192241", "RGB: 25, 34, 65 | CMYK: 90 77 27 60", "КОСМИЧЕСКОЕ НАПРАВЛЕНИЕ", "Цвет бесконечности и фундаментальных открытий. Применяется для оптических приборов, спутниковых систем и космических комплексов.", c_night, c_white),
        ("ВОЗДУХ (AIR)", "#A1C8DB", "RGB: 161, 200, 219 | CMYK: 41 10 10 1", "ГРАЖДАНСКАЯ ПРОДУКЦИЯ", "Цвет доверия, чистоты и ясности. Ассоциируется с небом и надежной средой жизни. Применяется в линейке гражданских приборов.", c_air, c_graphite),
        ("ЗАЩИТА (PROTECT)", "#ABB385", "RGB: 171, 179, 133 | CMYK: 35 16 53 9", "СПЕЦИАЛЬНОЕ / ВОЕННОЕ", "Цвет функциональности, маскировки и абсолютной надежности. Применяется для изделий специального и военного назначения.", c_protect, c_graphite)
    ]
    card_w3, card_h3, gap3 = Inches(3.64), Inches(4.9), Inches(0.3)
    for i, (name, hex_code, specs, category, desc, col, text_col) in enumerate(add_cards):
        cx = start_x + i * (card_w3 + gap3)
        card = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y, card_w3, card_h3)
        card.fill.solid()
        card.fill.fore_color.rgb = c_card_bg
        card.line.color.rgb = c_card_border
        swatch = s3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.25), card_y + Inches(0.25), card_w3 - Inches(0.5), Inches(1.8))
        swatch.fill.solid()
        swatch.fill.fore_color.rgb = col
        swatch.line.color.rgb = c_card_border
        p = swatch.text_frame.paragraphs[0]
        p.text = hex_code
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = text_col
        p.alignment = PP_ALIGN.CENTER
        tb = s3.shapes.add_textbox(cx + Inches(0.25), card_y + Inches(2.2), card_w3 - Inches(0.5), Inches(2.5))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = category
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = c_laser
        p = tf.add_paragraph()
        p.text = name
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = c_glass
        p.space_before = Pt(4)
        p = tf.add_paragraph()
        p.text = specs
        p.font.size = Pt(11)
        p.font.color.rgb = c_metal
        p.space_before = Pt(4)
        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(13)
        p.font.color.rgb = c_muted
        p.space_before = Pt(10)

    # Slide 4: Typography
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4)
    add_header(s4, "Раздел 3 • Шрифтовая система", "Типографика: Bebas Neue & Roboto Condensed")
    c_left = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.9), Inches(5.6), Inches(4.9))
    c_left.fill.solid()
    c_left.fill.fore_color.rgb = c_card_bg
    c_left.line.color.rgb = c_card_border
    tb_l = s4.shapes.add_textbox(Inches(1.2), Inches(2.1), Inches(5.0), Inches(4.5))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    p = tf_l.paragraphs[0]
    p.text = "АКЦЕНТНЫЙ ШРИФТ ЗАГОЛОВКОВ"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = c_laser
    p = tf_l.add_paragraph()
    p.text = "BEBAS NEUE"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = c_glass
    p.space_before = Pt(6)
    for b in ["Главные заголовки страниц (H1) и слоганы", "Крупные цифровые метрики и KPI (10×, 99.8%)", "Баннеры, промо-блоки, титульные листы", "Строго ЗАГЛАВНЫЕ буквы (UPPERCASE)"]:
        p = tf_l.add_paragraph()
        p.text = f"•  {b}"
        p.font.size = Pt(13)
        p.font.color.rgb = c_muted
        p.space_before = Pt(8)

    c_right = s4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.9), Inches(5.6), Inches(4.9))
    c_right.fill.solid()
    c_right.fill.fore_color.rgb = c_card_bg
    c_right.line.color.rgb = c_card_border
    tb_r = s4.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.0), Inches(4.5))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    p = tf_r.paragraphs[0]
    p.text = "ОСНОВНОЙ ТЕКСТ И ИНТЕРФЕЙСЫ"
    p.font.size = Pt(11)
    p.font.bold = True
    p.font.color.rgb = c_laser
    p = tf_r.add_paragraph()
    p.text = "ROBOTO CONDENSED"
    p.font.size = Pt(36)
    p.font.bold = True
    p.font.color.rgb = c_glass
    p.space_before = Pt(6)
    for b in ["Основной текст абзацев, описаний и документации", "Интерфейсы: кнопки, формы, инпуты, модальные окна", "Таблицы данных, графики и технические чертежи", "Высокая плотность информации без потери читаемости"]:
        p = tf_r.add_paragraph()
        p.text = f"•  {b}"
        p.font.size = Pt(13)
        p.font.color.rgb = c_muted
        p.space_before = Pt(8)

    # Slide 5: Frontend requirements
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5)
    add_header(s5, "Раздел 4 • ТЗ для фронтенд-разработки", "Технические стандарты реализации UI")
    tz_cards = [
        ("1. CSS Токены и переменные", [
            "--peleng-laser: #CC0000;",
            "--peleng-graphite: #232328;",
            "--peleng-metal: #7F8081;",
            "--peleng-glass: #EFEFEF;",
            "Все стили завязывать на переменные, хардкод HEX запрещен!"
        ]),
        ("2. Контрастность и доступность", [
            "WCAG 2.2 AA — строгий стандарт",
            "Текст на тёмном: только Стекло (#EFEFEF) или белый",
            "Лазер (#CC0000) — только для акцентов и кнопок действий",
            "Минимальный контраст текста 4.5:1 к фону"
        ]),
        ("3. Bento-сетка и формы", [
            "Радиус скругления карточек: 16–24px",
            "Тонкая рамка карточек: 1px rgba(127,128,129,0.35)",
            "Мягкие тени и лёгкий эффект матового стекла (backdrop-blur)",
            "Строгое соответствие отступов (система кратна 8px)"
        ])
    ]
    for i, (title, items) in enumerate(tz_cards):
        cx = start_x + i * (card_w3 + gap3)
        card = s5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y, card_w3, card_h3)
        card.fill.solid()
        card.fill.fore_color.rgb = c_card_bg
        card.line.color.rgb = c_card_border
        tb = s5.shapes.add_textbox(cx + Inches(0.25), card_y + Inches(0.3), card_w3 - Inches(0.5), card_h3 - Inches(0.6))
        tf = tb.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(18)
        p.font.bold = True
        p.font.color.rgb = c_glass
        for item in items:
            p = tf.add_paragraph()
            p.text = f"•  {item}"
            p.font.size = Pt(13)
            p.font.color.rgb = c_muted
            p.space_before = Pt(10)

    # Slide 6: Do's & Don'ts
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6)
    add_header(s6, "Раздел 5 • Brand Integrity", "Правила и строгие ограничения (Do's & Don'ts)")
    c_do = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.9), Inches(1.9), Inches(5.6), Inches(4.9))
    c_do.fill.solid()
    c_do.fill.fore_color.rgb = RGBColor(20, 36, 28)
    c_do.line.color.rgb = RGBColor(52, 211, 153)
    tb_do = s6.shapes.add_textbox(Inches(1.2), Inches(2.1), Inches(5.0), Inches(4.5))
    tf_do = tb_do.text_frame
    tf_do.word_wrap = True
    p = tf_do.paragraphs[0]
    p.text = "✓  ЧТО НУЖНО ДЕЛАТЬ (DO'S)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(52, 211, 153)
    for d in [
        "Использовать цвет «Лазер» (#CC0000) строго как акцент, для логотипа и ключевых кнопок действия.",
        "Использовать «Графит» (#232328) как основной тёмный фон для инженерного, технологичного вида.",
        "Использовать «Стекло» (#EFEFEF) для контрастного текста и полупрозрачных поверхностей.",
        "Применять цвета направлений («Ночь», «Воздух», «Защита») строго внутри соответствующих модулей."
    ]:
        p = tf_do.add_paragraph()
        p.text = f"✓  {d}"
        p.font.size = Pt(13)
        p.font.color.rgb = c_glass
        p.space_before = Pt(12)

    c_dont = s6.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(6.8), Inches(1.9), Inches(5.6), Inches(4.9))
    c_dont.fill.solid()
    c_dont.fill.fore_color.rgb = RGBColor(38, 20, 22)
    c_dont.line.color.rgb = RGBColor(239, 68, 68)
    tb_dont = s6.shapes.add_textbox(Inches(7.1), Inches(2.1), Inches(5.0), Inches(4.5))
    tf_dont = tb_dont.text_frame
    tf_dont.word_wrap = True
    p = tf_dont.paragraphs[0]
    p.text = "✕  ЧТО СТРОГО ЗАПРЕЩЕНО (DON'TS)"
    p.font.size = Pt(18)
    p.font.bold = True
    p.font.color.rgb = RGBColor(239, 68, 68)
    for d in [
        "КРАСИТЬ БОЛЬШИЕ ФОНЫ В КРАСНЫЙ («Лазер») — это перегружает глаза и ломает визуальную иерархию.",
        "ЗАМЕНЯТЬ ЦВЕТ ЛОГОТИПА на цвета направлений («Ночь», «Воздух», «Защита») — логотип всегда красный/белый.",
        "ИСПОЛЬЗОВАТЬ ДОПОЛНИТЕЛЬНЫЕ ЦВЕТА вместо основных в общей корпоративной продукции и одежде.",
        "СМЕШИВАТЬ ОТРАСЛЕВЫЕ ЦВЕТА (например, использовать цвет «Защита» в космическом интерфейсе)."
    ]:
        p = tf_dont.add_paragraph()
        p.text = f"✕  {d}"
        p.font.size = Pt(13)
        p.font.color.rgb = c_glass
        p.space_before = Pt(12)

    prs.save(OUTPUT_PATH)
    print(f"Presentation saved to: {OUTPUT_PATH}")

if __name__ == '__main__':
    build_presentation()
