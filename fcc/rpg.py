name = ' alenkeith'
print(' ' in name)

print (f"""hello {name},
are you good""")

full_dot = '●'
empty_dot = '○'
strength = 4
strengthDot = full_dot*strength + empty_dot * (10 - strength)
print( f"""{name}
    STR {strengthDot}

    """)

#final solution
full_dot = '●'
empty_dot = '○'

def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str):
        return "The character name should be a string"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"

    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    if (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"

    strengthDot = full_dot*strength + empty_dot * (10 - strength)
    intDot = full_dot*intelligence + empty_dot * (10 - intelligence)
    chDot = full_dot*charisma + empty_dot * (10 - charisma)

    return f"{name}\nSTR {strengthDot}\nINT {intDot}\nCHA {chDot}"

print(create_character("ren", 4, 2, 1))