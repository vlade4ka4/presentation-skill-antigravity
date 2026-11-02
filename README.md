# Проект: Брендбук ОАО «Пеленг» & Дизайн-система (Хакатон 2026)

## 📁 Структура проекта

```text
c:\хахатон\
├── assets/                          # Графические ассеты и визуализации
│   └── peleng_colors_palette.png    # Лист палитры 1920x1080 (все 7 цветов с кодировками)
│
├── docs/                            # Документация и ТЗ для тимейтов
│   └── PELENG_BRANDBOOK_GUIDELINES.md # Полная спецификация, CSS/Tailwind токены, правила
│
├── presentations/                   # Готовые презентации для команды и стейкхолдеров
│   ├── peleng_brandbook_tz.pptx     # 100% редактируемая презентация PowerPoint (16:9)
│   ├── peleng_brandbook_preview.html# Интерактивный веб-просмотр в браузере
│   └── demo/                        # Демонстрационные шаблоны
│
├── scripts/                         # Автоматизация и утилиты
│   ├── parsers/                     # Парсинг и сбор данных с официального сайта
│   │   ├── fetch_peleng_brandbook.py # Скрипт выгрузки и парсинга
│   │   └── raw/                     # Сырые данные (HTML и JSON)
│   │       ├── peleng_full.html
│   │       └── parsed_brandbook.json
│   │
│   └── generators/                  # Скрипты повторной сборки ассетов
│       ├── generate_palette_img.py  # Перегенерация картинки палитры
│       └── generate_peleng_pptx.py  # Перегенерация файла презентации .pptx
│
└── .agents/                         # Локальные настройки агента Antigravity
```

## 🚀 Быстрый старт

1. **Смотреть цвета на картинке:** [`assets/peleng_colors_palette.png`](assets/peleng_colors_palette.png)
2. **Читать ТЗ по разработке:** [`docs/PELENG_BRANDBOOK_GUIDELINES.md`](docs/PELENG_BRANDBOOK_GUIDELINES.md)
3. **Открыть презентацию в PowerPoint:** [`presentations/peleng_brandbook_tz.pptx`](presentations/peleng_brandbook_tz.pptx)
4. **Открыть презентацию в браузере:** [`presentations/peleng_brandbook_preview.html`](presentations/peleng_brandbook_preview.html)
