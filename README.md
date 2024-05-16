# <p align = "center">Стандарты аутентичного шифрования</p>

[crypto++](https://www.cryptopp.com/) | [AES](https://www.cryptopp.com/wiki/Advanced_Encryption_Standard) | [git lib rep](https://github.com/weidai11/cryptopp) | [helping hand](https://www.youtube.com/watch?v=5XE4zEN-WKg)

Программа на `C++`, представленная ниже, демонстрирует использование библиотеки `Crypto++` для обеспечения конфиденциальности и аутентичности данных. Она использует режим шифрования `CBC` для обеспечения конфиденциальности и `HMAC-SHA256` для аутентификации сообщений.

### Возможности использования

1. **Конфиденциальность и аутентичность данных**:
   - Программа обеспечивает шифрование данных, чтобы они оставались конфиденциальными.
   - Использование `HMAC-SHA256` для аутентификации гарантирует, что данные не были изменены в процессе передачи.

2. **Управление ключами**:
   - Программа генерирует ключи шифрования и аутентификации на основе пароля, что позволяет использовать парольную аутентификацию для шифрования данных.

3. **Поддержка различных сообщений и паролей**:
   - Сообщение и пароль могут быть заданы через аргументы командной строки, что делает программу гибкой и удобной для использования в различных сценариях.

### Код для полноценного приложения

```cpp
#include <iostream>                // Подключение стандартной библиотеки ввода-вывода
#include <string>                  // Подключение стандартной библиотеки строк
#include <cryptlib.h>              // Подключение Crypto++ библиотеки
#include <aes.h>                   // Подключение модуля AES
#include <cbcmac.h>                // Подключение модуля CBCMAC
#include <filters.h>               // Подключение фильтров Crypto++ библиотеки
#include <hmac.h>                  // Подключение модуля HMAC
#include <sha.h>                   // Подключение модуля SHA
#include <secblock.h>              // Подключение модуля SecBlock
#include <osrng.h>                 // Подключение генератора случайных чисел
#include <hex.h>                   // Подключение модуля HEX
#include "rijndael.h"              // Подключение модуля Rijndael
#include "modes.h"                 // Подключение модуля режимов шифрования
#include "files.h"                 // Подключение модуля файлов
#include <pwdbased.h>              // Подключение модуля PBKDF2

using namespace CryptoPP;         // Использование пространства имен CryptoPP
using namespace std;              // Использование стандартного пространства имен

void DeriveKeyAndIV(const string& password, unsigned int iterations,
    SecByteBlock& key, size_t keySize,
    SecByteBlock& iv, size_t ivSize,
    SecByteBlock& akey, size_t akeySize) {
    // Функция для производства ключей и вектора инициализации из пароля с помощью функции производства ключей (например, PBKDF2)
    PKCS5_PBKDF2_HMAC<SHA256> pbkdf;                 // Использование PBKDF2 с хэш-функцией SHA-256
    pbkdf.DeriveKey(key, keySize, 0x00,              // Производство ключа из пароля
        reinterpret_cast<const byte*>(password.data()), password.size(),
        nullptr, 0, iterations);

    pbkdf.DeriveKey(iv, ivSize, 0x01,                 // Производство вектора инициализации из пароля
        reinterpret_cast<const byte*>(password.data()), password.size(),
        nullptr, 0, iterations);

    pbkdf.DeriveKey(akey, akeySize, 0x02,             // Производство ключа аутентификации из пароля
        reinterpret_cast<const byte*>(password.data()), password.size(),
        nullptr, 0, iterations);
}

void PrintKeyAndIV(const SecByteBlock& ekey, const SecByteBlock& iv, const SecByteBlock& akey) {
    HexEncoder encoder(new FileSink(cout));          // Использование шестнадцатеричного кодировщика для вывода в консоль
    cout << "Encryption Key: ";                       // Вывод строки "Encryption Key: "
    encoder.Put(ekey, ekey.size());                   // Кодирование и вывод ключа шифрования
    encoder.MessageEnd();                             // Завершение сообщения кодировщика
    cout << "\nIV: ";                                 // Вывод строки "IV: "
    encoder.Put(iv, iv.size());                       // Кодирование и вывод вектора инициализации
    encoder.MessageEnd();                             // Завершение сообщения кодировщика
    cout << "\nAuthentication Key: ";                 // Вывод строки "Authentication Key: "
    encoder.Put(akey, akey.size());                   // Кодирование и вывод ключа аутентификации
    encoder.MessageEnd();                             // Завершение сообщения кодировщика
    cout << endl;                                     // Перевод строки
}

int main(int argc, char* argv[]) {
    string password = "Super secret password";        // Пароль по умолчанию
    if (argc >= 2 && argv[1] != nullptr) {            // Проверка наличия аргументов командной строки
        password = string(argv[1]);                   // Если аргументы есть, использовать второй аргумент как пароль
    }

    string message = "Now is the time for all good men to come to the aide of their country";  // Сообщение по умолчанию
    if (argc >= 3 && argv[2] != nullptr) {            // Проверка наличия аргументов командной строки
        message = string(argv[2]);                    // Если аргументы есть, использовать третий аргумент как сообщение
    }

    string cipher, recover;                           // Переменные для хранения зашифрованного сообщения и восстановленного сообщения
    SecByteBlock ekey(16), iv(16), akey(16);          // Байтовые блоки для ключа шифрования, вектора инициализации и ключа аутентификации

    // Генерация случайного вектора инициализации
    AutoSeededRandomPool prng;                        // Использование автоматически генерируемого генератора случайных чисел
    prng.GenerateBlock(iv, iv.size());                // Генерация блока случайных чисел для вектора инициализации

    // Производство ключей и вектора инициализации из пароля
    DeriveKeyAndIV(password, 100, ekey, ekey.size(), iv, iv.size(), akey, akey.size());

    // Создание объектов шифрования и расшифрования
    CBC_Mode<AES>::Encryption encryptor;              // Создание объекта шифрования AES в режиме CBC
    encryptor.SetKeyWithIV(ekey, ekey.size(), iv, iv.size());  // Установка ключа и вектора инициализации для объекта шифрования
    CBC_Mode<AES>::Decryption decryptor;              // Создание объекта расшифрования AES в режиме CBC
    decryptor.SetKeyWithIV(ekey, ekey.size(), iv, iv.size());  // Установка ключа и вектора инициализации для объекта расшифрования

```cpp
    hmac.SetKey(akey, akey.size());                         // Установка ключа аутентификации для объекта HMAC

    // Encrypt and authenticate data
    StringSource ss1(message, true,                           // Создание источника строки для шифрования и аутентификации данных
        new StreamTransformationFilter(encryptor,              // Фильтр шифрования
            new HashFilter(hmac,                              // Фильтр аутентификации с использованием HMAC
                new StringSink(cipher),                        // Выходной поток для зашифрованных данных
                true)));                                       // Указание на конец потока данных

    // Print encrypted message (for debugging purposes)
    cout << "Encrypted Message: ";                            // Вывод строки "Encrypted Message: "
    StringSource(cipher, true, new HexEncoder(new FileSink(cout)));  // Кодирование и вывод зашифрованного сообщения в шестнадцатеричном формате
    cout << endl;                                             // Перевод строки

    // Authenticate and decrypt data
    try {
        StringSource ss2(cipher, true,                           // Создание источника строки для аутентификации и расшифрования данных
            new HashVerificationFilter(hmac,                    // Фильтр проверки аутентификации с использованием HMAC
                new StreamTransformationFilter(decryptor,        // Фильтр расшифрования
                    new StringSink(recover)),                   // Выходной поток для восстановленных данных
                HashVerificationFilter::HASH_AT_END |           // Указание на то, что HMAC находится в конце сообщения
                HashVerificationFilter::PUT_MESSAGE |          // Указание на сохранение сообщения
                HashVerificationFilter::THROW_EXCEPTION));      // Указание на генерацию исключения при неудачной аутентификации

        cout << "Decrypted and authenticated message: " << recover << endl;  // Вывод расшифрованного и аутентифицированного сообщения
    }
    catch (const Exception& e) {                              // Обработка исключений
        cerr << "Authentication or decryption failed: " << e.what() << endl;  // Вывод сообщения об ошибке аутентификации или расшифровки
    }

    // Print keys and IV
    PrintKeyAndIV(ekey, iv, akey);                            // Вывод ключей и вектора инициализации

    return 0;                                                  // Возврат нуля, указывающего на успешное завершение программы
}
```
```

### Результат работы программы для приведенного сообщения

```bash
Encrypted Message: 920D365894661A48B81F524F28D5165FA9F5EF6BFC25DBF4BC2B4D97706837C108D55E33DEF19378627E69AAB6413B3F37316FBAFAFDD8164C3A1E30651009151E5054E1D00BAF5B37A96B87B183721B403563DC6EA21A408431A2FC51F7770964B425FB860E9978D1E97E70FFBAFE83
Decrypted and authenticated message: Now is the time for all good men to come to the aide of their country
Encryption Key: CF01289A38B86A65C87C21A6D18C894A
IV: CF01289A38B86A65C87C21A6D18C894A
Authentication Key: CF01289A38B86A65C87C21A6D18C894A

Z:\Terminal\Edu\Academic...\2.3Crypto.exe (process 26056) exited with code 0.
To automatically close the console when debugging stops, enable Tools->Options->Debugging->Automatically close the console when debugging stops.
Press any key to close this window . . .
```

### Возможные уязвимости и меры предосторожности

1. **Фиксированные IV**:
   - Использование фиксированного `IV` для каждого сообщения делает систему уязвимой для атак повторного воспроизведения. Необходимо использовать уникальный `IV` для каждого сообщения. В этом примере используется случайный `IV`.
   - Важно передавать `IV` вместе с зашифрованным сообщением для расшифровки.

2. **Производительность и безопасность пароля**:
   - Пароли, введенные с клавиатуры, могут быть слабыми. Рекомендуется использовать ключи, генерированные безопасным методом, и хранить их безопасно.
   - Использование `PBKDF2` с достаточным числом итераций помогает защитить пароль от атак грубой силы.

3. **Обработка ошибок**:
   - Необходимо обрабатывать возможные ошибки, связанные с шифрованием и аутентификацией, чтобы защитить систему от сбоев и атак.

4. **Использование проверенных криптографических библиотек**:
   - Crypto++ является хорошим выбором, но важно всегда следить за обновлениями и исправлениями безопасности в используемой библиотеке.

5. **Хранение и передача ключей**:
   - Ключи должны быть защищены при хранении и передаче. Рекомендуется использовать защищенные контейнеры для ключей и безопасные каналы связи.

6. **Интерфейс пользователя**:
   - Необходимо убедиться, что пользователь вводит пароль в защищенном режиме, чтобы предотвратить его перехват другими программами.

С учетом этих мер предосторожности, пример программы можно использовать в полноценном программном обеспечении для обеспечения конфиденциальности и аутентичности данных.
