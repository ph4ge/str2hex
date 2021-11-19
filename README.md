# str2hex

A quick and dirty tool to get a string hex representation, deal with endianness when trying to push strings on the stack.

Target ISA: x86

The is alpha code at best.

## Requirements

python >=3.7 : because of the use of *.isascii()*

fire

## Installation

It is preferable to install under a virtual environment([create python env](https://gist.github.com/ph4ge/97d2dbb6ca47434a8ee0e67aa47ad2c7))

```bash
python3 -m venv venv/py3-00/
```

Under the virtual environment:

```bash
pip3 install -r requirements.txt
```

or

```bash
pip3 install fire
pip3 install pytest-cov
```

## Running the tests

A number of trivial test cases exist under `tests/`. They can be ran:

Under the same virtual environment, we need `pytest`:

```bash
pip install pytest-cov
```
Running the tests under the `str2hex/`:

```bash
pytest
```

This step can be skipped.

## Running the script

```bash
# get hex representation of a string
python3 str2hex.py str2hex --astr="root"
root : 726f6f74

# get hex representation of a string and swap its endianness
python3 str2hex.py str2hex --astr="root" --se
root : 726f6f74
toor : 746f6f72

# get hex representation of for string with length > 4
python3 str2hex.py str2hex --astr="MessageBox"
Mess : 4d657373  ageB : 61676542  ox : 00006f78
```

