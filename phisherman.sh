#!/bin/bash

# Clear the screen
clear

# Style the prompt
PS1="\[\e[1m\]\$ \[\e[0m\]"

# Function to display text as if it's being typed
type_text() {
  local text="$1"
  local delay="0.0000000000000000000000000000005"
  local i=0

  while [ $i -lt ${#text} ]; do
    echo -n "$(expr substr "$text" $i 1)"
    sleep "$delay"
    i=$((i + 1))
  done

  echo
}

# Display the ASCII art with typewriter effect
type_text ""
type_text ""
type_text ""
type_text ""
type_text ""
type_text "            ------------------------------------  "
type_text "            |           PHISHERMAN             |  "
type_text "            ------------------------------------  "
echo "            | Tool          | PhisherMan       |  "
echo "            | Purpose       | Phishing         |  "
echo "            | Author        | ABC Dior         |  "
echo "            | Collaborators | None             |  "
echo "            | Version       | 1.0              |  "
type_text "            ------------------------------------  "

echo
type_text "           Type template number to select it. "
type_text "           For example, type: 01 to select Facebook "

echo "           | Code      |  Name               | "
echo "           | 01        |  Facebook           | "
echo "           | 02        |  Instagram          | "
echo "           | Others    |  Coming soon        | "
echo
python ".templates/host.py"
exit 0