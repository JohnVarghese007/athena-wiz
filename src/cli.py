import argparse
from utils import csv_reader, get_columns, get_csv_info,get_summary_stats
from plotting import get_linechart
from constants import COLORS
     

def introduce():
    print("\nHello there! \nI'm " + COLORS["BOLD"] + COLORS["CYAN"] + "Athena-Wiz"+COLORS["RESET"]+", a CLI plotting tool")
    print("Run with --commands to get started\n")

def menu():
    print(COLORS["BOLD"] + COLORS["MAGENTA"] +"\nCommands:"+COLORS["RESET"])
    print(COLORS["CYAN"]+ "--readcsv" + COLORS["RESET"] + " filename num_rows_to_display" + COLORS["CYAN"] + " --savecsv(optional)")
    print(COLORS["CYAN"]+ "--getcsvinfo" + COLORS["RESET"] + " filename")
    print(COLORS["CYAN"]+ "--summary" + COLORS["RESET"] + " filename")
    print(COLORS["CYAN"]+ "--getcols" + COLORS["RESET"] + " filename")
    print(COLORS["CYAN"]+ "--linechart" + COLORS["RESET"] + " filename" + COLORS["CYAN"] + " --saveplot(optional)\n"+COLORS["RESET"])
    


def main():
    introduce()
    parser = argparse.ArgumentParser(description = 'trial python cli argeparse code')
    parser.add_argument('--commands', action = 'store_true', help ='displaying list of commands' )

    parser.add_argument('--readcsv', nargs = 2, metavar=('filename','num_rows'), help='Read a CSV file')
    parser.add_argument('--savecsv', action='store_true', help='Save the output of --readcsv to the plots folder')

    parser.add_argument('--getcols', nargs = 1, type = str, metavar = ('filename'), help = 'get the column names for the csv file')

    parser.add_argument('--linechart', nargs = 1, type = str, metavar = ('filename'), help = 'plotting the line chart')
    parser.add_argument('--saveplot', action='store_true', help='Save the plot/chart to the plots folder')

    parser.add_argument('--summary', nargs = 1, metavar=('filename'), help = 'Printing summary stats')
    parser.add_argument('--getcsvinfo', nargs = 1, metavar=('filename'), help = 'Printing df.info()')
    


    parser = parser.parse_args()

    if parser.commands:        
        menu()
    
    elif parser.readcsv:
        csv_reader(parser)

    elif parser.getcols:
        get_columns(parser)

    elif parser.linechart:
        get_linechart(parser)
    
    elif parser.summary:
        get_summary_stats(parser)
    
    elif parser.getcsvinfo:
        get_csv_info(parser)
    
    # set up framework for use of colors
    # yellow -> ask user for input 
    # green displaying output for csv stuff
    # saving files to path - magenta
    # warning/disclaimer  - red
    # pprint message everytime a file is saved to memory along with location





            
        
    

if __name__ == "__main__":
    main()