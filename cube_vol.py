def cube_volume(x):
  return(x*x*x)

def get_side():
    side = int(input("Please enter the side length of your cube:"))
    return(side)

my_side = get_side()
volume = cube_volume(my_side)

print("Volume: " + str(volume))
