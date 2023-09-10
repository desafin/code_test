#include <string>
#include <vector>
//https://school.programmers.co.kr/learn/courses/30/lessons/76501
using namespace std;

int solution(vector<int> absolutes, vector<bool> signs) {
    int answer = 0;
    for (int i = 0; i < absolutes.size(); ++i)     {
    
    if(signs[i]==false){
        int num=absolutes[i]*-1;
        answer =answer+num;
    }
    else
    {
        int num=absolutes[i];
        answer =answer+num;
    }
    }
    return answer;
}