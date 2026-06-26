"""Password generation helpers.

Each `way_*` function returns a generated password string and prints a short explanation.
`randomly_choose()` selects and executes one of the ways and returns the password.
"""
import user_information
import random

def way_1():
    name = (user_information.user_name or '').strip()
    first = name[0].upper() if len(name) > 0 else 'X'
    last = name[-1].upper() if len(name) > 1 else first
    age = user_information.user_age or '0'
    bday = user_information.user_bday or '00000000'
    pw = first + last + '@' + age + ')' + bday
    
    print(f"""This is your generated password: {pw}
Your password is generated using the data in your user information.
In this case the first and last letter of your user name (uppercased) + '@' + age + ')' + bday are used.
""")
    return pw

def way_2():
    hobby = (user_information.user_hobby or '')
    fav = (user_information.user_favcolor or '').upper()
    first_h = hobby[0] if len(hobby) > 0 else 'x'
    last_h = hobby[-1] if len(hobby) > 0 else 'x'
    pw = first_h + '&' + fav + ':' + last_h
    
    print(f"""This is your generated password: {pw}
Your password is generated using hobby's first letter + '&' + favorite color (uppercased) + ':' + hobby's last letter.
""")
    return pw

def way_3():
    age = user_information.user_age or '0'
    name_up = (user_information.user_name or '').upper()
    bday_tail = (user_information.user_bday or '00000000')[-4:]
    pw = age + ':)' + name_up + ':(' + bday_tail
    
    print(f"""This is your generated password: {pw}
Your password is generated using age + ':)' + username (uppercased) + ':(' + last 4 digits of bday.
""")
    return pw

def way_4():
    fav = (user_information.user_favcolor or '')
    bday = user_information.user_bday or '00000000'
    b_first = bday[0] if len(bday) > 0 else '0'
    b_last = bday[-1] if len(bday) > 0 else '0'
    pw = fav + '?' + (b_first + b_last) + '!' + (user_information.user_hobby or '').upper()
    
    print(f"""This is your generated password: {pw}
Your password is generated using favorite color + '?' + first and last char of bday + '!' + hobby (uppercased).
""")
    return pw


def randomly_choose():
    chosen_way = random.choice([way_1, way_2, way_3, way_4])
    return chosen_way()
