import random
import pyotp


# Two factor authentication using python
def generate_otp(secret_key):
    totp = pyotp.TOTP(secret_key)
    otp = totp.now()
    return otp


# Example usage
secret_key = 'your_secret_key_here'
otp = generate_otp(secret_key)
print(otp)

# Copy to clipboard
import pyperclip
pyperclip.copy(otp)

# ---
# pip install pyotp qrcode
import time
import pyotp
import qrcode

key = 'GeeksforGeeksIsBestForEverything'
# otpauth://totp/username@company.com?secret=xxx&issuer=IssuerName%20User

uri = pyotp.totp.TOTP(key).provisioning_uri(name='name@company.com',
                                            issuer_name='google')

print(uri)

# Qr code generation step
qrcode.make(uri).save('qr.png')
"""Verifying stage starts"""

totp = pyotp.TOTP(key)

# verifying the code
while True:
    print(totp.verify(input(('Enter the Code : '))))

import pyotp
import pyperclip
pyperclip.copy(pyotp.TOTP('SECRETS').now())
