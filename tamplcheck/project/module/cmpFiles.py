#import docx


# анализ формата текста файла
def analysis_doc(doc):
    list_with_format = []
    dict_with_format = {}
    for paragraph in doc.paragraphs:
        # Имя стиля
        dict_with_format['Стиль абзаца'] = paragraph.style.name
        # Текст абзаца
        dict_with_format['Текст абзаца'] = paragraph.text
        # Горизонтальное выравнивание
        if paragraph.paragraph_format.alignment is None:
            dict_with_format['Горизонтальное выравнивание'] = doc.styles[
                paragraph.style.name].paragraph_format.alignment
        else:
            dict_with_format['Горизонтальное выравнивание'] = paragraph.paragraph_format.alignment
        # Отступ слева
        if paragraph.paragraph_format.left_indent is None:
            dict_with_format['Отступ слева'] = doc.styles[paragraph.style.name].paragraph_format.left_indent
        else:
            dict_with_format['Отступ слева'] = paragraph.paragraph_format.left_indent
        # Отступ первой строки абзаца
        if paragraph.paragraph_format.first_line_indent is None:
            dict_with_format['Отступ первой строки абзаца'] = doc.styles[
                paragraph.style.name].paragraph_format.first_line_indent
        else:
            dict_with_format['Отступ первой строки абзаца'] = paragraph.paragraph_format.first_line_indent
        # Отступ справа
        if paragraph.paragraph_format.right_indent is None:
            dict_with_format['Отступ справа'] = doc.styles[paragraph.style.name].paragraph_format.right_indent
        else:
            dict_with_format['Отступ справа'] = paragraph.paragraph_format.right_indent
        # Табуляция
        # print(paragraph.paragraph_format.tab_stops)
        # Интервалы между абзацами
        if paragraph.paragraph_format.space_before is None:
            dict_with_format['Интервалы между абзацами до'] = doc.styles[
                paragraph.style.name].paragraph_format.space_before
        else:
            dict_with_format['Интервалы между абзацами до'] = paragraph.paragraph_format.space_before
        if paragraph.paragraph_format.space_after is None:
            dict_with_format['Интервалы между абзацами после'] = doc.styles[
                paragraph.style.name].paragraph_format.space_after
        else:
            dict_with_format['Интервалы между абзацами после'] = paragraph.paragraph_format.space_after
        # Межстрочный интервал
        if paragraph.paragraph_format.line_spacing is None:
            dict_with_format['Межстрочный интервал'] = doc.styles[paragraph.style.name].paragraph_format.line_spacing
        else:
            dict_with_format['Межстрочный интервал'] = paragraph.paragraph_format.line_spacing
        # Поведение при встрече с границей страницы
        # print(paragraph.paragraph_format.keep_together)
        # print(paragraph.paragraph_format.keep_with_next)
        # print(paragraph.paragraph_format.page_break_before)
        # print(paragraph.paragraph_format.widow_control)
        for run in paragraph.runs[:1:]:
            # Шрифт
            if run.font.name is None:
                dict_with_format['Шрифт'] = doc.styles[paragraph.style.name].font.name
            else:
                dict_with_format['Шрифт'] = run.font.name
            # Размера шрифта
            if run.font.size is None:
                dict_with_format['Размера шрифта'] = doc.styles[paragraph.style.name].font.size
            else:
                dict_with_format['Размера шрифта'] = run.font.size
            # Курсив
            if run.font.italic is None:
                dict_with_format['Курсив'] = doc.styles[paragraph.style.name].font.italic
            else:
                dict_with_format['Курсив'] = run.font.italic
            # Жирный
            if run.font.bold is None:
                dict_with_format['Жирный'] = doc.styles[paragraph.style.name].font.bold
            else:
                dict_with_format['Жирный'] = run.font.bold
            # Подчеркнутый
            if run.font.underline is None:
                dict_with_format['Подчеркнутый'] = doc.styles[paragraph.style.name].font.underline
            else:
                dict_with_format['Подчеркнутый'] = run.font.underline
            # Цвет
            if run.font.color.rgb is None:
                dict_with_format['Цвет'] = doc.styles[paragraph.style.name].font.color.rgb
            else:
                dict_with_format['Цвет'] = run.font.color.rgb
        list_with_format.append(dict_with_format)
        dict_with_format = {}
    return list_with_format


# Функция проверки на соответиствие шаблону(в разработке)
# def comparison_algorithm(template, checked):
#    i = 0
#    j = 0
#    while i < len(template):
#        if template[i]['Жирный']:
#            for elem in template[i]:
#                template[i][elem] = checked[j][elem]
#                flag = 1
#        elif:
#
#        i += 1


# Считывание файлов
#template = docx.Document()
#checked_doc = docx.Document()

# словарь, в котором будем хранить информацию о формате текста документа
#template_format = analysis_doc(template)
#checked_format = analysis_doc(checked_doc)
#for i in template_format:
#    for j in i:
#        print(j, ":", i.get(j))
# print(comparison_algorithm(template_format,checked_format)
