print("Rules that govern the state of water")
# let the user pick a temp, see what happens to water (conditon statements)
current_temp = False

while current_temp is False:

	  current_temp = input("Enter a temperature: \n")
	  print(current_temp)
	  if(int(current_temp) < 0) or (int(current_temp) == 0):
	      print("water is a solid. icy!")
	      current_temp = False

	  elif (int(current_temp) < 100):
		  print("water is a Liquid. profit!")
		  current_temp = False

	  elif (int(current_temp > 100)) or (int(current_temp) == 100):
		  print("water is a vapor, cuz its HOT")
		  current_temp = False