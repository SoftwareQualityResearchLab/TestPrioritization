#!/bin/bash
session_name=findCoverage1-20
screen -d -m -U -S $session_name
command="python findCoverage.py 1 20
"
screen -S $session_name -X stuff "$command" 
sleep 2s
##################################################################
session_name=findCoverage20-36
screen -d -m -U -S $session_name
command="python findCoverage.py 20 36
"
screen -S $session_name -X stuff "$command" 
sleep 3s
##################################################################
session_name=findCoverage36-50
screen -d -m -U -S $session_name
sleep 2s
command="python findCoverageAfter36.py 36 50
"
screen -S $session_name -X stuff "$command" 
##################################################################
session_name=findCoverage50-70
screen -d -m -U -S $session_name
sleep 2s
command="python findCoverageAfter36.py 50 70
"
screen -S $session_name -X stuff "$command" 
##################################################################
session_name=findCoverage70-90
screen -d -m -U -S $session_name
sleep 2s
command="python findCoverageAfter36.py 70 90
"
screen -S $session_name -X stuff "$command" 
##################################################################
