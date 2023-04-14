#include<iostream>
#include<thread>
#include <boost/thread.hpp>

// Multithreading is the ability of the system to run multiple parts of code at the same time depending on the hardware availability
using namespace std;
void function1(){
	for(int i=0;i<200;i++){
		cout<<"+";
	}
}
void function2(){
	for(int i=0;i<200;i++){
		cout<<"-";
	}
}
int main(){
//	function1();
//	function2();
//	//Now this code first prints all the + and then prints all the -'s hence this is a single threaded code
	boost::thread worker1(function1);
	thread worker2(function2);
	return 0;
}
