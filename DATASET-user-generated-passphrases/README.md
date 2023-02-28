Readme updated.

## Run instructions
To run the code:
- Download the repository
- Extract the file **data.zip** in the **data** folder
- run
```
python passphrase-segmentation.py
```
- Results are saved in **segmented-passphrases.csv**

## Data files
Following are the data files in use:
- **cities.pkl** has the names of cities around the world
- **country.pkl** has all the country names
- **gerunds.pkl** has the gerund forms of most common verbs in English
- **first-names.txt** has list of common first names
- **orig-pw-w-freq.txt** has all the candidate passwords with frequencies attached
- **frequency_bigramdictionary** and **frequency_dictionary_en_82** are the bigram and unigram dictionaries used by **SymSpell** to get the word segmentation 
