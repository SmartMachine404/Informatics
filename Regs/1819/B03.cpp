#include <iostream>

int main(){
	long long k, v, u, a=-1;
	bool exist = false;
	std::cin >> k;
	if (k == 0){
		a = 0;
		exist = true;
	}
	else if (k > 0) {
		v = 1;
		while(v*v <= k){
			if (k % v == 0){ //found divizer
				u = k / v;
				if(v % 2 == u % 2){
					a = (u + v) / 2;
					exist = true;	
				}
			}
			v++;
		}
	} else {
		v = -1;
		while(v*v <= -k){
			if (k % v == 0)
			{
				u = k / v;
				if(-(v % 2) == u % 2){
					a = (u + v) / 2;
					exist = true;
				}
			}
			v--;
		}
	}
	if (exist){
		std::cout << a;
	} else {
		std::cout << "none";
	}
	return 0;
}