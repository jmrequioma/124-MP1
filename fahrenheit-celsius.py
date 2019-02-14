def convert_to_celsius(fahrenheit):
	return (fahrenheit - 32) * 5/9

def main():
	fahrenheit = input("Please enter temperature (°F): ")
	celsius = convert_to_celsius(float(fahrenheit))
	print("Equivalent temperature in °C " + str(celsius))

if __name__ == '__main__':
	main()