class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cmax =0;
        int count=0;
        for(int i=0;i<=nums.length-1;i++){
            if(nums[i]==1){
                count+=1;
                cmax=Math.max(count,cmax);
            }
            else{
                count=0;
            }
        }
   return cmax; }
}