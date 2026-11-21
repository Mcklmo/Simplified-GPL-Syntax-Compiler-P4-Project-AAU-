# Simplified GPL Syntax Compiler

## Requirements

Make sure you have a recent python version and all requirements installed, using:

`pip install -r requirements.txt`

You might have to first create a virtual environment:

`python -m venv env`

## Update parser

After making changes to the grammar.

`antlr4 -Dlanguage=Python3 src\AlgoPractise.g4 -visitor -no-listener`

>Remember to move `AlgoPractiseLexer.py` to `src/_lexer` and `AlgoPractiseParser.py` to `src/_parser`

### Alternative without python for Mac

```bash
brew install antlr
java -jar "$(brew --prefix)/opt/antlr/antlr-4.13.2-complete.jar" -Dlanguage=Python3 src/AlgoPractise.g4 -visitor -no-listener
```

## Compile source code

`src\main.py`

## Testing

`src\tests.py`
