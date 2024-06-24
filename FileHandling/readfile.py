f = open("demofile.txt", "r")
print(f.read())

# Return the 5 first characters of the file:
print(f.read(5))


# Read Lines
print(f.readline())


f.close()