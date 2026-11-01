class Solution {
public:

    int countstudent(vector<int>& nums , int pages){
        int student =1 ;
        long long pagesstudent = 0;
        for(int i =0 ; i<nums.size();i++){
            if(pagesstudent + nums[i] <= pages){
                pagesstudent += nums[i];
            }
            else{
                student += 1;
                pagesstudent = nums[i];
            }
        }
        return student;

    }
    int findpages(vector<int>& nums , int n , int m ){

        if(m > n) return - 1;
        int low = *max_element(nums.begin() , nums.end());
        int high = accumulate(nums.begin() ,nums.end() , 0);

        while(low <= high){
            int mid = (low + high)/2;
            int students = countstudent(nums , mid);
            if(students > m){
                low = mid + 1;
            }
            else{
                high = mid - 1;
            }
        }
        return low ;

    }

    


    int splitArray(vector<int>& nums, int k) {
        return findpages(nums , nums.size() , k);
        
    }
};