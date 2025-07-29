
import os, sys
filename = sys.argv[1]
# VULNERABLE: input passed to shell
os.system(f"cat {filename}")  # CWE-78
