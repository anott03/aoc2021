use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("./src/input")?;
    let reader = BufReader::new(file);
    let lines: Vec<String> = reader.lines()
        .filter(|item| item.is_ok())
        .map(|item| item.unwrap())
        .collect();

    let line = &lines[0];
    let nums: Vec<i32> = line.split(",")
        .map(|item| item.parse::<i32>().unwrap())
        .collect();

    println!("{}", part1(&nums, 80));
    println!("{}", part2(&nums));
    Ok(())
}

fn part1(ns: &Vec<i32>, iters: usize) -> usize {
    let mut nums = ns.clone();

    for _ in 0..iters {
        let mut new_nums = nums.clone();
        for i in 0..nums.len() {
            new_nums[i] -= 1;
            if new_nums[i] == -1 {
                new_nums[i] = 6;
                new_nums.push(8);
            }
        }
        nums = new_nums;
    }

    return nums.len();
}

fn part2(ns: &Vec<i32>) -> usize {
    let mut nums = ns.clone();
    let mut X = vec![0;9];

    for i in 0..nums.len() {
        X[ nums[i] as usize ] += 1;
    }

    for _ in 0..256 {
        let mut Y = vec![0;9];
        for i in 0..X.len() {
            if i == 0 {
                Y[6] += X[i];
                Y[8] += X[i];
            } else {
                Y[i-1] += X[i];
            }
        }
        X = Y;
    }

    let mut s = 0;
    for i in 0..X.len() {
        s += X[i];
    }

    return s;
}
