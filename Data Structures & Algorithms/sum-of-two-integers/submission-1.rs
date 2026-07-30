// 2⁸ * 2³ = 2^11 
// 2⁰ = 1 = 1 = 1 << 0
// 2¹ = 2 = 10 = 1 << 1
// log2(2^11) = 11 = 8 + 3
// how to log2 in binary
// 8 = 2^3 -> 1000
// just count the amount of zeros 
// 31 - number.leading_zeros()
// biggest problem here is the overflow case
// since we are making the numbers way bigger than what they should be

// 1 + 3 = 4 = 100
//   10
// 011 = 3
// 001 = 1
//       0

// A, B, carry
// SUM = A xor B xor carry
// carry = A and B xor SUM

// 1, 1, 1
// SUM =  1
// CARRY= 1

// 1,0,1
// SUM = 0
// carry = 1

// 0, 0,1
// SUM = 1
// carry = 0


impl Solution {
    /*
    pub fn get_sum(a: i32, b: i32) -> i32 {
        31i32 - (((1i32 << a)*(1i32 <<b) as i32)).leading_zeros() as i32
    }*/
    pub fn get_sum(a: i32, b: i32) -> i32 {
        add_ints(a,b)
    }
}


/// adds to numbers without using the + or - operator
pub fn add_ints(a: i32, b: i32) -> i32 {
    let mut carry = false;
    let mut res = 0;
    for i in 0..((std::mem::size_of::<i32>() * 8) as i32) {
        // extract the single bit inputs for our function
        let a = ((a >> i) & 1) == 1;
        let b = ((b >> i) & 1) == 1;

        let (s, c) = add_bits(a, b, carry);

        // save the next carry
        carry = c;

        // save this bit to the result
        res |= (s as i32) << i;
    }

    // overflows would just wrap around
    res
}
/// returns tuple (sum, carry)
fn add_bits(a: bool, b: bool, carry: bool) -> (bool, bool) {
    let sum: bool = a ^ b ^ carry;
    let carry: bool = (a && b) | (a && carry) | (b && carry);
    (sum, carry)
}


