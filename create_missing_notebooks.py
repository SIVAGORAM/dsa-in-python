import os
import shutil

base_dir = r"d:\python-dsa-journey\01-Python-Fundamentals"
template = r"d:\python-dsa-journey\notebook_template.ipynb"

files_to_create = [
    os.path.join(base_dir, r"03-Data-Structures\05-Comprehensions.ipynb"),
    os.path.join(base_dir, r"04-Functions\04-Scope-and-Closures.ipynb"),
    os.path.join(base_dir, r"05-Advanced-Python-for-DSA\01-Collections-Module.ipynb"),
    os.path.join(base_dir, r"05-Advanced-Python-for-DSA\02-Type-Hinting.ipynb"),
    os.path.join(base_dir, r"05-Advanced-Python-for-DSA\03-Python-Builtin-Complexity.ipynb"),
    os.path.join(base_dir, r"05-Advanced-Python-for-DSA\04-Iterators-and-Generators.ipynb"),
    os.path.join(base_dir, r"08-File-Handling\02-Context-Managers.ipynb"),
]

for file_path in files_to_create:
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory, exist_ok=True)
    if not os.path.exists(file_path):
        shutil.copy(template, file_path)
        print(f"Created: {file_path}")

print("Missing notebooks created from template.")
