#!/bin/bash

# Clear the screen
clear

# Style the prompt
PS1="\[\e[1m\]\$ \[\e[0m\]"

# Function to display text as if it's being typed
type_text() {
  local text="$1"
  local delay="0.00005"
  local i=0

  while [ $i -lt ${#text} ]; do
    echo -n "$(expr substr "$text" $i 1)"
    sleep "$delay"
    i=$((i + 1))
  done

  echo
}

# Display the ASCII art with typewriter effect
type_text "            ------------------------------------  "

type_text "            |           PHISHERMAN             |  "

type_text "            ------------------------------------  "
type_text "            | Tool          | PhisherMan       |  "
type_text "            | Purpose       | Phishing         |  "
type_text "            | Author        | ABC Dior         |  "
type_text "            | Collaborators | None             |  "
type_text "            | Version       | 1.0              |  "
type_text "            ------------------------------------  "
# Execute the Python script
python .templates/host.py
