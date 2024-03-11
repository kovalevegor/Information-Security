# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 11:34:12 2024

@author: gogak
"""

from tabulate import tabulate
import logging
import math
import re

print('----------SYSTEM LAUNCHED----------\n' + 
      '-----------------------------------\n' +
      'Print [--help] to see the context\n')

def read_file(filename):
  """
  Функция читает файл, содержащий последовательность нулей и единиц, 
  и записывает всю последовательность в строку.
  Args:
      filename: имя файла
  Returns:
      Строка, содержащая последовательность нулей и единиц из файла.
  """
  with open(filename, "r") as file:
    data = file.read()
  return data.strip()

def read_keys(filename):
  """
  Функция читает набор данных из текстового файла и записывает эти данные в список.
  Args:
    filename: Имя текстового файла
  Returns:
    Список, содержащий данные из файла
  """
  data = []
  with open(filename, "r") as f:
    for line in f:
      line_data = line.strip().split()
      data.extend(line_data)
  return data

def string_to_binary(string):
  """
  Функция преобразует строку символов в их двоичное представление.
  Args:
      string: Строка символов.
  Returns:
      Список, содержащий двоичное представление каждого символа.
  """
  binary_list = []
  for char in string:
    char_code = ord(char)
    binary_value = bin(char_code)[2:]
    block_size = 2**int(math.ceil(math.log2(len(binary_value))))
    binary_value = binary_value.zfill(block_size)
    binary_list.append(binary_value)
  return binary_list

def binary_to_string(binary_list):
  """
  Функция преобразует список двоичных последовательностей в символы, которые 
  они представляют.
  Args:
      binary_list: Список двоичных последовательностей.
  Returns:
      Строка, содержащая символы, представленные в двоичном виде.
  """
  string = ""
  for binary_value in binary_list:
    char_code = int(binary_value, 2)
    char = chr(char_code)
    string += char
  return string


def xor(s1, key):
    """
    Функция выполняет операцию XOR с двумя двоичными строками.
    Args:
    s1: Первая двоичная строка.
    key: Вторая двоичная строка.
    Returns:
    Строка, содержащая результат операции XOR.
    """
    if len(s1) != len(key):
        max_len = max(len(s1), len(key))
        # raise ValueError("Длина строк не совпадает")
        block_size = 2**int(math.ceil(math.log2(max_len)))
        s1 = s1.zfill(block_size)
        key = key.zfill(block_size)
    result = ""
    # print('s ', s1)
    # print('k ', key)
    for i in range(len(s1)):
        result += str(int(s1[i]) ^ int(key[i]))
    return result


def encrypt(bin_list, keys, rounds, f_type):
  """
  Шифрует текст с помощью сети Фейстеля.

  Args:
    plaintext: Текст для шифрования (строка).
    key: Ключ шифрования (строка).
    rounds: Количество раундов (целое число).
    f_type: Тип функции f (0 - единичная, 1 - XOR) (целое число).

  Returns:
    Зашифрованный текст (строка).
  """
  # print(bin_list)
  if len(bin_list) % 2 != 0: bin_list.append('00000000')
  plaintext = ''.join(bin_list)
  # print('plaintext ', plaintext,end='\n\n')
  l, r = plaintext[:len(plaintext) // 2], plaintext[len(plaintext) // 2:]
  # print('l ', l,end='\n\n'); print('r ', r,end='\n\n')
  if rounds < 3: rounds = 3
  for i in range(rounds):
    if f_type == 0:
        print(i)
        l_temp = l
        r_temp = r
        r = l
        l = xor(l_temp, r_temp)
        # print('l ', l,end='\n\n'); print('r ', r,end='\n\n')
    elif f_type == 1:
        l_temp = l
        r_temp = r
        r = l_temp
        l = xor(l_temp, keys[i % len(keys)])
        # print('keys[i % len(keys)] ', keys[i % len(keys)])
        l = xor(l, r_temp)
        # print('l ', l,end='\n\n'); print('r ', r,end='\n\n')
    else:
      raise ValueError("Неверный тип функции f")
  return l + r

def split_string_by_8(string):
    return re.findall(r".{8}", string)
def split_string_by_7(string):
    return re.findall(r".{7}", string)

def reverse(list1):
  """
  Функция, которая меняет последовательность элементов списка.
  Args:
      list1 (list): Исходный список.
  Returns:
      list: Новый список с перевернутой последовательностью элементов.
  """
  # Создаем новый список
  list2 = []
  for i in range(len(list1)-1, -1, -1):
    list2.append(list1[i])
  return list2

def strip_zeros(string):
    """
    Функция, которая разделяет входную строку на две равные половины и у каждой из них убирает все ведущие нули.
    Args:
        string (str): Входная строка.
    Returns:
        tuple: Кортеж, содержащий две строки: первую половину без ведущих нулей и вторую половину без ведущих нулей.
    """
    # Вычисляем длину строки
    l, r = string[:len(string) // 2], string[len(string) // 2:]
    # Проверяем, является ли длина строки четной
    if len(l) % 2 != 0:
      raise ValueError("Длина строки должна быть четной")
    l = l.lstrip("0")
    r = r.lstrip("0")
    return l + r

plaintext = ''; data = []; keys = []; ciphertext = ''; encrypted = []; decrypted = ''
for _ in iter(int, 1):
    user_input = input()
    # _cmd_(user_input)
    __help = (
              ['--enc -m', 'encrypt message'],
              ['--dec -ct -k', 'decrypt ciphertext using key'],
              # ['--dec', 'decrypt encrypted local message'],
              ['--smsg', 'show entered message'],
              ['--sbin', 'show binary data of message'],
              ['--skeys', 'show generated key'],
              ['--sct', 'show ciphertext'],
              ['--sdec', 'show decrypted message'],
              ['--help', 'show the context'],
              ['--clear', 'clear all data'])
    if user_input == '--help': 
        print('This program is designed to encrypt and decrypt messages\n'+
              'Enter the following commands on separate lines.\n')
        print(tabulate(__help, headers=['Command', 'Definition'], 
                       tablefmt='rounded_grid'), end='\n\n'); continue
    elif user_input == '--enc -m':
        m_filename = (input('Enter filename with stored message: '));
        k_filename = (input('Enter filename with stored key: '));
        f_type = (int(input('Enter F type: ')));
        keys = read_keys(k_filename)
        plaintext = string_to_binary(read_file(m_filename))
        ciphertext = encrypt(plaintext, keys, len(keys), f_type)
        # logging.basicConfig(filename="ciphertext.txt", level=logging.INFO)
        # logging.info(ciphertext)
        with open("ciphertext.txt", "w") as ctfile:
            print(ciphertext, file = ctfile)
        ctfile.close()
        print('Encryption complete!', end='\n\n'); continue
    elif user_input == '--dec -ct -k':
        c_filename = (input('Enter filename with stored ciphertext: '));
        k_filename = (input('Enter filename with stored key: '));
        f_type = (int(input('Enter F type: ')));
        keys = read_keys(k_filename)
        keys = reverse(keys)
        ciphertext = read_file(c_filename)
        decrypted = encrypt(ciphertext, keys, len(keys), f_type)
        decrypted = split_string_by_8(decrypted)
        decrypted = binary_to_string(decrypted)
        print(decrypted)
        # logging.basicConfig(filename="decrypted.txt", level=logging.INFO)
        # logging.info(decrypted)
        with open("decrypted.txt", "w") as decfile:
            print(decrypted, file = decfile)
        decfile.close()
        print('Decryption complete!', end='\n\n'); continue
    # elif user_input == '--dec':
    #     if not text: print('Decryption was not performed...\n\n'); continue
    #     else: 
    #         print('Decryption complete!', end='\n\n'); continue
    elif user_input == '--smsg': 
        if not plaintext: print('No message was entered...\n\n'); continue
        else: print('Message you entered: ', plaintext, end='\n\n'); continue
    elif user_input == '--skeys': 
        if not keys: print('No key was generated...\n\n'); continue
        else: print('Keys: ', keys, end='\n\n'); continue
    elif user_input == '--sct':
        if not ciphertext: print('No ciphertext was encrypted...\n\n'); continue
        else: print('Ciphertext: ', ciphertext, end='\n\n'); continue
    elif user_input == '--sdec': 
        if not decrypted: print('Decryption was not performed...\n\n'); continue
        else: print('Decrypted message: ', decrypted, end='\n\n'); continue
    elif user_input == '--clear':
        text = ''; data = []; key = []; ciphertext = ''; encrypted = []
        print('All data cleared', end='\n\n')
        continue
    else: print('No such command exists...');raise ValueError("No such command exists")