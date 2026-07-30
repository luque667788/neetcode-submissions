impl Solution {
    pub fn missing_number(nums: Vec<i32>) -> i32 {
        let mut x_r = 0;
        for i in 1..=nums.len(){
            x_r ^= i as i32; 
        }
        for n in nums {
            x_r ^= n;
        }
        x_r
    }
}

// 1
