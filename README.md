## Test project for Internal Development in QA (SDET) Team, task

This script copies all files and subfolder from source folder and paste into any other folder

Usage (one-time):

1. Terminal:

`$ python \folder_linker.py [folder1] [folder2] [logfile]`

2. Python module:

```python
from folder_linker import FolderLinker
folder1 = "source"
folder2 = "replica"
fl = FolderLinker(folder1, folder1)
```

Usage (periodically):

1. Script

`$ `

