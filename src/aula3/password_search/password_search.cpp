#include <bits/stdc++.h>

using namespace std;

//https://github.com/KHvic/uva-online-judge/blob/master/902-Password%20Search.cpp

int main()
{
    string in;
    int k;
    while(cin >> k){
        unordered_map<string,int> freqCount;
        cin >> in;
        for(int i=0;i+k<=in.length();i++){
            string sub = in.substr(i,k);
            freqCount[sub]++;
        }
        pair<string,int> res = {"",0};
        for(auto& p : freqCount){
            if(p.second > res.second)
                res = p;
        }
        cout << res.first << endl;
    }

    return 0;
}