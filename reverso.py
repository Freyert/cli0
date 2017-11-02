"""
REVERSE YOUR FILES!!
1. Reading in from the command line.
2. Writing out from the command line.
3. Piping into other programs.
4. Redirecting output to a file.
5. Redirecting keyboard input from a file. python reverso.py < babynames.txt
6. Talk about man files.
7. Talk about life at IBM.
8. Apprenticeship Program
"""
import sys

for line in sys.stdin:
    sys.stdout.write(line[::-1])
