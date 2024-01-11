public class isPalindrome {
    public boolean checkIfIsPalindrome(String s) {
        char[] array = s.toLowerCase().toCharArray();
        int left = 0;
        int right = array.length - 1;
        while (left < right) {
            if (!Character.isLetterOrDigit(array[left])) {
                left++;
                continue;
            }
            if (!Character.isLetterOrDigit(array[right])) {
                right--;
                continue;
            }

            if (array[left] != array[right]) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
