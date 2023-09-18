# `dynamic_import_from_folder` - dynamically imports modules from the specified directory and returns a list of imported modules along with their names.

```bash
import importlib
import os
from pathlib import Path

def dynamic_import_from_folder(folder_path):
    # Convert the directory path to a Path object
    folder_path = Path(folder_path)
    module_list = []

    # Locate all files in the specified directory and its subdirectories
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            # Check that the file has a .py extension
            if file_name.endswith('.py'):
                # Form the path to the module
                module_path = Path(root) / file_name
                # Convert the path to a Python-style module name (replace '/' with '.')
                module_name = module_path.with_suffix('').as_posix().replace('/', '.')
                # Import the module with the received name
                module = importlib.import_module(module_name)
                # Add information about the module and its name to the list
                module_list.append({
                    "module": module,         # Module instance
                    "module_name": module_name,  # Module name
                })

    # Return a list of imported modules
    return module_list
```

