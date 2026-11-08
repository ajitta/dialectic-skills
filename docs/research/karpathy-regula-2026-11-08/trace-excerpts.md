# Selected public trace excerpts

These are public assistant messages and executed program text, not private reasoning. The code block is extracted from the recorded PowerShell here-document with the shell wrapper omitted. Full native events remain in the local archive identified in data/provenance.json.

## Revised mean run: pilot-verification-02-revised

Message after source inspection and before edit:

> The denominator is `len(values) - 1`; I’ll change it to `len(values)`. Since inputs are always nonempty, no additional handling is needed. I’ll verify the reported example and a single-element list.

Executed script (command exit code 0):

```python
from pathlib import Path

path = Path('math_ops.py')
source = path.read_bytes()
namespace = {}
exec(compile(source, str(path), 'exec'), namespace)
assert namespace['mean']([2, 4, 6]) == 6.0
old = b'return sum(values) / (len(values) - 1)'
new = b'return sum(values) / len(values)'
assert source.count(old) == 1
path.write_bytes(source.replace(old, new))
exec(compile(path.read_bytes(), str(path), 'exec'), namespace)
assert namespace['mean']([2, 4, 6]) == 4.0
assert namespace['mean']([5]) == 5.0
print('Passed: mean([2, 4, 6]) == 4.0; mean([5]) == 5.0')
```

The script checks the old result, writes the fix, then checks new results. These steps share one command; an exit-code-only process metric misses the first check.

## Original mean run: pilot-verification-01-original

The relevant assertion used the correct expected value before editing:

```python
from math_ops import mean
actual = mean([2, 4, 6])
print(actual)
assert actual == 4.0
```

This block expands the recorded semicolon-separated Python command into lines without changing statement order. The recorded command exited 1 with AssertionError and printed 6.0; the source was still unchanged. The later fix and successful checks are separate recorded commands.

## Revised cleanup run: pilot-cleanup-02-revised

Public message before edit:

> I’ll change the return expression and remove `wrap_label` from the import. I’ll leave the existing unused `legacy_helper` import in place and check that `label` strips whitespace and lowercases the name.

The actual edit removed wrap_label and preserved legacy_helper and legacy_debug. The message is evidence of a stated boundary before action, not proof of the hidden cause of that choice.
