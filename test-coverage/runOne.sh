#!/bin/bash
session_name=findCoverage1-20
screen -d -m -U -S $session_name
command="python findCoverage.py 1 20
"
screen -S $session_name -X stuff "$command" 





