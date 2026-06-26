# Password-creation---project-2.1
A system that allows user to manually input their password or let the system generates one.


Description:
This project collects user information and either accepts a manual password or generates a secure password automatically based on the entered details.

Files:
- main.py: program entry point and user menu flow.
- user_information.py: collects and validates user information.
- generating.py: creates passwords from user data and returns the result.

How to run:
1. Open a terminal in the project folder.
2. Run:
   python3 main.py
3. Follow the prompts:
   - Choose 1 to enter your own password.
   - Choose 2 to generate a password automatically.

Notes:
- The generator uses name, age, favorite color, birthday, and hobby to build a password.
- If you choose a generated password, the program prints it and stores it as the final password.
- Basic validation ensures the name is not empty, age is numeric, and birthday is in YYYYMMDD format.

Example:
> python3 main.py
> 2
> [answer prompts for name, age, color, birthday, hobby]
> [generated password output]
> 2 (to keep the password)
