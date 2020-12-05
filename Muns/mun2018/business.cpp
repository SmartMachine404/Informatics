#include <iostream>

int main()
{
	int floors, workers, up, down, lift;
	int optimal_time;
	
	std::cin >> floors >> up >> down >> lift;
	workers = floors;

	for (int f = 1; f < floors + 1; ++f){
		int max_on_floor;

		for (int w = 1; w < workers + 1; ++w){
			int delta = w - f;

			int by_lift;
			if (delta >= 0){
				by_lift = delta * up + f * lift;
			} else{
				by_lift = -delta * up + f * lift;
			}

			int by_ledder = w * up;
			
			int optimal = std::min(by_lift, by_ledder);
			if (w == 1){
				max_on_floor = optimal;
			}
			if (optimal > max_on_floor){
				max_on_floor = optimal;
			}
		}

		if (f == 1){
			optimal_time = max_on_floor;
		}
		if (max_on_floor < optimal_time){
			optimal_time = max_on_floor;
		}
	}
	std::cout << optimal_time;
	return 0;
}