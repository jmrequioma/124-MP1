#include<iostream>

using namespace std;

int main(int argc,  char *argv[]) {
	double fahrenheit;
	double celsius;

	cout << "Enter the temperature in fahrenheit: ";
	cin >> fahrenheit;

	celsius = (fahrenheit - 32) * 5/9;

	cout << "The temperature in °C " << celsius << endl;
	return 0;
}