# Evaluation Summary

# Overview

The prescription parsing system was evaluated using a hybrid NLP approach combining text preprocessing, spaCy-based tokenization, and rule-based extraction (regex and keyword matching). The evaluation focuses on extraction accuracy, handling of noisy text, code quality, robustness, and overall approach.



# 1. Extraction Accuracy

The system performs well on structured and semi-structured prescription text.

# Correct Example

Raw Text:
"Tab. Amitriptyline 25 mg 1 tablet OD for 5 days at bedtime"

Output:

* medicine_name: Amitriptyline
* form: tablet 
* strength: 25 mg 
* dosage: 1 tablet 
* frequency: OD 
* duration: 5 days 
* notes: at bedtime 

# All fields were correctly extracted.


# 2. Handling of Abbreviations and Noisy Text

The system handles common abbreviations like OD, BD, and SOS using rule-based mapping, but struggles with misspellings and highly noisy input.

# Failure Example

Raw Text:
"Fexofenadin 120 mg OD allergy 7 days"

Issue:

* medicine_name incorrectly extracted due to spelling variation

Reason:

* No spell correction or dictionary mapping implemented


# 3. Code Quality and Readability

* The code is modular and divided into separate files (preprocessing, extraction, main pipeline)
* Functions are clearly defined for each field (medicine, dosage, frequency, etc.)
* Easy to understand and extend

# Overall, the code is clean, maintainable, and readable.


# 4. Robustness Across Different Formats

The system performs well on common prescription formats but has limitations in highly unstructured cases.

# Works Well

* "1 tablet BD for 5 days"
* "2 capsules TDS after food"

# Limitations

* Missing form (e.g., "Atorva 20 mg OD")
* Complex patterns like "HS/7d"
* Variations like "1-0-1" not fully interpreted


# 5. Clarity of Approach and Trade-offs

# Approach:

A hybrid NLP pipeline was used:

* Text preprocessing for normalization
* spaCy for tokenization
* Regex and rules for structured extraction

# Trade-offs:

* Fast and easy to implement
* Works well for structured data
* Limited generalization
* Not robust to spelling errors and unseen patterns


# Conclusion

The system provides a strong baseline for extracting structured information from prescription text. While rule-based methods ensure speed and simplicity, integrating machine learning models such as custom NER or transformer-based models can significantly improve accuracy and robustness.
