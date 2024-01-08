public class PlusOne {
    public int[] plusOne(int[] digits) {
        int n = digits.length;
        for (int i = n - 1; i >= 0; i--) {
            if (digits[i] < 9) {
                digits[i]++;
                return digits;
            }
            digits[i] = 0;
        }
        int[] answer = new int[n + 1];
        answer[0] = 1;
        return answer;
    }

    public static void main(String[] args) {
        PlusOne solution = new PlusOne();
        System.out.println(solution.plusOne(new int[] {1,2,3}));
    }
}