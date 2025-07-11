import os
import pandas as pd
from constants import INPUT_FOLDER, CSV_FOLDER, COLORS


def file_exists(filename):
    return os.path.exists(os.path.join(INPUT_FOLDER,filename))


def csv_reader(parser):
    if parser.readcsv[0] is None or parser.readcsv[1] is None:
            print('Invalid input. You must enter both filename and num_rows')
            return
    val = int(parser.readcsv[1])
    file_name = str(parser.readcsv[0])

    if(file_exists(file_name) is False):
        print(COLORS["RED"]+'Invalid file path'+COLORS["RESET"])
        return
    
    file_path = os.path.join(INPUT_FOLDER,file_name)
    df = pd.read_csv(file_path)
    new_df = df.head(val)

    if parser.savecsv:
        output_path = os.path.join(CSV_FOLDER, "filtered_df.csv")
        new_df.to_csv(output_path, index=False)
        print(f"{COLORS["GREEN"]}Saved top {val} rows to {output_path}{COLORS["RESET"]}")
    else:
        print(new_df)


def get_columns(parser):
    file_name = parser.getcols[0]
    if file_exists(file_name) is False:
        print(COLORS["RED"]+'Invalid file path'+COLORS["RESET"])
        return
    else:
        file_path = os.path.join(INPUT_FOLDER,file_name)
        df = pd.read_csv(file_path)
        colList = df.columns.to_list()
        print(f"total number of columns in dataframe = {len(colList)}")
        for i,item in enumerate(colList):
            if i % 3 == 0:
                print("\n"+item, end = "\t")
            print(item, end = "\t")


def get_csv_info(parser):
    file_name = str(parser.getcsvinfo[0])
    if file_exists(file_name) is False:
        print(COLORS["RED"]+'Invalid file path'+COLORS["RESET"])
        return
    else:
        file_path = os.path.join(INPUT_FOLDER,file_name)
        df = pd.read_csv(file_path)
        print(df.info())


def get_summary_stats(parser):
    file_name = str(parser.summary[0])
    if file_exists(file_name) is False:
        print(COLORS["RED"]+'Invalid file path'+COLORS["RESET"])
        return
    else:
        file_path = os.path.join(INPUT_FOLDER,file_name)
        df = pd.read_csv(file_path)
        print(df.describe().T)
