#include <iostream>

int main()
{
	// preparing data 
	int request, length_arr;
	std::cin >> request >> length_arr;
	int arr[length_arr];
	for (int i = 0; i < length_arr; ++i)
	{
		std::cin >> arr[i];
	}
	// binary search
	int middle, left = 0, right = length_arr;
	while (right - left > 1) {
		middle = (right + left) / 2;
		if (request > arr[middle]){
		  	left = middle + 1;
		} else if (request < arr[middle]){
			right = middle;
		} else {
			std::cout << middle;
			return 0; 
		}
	}
	std::cout << left;
	return 0;
}