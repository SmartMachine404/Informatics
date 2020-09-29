#include <iostream>
long long is_qube(long long n){
	long long root = -1, i = 0;
	while (i*i <= n) {
		if (i*i == n)
		{
			root = i;
			break;
		}
		i++;
	}
	return root;
}
int main()
{
	long long k, number_odd;
	std::cin >> k;
	if (k >=0)
	{
		long long sqrk = is_qube(k);
		if (sqrk != -1){
			std::cout << sqrk;
		}
		else if (k % 2 == 0) {
			std::cout << "none";
		} else {
			number_odd = (k + 1) / 2;
			std::cout << number_odd;
		}
	} else {
		long long sqrk = is_qube(-k);
		if (sqrk != -1){
			std::cout << 0;
		}
		else if (k % 2 == 0) {
			std::cout << "none";
		} else {
			number_odd = (-k - 1) / 2;
			std::cout << number_odd;
		}
	}
	return 0;
}