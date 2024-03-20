# Компьютерные вирусы

<br>

<img width="150" height="150" align="right" style="float: left; margin: 0 10px 0 0;" alt="Cutter logo" src="https://raw.githubusercontent.com/rizinorg/cutter/dev/src/img/cutter.svg?sanitize=true"> Для исследования demo-вируса был использован [Cutter](https://cutter.re/)

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

### Важные элементы 

+ Программа написана на языке `C`
+ `0x00400000` - адрес в памяти, по которому будет загружен код программы при запуске.
+ Порядок байтов: LE означает, что байты в файле хранятся в порядке от младшего к старшему (little endian).
+ FD: 3 - число, использующееся для определения того, как будут загружаться и выгружаться DLL-библиотеки, используемые программой.
+ Размер кода: 249856 bytes

**Декомпилированный код**
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
