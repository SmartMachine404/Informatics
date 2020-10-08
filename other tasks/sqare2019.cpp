#include <iostream>

int main()
{
	int n, m, t, h=0;
	std::cin >> n >> m >> t;
	int c = 2 * (m + n - 2);
	while(c <= t && c > 0){
		h++;
		t -= c;
		c -= 8;
	}
	std::cout << h;	
	return 0;
}