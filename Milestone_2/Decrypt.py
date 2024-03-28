lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt():
  shift = int(input('Shift: '))
  sms = input('Message: ')
  decrypted_sms = ''

  for symbol in sms:
    if symbol.isalpha():
      if symbol.isupper():
        index = (uppercase_letters.index(symbol) - shift) % 26
        decrypted_char = uppercase_letters[index]
      else:
        index = (lowercase_letters.index(symbol) - shift) % 26
        decrypted_char = lowercase_letters[index]
    else:
      decrypted_char = symbol
    decrypted_sms += decrypted_char
  print('Decoded message:', decrypted_sms)

decrypt() 