import argparse

import calculation_logic as calc


def main() -> None:
    #Declare a parser
    parser = argparse.ArgumentParser(prog= "Mental_Math",
                                     description= "A simple tool to train Mental Math")
    #Add four arguments to configure the number of questions, the operations type available, the min and max calue of the numbers
    parser.add_argument("-q", "--questions", type= int, action= "store", default = 1, help="Enter the number of questions (from 1 to 99)")
    parser.add_argument("-o", "--ops", "--operations", type= str, action= "store", default= "+", help = "Select the operations type you want (+ - * /)")
    parser.add_argument("-m", "--min", type= int, action="store", default="1", help= "Enter the maximum number value for the calculations")
    parser.add_argument("-m", "--max", type= int, action="store", default="100", help= "Enter the maximum number value for the calculations")

    args = parser.parse_args()
    

if __name__ == "__main__":
    main()