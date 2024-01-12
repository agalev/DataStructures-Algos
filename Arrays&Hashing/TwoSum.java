import java.util.HashMap;

public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) != null) {
                return new int[] {i, map.get(nums[i])};
            }
            map.put(target-nums[i], i);
        }
        return null;
    }
    public static void main(String[] args) {
        TwoSum twoSumObject = new TwoSum();
        int[] result = twoSumObject.twoSum(new int[] { 3, 2, 4 }, 6);
        if (result != null) {
            System.out.println("Indices: " + result[0] + ", " + result[1]);
        } else {
            System.out.println("No solution found.");
        }
    }
}
