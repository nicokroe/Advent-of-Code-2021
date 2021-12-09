import std/[strutils, strformat, sugar]
from std/os import parentDir

proc parse_input(): seq[int] =
  let file = currentSourcePath.parentDir() & "\\input.txt"
  result = collect(newSeq):
    for line in file.lines: line.strip.parseInt

proc part1(depths: seq[int]): int =
  var
    tmp: int = depths[0]
  for depth in depths:
    if depth > tmp:
      result += 1
    tmp = depth

proc part2(depths: seq[int]): int =
  for i, depth in depths[0..^4]:
    if depth < depths[i+3]:
      result += 1

proc main(): void =
  let data = parse_input()
  echo(fmt"{part1(data)=}")
  echo(fmt"{part2(data)=}")

when is_main_module:
  main()
