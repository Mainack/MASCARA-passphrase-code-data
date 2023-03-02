# MASCARA: Passphrase Generation

The file `mascara.py` is the underlying code used to generate a memorable passphrase as presented in our work. 

## Uncompress Data

## Requirements

The code is written in `Python3` and tested in `Python3.8`. The following python packages are the required dependencies

- `pickle`
- `numpy`
- `nltk`

The first time `mascara.py` is run, uncomment `lines 9,10,11` so that the required nltk packages can be downloaded.

## Running

To make the program straightforward, we didn't support any cmdline parameters, so it can be run using `python mascara.py` from this folder. This generates 30 passphrases of different lengths as defined in `line 137`. To control the number of passphrases generated and their length, modify the variable in `line 137` accordingly.

