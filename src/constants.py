import os

ROOT_FOLDER = r"C:\Users\User\OneDrive\Desktop\anacondaProjects\command_line_projects\athena-wiz" # replace this with path to project folder in your system
INPUT_FOLDER = os.path.join(ROOT_FOLDER,'input')
os.makedirs(INPUT_FOLDER, exist_ok=True)

OUTPUT_FOLDER = os.path.join(ROOT_FOLDER, 'output')
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

CSV_FOLDER = os.path.join(OUTPUT_FOLDER,'csv_files')
os.makedirs(CSV_FOLDER, exist_ok=True)

PLOT_FOLDER = os.path.join(OUTPUT_FOLDER,'plots')
os.makedirs(PLOT_FOLDER, exist_ok=True)

COLORS = {
    "RESET": '\033[0m',       # Resets all attributes
    "BOLD": '\033[1m',        # Bold text
    "UNDERLINE": '\033[4m',   # Underline text

    "RED": '\033[91m',
    "GREEN": '\033[92m',
    "YELLOW": '\033[93m',
    "BLUE": '\033[94m',
    "MAGENTA": '\033[95m',
    "CYAN": '\033[96m',
    "WHITE": '\033[97m',

    "BG_RED": '\033[101m',
    "BG_GREEN": '\033[102m',
    "BG_YELLOW": '\033[103m',
    "BG_BLUE": '\033[104m',
    "BG_MAGENTA": '\033[105m',
    "BG_CYAN": '\033[106m',
    "BG_WHITE": '\033[107m'
}
