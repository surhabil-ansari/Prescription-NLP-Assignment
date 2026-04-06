import re

FREQ_MAP = {
    "od": "OD",
    "bd": "BD",
    "tds": "TDS",
    "qid": "QID",
    "hs": "HS",
    "sos": "SOS",
    "prn": "PRN",
}


def extract_all(text):

    result = {
        "medicine_name": "",
        "form": "",
        "strength": "",
        "dosage": "",
        "frequency": "",
        "duration": "",
        "notes": "",
    }

    words = text.split()

    # FORM
    forms = ["tablet", "capsule", "syrup", "injection", "susp"]
    for f in forms:
        if f in text:
            result["form"] = f
            break

    # STRENGTH
    strength = re.search(r"\d+\s?(mg|iu|mcg|ml)", text)
    if strength:
        result["strength"] = strength.group()

    # DOSAGE
    dosage = re.search(r"\d+\s?(tablet|capsule|ml|ampoule|vial|units)", text)
    if dosage:
        result["dosage"] = dosage.group()

    # FREQUENCY
    for key in FREQ_MAP:
        if key in text:
            result["frequency"] = FREQ_MAP[key]
            break

    freq_pattern = re.search(r"\d-\d-\d", text)
    if freq_pattern:
        result["frequency"] = freq_pattern.group()

    # DURATION
    duration = re.search(r"\d+\s?(day|days|d|week|wk|weeks)", text)
    if duration:
        result["duration"] = duration.group()

    #  MEDICINE NAME
    ignore = ["tablet", "capsule", "syrup", "injection", "susp"]
    for w in words:
        if w not in ignore and not re.search(r"\d", w):
            result["medicine_name"] = w.capitalize()
            break

    # NOTES
    notes_keywords = ["after", "before", "bedtime", "morning", "empty", "with", "for"]
    notes = []
    for w in words:
        for k in notes_keywords:
            if k in w:
                notes.append(w)
    result["notes"] = " ".join(notes)

    return result
