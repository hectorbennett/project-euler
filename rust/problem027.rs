fn is_prime(n: i32) -> bool {
    let n_abs = n.abs() as u32;
    let limit = (n_abs as f64).sqrt() as u32;
    for i in 2..=limit {
        if n_abs % i == 0 {
            return false;
        }
    }
    return true
}

fn formula(a: i32, b: i32, n: i32) -> i32 {
    return n.pow(2) + a * n + b;
}

fn number_of_consecutive_primes(a: i32, b: i32) -> u32 {
    let mut count = 0;
    for n in 0..=a.abs() {
        if is_prime(formula(a, b, n)) {
            count += 1;
        } else {
            return count;
        }
    }
    return count;
}

fn main() {
    let limit = 1000;
    let mut max_a = 0;
    let mut max_b = 0;
    let mut max_result = 0;
    for a in -(limit-1)..limit {
        for b in -limit..=limit {
            let r = number_of_consecutive_primes(a, b);
            if r > max_result {
                max_result = r;
                max_a = a;
                max_b = b;
            }
        }
    }
    println!("{}", max_a * max_b);
}
