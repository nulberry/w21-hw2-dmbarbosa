'''
Checks the output of the solution for Q4
'''

import sys
import subprocess

print "testing Q4"

output=subprocess.check_output(["./bin/solution.out", "../q1/edmonton.db", "building=university", "wheelchair_accessible=yes"])
lines = output.strip().split('\n')

if len(lines) > 1:
	print "====> ERROR: the output has more lines than expected"
	exit(1)

if len(lines) == 0:
	print "====> ERROR: there is no output"
	exit(1)

numbers = lines[0].split()
if len(numbers) > 2:
	print "====> ERROR: output does not look like two numbers"
	exit(1)

try:
	number, max_dist = float(numbers[0]), float(numbers[1])
	print "====> SUCCESS: output is formatted correctly"
except:
	if lines[0] != 'error':
		print "====> ERROR: output does not look like two numbers"
		exit(1)

