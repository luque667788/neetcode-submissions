impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let sum_range: i32 = (nums.len() as i32)*(nums.len() as i32+ 1)/2;
        let sum_vec: i32 = nums.iter().sum();
        sum_range - sum_vec
    }
}
