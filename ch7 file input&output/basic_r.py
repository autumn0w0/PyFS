f = open("demo.txt", "r")
data = f.read()

line1 = f.readline()
print(f"First line: {line1}")

print(f"Data read from file: {data}")
f.close()