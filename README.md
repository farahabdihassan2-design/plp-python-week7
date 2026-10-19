# PLP Python Week 7:
Lists and Loops

## Files Included
* list_warmup.py:
  Demonstrates basic
  list creation,
  index access,
  append, remove,
  and len methods.
* shopping_list.py:
  Interactive menu-driven
  shopping list manager
  using a while loop
  and membership checks.
* list_report.py:
  Generates formatted
  lists, counts items
  by length, and finds
  the longest item
  using loop comparisons.

## Reflection
Question:
Why is it safer
to check `in`
before calling
`.remove()`?

Answer:
Calling `.remove()`
on an item that
does not exist in
a list raises a
ValueError and
crashes the program.
Checking membership
with the `in`
operator beforehand
ensures the value
exists, allowing
the program to handle
missing items safely
without unexpected
runtime failures.