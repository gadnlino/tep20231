fn main() {
    problem();
}

fn get_input() -> String {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).expect("Failed");
    buffer
}

fn recursive(total_length: usize, remaining_string: String) -> usize {
    //println!("{}, {}", total_length, remaining_string);

    if remaining_string.trim().is_empty() || remaining_string.trim().len() == 0 {
        //println!("caso 1");
        return total_length;
    }

    if remaining_string.len() == 1{
        return total_length - 1;
    }

    if remaining_string.chars().nth(0).unwrap() == remaining_string.chars().nth(1).unwrap() {
        //println!("caso 2");
        return recursive(
            total_length,
            remaining_string.get(2..remaining_string.len()).unwrap().to_string(),
        );
    }

    //println!("caso 3");

    let opt1 = (remaining_string.get(0..1).unwrap().to_owned()
                + remaining_string.get(2..remaining_string.len()).unwrap()).trim().to_string();

    let opt2 = remaining_string.get(1..remaining_string.len()).unwrap().trim().to_string();

    /////////println!("{}, {}", opt1, opt2);

    return std::cmp::max(
        recursive(
            total_length - 1,
            opt1
        ),
        recursive(
            total_length - 1,
            opt2
        )
    );
}

fn problem() {
    let nstrings = get_input().trim().parse::<i64>().unwrap();

    for __ in 0..nstrings {
        let s = get_input();

        let result = recursive(s.len(), s.clone());

        println!("{}", (s.len() - result).to_string());
    }
}
