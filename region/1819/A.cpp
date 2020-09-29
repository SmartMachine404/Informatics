#include <iostream>

int main(int argc, char const *argv[])
{
	int l, r, a, d_t, d_i;
	long long summ = 0;
	std::cin >> l >> r >> a;
	d_t = r - l;
	d_i = a;
	while (d_i < d_t + 1) {
		summ += (d_t - d_i + 1);
		d_i += a;
	}
	std::cout << summ;
	return 0;
}