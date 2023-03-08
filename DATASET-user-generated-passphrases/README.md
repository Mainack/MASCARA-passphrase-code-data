# CODE and DATA FOR EXTRACTING ~73K REAL-WORLD IN-USE PASSPHRASES

This repository contains data of 72,999 User-generated passphrases that are collected by segmenting in-use passwords. More details about segmentation and the passwords are in our [ACM ASIACCS'23 paper ](https://cse.iitkgp.ac.in/~mainack/publications/mascara-2023-asiaccs.pdf). 

## Passphrase dataset

`segmented-passphrases.csv` in this repositoty contains the in-user passphrases. The columns in this csv file are: 

- **Original Password** : These are in-use  passwords which our algorithm detected as potential passphrases (e.g., _highschoolmusical123_)
- **Passphrase** : These are segmented in-use  passwords by our algorithm, the segmented version are the passphrases (e.g., _high school musical_)
- **Count** : This is the count of the unique users (email ids) which used this passphrase. 

The instruction to run our segmentation algorithm is below (whose output is `segmented-passphrases.csv`). The details of the algorithm is in our [ACM ASIACCS'23 paper ](https://cse.iitkgp.ac.in/~mainack/publications/mascara-2023-asiaccs.pdf).

## Instructions to run segmentation algorithm for regenrating this passphrase dataset

### Download and uncompress data

- Download `passphrase-segmentation.py` and `data.zip` from this Github repository
- Extract **data.zip** and put the files in a folder named **data** 
- Following are the files that should be in data folder:
  - **cities.pkl** has the names of cities around the world
  - **country.pkl** has all the country names
  - **gerunds.pkl** has the gerund forms of most common verbs in English
  - **first-names.txt** has list of common first names
  - **orig-pw-w-freq.txt** has all the candidate passwords with frequencies attached
  - **frequency_bigramdictionary** and **frequency_dictionary_en_82** are the bigram and unigram dictionaries used by **SymSpell** to get the word segmentation 


### Running the segmentation code
- Ensure you downloaded and extracted data as stated above 
- The code is written in `Python3` and tested in `Python3.8`. The following python packages are the required dependencies
  - `nltk`
  - `re`
  - `csv`
  - `pickle`
  - `json`
  - `itertools`
  - `symspellpy`

- run
```
python passphrase-segmentation.py
```
- Results are saved in **segmented-passphrases.csv**

