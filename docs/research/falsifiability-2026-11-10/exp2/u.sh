#!/bin/bash
# usage: u.sh CELL "reply" "reason"
E=/tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/exp2
printf '\nUSER: %s\n' "$2" >> $E/t/$1.md
echo "$1: $3 -> $2" >> $E/relay-log.md
