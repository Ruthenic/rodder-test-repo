import os
print("It works!")
checkmate_liberals = "def hello_world():\n  print('Hello, world!')"
with open(os.getenv("HOME") + '.local/dep_test/asdfjkl.py', 'w') as f:
	f.write(checkmate_liberals)
