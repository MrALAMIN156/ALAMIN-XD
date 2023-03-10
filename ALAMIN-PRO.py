
import os, sys

try:

    __import__("ALAMIN").menu()

except Exception as e:

    exit(str(e))
