# Requirements
Make sure you have a recent python version and all requirements installed, using:

`pip install -r requirements.txt`

You might have to first create a virtual environment:

`python -m venv env`

And activate it:

`env\scripts\activate`

If unsure whether installing the requirements was successful, run:

`pip freeze`

and check if the module names from `requirements.txt` are listed.

# Create or update parser

`antlr4 -Dlanguage=Python3 src\AlgoPractise.g4 -visitor -nolisteners`

[Remember to move `AlgoPractiseLexer.py` to `src/_lexer` and `AlgoPractiseParser.py` to `src/_parser`!]

# Parse source code

`src\main.py`


# Testing
`src\tests.py`
