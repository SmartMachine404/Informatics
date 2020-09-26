#include <iostream>

int main(int argc, char const *argv[])
{
	int req_len, len;
	std::cin >> req_len >> len;
	int set[len];
	for (int i = 0; i < len; ++i)
	{
		std::cin >> set[i];
	}

	int 
	int middle, left = 0, right = len - 1;
	while(right - left > 1){
		middle = (right + left) / 2;
		if (r > set[middle])
		{
			left = middle;
		}
		else if (r < set[middle])
		{
			right = middle;
		} else {
			std::cout << "index of " << r << " is " << middle << '\n';
			break;
		}
	}
	middle = (right + left) / 2;
	if (r <= middle)
	{
		std::cout << "Set[" << left << "] = " << set[left] << " is the nearest to" << r;
	} else{
		std::cout << "Set[" << right << "] = " << set[right] << " is the nearest to" << r;

	}
	return 0;
}
