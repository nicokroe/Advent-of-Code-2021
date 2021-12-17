import std/[strutils, strformat, sugar, tables]
from std/os import parentDir

proc parse_input(): seq[string] =
  const file = currentSourcePath.parentDir() & "\\input.txt"
  result = collect(newSeq):
    for line in file.lines: line.strip

proc part1(commands: seq[string]): int =
  var submarine = to_table({"position": 0, "depth": 0})
  for command in commands:
    let cmd = command.split
    case cmd[0]:
      of "forward":
        submarine["position"] += cmd[1].parseInt
      of "up":
        submarine["depth"] -= cmd[1].parseInt
      of "down":
        submarine["depth"] += cmd[1].parseInt
  result = submarine["position"] * submarine["depth"]

proc part2(commands: seq[string]): int =
  var submarine = to_table({"position": 0, "depth": 0, "aim": 0})
  for command in commands:
    let cmd = command.split
    case cmd[0]:
      of "forward":
        submarine["position"] += cmd[1].parseInt
        submarine["depth"] += submarine["aim"] * cmd[1].parseInt
      of "up":
        submarine["aim"] -= cmd[1].parseInt
      of "down":
        submarine["aim"] += cmd[1].parseInt
  result = submarine["depth"]*submarine["position"]

proc main(): void =
  let data = parse_input()
  echo(fmt"{part1(data)=}")
  echo(fmt"{part2(data)=}")

when is_main_module:
  main()
