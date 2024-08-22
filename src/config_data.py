class Settings:
    poppler_path = r"poppler-22.12.0\Library\bin"
    tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    tesseract_lang = "rus"
    tesseract_config = "--psm 4"
    height_header = 0.14

    regex_tgc = r"(?<=[Адреспоал]{5}\W).{10,90}(?=[Ном]{3})"
    regex_tek = r"(?<=[Адрепсаол]{5}\W).{10,90}(?=[строС]{4})"
    regex_pte = r"(?<=[Адрепасол]{5}\W).{10,90}(?=[Ккодл]{3})"
    regex_te = r"(?<=[Адреспаол]{5}\W).{15,90}(?=[Тел]{3})"
    regex_oth = r"(?<=[Адреспоал]{5}\W).{20,90}(?=$)"

    regex_period = r"\w{3,}\s\d{4}|(?<=по\s\d{2}.)\d{2}\.\d{4}|(?<=за\s)\w{3,8}\s*\d{4}"


settings = Settings()


# psm
# 0 Только ориентация и обнаружение скриптов (OSD).
# 1 Автоматическая сегментация страницы с помощью экранного меню.
# 2 Автоматическая сегментация страницы, но без экранного меню или распознавания текста. (не реализовано)
# 3 Полностью автоматическая сегментация страницы, но без экранного меню. (По умолчанию)
# 4 Предполагается, что используется один столбец текста переменного размера.
# 5 Предполагается, что это один однородный блок текста, выровненный по вертикали.
# 6 Предполагается, что это один единообразный блок текста.
# 7 Обрабатывайте изображение как единую текстовую строку.
# 8 Обрабатывайте изображение как одно слово.
# 9 Обрабатывайте изображение как одно слово в круге.
# 10 Обрабатывайте изображение как один символ.
# 11 Разреженный текст. Найдите как можно больше текста без определенного порядка.
# 12 Разреженный текст с помощью экранного меню.
# 13 Необработанная строка. Обрабатывайте изображение как единую текстовую строку, минуя хаки, специфичные для Tesseract.
