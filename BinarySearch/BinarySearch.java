package BinarySearch;

public class BinarySearch {
    public int search(int[] nums, int target) {
        int begin = 0;
        int end = nums.length-1;
        while (end > begin) {
            int mid = (begin + end) / 2;
           if (nums[mid] == target) {
               return mid;
           } else if (nums[mid] < target) {
               begin = mid + 1;
           } else if (nums[mid] > target) {
               end = mid - 1;
           }
        }
        return -1;
    }
}