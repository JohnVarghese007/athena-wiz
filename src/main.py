import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

FILE_NAME = r"C:\Users\User\OneDrive\Desktop\anacondaProjects\world_bank_growth_potential_index\data\world_bank_data_2025.csv"
LINE_CHART_ACCEPTABLE_DTYPES = [
    int, float
]

def add_func(parser):
    result = parser.add[0] + parser.add[1]
    print(f"Result: {result}")

def subtract_func(parser):
    result = parser.subtract[0] - parser.subtract[1]
    print(f"Result: {result}")

def name_func(parser):
    result = parser.fullname[0] + " " + parser.fullname[1]
    print(f"Full name: {result}")

def file_exists(filename):
    return os.path.exists(filename)

def csv_reader(parser):
    val = int(parser.readcsv[1])
    file_path = parser.readcsv[0]
    file_path = FILE_NAME

    if(file_exists(file_path) is False):
        print('Invalid file path')
        return
    
    df = pd.read_csv(file_path)
    new_df = df.head(val)

    if parser.savecsv:
        output_path = "output_subset.csv"
        new_df.to_csv(output_path, index=False)
        print(f"Saved top {val} rows to {output_path}")
    else:
        print(new_df)

def get_columns(parser):
    file_path = parser.getcols[0]
    file_path = FILE_NAME
    if(file_exists(file_path) is False):
        print('Invalid file path')
        return
    else:
        df = pd.read_csv(file_path)
        colList = df.columns.to_list()
        print(f"total number of columns in dataframe = {len(colList)}")
        for i,item in enumerate(colList):
            if i % 3 == 0:
                print("\n"+item, end = "\t")
            print(item, end = "\t")

def get_linechart(parser):
    file_name = str(parser.linechart[0])
    x_col = str(parser.linechart[1])
    y_col = str(parser.linechart[2])

    if(file_exists(file_name) is False):
        print('Invalid file path')
        return
    
    df= pd.read_csv(file_name)
    colList = df.columns.to_list()
    if x_col not in colList or y_col not in colList:
        print("Enter a valid column")   
        print("see --commands for options to view all columns in file")
        return
    
    if(df[x_col].dtype not in LINE_CHART_ACCEPTABLE_DTYPES or df[y_col].dtype not in LINE_CHART_ACCEPTABLE_DTYPES):
        print(f"Invalid datatype in columns\n Acceptable datatypes are: {LINE_CHART_ACCEPTABLE_DTYPES}\n")
        return
    
    title = str(input("Enter the title for your bar chart"))
    grid = str(input("Do you want a grid?\nEnter YES for grid"))
    plt.plot(df[x_col], df[y_col], color = 'red', label = y_col)
    plt.title(title, fontsize=16)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    if(grid == 'YES'):
        plt.grid()
    plt.legend()
    plt.tight_layout()    
    plt.show()



        



def menu():
    print("Simple CLI calculator to perform arithmetic calculations on two numbers:")
    print("Here are your options:")
    print("--add number1 number 2")
    print("--subtract number1 number 2")
    print("--fullname firstname lastname")
    print("--readcsv filename num_rows_to_display")
    print("--getcols filename")
    print("--linechart filename column_name_for_xaxis column_name_y axis")

def main():
    parser = argparse.ArgumentParser(description = 'trial python cli argeparse code')
    parser.add_argument('--commands', action = 'store_true', help ='displaying list of commands' )
    parser.add_argument('--add', nargs=2, type=float, metavar=('num1', 'num2'),help='Add two numbers')
    parser.add_argument('--subtract', nargs=2, type=float, metavar=('num1', 'num2'),help='Subtract two numbers')
    parser.add_argument('--fullname', nargs=2, type=str, metavar=('first', 'last'),help='Print full name')

    parser.add_argument('--readcsv', nargs = 2, metavar=('filename','num_rows'), help='Read a CSV file')
    parser.add_argument('--savecsv', action='store_true', help='Save the output of --readcsv to the plots folder')

    parser.add_argument('--getcols', nargs = 1, type = str, metavar = ('filename'), help = 'get the column names for the csv file')

    parser.add_argument('--linechart', nargs = 3, type = str, metavar = ('filename','column name for x axis', 'column name for y axis'))
    parser.add_argument('--saveplot', action='store_true', help='Save the plot/chart to the plots folder')

    parser = parser.parse_args()

    if parser.commands:        
        menu()

    elif parser.add:
        add_func(parser)

    elif parser.subtract:
        subtract_func(parser)

    elif parser.fullname:
        name_func(parser)

    elif parser.readcsv:
        if parser.readcsv[0] is None or parser.readcsv[1] is None:
            print('Invalid input. You must enter both filename and num_rows')
            return
        csv_reader(parser)

    elif parser.getcols:
        get_columns(parser)

    elif parser.linechart:
        get_linechart(parser)

        
            
        
    

if __name__ == "__main__":
    main()