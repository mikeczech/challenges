use std::fs::File;
use std::io::{BufRead, BufReader};


fn main() -> std::io::Result<()>{
    let file = File::open("input")?;

    let reader = BufReader::new(file);

    for line in reader.lines() {
        println!("{}", line?)
    }

    Ok(())
}
