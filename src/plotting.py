import os
import pandas as pd
import pandas.api.types as ptypes
import matplotlib.pyplot as plt
import seaborn as sns
from constants import INPUT_FOLDER, PLOT_FOLDER
from utils import file_exists


def get_linechart(parser):
    print("DISCLAIMER: for accurate results please ensure there are no duplicates in the label for the x axis!")
    file_name = str(parser.linechart[0])
    x_col = str(input("Enter column label for x axis: "))
    y_col = str(input("Enter column label for y axis: "))

    if file_exists(file_name) is False:
        print('Invalid file path')
        return
    
    file_path = os.path.join(INPUT_FOLDER, file_name)
    df= pd.read_csv(file_path)
    colList = df.columns.to_list()
    if x_col not in colList or y_col not in colList:
        print("Not a valid column")   
        print("see --commands for options to view all columns in file")
        return
    
    if not ptypes.is_numeric_dtype(df[x_col]) or not ptypes.is_numeric_dtype(df[y_col]):
        print(f"Invalid datatype in columns\n Only columns with numeric datatypes allowed\n")
        return
    
    title = str(input("Enter the title for your bar chart: "))
    grid = str(input("Do you want a grid?\nEnter YES for grid\n"))

    df_sorted = df.sort_values(by=x_col)
    plt.plot(df_sorted[x_col], df_sorted[y_col], color = 'red', label = y_col)
    plt.title(title, fontsize=16)
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    if grid == 'YES':
        sns.set_theme(style = "whitegrid")
    plt.legend()
    plt.tight_layout()    
    if parser.saveplot:
        plt.savefig(os.path.join(PLOT_FOLDER,'line-chart.png'))
    plt.show()