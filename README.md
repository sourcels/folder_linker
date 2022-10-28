## Test project for Internal Development in QA (SDET) Team, task
\n
This script copies all files and subfolder from source folder and paste into any other folder\n
\n
Usage:\n
\n
1. Terminal:\n
\n
`& python \folder_linker.py [folder1] [folder2]`\n
\n
2. Python module:\n
\n
`from folder_linker import FolderLinker`\n
`folder1 = "source"`\n
`folder2 = "replica"`\n
`fl = FolderLinker(folder1, folder1)`\n
\n
Result of class method is `bool`...\n
`True` - successful\n
`False` - failed\n