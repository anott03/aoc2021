use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("./src/input")?;
    let reader = BufReader::new(file);
    let lines: Vec<String> = reader.lines()
        .filter(|item| item.is_ok())
        .map(|item| item.unwrap())
        .collect();

    part1(&lines);
    Ok(())
}

fn part1(ls: &Vec<String>) {
    let mut lines = ls.clone();
    let mut gamma_rate = String::new();
    let mut epsilon_rate = String::new();
    for _ in 0..12 {
        let mut x = 0;
        for i in 0..lines.len() {
            let d = lines[i].chars().next().unwrap().to_digit(10).unwrap();
            x += d;

            let mut s = lines[i].clone();
            s.remove(0);
            lines[i] = s;
        }
        if x < (lines.len() as u32)/2 {
            gamma_rate += "0";
            epsilon_rate += "1";
        } else {
            gamma_rate += "1";
            epsilon_rate += "0";
        }
    }

    let gamma = isize::from_str_radix(&gamma_rate, 2).unwrap();
    let epsilon = isize::from_str_radix(&epsilon_rate, 2).unwrap();
    println!("{}", gamma * epsilon);
}

fn part2(ls: &Vec<String>) {
    let mut lines = ls.clone();

}
