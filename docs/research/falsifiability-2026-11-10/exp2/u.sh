#!/bin/bash
# Relay one simulated-user reply into a transcript and log it.
# usage: u.sh CELL "reply" "reason"   (run from anywhere; paths are relative to this script)
E=$(cd "$(dirname "$0")" && pwd)
printf '\nUSER: %s\n' "$2" >> "$E/t/$1.md"
echo "$1: $3 -> $2" >> "$E/relay-log.md"
