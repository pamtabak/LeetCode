#include <iostream>
#include <string>

using namespace std;

class Solution {
public:
    string maximumTime(string time) {
        char* char_arr;
        string str_obj(time);
        char_arr = &str_obj[0];
        if (char_arr[0] == '?') {
            std::string s(1, char_arr[1]);
            if (char_arr[1] != '?' && stoi(s) >= 4) {
                char_arr[0] = '1';
            }
            else {
                char_arr[0] = '2';
            }
        }
        if (char_arr[1] == '?'){
            if (char_arr[0] == '2'){
                char_arr[1] = '3';
            }
            else{
                char_arr[1] = '9';
            }
        }
        if (char_arr[3] == '?'){
            char_arr[3] = '5';
        }
        if (char_arr[4] == '?'){
            char_arr[4] = '9';
        }
            
        cout << char_arr << endl;
        return string(char_arr);
    }
};