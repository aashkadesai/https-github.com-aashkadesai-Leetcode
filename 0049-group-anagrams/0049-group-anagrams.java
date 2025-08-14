class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> anagram = new HashMap<>();

        for (String str: strs){
            char[] chars = str.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);

            if(!anagram.containsKey(sorted)) {
                anagram.put(sorted, new ArrayList<>());
            }
            anagram.get(sorted).add(str);
        }
        return new ArrayList<>(anagram.values());
    }
}