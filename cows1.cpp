#include <iostream>

int bin_search(int* arr, len, num){
	int left = 0;
	int right = len + 1;
	int middle;
	while(right > left){
		middle = (right + left) / 2;
		if (arr[middle] < num){
			right = middle + 1;
		}
		else if (arr[middle] > num) {
			left = middle + 1;
		}
		else {
			return middle;
		}
	}
	return left;
}
int main()
{
	int N, K, max_pos;
	std::cin >> N >> K;
	max_pos = N / K;	
	int seq[N]:
	for (int i = 0; i < N; ++i)
	{
		std::cin >> seq[i]
	}

	return 0;
}