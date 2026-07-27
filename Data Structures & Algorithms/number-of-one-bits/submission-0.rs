impl Solution {
    pub fn hamming_weight(n: u32) -> i32 {
        let mut n_ones:  i32 = 0;
        for i in 0..=31 {
            let m = 1 << i;
            if (m & n) != 0 {
                n_ones += 1;
            }
        }
        n_ones
    }
}
