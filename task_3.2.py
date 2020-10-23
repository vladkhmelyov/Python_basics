
def pers_data(name, surname, d_birth, city, email, p_numb):
    """
    Описание персональных данных пользователя
    name - имя
    surname - фамилия
    d_birth - год рождения
    city - город проживания
    email - эл.почта
    p_numb - номер телефона
    """
    print(f"имя - {name}; фамилия - {surname}; год рождения - {d_birth}; "
          f"город проживания - {city}; эл.почта - {email}; номер телефона - {p_numb}")


name = input("ввести имя пользователя ")
surname = input("ввести фамилию пользователя ")
d_birth = input("ввести год рождения пользователя ")
city = input("ввести город проживания пользователя ")
email = input("ввести эл.почту пользователя ")
p_numb = input("ввести номер телефона пользователя ")
pers_data(name, surname, d_birth, city, email, p_numb)
