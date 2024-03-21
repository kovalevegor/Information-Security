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
/*код представляет собой функцию entry0, которая является точкой входа программы.
вызывает несколько других функций, а затем завершает работу Windows*/
/* jsdec pseudo code output */
/* Z:\Terminal...@ 0x43dca5 */
#include <stdint.h>
 
int32_t entry0 (void) {
    int32_t var_10h; /*Объявляет переменную var_10h*/
    eax = 0; /*Инициализирует переменную var_10h значением 0*/
    var_10h = eax;
    eax = 0x43db88;/* -> c8 57 fc ff eb f8 5d c3 1d 00 00 00 90 db 43 00 .W....J.......C.*/
    eax = fcn_00405ec4 (); /*Вызывает функцию fcn_00405ec4 и сохраняет результат в регистре eax*/
    eax = 0;
    *(fs:eax) = esp; /*Сохраняет значение регистра esp в адрес, указанный переменной eax (указатель стека)*/
    eax = &var_10h;
    fcn_00407be0 (); /*Вызывает функцию fcn_00407be0, передавая ей адрес переменной var_10h в качестве параметра*/
    ecx = var_10h; /*Загружает значение переменной var_10h в регистр ecx*/
    edx = 0;
    eax = 0x43dce8;
    fcn_0043db04 (); 
    eax = ExitWindowsEx (1, 0); /*Вызывает функцию ExitWindowsEx с параметрами 1 и 0, что приводит к завершению работы Windows*/
    eax = 0;
    *(fs:eax) = edx;
    eax = &var_10h;
    fcn_004038b4 (); /*Вызывает функцию fcn_004038b4, передавая ей адрес переменной var_10h в качестве параметра*/
    return eax;
}
```
Функция [`ExitWindowsEx`](https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-exitwindowsex) с параметрами `1` и `0`. Функция `ExitWindowsEx` предназначена для завершения работы Windows. Она может **использоваться для:** выключения компьютера, перезагрузки компьютера, завершения сеанса пользователя, смены пользователя. 

**Параметры функции:** 

+ `uFlags:` Флаг, который определяет, как будет завершена работа
+ `dwReserved:` Зарезервированный параметр, который должен быть установлен в 0.


```assembly
/*код представляет собой фрагмент программы, который получает дескриптор модуля,
сохраняет его в нескольких местах памяти и затем вызывает другие функции*/

/* jsdec pseudo code output */
/* Z:\Terminal... @ 0x405ec4 */
#include <stdint.h>
 
void fcn_00405ec4 (void) {
    eax = GetModuleHandleA_1 (0, eax); /*Функция для получения дескриптора модуля для текущего процесса*/
    edx = 0x43e0a4; /*Сохраняет дескриптор модуля в регистре eax*/
    *(0x43f4d4) = eax; /*Записывает значение eax в адрес, указанный в 0x43f4d4*/
    *((edx + 4)) = eax; /*Записывает значение eax в 4 байта после адреса, указанного в edx*/
    *((edx + 8)) = 0; /*Записывает 0 в 8 байт после адреса, указанного в edx*/
    *((edx + 0xc)) = 0; /*Записывает 0 в 12 байт после адреса, указанного в edx*/
    fcn_00405e78 ();
    fcn_0040368c ();
}
```

```assembly
/*код представляет собой фрагмент программы, который получает текущий рабочий каталог
и затем передает его другой функции*/
/* jsdec pseudo code output */
/* Z:\Terminal... @ 0x407be0 */
#include <stdint.h>
 
uint32_t fcn_00407be0 (void) {
    ebx = eax; /*Сохраняет текущее значение регистра eax в регистре ebx*/
    eax = GetCurrentDirectoryA (0x104, esp); /*Использует функцию GetCurrentDirectoryA для получения текущего рабочего каталога*/
    ecx = eax; /*Сохраняет возвращаемое значение GetCurrentDirectoryA в регистре eax*/
    edx = esp; /*Сохраняет значение регистра esp (указатель стека) в регистре edx*/
    eax = ebx; /*Восстанавливает значение регистра eax из регистра ebx*/
    fcn_0040399c (); /*Вызывает функцию fcn_0040399c, передавая ей адрес стека (edx) как параметр*/
    return eax; /*Возвращает значение, которое было в регистре eax до его сохранения в ebx*/
}
```

```assembly
/*код представляет собой фрагмент программы, который инициализирует три переменные,
вызывает неизвестную функцию, получает адрес другой функции,
вызывает ее и, наконец, вызывает ShellExecuteA*/

/* jsdec pseudo code output */
/* Z:\Terminal... @ 0x43db04 */
#include <stdint.h>
 
int32_t fcn_0043db04 (int32_t arg_8h) {
    int32_t var_f0h; /*Объявление переменной var_f0h*/
    int32_t var_a0h; /*Объявление переменной var_a0h*/
    int32_t var_50h; /*Объявление переменной var_50h*/
    edi = ecx; /*Сохраняет значения регистров ecx, edx и eax в локальные переменные*/
    esi = edx;
    ebx = eax;
    eax = arg_8h;
    eax = &var_f0h;
    edx = edi;
    eax = fcn_00407ccc (); /*Использует функцию fcn_00407ccc для инициализации var_f0h, var_a0h и var_50h*/
    eax = &var_a0h;
    edx = esi;
    eax = fcn_00407ccc ();
    eax = &var_50h;
    edx = ebx;
    eax = fcn_00407ccc ();
    eax = *(0x43eb28); /*Получает адрес функции из 0x43eb28*/
    eax = *(eax);
    eax = fcn_0043d97c ();
    ShellExecuteA (eax); /*Вызывает функцию ShellExecuteA с результатом предыдущего вызова в качестве параметра*/
    return eax; /*Возвращает результат вызова ShellExecuteA*/
}
```

Функция [`ShellExecuteA`](https://learn.microsoft.com/en-us/windows/win32/api/shellapi/nf-shellapi-shellexecutea) предназначена для выполнения различных действий с `файлами`, `папками` и `URL-адресами` в Windows. Она может использоваться для: открытия файлов, запуска приложений, просмотра папок, печати файлов, выполнения произвольных команд

**Параметры функции:**

+ `hwnd`: Указатель на окно, которое будет являться владельцем нового окна
+ `lpOperation`: Указатель на строку, которая определяет действие, которое нужно выполнить.
+ `lpFile`: Указатель на строку, которая содержит имя файла, папки или URL-адреса.
+ `lpParameters`: Указатель на строку, которая содержит параметры для команды.
+ `lpDirectory`: Указатель на строку, которая содержит начальный каталог для команды.
+ `nShowCmd`: Флаг, который определяет, как будет показано новое окно.
        
Возвращаемое значение: Функция ShellExecuteA возвращает значение, которое больше 32, если операция прошла успешно. 32 или меньше, если произошла ошибка.


```assembly
/*Декомпилированный код представляет собой фрагмент программы,
который проверяет два значения в памяти, и если они оба равны 0,
то вызывает другую функцию*/
/* jsdec pseudo code output */
/* Z:\Terminal... @ 0x4038b4 */
#include <stdint.h>
 
void fcn_004038b4 (void) {
    edx = *(eax); /*Сохраняет в регистр edx значение из адреса, хранящегося в регистре eax*/
    if (edx != 0) { /* Если значение edx не равно 0*/
        *(eax) = 0; /*Записывает 0 в адрес, хранящийся в регистре eax*/
        ecx = *((edx - 8)); /*Загружает значение из адреса, на 8 байт меньше, чем адрес в регистре edx*/
        ecx--; /*Уменьшает это значение на 1*/
        if (ecx < 0) { /*Если новое значение меньше 0*/
            goto label_0; /*Переходит к метке label_0*/
        }
        *((edx - 8))--; /*Записывает новое значение в адрес, на 8 байт меньше, чем адрес в регистре edx*/
        if (*((edx - 8)) != 0) { /*Если значение не равно 0*/
            goto label_0; /*Переходит к метке label_0*/
        }
        eax = edx - 8; /*Загружает значение из адреса, на 8 байт меньше, чем адрес в регистре edx*/
        fcn_004026d0 (); /*Вызывает функцию fcn_004026d0 с этим адресом в качестве параметра*/
    }
label_0: /*Метка*/
}
```
