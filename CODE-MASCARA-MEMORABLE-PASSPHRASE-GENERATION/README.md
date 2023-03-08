# CODE & DATA FOR MASCARA: Memorable and Secure Passphrase Generation

The file `mascara.py` is the underlying code used to generate memorable yet secure passphrases as presented in our [ACM ASIACCS'23 paper](https://cse.iitkgp.ac.in/~mainack/publications/mascara-2023-asiaccs.pdf). The running instructions are below for running MASCARA. 

## Running instructions for MASCARA

### Download and uncompress Data
- Please download the `mascara-data.zip` from [https://osf.io/dnrcj](https://osf.io/dnrcj).
- Extract the zip file, and put its contents in a `data` folder. The folder should contain the following files (unigram, bigram and their probabilities extracted from wikipedia dataset, details [in the paper](https://cse.iitkgp.ac.in/~mainack/publications/mascara-2023-asiaccs.pdf))
  - `biprob.pkl`
  - `unigram-5p.pkl`
  - `bigram.pickle`
- Download `mascara.py` and put in the parent folder of `data`


### Install requirements

The code is written in `Python3` and tested in `Python3.8`. The following python packages are the required dependencies

- `pickle`
- `numpy`
- `nltk`

The first time `mascara.py` is run, uncomment `lines 9,10,11` so that the required nltk packages can be downloaded.

### Run the code

To make the program straightforward, we didn't include any cmdline parameters---MASCARA can be run using 
```
python mascara.py
``` 
It will show the generated MASCARA passphrases in the stdout. 

### NOTES

- Make sure the `data` folder (with the downloaded pkl files) should be in the same folder as `mascara.py`. 

- The code currently generates 30 MASCARA passphrases of different lengths as defined in `line 137`. To control the number of passphrases generated and their length, modify the variable in `line 137` accordingly.

