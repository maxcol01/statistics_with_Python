from pathlib import Path
import shutil as sh

def load_file():
    directory = "/Users/maximecollet/Desktop/Bureau - iMac de Maxime/DOC MAX/Courses/ZTM_Statistics_Bootcamp/Statistics with Python/Inferential Statistics/Descriptive Statistics"
    target_directory = Path() / directory
    for file in target_directory.iterdir():
        sh.copy(file, Path.cwd())
