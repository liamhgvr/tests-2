# build a python program that will scan a given folder for json files, and for each found file, will execute a test program
# with parameters from the json file.
# in details:
# Create a python program with the following arguments
# test_dir - folder (relative/absolute) where to look for tests. default to "[current directory]/tests"
# test_program - program to execute on each json test file
# verbose - extra verbosity
# - The automation program will search for ".json" files in the [test_dir] folder (recusrively).
# - for each found .json file, the automation program will execute [test_program args] where the args are a serialization of all the json fields into the command line.
# - after execution, the program output should be stored. if the program returns non zero exit code, the automation should fail.
#
#
# EXAMPLE RUN: "python3 json_finder.py . check_json.py True"

import os, sys
import subprocess
import glob, json


json_files = []
failed_tests = {}
test_dir = os.popen('pwd').read()[:-1]  # Removing tailing '\n'
test_app = "check_json.py"  # Default test app
is_verbose = False

def read_json(file_2_read):

	f = open(file_2_read,) 
	data = json.load(f)
	return data
	f.close()


# Main - Accepting ARGVs
if len(sys.argv) > 3:
	is_verbose = sys.argv[3]
	test_app = sys.argv[2]
	test_dir = sys.argv[1]

elif len(sys.argv) > 2:
	test_app = sys.argv[2]
	test_dir = sys.argv[1]

elif len(sys.argv) > 1:
	test_dir = sys.argv[1]
else:
	print("No ARGV")

# Printing execution params
if is_verbose is True:
	print("test dir: ", test_dir)
	print("test app: ", test_app)
	print("is verbose: ", is_verbose)

# Creating a list of JSON files (recursively)
for f_name in glob.glob(test_dir + "/**/*.json", recursive=True): 
    
    json_files.append(f_name)
    if is_verbose is True:
    	print("FILE ==> " + f_name)
    
# Read and Iterate JSON files
for j_file in json_files:

	failed_tests[j_file] = []
	j_data = read_json(j_file)

	# Checking by level 1 keys in JSON
	for key, value in j_data.items():

		if len(failed_tests[j_file]) == 0: 
			failed_tests[j_file].append(key)  # Putting main key at index 0
		cmd = "python3 {} \"{}\"".format(test_app, str(value).replace(" ",""))

		if is_verbose is True: 
			print("CMD ==> " + cmd)

		# Executing secondery script and reading results
		out = os.popen(cmd).read()[:-1]
		failed_tests[j_file].append(out)

print("================Failed Tests=================\n",failed_tests)








