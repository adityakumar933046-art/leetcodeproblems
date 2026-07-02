class Solution {
    public int[] twoSum(int[] nums, int target) {
        int a = nums.length;
        for(int i=0; i<a; i++ ){
            for(int j=i+1;j<a; j++){
                if(nums[i]+nums[j]==target){
                    return new int[]{i,j};
                }
            }
        }
        return new int[]{};
    }
}