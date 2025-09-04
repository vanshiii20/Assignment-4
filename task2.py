filename = "Output.txt "
file = open('Output.txt','w')
writing_file = input("Enter text to write to the file :")
writing_file = file.write(writing_file+"\n")
print(f"Data Successfully written to {filename}.")
file.close()

file = open('Output.txt','a')
appending_file = input("Enter additional text to append:")
appending_file = file.write(appending_file)
print("Data successfully appended.")
file.close()

file = open('Output.txt', 'r')
print(f"Final content of {filename}:")
for line in file:
   print(line.strip())
file.close()

