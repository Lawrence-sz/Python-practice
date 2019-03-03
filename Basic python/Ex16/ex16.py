from sys import argv

script, filename = argv

print(f"We're gong to erase{filename}.")
print("if you don't want that, hit CRL - C(^C).")
print("If you don want taht, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "r+")
print(target.read())                    # pleae notice the print out result

print("Truncating the file. Goodbye!")
#target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("I;m going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we clost it.")
print(target.read())
print("read")
print(target.read())                   # please notice the print out results
target.close()
