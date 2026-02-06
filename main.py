import secrets
import string

print('Anna salasanan pituus.')
print('Salasanan vähimmäispituus on 4 merkkiä (suositus vähintään 12 merkkiä)')

while True:
    try:
        pw_lenght = int(input('Salasanan pituus--> '))
        if pw_lenght < 4:
            print('Virhe: Salasanan vähimmäispituus on 4 merkkiä')
        else:
            break
    except ValueError:
        print('Virhe: Syötä kokonaisluku.')


lowercases = string.ascii_lowercase
uppercases = string.ascii_uppercase
digits = string.digits
special_characters = string.punctuation

all_characters = lowercases + uppercases + digits + special_characters

chosen_lc = secrets.choice(lowercases)
chosen_uc = secrets.choice(uppercases)
chosen_d = secrets.choice(digits)
chosen_sc = secrets.choice(special_characters)

password_list = [chosen_lc, chosen_uc, chosen_d, chosen_sc]

for i in range(pw_lenght - 4):
    new_character = secrets.choice(all_characters)
    password_list.append(new_character)

secrets.SystemRandom().shuffle(password_list)
password = ''.join(password_list)

print(f'Uusi salasanasi on: {password}')
