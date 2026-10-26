// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int low = 1;         // Versions start at 1, not 0
        int high = n;        // The maximum version is n
        
        while (low < high) {
            int mid = low + (high - low) / 2; 
            
            if (isBadVersion(mid)) {
                high = mid; 
            } else {
                low = mid + 1;
            }
        }
        
        return low; 
    }
};