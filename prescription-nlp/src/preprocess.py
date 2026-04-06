def clean_text(text):
    text = text.lower()

    text = text.replace("tab.", "tablet")
    text = text.replace("tab", "tablet")
    text = text.replace("cap.", "capsule")
    text = text.replace("cap", "capsule")

    text = text.replace("fod", "food")
    text = text.replace("af", "after")
    text = text.replace("bf", "before")

    return text
