import java.util.HashMap;
import java.util.ArrayList;

class ValidParentheses {
    public boolean isValid(String s) {
        String[] charArray = s.split("");
        if (charArray.length < 2) {
            return false;
        }
        HashMap<String, String> map = new HashMap<>();
        ArrayList<String> que = new ArrayList<>();
        map.put(")", "(");
        map.put("]", "[");
        map.put("}", "{");
        for (String parenthes: charArray) {
            if (map.keySet().contains(parenthes) && que.size() == 0) {
                return false;
            } else if (map.values().contains(parenthes)) {
                que.add(parenthes);
            } else if (!map.get(parenthes).equals(que.get(que.size()-1))) {
                return false;
            }
            else if (map.get(parenthes).equals(que.get(que.size()-1))) {
                    que.remove(que.size()-1);
                }
            }
        return que.size() == 0;
        
    }
    public static void main(String[] args) {
        ValidParentheses isItValid = new ValidParentheses();
        System.out.println(isItValid.isValid("()")); //true
        System.out.println(isItValid.isValid("()[]{}")); //true
        System.out.println(isItValid.isValid("(]")); //false
        System.out.println(isItValid.isValid("(])")); //false
    }
}