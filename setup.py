from cx_Freeze import Executable, setup
import sys
import os
import shutil
PYTHON_INSTALL_DIR = os.path.dirname(sys.executable)
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
include_files = [(os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), os.path.join('lib', 'tk86.dll')),
                 (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                  os.path.join('lib', 'tcl86.dll')),
                 ('background.jpeg'), ('logo.ico'), ('logo.jpeg')]
base = None

if sys.platform == 'win32':
    base = "Win32GUI"
directory_table = [
    ("DesktopShortcut", "DesktopFolder",
     "Milk Rate Converter",
     "TARGETDIR",
     "[TARGETDIR]\MilkRateConverter.exe",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR",)
]
msi_data = {"Shortcut": directory_table}
bdist_msi_option = {'data': msi_data}
executables = [
    Executable(script="MilkRateConverter.py", base=base, icon="logo.ico")]

setup(
    name="Milk Rate Converter",
    version="1.0",
    author='Sakib Malik',
    description="Milk Rate Converter Software is build for Rate Converter for Everest Milk Machine",
    options={"build_exe": {"packages": ["tkinter", "os", "xlrd", "PIL"],
                           "include_files": include_files}, "bdist_msi": bdist_msi_option, },

    executables=executables
)

# Remove bdist folder
shutil.rmtree('build')
