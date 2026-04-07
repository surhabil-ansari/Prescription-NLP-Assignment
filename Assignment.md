# Prescription NLP Assignment

## Goal
Build an NLP pipeline that extracts structured prescription information from raw_text.

## Dataset
You are given a file named `prescription_raw_text_only.json`.

Each record contains only the raw prescription text that must be parsed by your pipeline.

Example input record:

```json
{
  "raw_text": "Tab. Amitriptyline 25 mg 1 tablet OD for 5 days at bedtime"
}
```

## Task
From each `raw_text` value, extract the following fields in structured JSON format:

- `medicine_name`
- `form`
- `strength`
- `dosage`
- `frequency`
- `duration`
- `notes`

## Expected Output Schema

```json
{
  "raw_text": "<original raw text>",
  "medicine_name": "<string>",
  "form": "<string>",
  "strength": "<string>",
  "dosage": "<string>",
  "frequency": "<string>",
  "duration": "<string>",
  "notes": "<string>"
}
```

Example output record:

```json
{
  "raw_text": "Tab. Amitriptyline 25 mg 1 tablet OD for 5 days at bedtime",
  "medicine_name": "Amitriptyline",
  "form": "tablet",
  "strength": "25 mg",
  "dosage": "1 tablet",
  "frequency": "OD",
  "duration": "5 days",
  "notes": "at bedtime"
}
```

## Requirements

- Read the input dataset from `prescription_raw_text_only.json`
- Design an extraction pipeline using NLP, rules, ML, or a hybrid approach
- Output the extracted results as structured JSON
- Handle noisy and inconsistent prescription text as robustly as possible

## Deliverables

- Source code
- A short README explaining the approach
- Output file containing structured records
- Brief evaluation summary with examples of correct predictions and failure cases

## Evaluation Criteria

- Extraction accuracy
- Handling of abbreviations and noisy text
- Code quality and readability
- Robustness across different prescription formats
- Clarity of approach and tradeoff discussion

## Important Expectation

This assignment is not intended to reward simply using the largest possible model to generate answers.

The main objective is to evaluate how professionally and effectively you apply machine learning and NLP techniques to a real extraction problem. We are looking for thoughtful problem formulation, strong preprocessing, sensible modeling choices, error analysis, and clear engineering judgment.

If you use LLMs, do so in a deliberate and well-justified way. The quality of your approach, rigor of your reasoning, and practicality of your solution matter more than raw model size.

## Notes

- You may use rule-based NLP, machine learning, spaCy, transformers, or a hybrid method
- You should document assumptions clearly
