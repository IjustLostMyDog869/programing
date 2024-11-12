cars = {
	"1970 vw bug":   (286, 9),
	"1979 firebird": (412, 40),
	"1980 subaru":   (361, 18),
	"1975 cutlass":  (161, 11)
}

print("Chose a car from the following:"), cars.keys())
mycar = input()
miles, gallons = cars[mycar]
mpg = float(miles) / gallons

print("Miles:", miles)
print("Gallons:", gallons)
print"MPG:", round(mpg, 1))

input()