# Simplified GPL Syntax Compiler

## Requirements

Install [uv](https://docs.astral.sh/uv/), then from the repository root:

```bash
uv sync
```

## Update parser

After making changes to the grammar.

`uv run antlr4 -Dlanguage=Python3 src/AlgoPractise.g4 -visitor -no-listener`

>Remember to move `AlgoPractiseLexer.py` to `src/_lexer` and `AlgoPractiseParser.py` to `src/_parser`

### Alternative without python for Mac

```bash
brew install antlr
java -jar "$(brew --prefix)/opt/antlr/antlr-4.13.2-complete.jar" -Dlanguage=Python3 src/AlgoPractise.g4 -visitor -no-listener
```

## Compile and run a program

Running the compiled program needs the [.NET SDK](https://dotnet.microsoft.com/download) 10 or newer (`dotnet` on your PATH).

From the repository root, run:

```bash
uv run src/main.py
```

This compiles `input_stream/qsort.algo` to `Program.cs`, then runs it with `dotnet run` and prints the output.

To compile a different program, change `SOURCE_CODE_FILE_NAME` in `src/main.py`, e.g. to `input_stream/fizzbuzz.algo`.

## Testing

```bash
uv run src/tests.py
```
