class Solution {
public:
    int findmax(vector<int>& v){
        int maxi = INT_MIN;
        for(int i = 0 ; i< v.size();i++){
            maxi = max(maxi , v[i]);
        }
        return maxi;
    }
    long long calculatehr(vector<int>& v , int hr){
        long long total_hr = 0;
        for(int i = 0 ; i< v.size() ; i++){
            total_hr +=(v[i] + (long long)hr - 1) / hr;
        }
        return total_hr;
    }
 

    int minEatingSpeed(vector<int>& piles, int h) {
        int low = 1 ;
        int high = findmax(piles);
        while(low <= high){
            int mid =low + (high - low)/ 2;
            long long total_hr = calculatehr( piles , mid);

            if(total_hr <= h){
                high = mid - 1;
            }
            else{
                low = mid + 1;
            }

            
        }
        return low ;
        
    }
};