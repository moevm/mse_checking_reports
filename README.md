# mse_checking_reports
# Tamplcheck

### Коротко о приложении
Основной функцией приложения "tamplcheck" является сравнение содержания 2 файлов(исходного и шаблона) в одинаковом формате. Сарвнение доступно для doc, docx, rtf, odt и в будущем pdf. Файлы должны быть в одинаковом формате. Работа механизма сравнения описана ниже. Также пользователю будет доступен отчет по работе алгоритма сравнения. 


### Запуск
В директории **project** запустите программу **run.sh** следующей командой:
````
./run.sh
````
Если в консоли приходит ответ об отсутствии прав на команду **run.sh**, тогда пропишите в консоли: **chmod +x run.sh**

### Инструменты
+ Flask
+ Docx

Работа модуля:
1) Подключение библиотеки python-docx(на данный момент работает только с docx, обработка doc будет достигнута с помощью конвертера doc в docx)
2) Для получения объекта документа используем функцию Document.
3) После получения объекта, мы можем обратится к списку параграфов.
Передаем объект Document, в функцию analysis_doc(), где происходит анализ каждого из абзаца. Данная функция возвращает список словарей, которые содержат информацию о формате данного абзаца(стиль, шрифт, цвет текса, размер шрифта, различные отступы и т.д.): 

Стиль абзаца : List Paragraph
Горизонтальное выравнивание : None
Отступ слева : 457200
Отступ первой строки абзаца : None
Отступ справа : None
Интервалы между абзацами до : None
Интервалы между абзацами после : 127000
Межстрочный интервал : 1.15
Шрифт : Times New Roman
Размера шрифта : 177800
Курсив : None
Жирный : None
Подчеркнутый : None
Цвет : None

4) После получения списков с информацией о шаблоне и проверяемом документе, списки передаются в функцию comparison_algorithm() где происходит сравнение документов. 
5) Описание алгоритма сравнения(находится на стадии доработки, одна из возможных реализаций):
  На данный момент происходит сравнение всех абзацев по порядку, но с учетом жирных заголовков, т.е. если после абзаца с жирным шрифтом, идет несколько абзацев с обычным текстом, они будут рассматриваться как один блок, это сделано для того, чтобы программа корекктно сравнивала документы с разным количеством абзацев текста в разделе. Пример: у одного студента описание "Цели работы" заняло 2 абзаца, у другого этот же раздел занял 3 абзаца, если бы сравнивались абзацы по порядку, произошел бы сбой индексов и  мы получили бы уведомление о не соответствии шаблона и проверяемого документа, а так произойдет проверка блоков на соответсвие друг другу и ошибки не произойдет. 
6) Функция возвращает True, если не было найдено отличий, в ином случае - список из номеров абзаца и словарей с отличающимися полями.  

### Пример работы
1) Запустим приложение в консоли  
![Начальный запуск](https://github.com/Villain123/images/blob/master/2.png)
2) Перейдем в браузер и впишем "localhost:5000"
![Открытие браузера](https://github.com/Villain123/images/blob/master/3.png)
3) Нажмем на кнопку загрузить документ
![Загрузка документа](https://github.com/Villain123/images/blob/master/4.png)
