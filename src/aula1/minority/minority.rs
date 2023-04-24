//use std::convert::TryInto;

fn main() {
    problem();
}

fn get_input() -> String {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).expect("Failed");
    buffer
}

fn count_chars(phrase: &str, ch: char)->i32{
    let mut result = 0;
    for c in phrase.chars() {
        // Count all chars that are not whitespace.
        if c == ch {
            result += 1;
        }
    }
    return result;
}

fn problem(){
    let ntests = get_input().trim().parse::<i64>().unwrap();

    for __ in 0..ntests{
        let line: String = get_input().trim().to_string();

        let zeroes = count_chars(&line ,'0');
        let ones = count_chars(&line ,'1');
        //println!("{}, {}", zeroes, ones);

        if zeroes == 0 || ones == 0 || zeroes == ones {
            println!("{}", 0);
            continue;
        }

        let mut minority_char: char = '0';
        //let mut minority_char_count: i32 = zeroes;

        if ones < zeroes {
            minority_char = '1';
            //minority_char_count = ones;
        }

        let mut max : i32 = 0;
        let mut removed_slice : String = String::new();

        for sz in 1..line.len(){
            for i in 0..line.len(){
                if i + sz -1 < line.len(){
                    let removed_str = line.get(i..i+sz).unwrap().to_owned().trim().to_string();
                    //println!("{}", removed_str);

                    if !removed_str.is_empty(){
                        let minority_removed = count_chars(&removed_str, minority_char);

                        if minority_removed  > max {
                            max = minority_removed;
                            removed_slice = removed_str;
                        }
                    }
                }
            }
        }

        println!("{}", max);
        //println!("{}, {}", max, removed_slice);
    }
}