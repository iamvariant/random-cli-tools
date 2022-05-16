import os


path = str(input("What path are the files in? (Default: current directory) ") or os.getcwd())
startIndex = int(input("What number should we start with? (Default: 1) ") or 1)
originalNames = []
modifiedNames = []


for idx, item in enumerate(os.scandir(path), start=startIndex):
	if item.is_file():
		originalNames.append(str(item.name))
		modifiedName = str(idx) + " - " + str(item.name)
		modifiedNames.append(modifiedName)


print("Files in '%s':" % path)
print(originalNames)
print("Will be renamed to:")
print(modifiedNames)
print("Do you want to continue? [Y/N]")


confirmation = str(input()).casefold()
if confirmation == "y":
	count = 0
	for item in os.scandir(path):
		src = os.path.join(path, item.name)
		dst = os.path.join(path, modifiedNames[int(count)])
		os.rename(src, dst)
		print("Renamed " + str(src) + " to " + str(dst))
		count += 1
	print("Operation complete.")
else:
	print("Operation cancelled.")


input("Press Enter to quit.")
os.scandir(path).close()