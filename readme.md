# Competitor Analysis

* **Author**: Jayesh Sidhwani

I started working on this project to use NLP to find competitors for a given company. It is usually a tough process
to google on the seed keyword, find companies and then find more keywords to find more companies. This was an attempt
to automate this process.

How it works:
1. Choose a seed keyword
2. Fetch all companies from crunchbase / other ways that use this keyword
3. Analyse their description using NLP to find more keywords that these companies use
4. Eventually you get a bag of keywords that you can target.
5. [Addition] I am planning to add a functionality that finds your closest competitors based on the keywords you have chosen

###Requirements

1. python - 2.7
2. NLTK: sudo pip install nltk

###Usage

Checkout the Github repo and import in your project


####Usage

##### Finding keywords:
```python

from analyse import Analyse
Analyse().extract_keywords()
```
---
##### Fetch companies based on your seed keyword:
```python

from fetch_company import FetchCompany
FetchCompany().get_crunchbase(_keyword_)
```
