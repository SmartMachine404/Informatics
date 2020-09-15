#include <iostream>
int main(){
	int n, left, right, middle;
	bool lied;	
	std::string status, ask, answer, answer2;
	
	status = "Correct";
	std::cin >> n;
	const int RIGHT = n + 1;
	
	while(status != "Done"){
		//Scanning planet
		left = 1;
		right = RIGHT;
		lied = false;
		while(right - left > 1){
			middle = (left + right) / 2;
			std::cout << "? " << middle <<'\n';
			std::cin >> answer;
			if (!lied){
				std::cout << "? " << middle <<'\n';
				std::cin >> answer2;
				if (answer != answer2){
					lied = true;
					std::cout << "? " << middle <<'\n';
					std::cin >> answer;
				}
			}
			if (answer == "Yes") left = middle;
			else right = middle;
		}
		std::cout << "! " << left <<'\n';
		std::cin >> status;
	}

	return 0;
}