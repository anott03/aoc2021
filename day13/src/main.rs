use std::fs::File;
use std::io::{self, prelude::*, BufReader};

fn main() -> io::Result<()> {
    let file = File::open("./src/13.in")?;
    let reader = BufReader::new(file);

    let lines: Vec<String> = reader.lines()
        .filter(|item| item.is_ok())
        .map(|item| item.unwrap())
        .collect();

    let mut coords: Vec<(i32, i32)> = Vec::new();
    let mut i = 0;
    loop {
        if lines[i] == "" {
            break;
        }
        let mut x = lines[i].split(",");
        coords.push((
            x.next()
                .unwrap()
                .parse::<i32>()
                .unwrap(),
            x.next()
                .unwrap()
                .parse::<i32>()
                .unwrap()
        ));
        i += 1
    }

    let mut folds: Vec<(char, i32)> = Vec::new();
    let mut start = false;
    for i in 0..lines.len() {
        if start {
            let mut x = lines[i].split("=");
            let mut c: char = 'x';
            if x.next().unwrap().contains("y") {
                c = 'y';
            }
            folds.push((
                c,
                x.next().unwrap().parse::<i32>().unwrap()
            ));
        }
        else if lines[i] == "" {
            start = true;
        }
    }

    println!("{}", p1(&coords, &folds).unwrap());
    Ok(())
}

fn p1(coords: &Vec<(i32, i32)>, folds: &Vec<(char, i32)>) -> Result<i32, String> {
    let axis = folds[0].0;
    let val = folds[0].1;

    let mut new_coords: Vec<(i32, i32)> = Vec::new();

    for c in coords {
        if axis == 'x' {
            if c.1 < val {
                new_coords.push(c.clone());
            } else if c.1 > val {
                let dist = c.1 - val;
                let coord = (c.0, val - dist);
                if !new_coords.iter().any(|&i| i == coord) {
                    new_coords.push(coord);
                }
            }
        } else {
            if c.0 < val {
                new_coords.push(c.clone());
            } else if c.0 > val {
                let dist = c.0 - val;
                let coord = (
                    val - dist,
                    c.1
                );
                if !new_coords.iter().any(|&i| i == coord) {
                    new_coords.push(coord);
                }
            }
        }
    }

    // 797 – too high
    Ok(new_coords.len() as i32)
}
