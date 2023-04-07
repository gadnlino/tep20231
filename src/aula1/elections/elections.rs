fn main() {
    problem();
}

fn get_input() -> String {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).expect("Failed");
    buffer
}

fn problem() {
    let n = get_input().trim().parse::<i64>().unwrap();

    for __ in 0..n {
        let liine: String = get_input();

        let numbers: Vec<i32> = liine
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();

        let max: i32 = *(numbers.iter().max().unwrap());

        let mut result: Vec<String> = Vec::new();

        let mut nmax: i32 = 0;

        for nn in &numbers {
            if *nn == max {
                nmax += 1;
            }
        }

        for number in numbers {
            if (number == max && nmax == 1) {
                result.push(0.to_string());
            } else if (number == max && nmax > 1) {
                result.push(1.to_string());
            } else {
                result.push((max - number + 1).to_string());
            }
        }

        println!("{}", result.join(" "));
    }
}