import java.util.ArrayList;
import java.util.List;

class FizzBuzz {
  public List<String> fizzBuzz(int n) {
      List<String> answer = new ArrayList<String>();

      for (int num = 1; num <= n; num++) {

      boolean divisibleBy5 = (num % 5 == 0);
      boolean divisibleBy3 = (num % 3 == 0);

          if (divisibleBy5 && divisibleBy3) {
              answer.add("FizzBuzz");
          } else if (divisibleBy3) {
              answer.add("Fizz");
          } else if (divisibleBy5) {
              answer.add("Buzz");
          } else {
              answer.add(Integer.toString(num));
          }
      }

      return answer;

    }
    public static void main(String[] args) {
      FizzBuzz fb = new FizzBuzz();
      System.out.println(fb.fizzBuzz(15));
    }
}