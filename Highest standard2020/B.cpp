#include <iostream>

int main()
{
	int towns, trees;
	std::cin >> towns;
	int beauty[towns];
	long long int s=0;
	for (int i = 0; i < towns; ++i)
	{
		std::cin >> beauty[i];
	}
	std::cin >> trees;
	for (int tr = 0; tr < trees; ++tr)
	{
		int l, r;
		std::cin >> l >> r;
		int steps=(r - l + 1) / 2;
		for (int city = 0; city < steps; ++city)
		 {
		 	int num_toys = (city + 2)*(city+1) / 2;
		 	long long int city_b = beauty[l-1 + city]*num_toys;
		 	s += city_b;
		 }
		for (int city = steps; city < 2*steps; ++city)
		 {
		 	int n = 2*steps - city;
		 	int num_toys = (n+1)*(n) / 2;
		 	long long int city_b = beauty[l-1 + city]*num_toys;
		 	s += city_b;
		 }
		std::cout << s%998244353 << '\n';
		s = 0;
	}
	return 0;
}