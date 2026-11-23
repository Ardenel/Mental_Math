import argparse

import mental_math.calculation_logic as calc


def main() -> None:
    #Declare a parser
    parser = argparse.ArgumentParser(prog= "Mental_Math",
                                     description= "A simple tool to train Mental Math")
    #Add four arguments to configure the number of questions, the operations type available, the min and max calue of the numbers
    parser.add_argument("-q", "--questions", type= int, action= "store", default = 1, help="Enter the number of questions (from 1 to 99)")
    parser.add_argument("-o", "--ops", "--operations", type = str, nargs="+", choices=["+", "-", "*"], action= "store", default= ["+"], help = "Select the operations type you want (+ - *)")
    parser.add_argument("-mi", "--min", type= int, action="store", default= 1, help= "Enter the maximum number value for the calculations")
    parser.add_argument("-ma", "--max", type= int, action="store", default= 100, help= "Enter the maximum number value for the calculations")

    args = parser.parse_args()

    #Create a mental math session
    session : calc.Session = calc.Session(args.questions, args.ops, args.min, args.max)
    #While the current number of questions is below the value asked by the user, print the question and get the answer
    while not session.is_finished():
        print(session.create_questions())
        answer = ask_int()
        #Print correct if correct or False instead
        print("Correct !" if session.check_answer(answer) else "False.")
    print(f"Score : {session.score}/{args.questions}")

#Get the user input
def ask_int() -> int:
    while True:
        #Try to convert the user input as an integer or raise an Exception
        try:
            return int(input())
        except ValueError:
            print("Enter an integer value")
    


if __name__ == "__main__":
    main()