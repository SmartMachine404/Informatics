#include <iostream>

void sort(int* arr, int len){
	int tmp, p;
	for (int i = 0; i < len - 1; ++i)
	{
		for (int p = i + 1; p < len; ++p)
		{
			if (arr[p] < arr[i]){
				tmp = arr[i];
				arr[i] = arr[p];
				arr[p] = tmp;
			}
		}
	}
}
void print_array(int* arr, int len){
	for (int i = 0; i < len; ++i)
	{
		std::cout << arr[i] << '\t';
	}
}
void fill_array(int* arr, int len){
	for (int i = 0; i < len; ++i)
	{
		std::cin >> arr[i];
	}
}

int main(int argc, char const *argv[])
{
	int length;
	std::cin >> length;
	int sequence[length];
	fill_array(sequence, length);
	sort(sequence, length);
	std::cerr << "Completed!\n";
	print_array(sequence, length);
	return 0;
}