## Test project for Internal Development in QA (SDET) Team, task

This script copies all files and subfolder from source folder and paste into any other folder

Usage:

1. Terminal:

`& python \folder_linker.py [folder1] [folder2]`

2. Python module:
   
`from folder_linker import FolderLinker`
`folder1 = "source"`
`folder2 = "replica"`
`fl = FolderLinker(folder1, folder1)`

Result of class method is `bool`...
`True` - successful
`False` - failed