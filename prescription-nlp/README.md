# Prescription NLP Pipeline

# Approach

This project extracts structured information from raw prescription text using a hybrid NLP approach.

# 1. Preprocessing

* Converted text to lowercase
* Normalized common abbreviations (e.g., tab → tablet, cap → capsule)
* Cleaned noisy and inconsistent text

# 2. NLP Processing

* Used spaCy for basic text processing and tokenization

# 3. Information Extraction

* Applied regex patterns to extract:

  * Strength (e.g., 25 mg)
  * Dosage (e.g., 1 tablet)
  * Duration (e.g., 5 days)
* Used rule-based logic to identify:

  * Medicine name
  * Frequency (OD, BD, TDS, etc.)
  * Notes (after food, at bedtime, etc.)

# 4. Output

* Converted extracted data into structured JSON format



#  Pipeline Flow

Raw Text → Cleaning → NLP → Rule-based Extraction → JSON Output



# Trade-offs

* Fast and simple
* Works well for structured prescriptions
* Limited handling of spelling errors
* Depends on predefined rules


