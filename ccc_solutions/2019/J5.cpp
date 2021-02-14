#include <bits/stdc++.h>

using namespace std;
//required moves
int k;
//array for our steps 
vector<string> seenstr;
//array for the role number and the position it was applied
vector<pair<int, int>> rulenpos;
//our starting string and our goal
string istring, fstring;
//our rules
pair<string, string> rules[3];
//A timesaver - if a string has already been seen at a certain depth, we don't want to search it again
//set to size 15 as according to input the max depth is 15
unordered_set<string> visited[15];
//recursive function that returns a boolean value
//takes a string and the current depth
bool solve(string s, int d){
    //our base case: if we are at the correct depth
    if (d==k){
        //return whether we have found our desired string
        if (s==fstring) return true;
        return false;
    }
    //if we have already seen this string at this depth, return false
    //this is a form of "dynamic programming"
    if (visited[d].find(s)!=visited[d].end()) return false;
    //mark as seen
    visited[d].insert(s);
    //a variable to hold our new string
    string ne;
    //loop through our string rules
    for (int l=0; l<3; l++){
        //store the string rule
        pair<string, string> &r = rules[l];
        //search for the "key" of the stringrule in our input string
        size_t pos = s.find(r.first, pos+1);
        //this basically gets all the locations of the key in our string
        while (pos != string::npos){
            //activate the stringrule, essentially delete the string thats being replaced and insert the new string
            ne = s.substr(0, pos);
            ne += r.second;
            ne += s.substr(pos+r.first.size(), s.size()-(pos+r.first.size())+1);
            //recur and check if true
            if (solve(ne, d+1)){
                //if true, store the stringrule number (1-3) and where it was applied
                rulenpos.push_back(make_pair(l+1, pos+1));
                //store the string we passed
                seenstr.push_back(ne);
                //return true as well
                //this will create a sort of "chain" that moves up the recursive calls and stores
                //what we want
                return true;
            }
            //c++ thing that goes to the next location of the stringrule
            pos = s.find(r.first, pos+1);
        }
    }
    return false;
    
}
int main() {
    //c++ stuff
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    //get our stringrules from input and store them
    string a, b;
    for (int i=0; i<3; i++){
        cin >> a >> b;
        rules[i] = make_pair(a, b);
    }
    //get our starting string and our desired output
    cin >> k >> istring >> fstring;
    //activate function
    solve(istring, 0);
    //output: loop through our stored data and print
    //loop in reverse due to how data is added
    for (int j=k-1; j>=0; j--){
        pair<int, int> &temp = rulenpos[j];
        string &res = seenstr[j];
        cout << temp.first << " " << temp.second << " " << res << "\n";
    }
    return 0;
}
