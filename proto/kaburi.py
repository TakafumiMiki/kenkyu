import glob

get_file_index = glob.glob("audio[0-9]*.txt")

get_file_index.sort(reverse = True)

if len(get_file_index) != 0:
    max_index = ''.join(c for c in get_file_index[0] if c.isdigit())
    this_index = int(max_index) + 1

print("audio" + str(this_index) + ".txt")
