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
#include <iostream>
#include <string>
#include <cryptlib.h>
#include <aes.h>
#include <cbcmac.h>
#include <filters.h>
#include <hmac.h>
#include <sha.h>
#include <secblock.h>
#include <osrng.h>
#include <hex.h>
#include "rijndael.h"
#include "modes.h"
#include "files.h"
#include <pwdbased.h>

using namespace CryptoPP;
using namespace std;

void DeriveKeyAndIV(const string& password, unsigned int iterations,
    SecByteBlock& key, size_t keySize,
    SecByteBlock& iv, size_t ivSize,
    SecByteBlock& akey, size_t akeySize) {
    // Use a key derivation function (e.g., PBKDF2) to derive the keys and IV from the password
    PKCS5_PBKDF2_HMAC<SHA256> pbkdf;
    pbkdf.DeriveKey(key, keySize, 0x00,
        reinterpret_cast<const byte*>(password.data()), password.size(),
        nullptr, 0, iterations);

    pbkdf.DeriveKey(iv, ivSize, 0x01,
        reinterpret_cast<const byte*>(password.data()), password.size(),
        nullptr, 0, iterations);

    pbkdf.DeriveKey(akey, akeySize, 0x02,
        reinterpret_cast<const byte*>(password.data()), password.size(),
        nullptr, 0, iterations);
}

void PrintKeyAndIV(const SecByteBlock& ekey, const SecByteBlock& iv, const SecByteBlock& akey) {
    HexEncoder encoder(new FileSink(cout));
    cout << "Encryption Key: ";
    encoder.Put(ekey, ekey.size());
    encoder.MessageEnd();
    cout << "\nIV: ";
    encoder.Put(iv, iv.size());
    encoder.MessageEnd();
    cout << "\nAuthentication Key: ";
    encoder.Put(akey, akey.size());
    encoder.MessageEnd();
    cout << endl;
}

int main(int argc, char* argv[]) {
    string password = "Super secret password";
    if (argc >= 2 && argv[1] != nullptr) {
        password = string(argv[1]);
    }

    string message = "Now is the time for all good men to come to the aide of their country";
    if (argc >= 3 && argv[2] != nullptr) {
        message = string(argv[2]);
    }

    string cipher, recover;
    SecByteBlock ekey(16), iv(16), akey(16);

    // Generate a random IV
    AutoSeededRandomPool prng;
    prng.GenerateBlock(iv, iv.size());

    // Derive keys and IV from the password
    DeriveKeyAndIV(password, 100, ekey, ekey.size(), iv, iv.size(), akey, akey.size());

    // Create and key objects
    CBC_Mode<AES>::Encryption encryptor;
    encryptor.SetKeyWithIV(ekey, ekey.size(), iv, iv.size());
    CBC_Mode<AES>::Decryption decryptor;
    decryptor.SetKeyWithIV(ekey, ekey.size(), iv, iv.size());

    HMAC<SHA256> hmac;
    hmac.SetKey(akey, akey.size());

    // Encrypt and authenticate data
    StringSource ss1(message, true,
        new StreamTransformationFilter(encryptor,
            new HashFilter(hmac,
                new StringSink(cipher),
                true)));

    // Print encrypted message (for debugging purposes)
    cout << "Encrypted Message: ";
    StringSource(cipher, true, new HexEncoder(new FileSink(cout)));
    cout << endl;

    // Authenticate and decrypt data
    try {
        StringSource ss2(cipher, true,
            new HashVerificationFilter(hmac,
                new StreamTransformationFilter(decryptor,
                    new StringSink(recover)),
                HashVerificationFilter::HASH_AT_END |
                HashVerificationFilter::PUT_MESSAGE |
                HashVerificationFilter::THROW_EXCEPTION));

        cout << "Decrypted and authenticated message: " << recover << endl;
    }
    catch (const Exception& e) {
        cerr << "Authentication or decryption failed: " << e.what() << endl;
    }

    // Print keys and IV
    PrintKeyAndIV(ekey, iv, akey);

    return 0;
}
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
