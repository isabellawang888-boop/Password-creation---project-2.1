def main():
    print('Hi! Welcome!')
    print('Before starting, we would like to know more about you!')
    print("Let's get started!")
    unsure_password = ''
    while True:
        while True:
            print("""If you would like to manually enter your own password that you want for 
            your account, return 1. If you would like us to generate a secure and strong password for you, 
            press 2 """)
            user_choice_generate_or_manually = input('1 or 2 ?: ')
            if user_choice_generate_or_manually == '1':
                import user_information
                user_information.user_info()
                unsure_password = input('Pls enter your password: ')
                print(f'Your password is {unsure_password}.')
                break

            elif user_choice_generate_or_manually == '2':
                import user_information
                user_information.user_info()
                import generating
                unsure_password = generating.randomly_choose()
                break
            else:
                print('invalid format of input, press 1 or 2')
                

        print('Did you like your password?')
        print("""If you want to change your password, please press 1. If you want to keep your password, press 2.""")
        user_choice_change_or_keep = input('1 or 2 ? :')
        if user_choice_change_or_keep == '1':
            
            print('Resetting your password...')
            continue
        if user_choice_change_or_keep == '2':
            # unsure_password to user_password in the user_information
            user_password = unsure_password
            try:
                import user_information
                user_information.user_password = user_password
            except Exception:
                pass
        print(f'Your password is officially set {user_password}.')
        break
            


if __name__ == '__main__':
    main()
