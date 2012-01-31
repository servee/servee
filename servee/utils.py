def space_out_camel_case(camel):
    """
    Converts a "CamelCasedName" to "Camel Case Name".
    """
    chars = []

    for char in camel:
        if len(chars) >= 2 and chars[-1] != ' ':
            if char.isupper() and chars[-1].islower():
                chars.append(' ')
            elif char.islower() and chars[-1].isupper() and chars[-2].isupper():
                chars.insert(len(chars) - 1, ' ')

        chars.append(char)

    return ''.join(chars)
