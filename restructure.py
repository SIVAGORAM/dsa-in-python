import os
import shutil
import time

base_dir = r"d:\python-dsa-journey\01-Python-Fundamentals"
logic_building_dir = r"d:\python-dsa-journey\02-Logic-Building"

# Folders to rename (by moving contents and removing old)
folder_map = {
    "Basics": "01-Basics",
    "Control Flow": "02-Control-Flow",
    "Data Structures": "03-Data-Structures",
    "Functions": "04-Functions",
    "Oops": "06-OOP",
    "Exception Handling": "07-Exception-Handling",
    "File Handling": "08-File-Handling",
    "Modules & packages & library": "09-Modules-and-Packages",
}

for old, new in folder_map.items():
    old_path = os.path.join(base_dir, old)
    new_path = os.path.join(base_dir, new)
    if os.path.exists(old_path) and not os.path.exists(new_path):
        os.makedirs(new_path, exist_ok=True)
        # Move all files and subdirectories
        for item in os.listdir(old_path):
            try:
                shutil.move(os.path.join(old_path, item), os.path.join(new_path, item))
            except Exception as e:
                print(f"Error moving {item}: {e}")
        try:
            os.rmdir(old_path)
        except Exception as e:
            print(f"Error removing {old_path}: {e}")

# Move Problem Solving to 02-Logic-Building
prob_solving = os.path.join(base_dir, "Problem Solving")
if os.path.exists(prob_solving):
    for item in os.listdir(prob_solving):
        try:
            shutil.move(os.path.join(prob_solving, item), os.path.join(logic_building_dir, item))
        except Exception as e:
            print(f"Error moving {item}: {e}")
    try:
        os.rmdir(prob_solving)
    except:
        pass

# Create 05-Advanced-Python-for-DSA
advanced_dir = os.path.join(base_dir, "05-Advanced-Python-for-DSA")
os.makedirs(advanced_dir, exist_ok=True)

# Now, rename the .ipynb files
basics_files = {
    "basics.ipynb": "01-Introduction.ipynb",
    "Variables.ipynb": "02-Variables-and-Datatypes.ipynb",
    "Operators.ipynb": "03-Operators.ipynb",
    "Datatypes.ipynb": "04-Type-Casting.ipynb",
}
basics_dir = os.path.join(base_dir, "01-Basics")
if os.path.exists(basics_dir):
    for old, new in basics_files.items():
        if os.path.exists(os.path.join(basics_dir, old)):
            try:
                os.rename(os.path.join(basics_dir, old), os.path.join(basics_dir, new))
            except:
                pass

# 02-Control-Flow
control_files = {
    "ConditionalStatements.ipynb": "01-Conditional-Statements.ipynb",
    "Loops.ipynb": "02-Loops.ipynb",
}
control_dir = os.path.join(base_dir, "02-Control-Flow")
if os.path.exists(control_dir):
    for old, new in control_files.items():
        if os.path.exists(os.path.join(control_dir, old)):
            try:
                os.rename(os.path.join(control_dir, old), os.path.join(control_dir, new))
            except:
                pass

# 03-Data-Structures
ds_files = {
    "list.ipynb": "01-Lists.ipynb",
    "ListExamples.ipynb": "01a-List-Examples.ipynb",
    "Tuples.ipynb": "02-Tuples.ipynb",
    "Sets.ipynb": "03-Sets.ipynb",
    "Dictionaries.ipynb": "04-Dictionaries.ipynb",
}
ds_dir = os.path.join(base_dir, "03-Data-Structures")
if os.path.exists(ds_dir):
    for old, new in ds_files.items():
        if os.path.exists(os.path.join(ds_dir, old)):
            try:
                os.rename(os.path.join(ds_dir, old), os.path.join(ds_dir, new))
            except:
                pass

# 04-Functions
func_files = {
    "Functions.ipynb": "01-Function-Basics.ipynb",
    "FunctionExamples.ipynb": "02-Function-Examples.ipynb",
    "LambdaFunction.ipynb": "05-Lambda-Functions.ipynb",
    "MapFunction.ipynb": "05a-Map-Function.ipynb",
    "FilterFunctions.ipynb": "05b-Filter-Function.ipynb",
}
func_dir = os.path.join(base_dir, "04-Functions")
if os.path.exists(func_dir):
    for old, new in func_files.items():
        if os.path.exists(os.path.join(func_dir, old)):
            try:
                os.rename(os.path.join(func_dir, old), os.path.join(func_dir, new))
            except:
                pass

# 06-OOP
oop_files = {
    "Classes&Objects.ipynb": "01-Classes-and-Objects.ipynb",
    "Inheritance.ipynb": "02-Inheritance.ipynb",
    "Polymorphism.ipynb": "03-Polymorphism.ipynb",
    "Encapsulation.ipynb": "04-Encapsulation.ipynb",
    "Abstraction.ipynb": "05-Abstraction.ipynb",
    "Magicmethods.ipynb": "06-Magic-Methods.ipynb",
    "OperatorOverloading.ipynb": "07-Operator-Overloading.ipynb",
}
oop_dir = os.path.join(base_dir, "06-OOP")
if os.path.exists(oop_dir):
    for old, new in oop_files.items():
        if os.path.exists(os.path.join(oop_dir, old)):
            try:
                os.rename(os.path.join(oop_dir, old), os.path.join(oop_dir, new))
            except:
                pass

# 07-Exception-Handling
eh_files = {
    "exception.ipynb": "01-Try-Except-Finally.ipynb",
    "CustomException.ipynb": "02-Custom-Exceptions.ipynb",
}
if os.path.exists(oop_dir) and os.path.exists(os.path.join(oop_dir, "CustomException.ipynb")):
    eh_dir = os.path.join(base_dir, "07-Exception-Handling")
    try:
        shutil.move(os.path.join(oop_dir, "CustomException.ipynb"), os.path.join(eh_dir, "02-Custom-Exceptions.ipynb"))
    except:
        pass
if os.path.exists(os.path.join(base_dir, "07-Exception-Handling")):
    eh_dir = os.path.join(base_dir, "07-Exception-Handling")
    if os.path.exists(os.path.join(eh_dir, "exception.ipynb")):
        try:
            os.rename(os.path.join(eh_dir, "exception.ipynb"), os.path.join(eh_dir, "01-Try-Except-Finally.ipynb"))
        except:
            pass

# 08-File-Handling
fh_files = {
    "Fileoperation.ipynb": "01-Read-Write-Files.ipynb",
    "filepath.ipynb": "01a-File-Paths.ipynb",
}
fh_dir = os.path.join(base_dir, "08-File-Handling")
if os.path.exists(fh_dir):
    for old, new in fh_files.items():
        if os.path.exists(os.path.join(fh_dir, old)):
            try:
                os.rename(os.path.join(fh_dir, old), os.path.join(fh_dir, new))
            except:
                pass

# 09-Modules-and-Packages
mod_files = {
    "Imports.ipynb": "01-Imports-Basics.ipynb",
    "Standardlibrary.ipynb": "02-Standard-Library.ipynb",
}
mod_dir = os.path.join(base_dir, "09-Modules-and-Packages")
if os.path.exists(mod_dir):
    for old, new in mod_files.items():
        if os.path.exists(os.path.join(mod_dir, old)):
            try:
                os.rename(os.path.join(mod_dir, old), os.path.join(mod_dir, new))
            except:
                pass

print("Restructure complete!")
