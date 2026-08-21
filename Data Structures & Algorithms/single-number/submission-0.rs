impl Solution {
    pub fn single_number(nums: Vec<i32>) -> i32 {
        // this looks like it will be the xor property
        // if i recall correctly tthere is a property where if i xor stuff together
        // if they are the same it is zero
        // xor with zero is the same number
        // and the order of xor operation dont matter
        let mut res = 0;
        for n in nums{
            res = res ^ n;}
        return res;


    }
}
