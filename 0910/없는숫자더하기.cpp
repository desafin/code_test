#include <string>
#include <vector>
//https://school.programmers.co.kr/learn/courses/30/lessons/86051
using namespace std;

int solution(vector<int> numbers)
{
    int answer = 0;
    vector<int> vec = {1, 2, 3, 4, 5, 6, 7, 8, 9};

    for (int i = 0; i < numbers.size(); ++i)
    {
        for (int j = 0; j < vec.size(); ++j)
        {
            if (numbers[i] == vec[j])
            {
                vec.erase(vec.begin() + j); // 해당 숫자를 제거
                break; // 중복된 숫자를 발견하면 루프 종료
            }
        }
    }

    for (int j = 0; j < vec.size(); ++j)
    {
        answer += vec[j]; // 벡터의 남은 원소를 더함
    }

    return answer;
}
