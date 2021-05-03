def cube_volume(x):
  return(x*x*x)

side = int(input("Please enter the side length of your cube:"))
volume = cube_volume(side)

print("Volume: " + str(volume))
