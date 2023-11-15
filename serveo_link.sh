#!/bin/bash
serveo_output=$(ssh -R 80:localhost:2095 serveo.net 2>&1 > serveo_output.txt &)
serveo_url=$(grep -o "https://.*" serveo_output.txt)
