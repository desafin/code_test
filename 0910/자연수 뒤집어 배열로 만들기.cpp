//자연수 뒤집어 배열로 만들기

#include <string>
#include <vector>

using namespace std;

vector<int> solution(long long n) {
    vector<int> answer;
    while (n > 0) {
        int digit = n % 10; // 맨 끝 자리 숫자 추출
        answer.insert(answer.begin(), digit); // 배열의 앞에 삽입
        n /= 10; // 맨 끝 자리 숫자 제거
    }
    
    vector<int> reversed(answer.rbegin(), answer.rend()); 
    
    return reversed;
}