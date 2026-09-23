
"""
Brainfuck Easy Mode
A configurable Brainfuck compiler/interpreter.

File format:

CONFIG{
    > = "q"
    < = "w"
    + = "e"
    - = "r"
    . = "t"
    , = "y"
    [ = "u"
    ] = "i"
}
PROGRAM-
eeeeet

Usage:
    python bem.py program.bem
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


VERSION = "1.0.0"

# The ONLY hardcoded part:
# Brainfuck's 8 operations.
OPERATIONS = {
    ">": "pointer right",
    "<": "pointer left",
    "+": "increment",
    "-": "decrement",
    ".": "output",
    ",": "input",
    "[": "loop start",
    "]": "loop end",
}


class BEMError(Exception):
    """Base error for Brainfuck Easy Mode."""


def error(message: str) -> None:
    raise BEMError(message)


def parse_config(source: str) -> dict[str, str]:
    match = re.search(
        r"\bCONFIG\s*\{(.*?)\}",
        source,
        re.DOTALL,
    )

    if not match:
        error("CONFIG block not found.")

    body = match.group(1)

    config: dict[str, str] = {}

    # Values can be ANY non-empty string.
    # Examples:
    # "q"
    # "hello"
    # "DO_THE_THING"
    # "🐸"
    pattern = re.compile(
        r'([><+\-.,\[\]])\s*=\s*"([^"]+)"'
    )

    for symbol, name in pattern.findall(body):
        if symbol in config:
            error(
                f'Duplicate configuration for "{symbol}".'
            )

        if name in config.values():
            error(
                f'Duplicate command name "{name}". '
                "Every command name must be unique."
            )

        config[symbol] = name

    missing = set(OPERATIONS) - set(config)

    if missing:
        missing_text = ", ".join(
            f'"{x}"' for x in sorted(missing)
        )
        error(
            "CONFIG is missing command(s): "
            + missing_text
        )

    return config


def parse_program(source: str) -> str:
    match = re.search(
        r"\bPROGRAM-\s*(.*)",
        source,
        re.DOTALL,
    )

    if not match:
        error("PROGRAM- section not found.")

    return match.group(1).strip()


def compile_program(
    program: str,
    config: dict[str, str],
) -> str:

    # Reverse mapping:
    # user's custom token -> Brainfuck symbol
    tokens = {
        name: symbol
        for symbol, name in config.items()
    }

    # Longest tokens first.
    # This allows names such as:
    #
    # "add"
    # "add_more"
    #
    # to coexist safely.
    ordered = sorted(
        tokens,
        key=len,
        reverse=True,
    )

    if not ordered:
        error("No commands configured.")

    code = []
    position = 0

    while position < len(program):

        # Ignore whitespace.
        if program[position].isspace():
            position += 1
            continue

        found = False

        for token in ordered:
            if program.startswith(token, position):
                code.append(tokens[token])
                position += len(token)
                found = True
                break

        if not found:
            preview = program[position:position + 20]
            error(
                f'Unknown command near: "{preview}"'
            )

    return "".join(code)


def build_jump_table(code: str) -> dict[int, int]:
    jumps: dict[int, int] = {}
    stack: list[int] = []

    for position, command in enumerate(code):

        if command == "[":
            stack.append(position)

        elif command == "]":

            if not stack:
                error(
                    f"Unmatched ']' at instruction "
                    f"{position}."
                )

            start = stack.pop()

            jumps[start] = position
            jumps[position] = start

    if stack:
        error(
            f"Unmatched '[' at instruction "
            f"{stack[-1]}."
        )

    return jumps


def run(code: str) -> None:
    memory = [0] * 30_000
    pointer = 0
    instruction = 0

    jumps = build_jump_table(code)

    while instruction < len(code):

        command = code[instruction]

        if command == ">":
            pointer += 1

            if pointer >= len(memory):
                memory.append(0)

        elif command == "<":

            if pointer == 0:
                error(
                    "Memory pointer moved before cell 0."
                )

            pointer -= 1

        elif command == "+":
            memory[pointer] = (
                memory[pointer] + 1
            ) % 256

        elif command == "-":
            memory[pointer] = (
                memory[pointer] - 1
            ) % 256

        elif command == ".":
            print(
                chr(memory[pointer]),
                end="",
                flush=True,
            )

        elif command == ",":
            try:
                value = input(
                    "\nInput one byte: "
                )
            except EOFError:
                value = ""

            memory[pointer] = (
                ord(value[0]) if value else 0
            ) % 256

        elif command == "[":
            if memory[pointer] == 0:
                instruction = jumps[instruction]

        elif command == "]":
            if memory[pointer] != 0:
                instruction = jumps[instruction]

        instruction += 1

    print()


def show_info(config: dict[str, str]) -> None:
    print()
    print("Brainfuck Easy Mode")
    print(f"Version {VERSION}")
    print()
    print("Configured language:")
    print()

    for symbol, meaning in OPERATIONS.items():
        print(
            f"  {symbol}  ->  "
            f"{config[symbol]!r:<20} "
            f"({meaning})"
        )

    print()


def compile_file(filename: str) -> None:
    path = Path(filename)

    if not path.exists():
        error(f'File not found: "{filename}"')

    if not path.is_file():
        error(f'Not a file: "{filename}"')

    source = path.read_text(
        encoding="utf-8"
    )

    config = parse_config(source)
    program = parse_program(source)

    brainfuck = compile_program(
        program,
        config,
    )

    show_info(config)

    print(
        f"Compiled {len(brainfuck)} "
        f"Brainfuck instructions."
    )

    print()
    print("Output")
    print("──────")

    run(brainfuck)

    print("──────")


def main() -> None:

    if len(sys.argv) == 1:
        print("Brainfuck Easy Mode")
        print(f"v{VERSION}")
        print()
        print("Usage:")
        print("  python bem.py <file>")
        print()
        print("Example:")
        print("  python bem.py hello.bem")
        return

    if len(sys.argv) != 2:
        print(
            "Usage: python bem.py <file>",
            file=sys.stderr,
        )
        sys.exit(2)

    try:
        compile_file(sys.argv[1])

    except BEMError as exc:
        print(
            f"\nBEM ERROR: {exc}",
            file=sys.stderr,
        )
        sys.exit(1)

    except UnicodeDecodeError:
        print(
            "\nBEM ERROR: File must be UTF-8.",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
