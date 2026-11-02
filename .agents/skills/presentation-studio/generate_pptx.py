import sys
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_sample_deck(output_path):
    prs = Presentation()
    # 16:9 widescreen (13.333 x 7.5 inches)
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    
    blank_layout = prs.slide_layouts[6]
    
    # Colors
    c_bg = RGBColor(11, 15, 25)          # #0b0f19
    c_card = RGBColor(22, 31, 48)        # #161f30
    c_accent = RGBColor(56, 189, 248)    # #38bdf8
    c_text = RGBColor(248, 250, 252)     # #f8fafc
    c_muted = RGBColor(148, 163, 184)    # #94a3b8
    c_border = RGBColor(40, 53, 76)
    
    # Slide 1: Cover
    slide1 = prs.slides.add_slide(blank_layout)
    bg1 = slide1.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = c_bg
    bg1.line.fill.background()
    
    # Badge
    badge_box = slide1.shapes.add_textbox(Inches(1.2), Inches(1.8), Inches(4.5), Inches(0.5))
    tf_badge = badge_box.text_frame
    tf_badge.word_wrap = True
    p_b = tf_badge.paragraphs[0]
    p_b.text = "✦ ХАКАТОН 2026 | ПРЕЗЕНТАЦИЯ РЕШЕНИЯ"
    p_b.font.size = Pt(13)
    p_b.font.bold = True
    p_b.font.color.rgb = c_accent
    p_b.font.name = "Segoe UI"
    
    # Title
    title_box = slide1.shapes.add_textbox(Inches(1.2), Inches(2.5), Inches(10.5), Inches(2.2))
    tf_title = title_box.text_frame
    tf_title.word_wrap = True
    p_t = tf_title.paragraphs[0]
    p_t.text = "Интеллектуальная AI-система для анализа и автоматизации"
    p_t.font.size = Pt(40)
    p_t.font.bold = True
    p_t.font.color.rgb = c_text
    p_t.font.name = "Segoe UI"
    
    # Subtitle
    sub_box = slide1.shapes.add_textbox(Inches(1.2), Inches(4.7), Inches(10), Inches(1.5))
    tf_sub = sub_box.text_frame
    tf_sub.word_wrap = True
    p_s = tf_sub.paragraphs[0]
    p_s.text = "Автономные агенты, мгновенная обработка данных и кратный рост производительности."
    p_s.font.size = Pt(20)
    p_s.font.color.rgb = c_muted
    p_s.font.name = "Segoe UI"
    
    # Slide 2: Bento Grid 3 cards
    slide2 = prs.slides.add_slide(blank_layout)
    bg2 = slide2.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(13.333), Inches(7.5))
    bg2.fill.solid()
    bg2.fill.fore_color.rgb = c_bg
    bg2.line.fill.background()
    
    # Header
    h_box = slide2.shapes.add_textbox(Inches(1.2), Inches(0.8), Inches(10.5), Inches(1.2))
    tf_h = h_box.text_frame
    p_h1 = tf_h.paragraphs[0]
    p_h1.text = "МЕТРИКИ И РЕЗУЛЬТАТЫ"
    p_h1.font.size = Pt(12)
    p_h1.font.bold = True
    p_h1.font.color.rgb = c_accent
    p_h1.font.name = "Segoe UI"
    
    p_h2 = tf_h.add_paragraph()
    p_h2.text = "Ключевые показатели эффективности"
    p_h2.font.size = Pt(28)
    p_h2.font.bold = True
    p_h2.font.color.rgb = c_text
    p_h2.font.name = "Segoe UI"
    
    # 3 Cards
    cards_data = [
        ("10×", "Скорость работы", "Ускорение аналитических циклов и генерации отчетов"),
        ("−70%", "Рутинные операции", "Освобождение времени сотрудников от монотонных задач"),
        ("99.4%", "Точность моделей", "Минимизация ошибок за счет архитектуры верификации")
    ]
    
    card_w = Inches(3.4)
    card_h = Inches(3.8)
    card_y = Inches(2.4)
    card_gap = Inches(0.35)
    start_x = Inches(1.2)
    
    for i, (metric, title, desc) in enumerate(cards_data):
        cx = start_x + i * (card_w + card_gap)
        card_shape = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y, card_w, card_h)
        card_shape.fill.solid()
        card_shape.fill.fore_color.rgb = c_card
        card_shape.line.color.rgb = c_border
        card_shape.line.width = Pt(1.5)
        
        # Text inside card
        tb = slide2.shapes.add_textbox(cx + Inches(0.3), card_y + Inches(0.4), card_w - Inches(0.6), card_h - Inches(0.8))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p_m = tf.paragraphs[0]
        p_m.text = metric
        p_m.font.size = Pt(44)
        p_m.font.bold = True
        p_m.font.color.rgb = c_accent
        p_m.font.name = "Segoe UI"
        
        p_t = tf.add_paragraph()
        p_t.text = title
        p_t.font.size = Pt(18)
        p_t.font.bold = True
        p_t.font.color.rgb = c_text
        p_t.font.name = "Segoe UI"
        p_t.space_before = Pt(16)
        
        p_d = tf.add_paragraph()
        p_d.text = desc
        p_d.font.size = Pt(13)
        p_d.font.color.rgb = c_muted
        p_d.font.name = "Segoe UI"
        p_d.space_before = Pt(8)
        
    prs.save(output_path)
    print(f"Presentation saved successfully to: {output_path}")

if __name__ == "__main__":
    create_sample_deck(r"c:\хахатон\presentation_demo.pptx")
