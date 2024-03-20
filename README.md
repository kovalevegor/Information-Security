# Компьютерные вирусы

<br>

<img width="150" height="150" align="center" style="float: left; margin: 0 10px 0 0;" alt="Cutter logo" src="https://raw.githubusercontent.com/rizinorg/cutter/dev/src/img/cutter.svg?sanitize=true"> Для исследования demo-вируса был использован [Cutter](https://cutter.re/), основанный на фреймворке [Radare2](https://www.radare.org/n/radare2.html).<img width="128" height="57" align="center" style="float: left; margin: 0 10px 0 0;" alt="Cutter logo" src="https://github.com/radareorg/radare2/raw/master/doc/images/r2emoji.png">

---

<br>

# ОБЗОР
### Информация

| | | | | | |
---|---|---|---|---|---
|**Файл** | `drop.exe` | **FD:** | 3 | **Архитектура:** | x86 |
|**Формат:**|pe|**Базовый адрес:**|0x00400000|**Устройство:**|i386|
|**Биты:**|32|**Виртуальный адрес:**|True|**ОС:**|windows|
|**Класс:**|PE32|**Canary:**|False|**Подсистема:**|Windows GUI|
|**Режим:**|r-x|**Crypto:**|False|**Пустой:**|False|
|**Размер:**|283 kB|**NX bit:**|False|**Relocs:**|False|
|**Тип:**|EXEC (Executable file)|**PIC:**|False|**Порядок байтов:**|LE|
|**Язык:**|c|**Static:**|False|**Скомпилирован:**|Jun 20 06:22:17 1992 UTC+8|
|| |**Relro:**|N/A|**Компилятор:**|Н/Д|

**Важные элементы** 

+ Программа написана на языке `C`
+ `0x00400000` - адрес в памяти, по которому будет загружен код программы при запуске.
+ Порядок байтов: LE означает, что байты в файле хранятся в порядке от младшего к старшему (little endian).
+ FD: 3 - число, использующееся для определения того, как будут загружаться и выгружаться DLL-библиотеки, используемые программой.
+ Размер кода: 249856 bytes

### Декомпилированный код
```c
/* jsdec pseudo code output */
/* Z:\Terminal...@ 0x43dca5 */
#include <stdint.h>
 
int32_t entry0 (void) {
    int32_t var_10h;
    eax = 0;
    var_10h = eax;
    eax = 0x43db88;
    eax = fcn_00405ec4 ();
    eax = 0;
    *(fs:eax) = esp;
    eax = &var_10h;
    fcn_00407be0 ();
    ecx = var_10h;
    edx = 0;
    eax = 0x43dce8;
    fcn_0043db04 ();
    eax = ExitWindowsEx (1, 0);
    eax = 0;
    *(fs:eax) = edx;
    eax = &var_10h;
    fcn_004038b4 ();
    return eax;
}
```

+ Декомпилированный код C представляет собой функцию entry0, которая является точкой входа программы.
+ Эта функция выполняет следующие действия:
 1. Инициализирует переменную var_10h значением 0.
 2. Вызывает функцию fcn_00405ec4.
 3. Сохраняет значение регистра ESP в адрес, указанный переменной eax.
 4. Вызывает функцию fcn_00407be0, передавая ей адрес var_10h.
 5. Формирует аргументы ecx = var_10h и edx = 0 и вызывает функцию fcn_0043db04.
 6. Вызывает ExitWindowsEx с параметрами 1 и 0.
 7. Восстанавливает значение регистра ESP из адреса, указанного переменной eax.
 8. Вызывает функцию fcn_004038b4, передавая ей адрес var_10h.
 9. Возвращает значение 0.

+ Особенности:
1. Код использует регистры eax, ecx и edx для хранения данных и передачи параметров функциям.
2. Используются функции fcn_00405ec4, fcn_00407be0, fcn_0043db04 и ExitWindowsEx.
3. Значение переменной var_10h используется несколько раз.

Ограничения:

    Без информации о функциях fcn_00405ec4, fcn_00407be0 и fcn_0043db04 сложно полностью понять функциональность декомпилированного кода.
    Неясно, что происходит с данными, которые передаются и возвращаются функциями.
    Неясно, как код взаимодействует с операционной системой.

```c
/* jsdec pseudo code output */
/* Z:\Terminal... @ 0x405ec4 */
#include <stdint.h>
 
void fcn_00405ec4 (void) {
    eax = GetModuleHandleA_1 (0, eax);
    edx = 0x43e0a4;
    *(0x43f4d4) = eax;
    *((edx + 4)) = eax;
    *((edx + 8)) = 0;
    *((edx + 0xc)) = 0;
    fcn_00405e78 ();
    fcn_0040368c ();
}
```


    Декомпилированный код C представляет собой функцию fcn_00405ec4.
    Эта функция выполняет следующие действия:
        Получает дескриптор модуля для текущего процесса, используя GetModuleHandleA_1.
        Сохраняет дескриптор модуля в переменной eax.
        Записывает значение eax в адрес, указанный в 0x43f4d4.
        Записывает значение eax в 4 байта после адреса, указанного в edx.
        Записывает 0 в 8 байт после адреса, указанного в edx.
        Записывает 0 в 12 байт после адреса, указанного в edx.
        Вызывает функцию fcn_00405e78.
        Вызывает функцию fcn_0040368c.

Особенности:

    Код использует регистры eax, edx для хранения данных.
    Используются функции GetModuleHandleA_1, fcn_00405e78 и fcn_0040368c.
    Дескриптор модуля используется несколько раз.

Ограничения:

    Без информации о функциях fcn_00405e78 и fcn_0040368c сложно полностью понять функциональность декомпилированного кода.
    Неясно, что происходит с данными, которые передаются и возвращаются функциями.

```c
/* jsdec pseudo code output */
/* Z:\Terminal\Edu\Academic\3Course\Информационная @ 0x407be0 */
#include <stdint.h>

uint32_t fcn_00407be0 (void) {
    ebx = eax;
    eax = GetCurrentDirectoryA (0x104, esp);
    ecx = eax;
    edx = esp;
    eax = ebx;
    fcn_0040399c ();
    return eax;
}
```
Функциональность:

    Декомпилированный код C представляет собой функцию fcn_00407be0.
    Эта функция выполняет следующие действия:
        Сохраняет значение регистра eax в регистре ebx.
        Вызывает GetCurrentDirectoryA, чтобы получить текущий рабочий каталог.
        Сохраняет возвращаемое значение GetCurrentDirectoryA в регистре ecx.
        Сохраняет значение регистра esp в регистре edx.
        Восстанавливает значение регистра eax из регистра ebx.
        Вызывает функцию fcn_0040399c.
        Возвращает значение регистра eax.

Особенности:

    Код использует регистры eax, ebx, ecx, edx для хранения данных.
    Используются функции GetCurrentDirectoryA и fcn_0040399c.
    Текущий рабочий каталог используется как параметр функции fcn_0040399c.

Ограничения:

    Без информации о функции fcn_0040399c сложно полностью понять функциональность декомпилированного кода.
    Неясно, что происходит с данными, которые передаются и возвращаются функциями.
```c
/* jsdec pseudo code output */
/* Z:\Terminal... @ 0x4063b8 */
#include <stdint.h>
 
void ExitWindowsEx (void) {
}
```

Анализ декомпилированного кода C

Функциональность:

    Декомпилированный код C представляет собой функцию ExitWindowsEx.
    Эта функция не имеет параметров и не возвращает значения.

Особенности:

    Код не содержит никаких инструкций.

Ограничения:

    Из-за отсутствия инструкций невозможно определить, что делает эта функция.
