#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <sstream>
#include <typeinfo>
#include <fstream>

using namespace std;

class UnsortedSequence 
{
public:
	vector<int> getUnsorted(vector<int> s)
	{
		sort(s.begin(), s.end());
		if (s[0] == s[s.size()-1])
			return vector<int>();
		next_permutation(s.begin(), s.end());
		return s;
	}
};
