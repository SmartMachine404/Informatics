#include <iostream>

int main()
{
	long k, number_odd;
	std::cin >> k;
	if (k == 0) std::cout << 0;
	else if (k % 2 == 0)
	{
		std::cout << "none";
	}
	else if (k >= 0)
	{
		number_odd = (k + 1) / 2;
		std::cout << number_odd;
	} else {
		number_odd = (-k + 1) / 2;
		std::cout << number_odd - 1  << '\n';
	}

	return 0;
}