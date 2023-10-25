def to_camel_case(text):
    ultimaLocalizacion = 0
    for character in text:
        if character == "-":
            localizacion = text.find("-", ultimaLocalizacion + 1)
            caracterUpper = text[localizacion + 1].upper()
            text = text.replace(text[localizacion + 1], caracterUpper, 1)
            ultimaLocalizacion = localizacion
        elif character == "_":
            localizacion = text.find("_", ultimaLocalizacion + 1)
            caracterUpper = text[localizacion + 1].upper()
            text = text.replace(text[localizacion + 1], caracterUpper, 1)
            ultimaLocalizacion = localizacion

    text = text.replace ("_", "")
    text = text.replace ("-", "")
    return text
print(to_camel_case('A-Pippi-is-Omoshiroi'))