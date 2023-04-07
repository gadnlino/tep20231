fn main() {
    problem();
}

fn get_input() -> String {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).expect("Failed");
    buffer
}

fn problem(){
    let nstrings = get_input().trim().parse::<i64>().unwrap();

    for __ in 0..nstrings{
        let s = get_input();

        let mut remaining : Vec<char> = Vec::new();

        for idx in (1..s.len()).step_by(2){
            if s.chars().nth(idx-1).unwrap() != s.chars().nth(idx).unwrap(){
                remaining.push(s.chars().nth(idx).unwrap());
            }
        }

        println!("{}", remaining.len());
    }
}