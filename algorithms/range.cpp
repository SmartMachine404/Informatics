#include <iostream>

int* range(int start, int stop, int step){
	int length = (stop - start + step - 1) / step;
	int sequence[length];
	int index = 0;
	for (int i = start; i < step; i += step)
	{
		sequence[index] = i;
	}

	return *sequence;
}

void print_range(int start, int stop, int step){
	for (int i = start; i < stop; i += step)
	{
		std::cout << i << '\t';
	}
}

int main(int argc, char const *argv[])
{
	int start, stop, step;
	std::cin >> start;
	std::cin >> stop;
	std::cin >> step;
	// int length = (stop - start + step - 1) / step;
	// int* seq = range(start, stop, step);
	// for (int i = 0; i < length; ++i)
	// {
	// 	std::cout << &seq[i];
	// }
	print_range(start, stop, step);
	return 0;
}