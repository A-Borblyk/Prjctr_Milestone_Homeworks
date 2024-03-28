lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def encrypt():
  shift = int(input('Shift: '))
  sms = input('Message: ')
  encrypted_sms = ''

  for symbol in sms:
    if symbol.isalpha():
      if symbol.isupper():
        index = (uppercase_letters.index(symbol) + shift) % 26
        encoded_char = uppercase_letters[index]
      else:
        index = (lowercase_letters.index(symbol) + shift) % 26
        encoded_char = lowercase_letters[index]
    else:
      encoded_char = symbol
    encrypted_sms += encoded_char
  print('Encoded message:', encrypted_sms)

encrypt()