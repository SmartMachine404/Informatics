#include <iostream>
using std::string;
int main(int argc, char const *argv[])
{
	int max_level, middle, right, left;
	bool lied;
	string ask, answer, answer2, status="Correct";
	while(status != "Done"){
		right = max_level + 1;
		left = 0;
		lied = false;
		while(right - left > 1){
			middle = (right - left) / 2;
			ask = "? " + middle;

			std::cout << ask;
			std::cin >> answer;
			if( !lied){
				
			}
		} 		
	}

	return 0;
}