class Solution {
    public int longestSubarray(int[] nums) {
        // length of the window
        int l = 0;
        boolean onlyone = true;
        int temp = 0;
        int loc = 0;
        boolean flag = false;
        int i = 0;
        while ( i < nums.length) {
            // temp subarray length
            // location of last zero
            if (nums[i] == 1){
                temp += 1;
            }
            else if (nums[i] == 0 & !flag) {
                flag = true;
                onlyone = false;
                loc = i;
            }
            else {
                if (temp > l){
                    l = temp;

                }
                temp = 0;
                flag = false;
                i = loc;
            }
            i++;
        }

        if (temp > l){
            l = temp;
        }

        if (onlyone){
            l -= 1;
        }

        return l;
    }
}

public class Array {
    public static void main(String[] args){
        // solution test of longest subarray problem.
        Solution sol = new Solution();
        int[] arr = {1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1};
        int k = sol.longestSubarray(arr);
        System.out.println(k);
    }
}
