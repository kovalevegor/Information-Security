# Информационная безопасность . Лабораторная работа 1

# Контрольные вопросы 
### 1.	Представить сходство и отличия одноключевых блочных шифров.

Одноключевые блочные шифры - это класс криптографических алгоритмов, которые шифруют данные блоками определенной длины с использованием одного ключа для шифрования и дешифрования. 

**Сходства одноключевых блочных шифров:**

+ Все они используют ключ для шифрования и дешифрования данных.
+ Все они работают с данными, разбитыми на блоки определенной длины.
+ Все они выполняют серию простых математических операций над блоками данных для обеспечения конфиденциальности и целостности информации.
+ Все они обычно состоят из определенного количества раундов, каждый из которых выполняет определенные математические операции над данными.

**Различия одноключевых блочных шифров:**

+ Размер блока: некоторые шифры работают с блоками размером 64 бита (например, AES), другие с блоками большего или меньшего размера.
+ Количество раундов: разные шифры могут иметь разное количество раундов.
+ Математические операции: в разных шифрах могут использоваться разные математические операции, такие как сложение, умножение, исключающее ИЛИ и т.д.

---

### 2.	Что определяет выбор размерности таблицы.

Выбор размерности таблицы определяется количеством символов, которые нужно зашифровать. Чем больше символов в тексте, тем больше размерность таблицы нужно выбрать

---

### 3.	Для чего нужно ключевое слово?

Ключевое слово используется для установления правил шифрования и расшифрования данных. Оно является секретным элементом, который определяет способ преобразования текста. Без ключевого слова невозможно правильно расшифровать зашифрованные данные

---


# Задание на выполнение лабораторной работы:

### 1.	Используя простейший шифр перестановки зашифровать следующий текст: «Безопасность — это самая опасная иллюзия». Размеры таблицы задайте самостоятельно. 

Для выполнения лабораторной работы по шифру перестановки можно использовать, например, таблицу размером 4x9 (4 строки и 9 столбцов). Зашифруем текст "Безопасность — это самая опасная иллюзия" следующим образом:

1. Запишем текст построчно в таблицу:

| | | | | | | | | |
---|---|---|---|---|---|---|---|---
Б | Е | З | О | П | А | С | Н | О 
С | Т | Ь | - | Э | Т | О | С | А 
М | А | Я | О | П | А | С | Н | А 
Я | И | Л | Л | Ю | З | И | Я |

2. Зашифруем текст, читая его по столбцам:

БСМЯ ЕТАИ ЗЬЯЛ О-ОЛ ПЭПЮ АТАЗ СОСИ НСНЯ ОАА

Таким образом, текст "Безопасность — это самая опасная иллюзия" зашифрован шифром перестановки.

---

### 2.	Используя шифр простой перестановки (рис. 1.5) зашифровать вышеприведенный текст. Размер блока 6, ключевое слово придумать самостоятельно.
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---
Б | Е | З | О | П | А | С | Н | О | С | Т | Ь | - | Э | Т | О | С | А | М | А | Я | О | П | А | С | Н | А | Я | И | Л | Л | Ю | З | И | Я
| | | | | | | | | | К | О | Р | Е | Н | Ь | | | | | | | | | | | | | | | | | |
| | | | | | | | | | 4 | 2 | 1 | 3 | 5 | 6 | | | | | | | | | | | | | | | | | |
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
| 4 | 2 | 1 | 3 | 5 | 6 | 4 | 2 | 1 | 3 | 5 | 6 | 4 | 2 | 1 | 3 | 5 | 6 | 4 | 2 | 1 | 3 | 5 | 6 | 4 | 2 | 1 | 3 | 5 | 6 | 4 | 2 | 1 | 3 | 5 | 6 |
О | Е | Б | З | П | А | C | Н | С | О | Т | Ь | О | Э | - | Т | С | А | О | А | М | Я | П | А | Я | Н | С | А | И | Л | З | Л | Л | Ю | И | Я

Таким образом мы получаем следующее сообщение: 

ОЕБЗПАCНСОТЬОЭ-ТСАОАМЯПАЯНСАИЛЗЛЛЮИЯ

---

### 3.	Используя прежнее ключевое слово, зашифруйте ту же фразу с помощью таблицы 

Ключь - 4 2 1 3 5 6 

| | | | | | | | | | | | | |
---|---|---|---|---|---|---|---|---|---|---|---|---
1 | 2 | 3 | 4 | 5 | 6 | $\to$ | 4 | 2 | 1 | 3 | 5 | 6
Б | Е | З | О | П | А | $\to$ | О | Е | Б | З | П | А 
С | Н | О | С | Т | Ь | $\to$ | C | Н | С | О | Т | Ь
\-| Э | Т | О | С | А | $\to$ | О | Э | - | Т | С | А
М | А | Я | О | П | А | $\to$ | О | А | М | Я | П | А
С | Н | А | Я | И | Л | $\to$ | Я | Н | С | А | И | Л
Л | Ю | З | И | Я |   | $\to$ | З | Л | Ю | И | Я | 

Таким образом мы получаем следующее сообщение: 

ОЕБЗПАCНСОТЬОЭ-ТСАОАМЯПАЯНСАИЛЗЛЛЮИЯ


### 4.	Зашифровать вышеприведенную фразу с использованием «магических квадратов» (рис. 1.7). «Магический квадрат» можно использовать любой размерности, в том числе придуманный самостоятельно.
| | | | | | |
---|---|---|---|---|---
35|26|1|19|6|24
8|17|28|10|33|15
3|21|32|23|7|25
30|12|5|14|34|16
31|22|9|27|2|20
4|13|36|18|29|11

### 5.	Определите ключи шифра Цезаря, если известны следующие пары открытый текст – шифротекст (исходный алфавит: АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ): 
`АПЕЛЬСИН - ТВЧЮОДЫА`

КЛЮЧ - 19

`МАНДАРИН – ТЁУЙЁЦОУ`

КЛЮЧ - 6

### 6.	Расшифруйте следующие сообщения, зашифрованные шифром Цезаря, и определите ключ n, 0<n<33, если известно, что исходные сообщения составлены из алфавита АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ: 
`ЮВПЛШУХ` - `УЧЕБНИК` К = 11

`СФЫЮБШЯФУ` - `ВЕЛОСИПЕД` К = 16
