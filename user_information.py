def user_info():
    while True:
        global user_name, user_age, user_favcolor, user_bday, user_password, user_hobby
        user_name = input('What is your name? :').strip()
        user_age = input('What is your age? :').strip()
        user_favcolor = input('What is your favorite color? :').strip()
        user_bday = input('When is your birthday? (YYYYMMDD, example: 20101209 means December 9 in 2010): ').strip()
        user_hobby = input('What is your hobby? :').strip()
        user_password = ''

        # basic validation
        if not user_name:
            print('Name cannot be empty. Let us try again.')
            continue
        if not user_age.isdigit():
            print('Age should be numeric. Let us try again.')
            continue
        if not (len(user_bday) == 8 and user_bday.isdigit()):
            print('Birthday must be 8 digits in YYYYMMDD. Let us try again.')
            continue
        
        user_choice_change_or_keep_in_only_user_information = input('Are you sure, you want to change(1) or keep(2)? Once you keep, you cannot reset the information!')
        if user_choice_change_or_keep_in_only_user_information == '1':
            print('Ok, let us reset your information...')
            continue
        if user_choice_change_or_keep_in_only_user_information == '2':
            print('Saving...')
            break
