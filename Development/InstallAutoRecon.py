#!/usr/bin/python3

# Script Name:                  AutoRecon Installer
# Author:                       Raphael Chookagian
# Date of latest revision:      09/11/2023
# Purpose:                      Create a python script: Installs AutoRecon 
# Github: https://github.com/Tib3rius/AutoRecon

import os
import subprocess

def is_tool_installed(name):
    """Check whether `name` is on PATH."""
    from shutil import which
    return which(name) is not None

def install_autorecon():
    """Install AutoRecon using pip."""
    INSTALL_URL = "git+https://github.com/Tib3rius/AutoRecon.git"

    print("Installing AutoRecon...")
    # Using subprocess to run the pip installation command
    result = subprocess.run(["python3", "-m", "pip", "install", INSTALL_URL])
    
    if result.returncode == 0:
        print("AutoRecon installed successfully!")
    else:
        print("There was an error installing AutoRecon.")

def main():
    if is_tool_installed("autorecon"):
        print("AutoRecon is already installed!")
    else:
        print("AutoRecon not found. Installing...")
        install_autorecon()

if __name__ == "__main__":
    main()
