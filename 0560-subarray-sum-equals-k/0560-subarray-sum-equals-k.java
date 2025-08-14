class Solution {
    public int subarraySum(int[] nums, int k) {
        Map<Integer, Integer> prefixMap = new HashMap<>();
        prefixMap.put(0, 1);

        int count = 0;
        int prefixSum = 0;

        for(int num: nums) {
            prefixSum += num;

            if(prefixMap.containsKey(prefixSum - k)) {
                count += prefixMap.get(prefixSum - k);
            }
            prefixMap.put(prefixSum, prefixMap.getOrDefault(prefixSum, 0) + 1);
        }
        return count;
    }
}