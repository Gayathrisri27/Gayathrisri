#personality test application using python
import sys

def display(personality_type):
    print(f"Your personality type is -> {personality_type}")
def run():
    questions: list = [
        """
Question 1:
a.I love being with my friend groups or
b.I love enjoying alone
""",
        """
Question 2:
a.I share my thoughts with others or
b.I keep my thoughts private
""",
        """
Question 3:
a.I love organising events,interact with people and co ordinate with them or
b.seek private, solitary activities with quiet to concentrate
""",
        """
Question 4:
a.external, communicative, express yourself or
b.internal, reticent, keep to yourself
""",
        """
Question 5:
a.I initiate the activities or
b.I am deliberative
""",
        """
Question 6:
a. Horror genre  or
b.Humor genre
""",
        """
Question 7:
a.Beach or
b.Mountain
""",
        """
Question 8:
a. conventional or
b. unique
""",
        """
Question 9:
a.focus on here-and-now or
b.look to the future, global perspective, “big picture”
""",
        """
Question 10:
a.Past or
b.future
""",
        """
Question 11:
a.creative thinking or
b.critical thinking
""",
        """
Question 12:
a. frank or
b.  encouraging
""",
        """
Question 13:
a. tend to criticize or
b. tend to appreciate
""",
        """
Question 14:
a.tough-minded or
b.tender-hearted
""",
        """
Question 15:
a. issue-oriented or
b.people-oriented
""",
        """
Question 16:
a. organized or
b. flexible
""",
        """
Question 17:
a.  scheduled or
b.  spontaneous
""",
        """
Question 18:
a.regulated or
b. “live” and “let live”
""",
        """
Question 19:
a.preparation or
b.go with the flow
""",
        """
Question 20:
a. govern or
b. freedom
"""
    ]

    count_of_a: int = 0
    count_of_b: int = 0
    personality_dichotomy: str = ''
    count = 0

    for question in questions:
        answer = ''
        while not (answer == 'A' or answer == 'B'):
            count_of_a = 0
            count_of_b = 0
            try:
                answer = input(question).upper()
                if not (answer == 'A' or answer == 'B'):
                    raise ValueError("Invalid input")
            except ValueError as error:
                print(error)
            else:
                if answer == 'A':
                    count_of_a = count_of_a + 1
                if answer == 'B':
                    count_of_b = count_of_b + 1
                count = count + 1

        if count == 5:
            if count_of_a > count_of_b:
                personality_dichotomy = personality_dichotomy + 'E '
            else:
                personality_dichotomy = personality_dichotomy + 'I '
        else:
            if count == 10:
                if count_of_a > count_of_b:
                    personality_dichotomy = personality_dichotomy + 'S '
                else:
                    personality_dichotomy = personality_dichotomy + 'N '
            else:
                if count == 15:
                    if count_of_a > count_of_b:
                        personality_dichotomy = personality_dichotomy + 'T '
                    else:
                        personality_dichotomy = personality_dichotomy + 'F '
                else:
                    if count == 20:
                        if count_of_a > count_of_b:
                            personality_dichotomy = personality_dichotomy + 'J '
                        else:
                            personality_dichotomy = personality_dichotomy + 'P '

    display(personality_dichotomy)


def exit_application():
    print("Exiting application...")
    sys.exit(0)


def main():
    user_input = input("""
    Welcome to the  Personality Test
    Press 1  to take test
    Press 2 to close the app -> """)
    try:
        if not (user_input == "1" or user_input == "2"):
            raise ValueError("Invalid input")
    except ValueError as error:
        print(error)
    else:
        switcher = {
            "1": run,
            "2": exit_application
        }
        return switcher.get(user_input)()


if __name__ == "__main__":
    main()
