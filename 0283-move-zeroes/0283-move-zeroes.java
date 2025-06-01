class Solution {
    public void moveZeroes(int[] nums) {
        int i = 0, j = 1;

        while(j < nums.length){
            if (nums[i] == 0 && nums[j] != 0) {
                swap(nums, i, j);
                i++;
                j++;
            } else if (nums[i] != 0) {
                i++;
                if(i == j) j++;
            } else
            j++;
        }
    }
     
    public void swap(int[] nums, int i, int j){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}