#  Mitsu

A lightweight and simple password generator CLI written in Python.

Generate secure passwords directly from your terminal with customizable length, character sets, and batch generation.

## Features

-  Custom password length
-  Include numbers
-  Include uppercase letters
-  Include special characters
-  Generate multiple passwords at once
-  Simple and easy-to-use command-line interface

##  Installation

Clone the repository:

```bash
git clone https://github.com/your-username/mitsu.git
cd mitsu
```

Run the script:

```bash
python mitsu.py [options]
```

##  Usage

```bash
python mitsu.py -l 12 -n -u -s -c 3
```

### Available Options

| Option | Description |
|---------|-------------|
| `-l`, `--length` | Set password length |
| `-c`, `--count` | Number of passwords to generate |
| `-n`, `--numbers` | Include numbers (`0-9`) |
| `-u`, `--uppercase` | Include uppercase letters (`A-Z`) |
| `-s`, `--special` | Include special characters |

##  Examples

Generate a 16-character password:

```bash
python mitsu.py -l 16
```

Generate 5 passwords with uppercase letters and numbers:

```bash
python mitsu.py -l 14 -u -n -c 5
```

Generate strong passwords with all character types:

```bash
python mitsu.py -l 20 -u -n -s -c 3
```

##  Built With

- Python 3
- argparse
- string
- random / secrets
