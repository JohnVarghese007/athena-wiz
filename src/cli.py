import argparse
from utils import csv_reader,get_columns
from plotting import get_linechart
from constants import COLORS
     

def introduce():
    print("\nHello there! \nI'm " + COLORS["BOLD"] + COLORS["CYAN"] + "Athena-Wiz"+COLORS["RESET"]+", a CLI plotting tool")
    print("Run with --commands to get started\n")

def menu():
    print(COLORS["BOLD"] + COLORS["MAGENTA"] +"\nCommands:"+COLORS["RESET"])
    print(COLORS["YELLOW"]+ "--readcsv filename num_rows_to_display --savecsv(optional)"+COLORS["RESET"])
    print(COLORS["YELLOW"]+ "--getcols filename")
    print(COLORS["YELLOW"]+ "--linechart filename --saveplot(optional)\n"+COLORS["RESET"])

def main():
    introduce()
    parser = argparse.ArgumentParser(description = 'trial python cli argeparse code')
    parser.add_argument('--commands', action = 'store_true', help ='displaying list of commands' )

    parser.add_argument('--readcsv', nargs = 2, metavar=('filename','num_rows'), help='Read a CSV file')
    parser.add_argument('--savecsv', action='store_true', help='Save the output of --readcsv to the plots folder')

    parser.add_argument('--getcols', nargs = 1, type = str, metavar = ('filename'), help = 'get the column names for the csv file')

    parser.add_argument('--linechart', nargs = 1, type = str, metavar = ('filename'), help = 'plotting the line chart')
    parser.add_argument('--saveplot', action='store_true', help='Save the plot/chart to the plots folder')

    parser = parser.parse_args()

    if parser.commands:        
        menu()
    
    elif parser.readcsv:
        csv_reader(parser)

    elif parser.getcols:
        get_columns(parser)

    elif parser.linechart:
        get_linechart(parser)


# WORK ON A --getcsvinfo filename command
# WORK ON A --histogram filename command
# that should hopefully be it
# figure out how to split main into multiple files
#also remmember to add savefig for all the plots, currently not saving anything


            
        
    

if __name__ == "__main__":
    main()