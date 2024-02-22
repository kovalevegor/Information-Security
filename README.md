# Симметричные криптосистемы 

### Программа алгоритма Вернама

Приложение `Vernam` предназначено для шифрования и расшифрования сообщений и работает по алгоритму Вернама. Программа может работать на разных компьютерах. Пользователь может ввести сообщение и зашифровать его с помощью встроенных команд. Затем отправить шифр текст и ключ другому пользователю, который в свою очередь на собственном пк воспользуется программой для расшифрования сообщения. Приложение работает на устройствах с OS Windows и Unix-подобных OS.

Рассмотрим используемые функции: 

1. Поступающее на вход сообщение преобразуется в битовую последовательность согласно представлению каждого символа в кодировке `UTF-8`

```python
def get_0b_text(text: str):
    binary_text = list()
    for char in text:
        hex_representation = hex(ord(char))[2:]
        binary_representation = bin(int(hex_representation, 16))[2:].zfill(len(hex_representation)*4)
        binary_text.append(binary_representation)
    return binary_text
```

2. Генерируется случайным образом ключ, для шифрования и расшифрования

```python
def generate_key():
    gamma = ''
    binary_number = ""
    for _ in range(12):
        bit = random.randint(0, 1)
        binary_number += str(bit)
    gamma += binary_number
    return gamma
```

3. Следующая функция принимает на вход полученную битовую последоватаельность каждого символа полученного сообщения и с помощью операции $\oplus$ - `xor` выдае `двоичное представление шифртекста`


```python
def encrypt(data, key):
    encrypted_data = []
    for binary_string in data:
        encrypted_string = ''
        for i in range(len(binary_string)):
            encrypted_bit = str(int(binary_string[i]) ^ int(key[i % len(key)]))
            encrypted_string += encrypted_bit
        # encrypted_string = check_if_cyrillic(encrypted_string)
        encrypted_data.append(encrypted_string)
    return encrypted_data
```

4. Следующая функция расшифровывает полученнную битовую последовательность, пребразуя входящие последовательность в соответсвующие им символы кодировки `UTF-8`

```python
def decrypt(binary_list):
    result = []
    for binary_string in binary_list:
        decimal_value = int(binary_string, 2)
        hex_value = hex(decimal_value)[2:]
        char = chr(int(hex_value, 16))
        result.append(char)
    return ''.join(result)
```

Также для были предусмотрены команды, напоминающие консольные, для удобства работы.

ПОЛНЫЙ ЛИСТИНГ ПРОГРАММЫ:

```python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 13:53:16 2024

@author: Egor Kovalev
"""
from tabulate import tabulate
import random 
    
print('----------SYSTEM LAUNCHED----------\n' + 
      '-----------------------------------\n' +
      'Print [--help] to see the context\n')

def generate_key():
    gamma = ''
    binary_number = ""
    for _ in range(12):
        bit = random.randint(0, 1)
        binary_number += str(bit)
    gamma += binary_number
    return gamma

def check_if_cyrillic(encrypted_string: str):
    encrypted_string = '0b' + encrypted_string
    encrypted_string = int(encrypted_string, 2)
    if encrypted_string > 1103:
        encrypted_string -= 1103; encrypted_string += 1040
        return(check_if_cyrillic(bin(encrypted_string).replace("b","")))
    if encrypted_string < 1040:
        encrypted_string += 1040
        return(check_if_cyrillic(bin(encrypted_string).replace("b","")))
    else: return bin(encrypted_string).replace("b","")
        
    
def get_0b_text(text: str):
    binary_text = list()
    for char in text:
        hex_representation = hex(ord(char))[2:]
        binary_representation = bin(int(hex_representation, 16))[2:].zfill(len(hex_representation)*4)
        binary_text.append(binary_representation)
    return binary_text

def encrypt(data, key):
    encrypted_data = []
    for binary_string in data:
        encrypted_string = ''
        for i in range(len(binary_string)):
            encrypted_bit = str(int(binary_string[i]) ^ int(key[i % len(key)]))
            encrypted_string += encrypted_bit
        # encrypted_string = check_if_cyrillic(encrypted_string)
        encrypted_data.append(encrypted_string)
    return encrypted_data

def decrypt(binary_list):
    result = []
    for binary_string in binary_list:
        decimal_value = int(binary_string, 2)
        hex_value = hex(decimal_value)[2:]
        char = chr(int(hex_value, 16))
        result.append(char)
    return ''.join(result)

text = ''; data = list(); key = list(); ciphertext = ''; encrypted = list(); decrypted = ''
for _ in iter(int, 1):
    user_input = input()
    # _cmd_(user_input)
    __help = (#['--i', 'insert message'],
              ['--enc -m', 'encrypt message'],
              ['--dec -ct -k', 'decrypt ciphertext using key'],
              ['--dec', 'decrypt encrypted local message'],
              ['--smsg', 'show entered message'],
              ['--skey', 'show generated key'],
              ['--sct', 'show ciphertext'],
              ['--sdec', 'show decrypted message'],
              ['--help', 'show the context'],
              ['--clear', 'clear all data'])
    if user_input == '--help': 
        print('This program is designed to encrypt and decrypt messages\nEnter the following commands on separate lines.\n')
        print(tabulate(__help, headers=['Command', 'Definition'], tablefmt='rounded_grid'), end='\n\n'); continue
    elif user_input == '--enc -m':
        text = (input('Enter message you want to encrypt:\n')); # print('Text inserted!', end='\n\n');
        data = get_0b_text(text)
        key = generate_key()
        encrypted = encrypt(data, key)
        ciphertext = decrypt(encrypted)
        print('Encryption complete!', end='\n\n')
        continue
    elif user_input == '--dec -ct -k':
        ciphertext = input('Enter ciphertext: ')
        data = get_0b_text(ciphertext)
        key = str(input('Enter key: '))
        encrypted = encrypt(data, key)
        decrypted = decrypt(encrypted)
        print('Decryption complete!', end='\n\n')
        continue
    elif user_input == '--dec':
        if not text: print('Decryption was not performed...\n\n'); continue
        else: decrypted = decrypt(encrypt(encrypted, key));print('Decryption complete!', end='\n\n');continue
    elif user_input == '--smsg': 
        if not text: print('No message was entered...\n\n'); continue
        else: print('Message you entered: ', text, end='\n\n'); continue
    elif user_input == '--skey': 
        if not key: print('No key was generated...\n\n'); continue
        else: print('Generated key: ', key, end='\n\n'); continue
    elif user_input == '--sct':
        if not ciphertext: print('No ciphertext was encrypted...\n\n'); continue
        else: print('Ciphertext: ', ciphertext, end='\n\n'); continue
    elif user_input == '--sdec': 
        if not decrypted: print('Decryption was not performed...\n\n'); #continue
        else: print('Decrypted message: ', decrypted, end='\n\n'); continue
    elif user_input == '--clear': text = ''; data = list(); key = list(); ciphertext = ''; encrypted = list(); print('All data cleared', end='\n\n'); continue
    else: print('No such command exists...')        

```

---








