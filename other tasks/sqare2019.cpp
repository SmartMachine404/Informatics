#include <iostream>

int main()
{
	int n, m, t, cur, prev, h=0;
	std::cin >> n >> m >> t;
	int used = 2 * (m + n - 2);
	prev = used;
	while(used <= t){
		h++;
		cur = prev - 4;
		used += cur;
		prev = cur;
	}
	std::cout << h;
	
	return 0;
}