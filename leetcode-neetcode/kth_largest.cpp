#include <algorithm>
#include <vector>
#include <queue>

using namespace std;
        
class Solution {
public:
    int findKthLargest(std::vector<int>& nums, int k) {
        int ans;
        priority_queue<int> pq;
        
        // Insert all elements into the priority queue
        for(int x: nums) {
            pq.push(x);
        }
        
        // Pop the largest element K times
        for(int i = 0; i < k; i++) {
            ans = pq.top();
            pq.pop();
        }
        
        return ans;
    }
};