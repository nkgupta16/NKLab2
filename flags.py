# colors
red = "\u001b[41m"
white = "\u001b[47m"
green = "\u001b[42m"
yellow = "\u001b[43m"
blue = "\u001b[44m"
reset = "\033[0m"


# French Flag Representation
print("French Flag \n")
for _ in range(15):
  print(blue + " " * 16 + reset + white + " " * 16 + reset + red + " " * 16 + reset)


# Bangladesh Flag Representation
print("\n Bangladesh Flag\n")
# Defining the dimensions
width, height = 48, 15
radius = 5
circle_center = (width // 2, height // 2)

# Function to check if a point is inside the circle
def is_inside_circle(x, y, center, radius):
    return (x - center[0]) ** 2 + (y - center[1]) ** 2 < radius ** 2

# Generating the flag
for y in range(height):
    for x in range(width):
        if is_inside_circle(x, y, circle_center, radius):
            print("\033[41m \033[0m", end='')
        else:
            print("\033[42m \033[0m", end='')
    print()

# Netherlands Flag Representation
print("\n Netherlands Flag \n")
color_codes = [red, white, blue]

for code in color_codes:
    for _ in range(5):
        print(code + " " * 48 + reset)


# Poland Flag Representation
print("\n Poland Flag \n")
color_codes = [red, white]

for code in color_codes:
    for _ in range(8):
        print(code + " " * 48 + reset)



# Lithuania Flag Representation
print("\n Lithuania Flag \n")
color_codes = [yellow, green, red]

for code in color_codes:
    for _ in range(5):
        print(code + " " * 48 + reset)


# Thailand Flag Representation
print("\n Thailand Flag \n")
color_codes = [red, white, blue]

for code in color_codes[0:2]:
    for _ in range(2):
        print(code + " " * 48 + reset)

for _ in range(6):
      print(blue + " " * 48 + reset)

for code in reversed(color_codes[0:2]):
    for _ in range(2):
      print(code + " " * 48 + reset)


# Japan Flag Representation
print("\n Japan Flag \n")
# Defining the dimensions
width, height = 48, 15
radius = 5
circle_center = (width // 2, height // 2)

# Function to check if a point is inside the circle
def is_inside_circle(x, y, center, radius):
    return (x - center[0]) ** 2 + (y - center[1]) ** 2 < radius ** 2

# Generating the flag
for y in range(height):
    for x in range(width):
        if is_inside_circle(x, y, circle_center, radius):
            print("\033[41m \033[0m", end='')
        else:
            print("\033[47m \033[0m", end='')
    print()


# Benin Flag Representation
print("\n Benin Flag\n")
for _ in range(7):
  print(green + " " * 18 + reset + yellow + " " * 30 + reset)

for _ in range(7):
  print(green + " " * 18 + reset + red + " " * 30 + reset)


# Finland Flag Representation
print("\n Finland Flag \n")
for _ in range(6):
  print(white + " " * 12 + reset + blue + " " * 6 + reset + "\033[47m" + " " * 30 + reset)

for _ in range(3):
  print(blue + " " * 48 + reset)

for _ in range(6):
  print(white + " " * 12 + reset + blue + " " * 6 + reset + "\033[47m" + " " * 30 + reset)


# Switzerland Flag Representation
print("\n Switzerland Flag \n")
for _ in range(2):
  print(red + " " * 48 + reset)

for _ in range(4):
  print(red + " " * 20 + reset + white + " " * 8 + reset + red + " " * 20 + reset)

for _ in range(3):
  print(red + " " * 10 + reset + white + " " * 28 + reset + red + " " * 10 + reset)

for _ in range(4):
  print(red + " " * 20 + reset + white + " " * 8 + reset + red + " " * 20 + reset)

for _ in range(2):
  print(red + " " * 48 + reset)
