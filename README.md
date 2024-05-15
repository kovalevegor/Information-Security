# <p align = "center">Стандарты аутентичного шифрования</p>

[crypto++](https://www.cryptopp.com/) | [AES](https://www.cryptopp.com/wiki/Advanced_Encryption_Standard) | [git lib rep](https://github.com/weidai11/cryptopp) | [helping hand](https://www.youtube.com/watch?v=5XE4zEN-WKg)

Ниже показан пример обеспечивающий конфиденциальность и аутентичности для блочного шифра в режиме CBC и HMAC. Похожий алгоритм используется в IPSec. Сначала данные приводятся к зашифрованному виду, после чего к ним добалвяется код аутентификации. Тег аутентификации помещается в конце сообщения.

Проанализируйте пример. Опишите возможности использования в полноценном программном обеспечении и используйте этот пример для построения работающего образца. Какие уязвимости могут быть характерны для этой реализации? (предположим, что пароль всё-таки вводится с клавиатуры!) При построении убедитесь, что каждое сообщение получает уникальный IV. Убедитесь, что для аутентификации используется пара {IV, шифротекст}.

```cpp
string password = "Super secret password";
if(argc >= 2 && argv[1] != NULL)
    password = string(argv[1]);

string message = "Now is the time for all good men to come to the aide of their country";
if(argc >= 3 && argv[2] != NULL)
    message = string(argv[2]);

string cipher, recover;
SecByteBlock ekey(16), iv(16), akey(16);

// Derive keys an IV from the password
DeriveKeyAndIV(password, 100, ekey, ekey.size(), iv, iv.size(), akey, akey.size());

// Create and key objects
CBC_Mode<AES>::Encryption encryptor;
encryptor.SetKeyWithIV(ekey, ekey.size(), iv, iv.size());
CBC_Mode<AES>::Decryption decryptor;
decryptor.SetKeyWithIV(ekey, ekey.size(), iv, iv.size());

HMAC< SHA256> hmac;
hmac.SetKey(akey, akey.size());

// Encrypt and authenticate data
StringSource ss1(message, true /*pumpAll*/,
                 new StreamTransformationFilter(encryptor,
                     new HashFilter(hmac,
                         new StringSink(cipher),
                     true /*putMessage*/)));

// Authenticate and decrypt data
StringSource ss2(cipher, true /*pumpAll*/,
                 new HashVerificationFilter(hmac,
                     new StreamTransformationFilter(decryptor,
                         new StringSink(recover)),
                     HASH_AT_END | PUT_MESSAGE | THROW_EXCEPTION));
    
// Print stuff
PrintKeyAndIV(ekey, iv, akey);
```

```cpp
#include <iostream>
#include <string>
#include <cryptopp/cryptlib.h>
#include <cryptopp/aes.h>
#include <cryptopp/modes.h>
#include <cryptopp/hmac.h>
#include <cryptopp/sha.h>
#include <cryptopp/filters.h>
#include <cryptopp/secblock.h>
#include <cryptopp-authenc.cpp>

using namespace std;
using namespace CryptoPP;

void DeriveKeyAndIV(const string& password, int iterations, SecByteBlock& ekey, size_t ekeySize, SecByteBlock& iv, size_t ivSize, SecByteBlock& akey, size_t akeySize) {
    // Реализация функции DeriveKeyAndIV
}

void PrintKeyAndIV(const SecByteBlock& ekey, const SecByteBlock& iv, const SecByteBlock& akey) {
    // Реализация функции PrintKeyAndIV
}

int main(int argc, char* argv[]) {
    string password = "Super secret password";
    if (argc >= 2 && argv[1] != NULL)
        password = string(argv[1]);

    string message = "Now is the time for all good men to come to the aide of their country";
    if (argc >= 3 && argv[2] != NULL)
        message = string(argv[2]);

    string cipher, recover;
    SecByteBlock ekey(16), iv(16), akey(16);

    // Derive keys an IV from the password
    DeriveKeyAndIV(password, 100, ekey, ekey.size(), iv, iv.size(), akey, akey.size());

    // Create and key objects
    CBC_Mode<AES>::Encryption encryptor;
    encryptor.SetKeyWithIV(ekey, ekey.size(), iv, iv.size());
    CBC_Mode<AES>::Decryption decryptor;
    decryptor.SetKeyWithIV(ekey, ekey.size(), iv, iv.size());

    HMAC< SHA256> hmac;
    hmac.SetKey(akey, akey.size());

    // Encrypt and authenticate data
    StringSource ss1(message, true /*pumpAll*/,
        new StreamTransformationFilter(encryptor,
            new HashFilter(hmac,
                new StringSink(cipher),
                true /*putMessage*/)));

    // Authenticate and decrypt data
    StringSource ss2(cipher, true /*pumpAll*/,
        new HashVerificationFilter(hmac,
            new StreamTransformationFilter(decryptor,
                new StringSink(recover)),
            HASH_AT_END | PUT_MESSAGE | THROW_EXCEPTION));

    // Print stuff
    PrintKeyAndIV(ekey, iv, akey);

    return 0;
}
```
