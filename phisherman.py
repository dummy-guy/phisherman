#!/usr/bin/env python3
import subprocess
import json
from color_functions import type_text, display_template, index_str, check_installed
from color_functions import cyan as cyan, magenta as magenta, reset as reset, yellow as yellow, green as green, light_blue as light_blue

# Clear the screen
subprocess.run(['clear'])

# Read manifest from JSON
with open('manifest.json', 'r') as manifest_file:
    manifest = json.load(manifest_file)
    templates = manifest.get('templates', [])
    requirements = manifest.get('requirements', [])
    python_dependencies = manifest.get('python_dependencies', [])

# Display ASCII art
with open('doom.txt', 'r') as doom_file:
    doom_content = doom_file.read()
    print(f"{green}{doom_content}{reset}")

type_text(f"{yellow}{manifest['name']} is for educational purposes only‼️{reset}")
type_text(f"{light_blue}Follow and collaborate with the developer on{reset}")
print(f"  {yellow}[{green}~{yellow}] {magenta}GitHub  {cyan}:{green} @dummy-guy{reset}")
print(f"  {yellow}[{green}~{yellow}] {magenta}{magenta}Snapchat{cyan}:{green} @dummyguy123{reset}")
print("-------------------------------------------")
print()

print(f"{light_blue}Type template number to select it.{reset}")
type_text(f"{yellow}For example, type: 01 to select Facebook{reset}")
type_text(f"")

# Loop through templates
for i, template in enumerate(templates, start=1):
    indexed_str = index_str(i)
    display_template(indexed_str, template)
    print()

# Check if Linux packages are installed
not_installed_requirements = [pkg for pkg in requirements if not check_installed(['dpkg', '-s', pkg])]
if not_installed_requirements:
    type_text("Installing Linux packages...")
    subprocess.run(['apt', 'install'] + not_installed_requirements)
else:
    type_text(f"{green}Linux packages are already installed.{reset}")

# Check if Python dependencies are installed
not_installed_dependencies = [dep for dep in python_dependencies if not check_installed(['pip3', 'show', dep])]
if not_installed_dependencies:
    type_text("Installing Python dependencies...")
    subprocess.run(['pip3', 'install'] + not_installed_dependencies)
else:
    type_text(f"{green}Python dependencies are already installed.{reset}")

type_text("Please wait...")

subprocess.run(['python3', '.templates/host.py'])

exit(0)
