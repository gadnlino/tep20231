fn main() {
    problem();
}

fn get_input() -> String {
    let mut buffer = String::new();
    std::io::stdin().read_line(&mut buffer).expect("Failed");
    buffer
}

fn problem(){
    let ntests = get_input().trim().parse::<i64>().unwrap();

    for __ in 0..ntests{
        let ncandies = get_input().trim().parse::<i64>().unwrap();

        let liine: String = get_input();

        let mut candies_count: Vec<i64> = liine
            .split_whitespace()
            .map(|s| s.parse().unwrap())
            .collect();

        candies_count.sort_by(|a, b| b.cmp(a));

        let max = candies_count[0];

        let mut veredict : String = "YES".to_string();

        let mut idx_last_chosen = 0;

        let mut candies_eaten = 1;

        while true{
            let possible_choices = candies_count.filter(|a| a >= candies_count[idx_last_chosen]).collect();
        }

        //println!("{}, {}, {}, {}", ncandies, max, candies_count[0], candies_count[1]);

        // if ncandies == 1 && max > 1{
        //     veredict = "NO".to_string();
        //     println!("{}", veredict);
        //     continue;
        // }

        // if ncandies == 1 && max == 1{
        //     veredict = "YES".to_string();
        //     println!("{}", veredict);
        //     continue;
        // }

        // for i in 0..candies_count.len()-1{
        //     if candies_count[i] - candies_count[i+1] > 1{
        //         veredict = "NO".to_string();
        //         break;
        //     }
        // }

        println!("{}", veredict);
    }
}