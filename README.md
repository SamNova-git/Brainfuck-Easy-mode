# 🧠 Brainfuck Easy Mode

> Brainfuck, but you choose the commands.

**Brainfuck Easy Mode (BEM)** is a configurable Brainfuck compiler/interpreter written in a single Python file.

Instead of being forced to write:

`+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++.`

you can define your own names for Brainfuck commands.

For example:

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
    eeeeeeeeeeeeeet

The compiler converts your custom commands into normal Brainfuck and executes the result.

---

## ✨ Features

- 🧠 Based on Brainfuck
- 🔧 Fully customizable commands
- 🔤 Command names can be anything
- 📏 Multi-character commands supported
- ⚡ Longest-token matching
- 🔁 Brainfuck loops supported
- ⌨️ Input supported
- 💾 30,000 memory cells
- 🔢 8-bit cells
- 🛑 Compiler error checking
- 📦 Single-file compiler
- 🐍 Pure Python
- 🚫 No external dependencies

---

## 📥 Getting Started

### Requirements

You need:

- Python 3.x
- Git (optional)

Clone the repository:

    git clone https://github.com/YOUR_USERNAME/Brainfuck-Easy-Mode.git
    cd Brainfuck-Easy-Mode

Run BEM:

    python bem.py

Run a program:

    python bem.py hello.bem

---

# 📖 BEM Syntax

A BEM program has two sections:

    CONFIG{
        ...
    }

    PROGRAM-
    ...

The `CONFIG` section defines the names of the eight Brainfuck commands.

The `PROGRAM-` section contains your actual program.

---

# ⚙️ CONFIG

There are exactly eight Brainfuck commands:

| Brainfuck | Function |
|---|---|
| `>` | Move pointer right |
| `<` | Move pointer left |
| `+` | Increment cell |
| `-` | Decrement cell |
| `.` | Output character |
| `,` | Input character |
| `[` | Start loop |
| `]` | End loop |

You can give every command your own name.

Example:

    CONFIG{
        > = "right"
        < = "left"
        + = "add"
        - = "remove"
        . = "print"
        , = "input"
        [ = "start"
        ] = "end"
    }

Then:

    addaddaddprint

represents:

    +++.

---

# 🤯 The Names Can Be Anything

The compiler does **not** give command names special meanings.

For example:

    CONFIG{
        > = "banana"
        < = "potato"
        + = "waffle"
        - = "cheese"
        . = "pizza"
        , = "keyboard"
        [ = "lol"
        ] = "NOPE"
    }

This is completely valid.

The compiler only cares about the mapping.

If the configuration contains:

    + = "waffle"

then `waffle` represents `+`.

It does not matter what the word actually means.

---

# 🔥 Multi-Character Commands

Command names can contain multiple characters.

Example:

    CONFIG{
        > = "MOVE_RIGHT"
        < = "MOVE_LEFT"
        + = "INCREASE"
        - = "DECREASE"
        . = "DISPLAY"
        , = "READ"
        [ = "LOOP_START"
        ] = "LOOP_END"
    }

    PROGRAM-
    INCREASEINCREASEINCREASEDISPLAY

This is equivalent to:

    +++.

---

# 📝 Example Program

Create a file called `hello.bem`.

Put this inside:

    CONFIG{
        > = "R"
        < = "L"
        + = "PLUS"
        - = "MINUS"
        . = "OUT"
        , = "IN"
        [ = "BEGIN"
        ] = "END"
    }

    PROGRAM-
    PLUSPLUSPLUSPLUSPLUSPLUSPLUSPLUSPLUSPLUSOUT

Run it:

    python bem.py hello.bem

---

# 🧩 Brainfuck Compatibility

You can configure BEM to use the original Brainfuck syntax:

    CONFIG{
        > = ">"
        < = "<"
        + = "+"
        - = "-"
        . = "."
        , = ","
        [ = "["
        ] = "]"
    }

    PROGRAM-
    ++++++++++.

This means BEM can also behave like a normal Brainfuck interpreter.

---

# 🛠️ Compiler Pipeline

    BEM source
        │
        ▼
    CONFIG parser
        │
        ▼
    Command mapping
        │
        ▼
    Tokenizer
        │
        ▼
    Brainfuck code
        │
        ▼
    Brainfuck interpreter
        │
        ▼
    Program output

---

# 🚨 Error Checking

BEM detects problems such as:

- Missing `CONFIG`
- Missing `PROGRAM-`
- Missing Brainfuck commands
- Duplicate command names
- Unknown commands
- Unmatched `[`
- Unmatched `]`
- Moving the memory pointer before cell 0
- Missing source files
- Invalid UTF-8 files

Example error:

    BEM ERROR: CONFIG is missing command(s): "+"

---

# 💻 Running BEM

Run a program:

    python bem.py program.bem

Run without arguments:

    python bem.py

BEM displays usage information.

---

# 📂 Project Structure

    Brainfuck-Easy-Mode/
    │
    ├── bem.py
    ├── README.md
    ├── LICENSE
    │
    └── examples/
        ├── hello.bem
        └── ...

The compiler itself is just:

    bem.py

No external dependencies are required.

---

# 🐍 Requirements

- Python 3.x
- No external Python packages

Check your Python version:

    python --version

---

# 🚀 Roadmap

- [x] Configurable Brainfuck commands
- [x] Multi-character commands
- [x] Brainfuck interpreter
- [x] Loops
- [x] Input
- [x] Error handling
- [x] Single-file compiler
- [ ] Compile to `.bf`
- [ ] `--compile`
- [ ] `--run`
- [ ] `--version`
- [ ] `--help`
- [ ] Better line/column error reporting
- [ ] Comments
- [ ] Debug mode
- [ ] Memory visualizer
- [ ] Step-by-step execution
- [ ] VS Code syntax highlighting
- [ ] VS Code extension
- [ ] More example programs

---

# 🧪 Cursed Example

You can make a completely ridiculous language configuration:

    CONFIG{
        > = "GO"
        < = "BACK"
        + = "MORE"
        - = "LESS"
        . = "YAP"
        , = "LISTEN"
        [ = "DO"
        ] = "DONE"
    }

    PROGRAM-
    MOREMOREMOREMOREMOREYAP

BEM doesn't care whether the names make sense.

That's the point. 😭

---

# 🎯 Why Brainfuck Easy Mode?

Brainfuck is famous for being extremely minimal.

It has only eight commands:

    > < + - . , [ ]

BEM keeps those eight commands while allowing programmers to rename them.

This makes BEM useful for:

- Learning Brainfuck
- Experimenting with programming languages
- Creating cursed programming languages
- Creating custom syntax
- Building Brainfuck-based projects
- Language design experiments

---

# 📜 License

See the `LICENSE` file for the license used by this project.

---

# 👤 Author

Created by **Samuel Shinto**.

Brainfuck Easy Mode is an experimental programming language and compiler built around the idea of making Brainfuck customizable.

---

# ⭐ Support

If you like the project, consider giving the repository a ⭐ on GitHub.

    Brainfuck
        ↓
    Brainfuck Easy Mode
        ↓
    Custom commands
        ↓
    Absolute chaos

**Welcome to Brainfuck Easy Mode. 🧠🔥**
