
print("reading file content :")
file_read_line = open('sample.txt','r')
line1 = file_read_line.readline()
line2 = file_read_line.readline()
print(f"line 1: {line1.strip()}")

print(f"line 2: {line2.strip()}")
file_read_line.close()



