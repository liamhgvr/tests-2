# Python1
import sys,json

# Checking for argv
if len(sys.argv) > 1:
    input_str = sys.argv[1]
    input_str2 = input_str.replace("'", '"')
    input_dict = json.loads(input_str2)
else:
    input_dict = {'DEF_KEY': False}

# Varify value ( 1 = failed )
for key, value in input_dict.items():
    if input_dict[key] == 1:
        print(key, "-", value)  # sending failed test to STDOUT
    else:
        pass
