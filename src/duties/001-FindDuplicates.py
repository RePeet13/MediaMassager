import os

d = os.getcwd()

folders = [x for x in os.listdir(d) if not os.path.isfile(os.path.join(d, x)) and x[0] != '.']
files = [x for x in os.listdir(d) if os.path.isfile(os.path.join(d, x)) and x[0] != '.' and not x.endswith('.py')]

print str(folders)
print('Folders: ' + str(len(folders)))

print str(files)
print('Files: ' + str(len(files)))