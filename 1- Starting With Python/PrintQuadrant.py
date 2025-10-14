#Given (x, y), print Quadrant I, II, III, IV or “Axis”.


print("--- Print The Quadrant ---")



x=int(input("Enter the X axis: \n"));
y=int(input("Enter the Y asis: \n"));


if x == 0 or y == 0:
        print("Point lies on the Axis")
elif x>0 and y >0:
		print(" Quadrant --> I");
elif y>0 and x<0:
		print(" Quadrant --> II");
elif y<0 and x<0:
		print(" Quadrant --> III");
else:
		print("	Quadrant --> IV");