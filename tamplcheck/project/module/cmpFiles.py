# coding=utf-8
"""Библиотека для работы с docx файлами"""
import docx


# анализ формата текста файла
def analysis_doc(filename):
    """ анализ формата текста файла
        :param filename: полный путь до файла + его имя
        :return: список раздичных парметров файла"""
    doc = docx.Document(filename)
    list_with_format = []
    dict_with_format = {}
    for paragraph in doc.paragraphs:
        # Имя стиля
        dict_with_format['Style of paragraph'] = paragraph.style.name
        # Горизонтальное выравнивание
        if paragraph.text != '':
            if paragraph.paragraph_format.alignment is None:
                dict_with_format['Horizontal alignment'] = doc.styles[paragraph.style.name].paragraph_format.alignment
            else:
                dict_with_format['Horizontal alignment'] = paragraph.paragraph_format.alignment
        # Отступ слева
        if paragraph.paragraph_format.left_indent is None:
            dict_with_format['Left margin'] = doc.styles[paragraph.style.name].paragraph_format.left_indent
        else:
            dict_with_format['Left margin'] = paragraph.paragraph_format.left_indent
        # Отступ первой строки абзаца
        if paragraph.paragraph_format.first_line_indent is None:
            dict_with_format['Indent the first line of a paragraph'] = \
                doc.styles[paragraph.style.name].paragraph_format.first_line_indent
        else:
            dict_with_format['Indent the first line of a paragraph'] = paragraph.paragraph_format.first_line_indent
        # Отступ справа
        if paragraph.paragraph_format.right_indent is None:
            dict_with_format['Indent on the right'] = doc.styles[paragraph.style.name].paragraph_format.right_indent
        else:
            dict_with_format['Indent on the right'] = paragraph.paragraph_format.right_indent
        # Табуляция
        # print(paragraph.paragraph_format.tab_stops)
        # Интервалы между абзацами
        if paragraph.paragraph_format.space_before is None:
            dict_with_format['Intervals between paragraphs to'] = doc.styles[
                paragraph.style.name].paragraph_format.space_before
        else:
            dict_with_format['Intervals between paragraphs to'] = paragraph.paragraph_format.space_before
        if paragraph.paragraph_format.space_after is None:
            dict_with_format['Intervals between paragraphs after'] = doc.styles[
                paragraph.style.name].paragraph_format.space_after
        else:
            dict_with_format['Intervals between paragraphs after'] = paragraph.paragraph_format.space_after
        # Межстрочный интервал
        if paragraph.paragraph_format.line_spacing is None:
            dict_with_format['Line spacing'] = doc.styles[paragraph.style.name].paragraph_format.line_spacing
        else:
            dict_with_format['Line spacing'] = paragraph.paragraph_format.line_spacing
        # Поведение при встрече с границей страницы
        # print(paragraph.paragraph_format.keep_together)
        # print(paragraph.paragraph_format.keep_with_next)
        # print(paragraph.paragraph_format.page_break_before)
        # print(paragraph.paragraph_format.widow_control)

        for run in paragraph.runs[:1]:
            # Шрифт
            if run.font.name is None:
                dict_with_format['Font'] = doc.styles[paragraph.style.name].font.name
            else:
                dict_with_format['Font'] = run.font.name
            # Размера шрифта
            if run.font.size is None:
                dict_with_format['Font size'] = doc.styles[paragraph.style.name].font.size
            else:
                dict_with_format['Font size'] = run.font.size
            # Курсив
            if run.font.italic is None:
                dict_with_format['Italic'] = doc.styles[paragraph.style.name].font.italic
            else:
                dict_with_format['Italic'] = run.font.italic
            # Жирный
            if run.font.bold is None:
                dict_with_format['Bold'] = doc.styles[paragraph.style.name].font.bold
            else:
                dict_with_format['Bold'] = run.font.bold
            # Подчеркнутый
            if run.font.underline is None:
                dict_with_format['Underline'] = doc.styles[paragraph.style.name].font.underline
            else:
                dict_with_format['Underline'] = run.font.underline
            # Цвет
            if run.font.color.rgb is None:
                dict_with_format['Color'] = str(doc.styles[paragraph.style.name].font.color.rgb)
            else:
                dict_with_format['Color'] = str(run.font.color.rgb)
        dict_with_format['Text'] = paragraph.text
        list_with_format.append(dict_with_format)
        dict_with_format = {}
    return list_with_format


# Функция проверки на соответиствие шаблону
def comparison_algorithm(template, checked):
    counter_for_template = 0
    counter_for_checked = 0
    result = []
    flag_for_lines = 0
    flag_in_block = 0
    mismatch_list = {}
    true_list = {}
    mismatch_blocks = []
    dict_for_blocks = {}
    while counter_for_template < len(template):
        if template[counter_for_template].get('Text') == '':
            flag_for_lines = 1
           # if flag_for_lines == 0:
           #     if checked[counter_for_checked].get('Text') != '':
           #         mismatch_blocks.append("Была пропущена строка в {0} ".format(counter_for_checked))
        elif template[counter_for_template].get('Color') == '000000' \
                or template[counter_for_template].get('Color') == 'None':
            flag_for_lines = 0
            k = 0
            while k < len(checked):
                if template[counter_for_template].get('Text') == checked[k].get('Text'):
                    flag_in_block = 1
                    break
                k += 1
            if flag_in_block == 1:
                dict_for_blocks[counter_for_template] = k
                counter_for_checked = k
            else:
                dict_for_blocks[counter_for_template] = -1
                mismatch_blocks.append("Пункт:'{0}', был пропущен, либо в нем была допущена ошибка.".format(template[counter_for_template].get('Text')))
        else:
            flag_for_lines = 1
        flag_in_block = 0
        counter_for_template += 1
        counter_for_checked += 1
    if mismatch_blocks:
        mismatch_blocks.append("Исправьте структуру проверямого документа для последущей проверки формата.")
        return mismatch_blocks
    counter_for_checked = 0
    counter_for_template = 0
    while counter_for_template < len(template):
        if template[counter_for_template].get('Text') == '':
            counter_for_template += 1
        elif template[counter_for_template].get('Color') == '000000' \
                or template[counter_for_template].get('Color') == 'None':
            if dict_for_blocks.get(counter_for_template) != -1:
                counter_for_checked = dict_for_blocks.get(counter_for_template)
                for key in template[counter_for_template].keys():
                    if template[counter_for_template].get(key) != checked[counter_for_checked].get(key):
                        result.append({"В строке {0} шаблона".format(counter_for_template): {key: template[counter_for_template].get(key)}})
                        result.append({"В строке {0} проверяемого документа".format(counter_for_checked): {key: checked[counter_for_checked].get(key)}})
                counter_for_template += 1
                counter_for_checked += 1
            else:
                counter_for_template += 1
        else:
            i = counter_for_template
            while counter_for_template < len(template):
                if dict_for_blocks.get(counter_for_template) is None:
                    counter_for_template += 1
                else:
                    flag_in_block = dict_for_blocks.get(counter_for_template)
                    break
            if template[i].get('Text') != '':
                for j in range(counter_for_checked, flag_in_block):
                    if checked[j].get('Text') != '':
                        for key in checked[j].keys():
                            if key != 'Text' and key != 'Color':
                                if template[i].get(key) != checked[j].get(key) and checked[j].get('Text') != '':
                                    mismatch_list[key] = checked[j].get(key)
                                    true_list[key] = template[i].get(key)
                        if mismatch_list:
                            result.append({"В строке {0} шаблона".format(counter_for_template - 1): true_list,
                                           "В строке {0} проверяемого документа".format(j - 1): mismatch_list})
                        mismatch_list = {}
                        true_list = {}
    return result


# Считывание файлов
#template_doc = docx.Document("template.docx")
#checked_doc = docx.Document("checked.docx")
#
# словарь, в котором будем хранить информацию о формате текста документа
#template_format = analysis_doc(template_doc)
#checked_format = analysis_doc(checked_doc)
# вывод полей
#for i in range(0, len(checked_format), 2):
#   for j in checked_format[i]:
#       print(j, ":", checked_format[i].get(j))
# вывод отличий файла
#print(comparison_algorithm(template_format, checked_format))
