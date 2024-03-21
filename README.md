# <p align="center">Компьютерные вирусы</p>

<img width="150" height="150" align="center" style="float: left; margin: 0 10px 0 0;" alt="Cutter logo" src="https://raw.githubusercontent.com/rizinorg/cutter/dev/src/img/cutter.svg?sanitize=true"> Для исследования `drop.exe` был использован [Cutter](https://cutter.re/), основанный на фреймворке [Radare2](https://www.radare.org/n/radare2.html).



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
```assembly
/* jsdec pseudo code output */
/* Z:\Terminal...@ 0x43dca5 */
#include <stdint.h>
 
int32_t entry0 (void) {
    int32_t var_10h;
    eax = 0;
    var_10h = eax;
    eax = 0x43db88;/* -> c8 57 fc ff eb f8 5d c3 1d 00 00 00 90 db 43 00 .W....J.......C.*/
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

+ Декомпилированный код C представляет собой функцию `entry0`, которая является точкой входа программы.
+ Эта функция выполняет следующие действия:
1. Инициализирует переменную `var_10h` значением `0`.
2. Вызывает функцию `fcn_00405ec4`.
3. Сохраняет значение регистра `ESP` в адрес, указанный переменной `eax`.
4. Вызывает функцию `fcn_00407be0`, передавая ей адрес `var_10h`.
5. Формирует аргументы `ecx = var_10h` и `edx = 0` и вызывает функцию `fcn_0043db04`.
6. Вызывает `ExitWindowsEx` с параметрами `1` и `0`.
7. Восстанавливает значение регистра `ESP` из адреса, указанного переменной `eax`.
8. Вызывает функцию `fcn_004038b4`, передавая ей адрес `var_10h`.
9. Возвращает значение `0`.

```assembly
/* jsdec pseudo code output */
/* Z:\Terminal\Edu\Academic\3Course\Информационная @ 0x405ec4 */
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

```assembly
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

```assembly
/* jsdec pseudo code output */
/* Z:\Terminal\Edu\Academic\3Course\Информационная @ 0x43db04 */
#include <stdint.h>
 
int32_t fcn_0043db04 (int32_t arg_8h) {
    int32_t var_f0h;
    int32_t var_a0h;
    int32_t var_50h;
    edi = ecx;
    esi = edx;
    ebx = eax;
    eax = arg_8h;
    eax = &var_f0h;
    edx = edi;
    eax = fcn_00407ccc ();
    eax = &var_a0h;
    edx = esi;
    eax = fcn_00407ccc ();
    eax = &var_50h;
    edx = ebx;
    eax = fcn_00407ccc ();
    eax = *(0x43eb28);
    eax = *(eax);
    eax = fcn_0043d97c ();
    ShellExecuteA (eax);
    return eax;
}
```

```assembly
/* jsdec pseudo code output */
/* Z:\Terminal\Edu\Academic\3Course\Информационная @ 0x4038b4 */
#include <stdint.h>
 
void fcn_004038b4 (void) {
    edx = *(eax);
    if (edx != 0) {
        *(eax) = 0;
        ecx = *((edx - 8));
        ecx--;
        if (ecx < 0) {
            goto label_0;
        }
        *((edx - 8))--;
        if (*((edx - 8)) != 0) {
            goto label_0;
        }
        eax = edx - 8;
        fcn_004026d0 ();
    }
label_0:
}
```
