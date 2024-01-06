class ConcatenationOfArray {
    public int[] getConcatenation(int[] nums) {
        int[] ans = new int[nums.length*2];
        for (int i = 0; i < nums.length; i++) {
            ans[i] = nums[i];
            ans[i+nums.length] = nums[i];
        }
        return ans;
    }
    public static void main(String[] args) {
        ConcatenationOfArray concat = new ConcatenationOfArray();
        System.out.println(concat.getConcatenation(new int[] {1,2,3}));
    }
}