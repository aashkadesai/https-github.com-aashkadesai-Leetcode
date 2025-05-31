// class Solution {
//     public void sortColors(int[] nums) {
//         int n = nums.length;
//         int low = 0, mid = 0, high = n - 1;

//         while(mid <= high){
//             if(nums[mid] == 0){
//                 swap(nums, mid, low);
//                 mid++;
//                 low++;
//             } else if(nums[mid] == 1){
//                 mid++;
//             } else {
//                 swap(nums, mid, high);
//                 high--;
//             }
//         }
//     }
//     private void swap(int[] nums, int i, int j) {
//             int temp = nums[i];
//             nums[i] = nums[j];
//             nums[j] = temp;
//         }
// }

class Solution {
    public void sortColors(int[] nums) {
        if (nums.length <= 1) return;
        int n = nums.length;
        int[] count = new int[3];

        for(int num: nums){
            count[num]++;
        }

        int idx = 0;
        for(int i = 0; i <= 2; i++) {
            while(count[i] > 0) {
                nums[idx] = i;
                idx++;
                count[i]--;
            }
        }
    }
}