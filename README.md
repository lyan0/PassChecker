# PassChecker

A Python CLI tool that scores password strength and checks against leaked-password lists like RockYou.

![Python](https://img.shields.io/badge/python-3.8+-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Features

- Scores passwords 0–100
- Checks against RockYou or any leaked-password list
- Ratings: Very Weak / Weak / Moderate / Strong / Excellent
- Detects lowercase, uppercase, digits, symbols, length, and leaks
- Customizable symbol list
- No external dependencies

## Scoring

| Rule | Points |
|---|---|
| Contains lowercase (a-z) | +5 |
| Contains uppercase (A-Z) | +10 |
| Contains digit (0-9) | +10 |
| Contains symbol | +20 |
| Longer than 8 chars | +15 |
| Not leaked | +40 |
| **Total** | **100** |

## Requirements

- Python 3.8+
- A leaked-password list (not included)

## Setup

### 1. Clone the repo

bash
git clone https://github.com/lyan0/passchecker.git
cd passchecker

2. Get a password list

On Kali / Parrot:

bash
sudo gunzip /usr/share/wordlists/rockyou.txt.gz

On other systems:

bash
wget https://github.com/brannondorsey/naive-hashcat/releases/download/data/rockyou.txt

3. Set the path (optional)

The tool looks for RockYou at /usr/share/wordlists/rockyou.txt by default.

To use a different list, pick one:

Option A — Edit the script:

python
PASSWORD_FILE = os.getenv("PASSWORD_FILE", "/your/path/here.txt")

Option B — Environment variable (temporary):

bash
export PASSWORD_FILE=/your/path/here.txt

Option C — Run inline (one time):

bash
PASSWORD_FILE=/your/path/here.txt python3 passchecker.py

## Usage

bash
python3 passchecker.py

## Example:

Enter password to check (or 'q' to quit): X9$mK#pL2@vQ
Score: 100%  ->  Excellent
Meets all requirements: YES
Leaked: NO

## Privacy

· Passwords are never stored or sent anywhere.
· The tool only compares against a local list.
· No data leaves your machine.

## Disclaimer

For educational and defensive use only. Do not use against systems you don't own.

## License

MIT
