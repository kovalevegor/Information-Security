# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 10:39:03 2024

@author: Kovalev Egor
"""

import numpy as np

def KSA(key):
  key_length = len(key)
  S = list(range(256))
  j = 0
  for i in range(256):
    if key[i % key_length].isnumeric():
      j = (j + S[i] + int(key[i % key_length])) % 256
    else:
      # Handle non-numeric characters (optional)
      pass
    S[i], S[j] = S[j], S[i]
  return S

def PRGA(S, n):
  i = 0; j = 0; key = []
  while n > 0:
    n = n - 1
    i = (i + 1) % 256
    j = (j + S[i]) % 256
    S[i], S[j] = S[j], S[i]
    k = S[(S[i] + S[j]) % 256]
    key.append(k)
  return key

key = 'KAPERNIK'  # Original key with non-numeric character
# key = '12345'  # Example key with only numeric characters

plaintext = 'Mission Impossible'

def preparing_key_array(s):
  return [ord(c) for c in s]

S = KSA(key)
keystream = np.array(PRGA(S, len(plaintext)))
print(keystream)

plaintext = np.array([ord(i) for i in plaintext])
print(keystream)

cipher = keystream ^ plaintext 
print(cipher.astype(np.uint8).data.hex())
print([chr(c) for c in cipher])













