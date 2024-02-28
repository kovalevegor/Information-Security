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
    '''function to generate random key'''
    gamma = ''
    binary_number = ""
    for _ in range(16):
        bit = random.randint(0, 1)
        binary_number += str(bit)
    gamma += binary_number
    return gamma

def get_0b_text(text: str):
    '''function to convert text to binary representation'''
    binary_text = []
    for char in text:
        hex_representation = hex(ord(char))[2:]
        binary_representation = bin(
            int(hex_representation, 16))[2:].zfill(16)
        # print(binary_representation)
        binary_text.append(binary_representation)
    return binary_text

def encrypt(data, key):
    '''function to apply xor to binary sequence with key'''
    encrypted_data = []
    for binary_string in data:
        encrypted_string = ''
        for i in range(len(binary_string)):
            encrypted_bit = str(
                int(binary_string[i]) ^ int(key[i % len(key)]))
            encrypted_string += encrypted_bit
        encrypted_data.append(encrypted_string)

    return encrypted_data

def decrypt(binary_list):
    '''function to convert binary sequence to utf-8 symbols'''
    result = []
    for binary_string in binary_list:
        decimal_value = int(binary_string, 2)
        hex_value = hex(decimal_value)[2:]
        char = chr(int(hex_value, 16))
        result.append(char)
    return ''.join(result)

def binary_to_utf8_hex(binary_str):
    '''function to get hex representation of binary sequence of utf-8'''
    utf8_hex = hex(int(binary_str, 2))[2:].upper().zfill(2)
    return utf8_hex

def convert_binary_list_to_hex(binary_list):
    '''function to '''
    utf8_hex_list = [binary_to_utf8_hex(binary_str) for binary_str in binary_list]
    return utf8_hex_list

def utf8_hex_to_binary(hex_str):
    '''function to get hex representation of binary sequence of utf-8 in a list'''
    binary_str = bin(int(hex_str, 16))[2:].zfill(12)
    return binary_str

def convert_hex_list_to_binary(hex_list):
    '''function to covert hex sequence to binary sequence'''
    binary_list = [utf8_hex_to_binary(hex_str) for hex_str in hex_list]
    return binary_list

def create_ciphertext(input_list):
    '''function to create a ciphertext from a given sequence of hex'''
    result_str = ''
    for element in input_list:
        length = len(element)
        result_str += str(length) + element
    return result_str

def restore_cipher(input_string):
    '''function to restore hex sequence from a ciphertext'''
    elements = []
    while input_string:
        length = int(input_string[0])
        element = input_string[1:length+1]
        elements.append(element)
        input_string = input_string[length+1:]
    return elements

text = ''; data = []; key = []; ciphertext = ''; encrypted = []; decrypted = ''
for _ in iter(int, 1):
    user_input = input()
    # _cmd_(user_input)
    __help = (
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
        print('This program is designed to encrypt and decrypt messages\n'+
              'Enter the following commands on separate lines.\n')
        print(tabulate(__help, headers=['Command', 'Definition'], 
                       tablefmt='rounded_grid'), end='\n\n'); continue
    elif user_input == '--enc -m':
        text = (input('Enter message you want to encrypt:\n'));
        data = get_0b_text(text)
        key = generate_key()
        encrypted = encrypt(data, key)
        # ciphertext = decrypt(encrypted)
        ciphertext = convert_binary_list_to_hex(encrypted)
        print('Encryption complete!', end='\n\n'); continue
    elif user_input == '--dec -ct -k':
        ciphertext = restore_cipher(input('Enter ciphertext: '))
        data = convert_hex_list_to_binary(ciphertext)
        key = str(input('Enter key: '))
        encrypted = encrypt(data, key)
        decrypted = decrypt(encrypted)
        print('Decryption complete!', end='\n\n'); continue
    elif user_input == '--dec':
        if not text: print('Decryption was not performed...\n\n'); continue
        else: 
            decrypted = decrypt(encrypt(encrypted, key));
            print('Decryption complete!', end='\n\n'); continue
    elif user_input == '--smsg': 
        if not text: print('No message was entered...\n\n'); continue
        else: print('Message you entered: ', text, end='\n\n'); continue
    elif user_input == '--skey': 
        if not key: print('No key was generated...\n\n'); continue
        else: print('Generated key: ', key, end='\n\n'); continue
    elif user_input == '--sct':
        if not ciphertext: print('No ciphertext was encrypted...\n\n'); continue
        else: print('Ciphertext: ', create_ciphertext(ciphertext), end='\n\n'); continue
    elif user_input == '--sdec': 
        if not decrypted: print('Decryption was not performed...\n\n'); continue
        else: print('Decrypted message: ', decrypted, end='\n\n'); continue
    elif user_input == '--clear':
        text = ''; data = []; key = []; ciphertext = ''; encrypted = []
        print('All data cleared', end='\n\n')
        continue
    else: print('No such command exists...')        











