import os
def isBinod(filename):
	with open(filename, "r") as f:
		fileContent=f.read()
	if "binod" in fileContent.lower():
		return True
	else:
		return False
#@deeplearningindia
dir_contents = os.listdir()
for item in dir_contents:
	if item.endswith( 'txt'):
		print(f"Detecting Binod in {item}")
		isBinod(item)
		flag = isBinod(item)
		if(flag):
			print(f"binod found in {item}")
		else:
			print(f"binod not found in {item}")



