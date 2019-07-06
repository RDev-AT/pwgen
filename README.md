# pwgen

## What is pwgen

pwgen is yet another simple passphrase-generator (yes, passphrase, not password) written in Python - without any external dependencies. The goal of this tool is, to create easy-rememberable passwords without sacrificing security. pwgen reads words from any given dictionary and generates cryptographically secure passphrase out of it.

## What makes pwgen different

to be honest, there are many passphrase-generators, but here's what makes pwgen special

* pwgen can create passphrases by any given dictionary as input
* pwgen uses a cryptographically secure Random-Generation (not the usaul PRNG)
* pwgen reduces passphrases with repeating characters and patterns
* pwgen is free & open source, developed in stock Python

## Why do we need pwgen

Nowadays everybody is trying to find and enforce proper security- and data-protection policies.
Overly-fancy tooling supports achieving this goal, however what the tooling isn't capable of mitigating, is the
weakest link in the chain of any IT-System - the human being. No IT-System with human-interaction can be hardened to a level, that is able to counteract the weak passwords people pick.

The fundamental problem here is, that over the past 10 years, we taught people to pick overly complex passwords,
rather than actual secure passwords (see [relevant XKCD](https://www.xkcd.com/936/)). The effects of this misunderstanding can be found in various lists of exploited passwords (e.g. [SecLists by Daniel Miessler](https://github.com/danielmiessler/SecLists)).

### Caveats of traditional passwords

* passwords are to complex, people write it down somewhere
* passwords are to complex, people frequently forget them (poor Sysadmins need to reset it)
* passwords are not complex enough, passwords can be brute-forced
* passwords are not unique enough, passwords can be found in rainbow-tables

### Proper Passphrases with pwgen

Instead of creating hard to remember passwords, pwgen creates passphrases based on a dictionary (e.g. the english-language dictionary). Resulting passwords may look something like this:

* ```complete theory testwise fixture maniac super```
* ```terrible octopus likewise sounding poster couple```

You see, the generated passwords are easy to remember with a small mnemonic by hand, but they fulfill
all requirements for a secure password.

#### Quick probabilistic analysis

According to [wordcounter.io](https://wordcounter.io/blog/how-many-words-are-in-the-english-language/) the   Oxford English Dictionary (20th Edition) contains 171.476 unique words.

Just picking 6 words (not considering length of the words and duplicates) at random - of course with considering the order - from a total 171.476 words gives us the following amount of combinations, that are required to guess (brute-force) the passphrase:

n! / (n-k)! = 171476! / (171476 - 6)! = 2,542038212x10³¹ distinct combinations

In comparison: the total amount of atoms in the whole universe is estimated with approx. 3,0x10²³.
This means, guessing (and even brute-forcing) the password is very unlikely!

## Installation & first-run

* Clone the repository ```git clone https://github.com/r4r3-at/pwgen.git```
* Change to the cloned Repo ```cd pwgen/pwgen```
* You might want to add this directoy to the PATH-variable
* Use Python to run the Script ```python app.py```

## Usage

* create a profile matching your needs.
* get billions of custom, unique and mostly "speakable" passwords.

See comments in pwgen/app.py for quick results. For a more advanced
usage you probably should see pwgen/config.py too.

## Contribution

Feel free to contribute to this project! Thanks in advance!

## License GNU General Public License Version 3

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see [gnu.org/licenses](https://www.gnu.org/licenses/).
