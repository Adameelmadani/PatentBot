"""
==========================================================
Test Authentication
==========================================================
"""

from auth import get_access_token
from config import SEPARATOR


print(SEPARATOR)
print("AUTHENTICATION TEST")
print(SEPARATOR)

try:

    token = get_access_token()

    print("Authentication successful.\n")

    print("Access Token :")
    print(token)

    print("\nToken length :", len(token))

except Exception as e:

    print("Authentication failed.\n")

    print(e)