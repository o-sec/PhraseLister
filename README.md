# PhraseLister

**PhraseLister** is a simple and command-line tool that helps you generate targeted wordlists based on user-provided input. useful when you need a custom wordlist to crack passwords that consists of multi words such as : "robertlee123" .

## Features

- Interactive input for wordlist generation 
- Simple and fast 
- Output to custom file 
- Generate a large and completely unique passwords 

## Usage

```bash
usage: PhraseLister.py -o output.txt

```

You will be prompted to enter words:

```
Enter words related to your target to generate a customized wordlist. ( Separate each word with "," ) 

 ~~> 
```

The tool will then generate combinations or entries based on the provided words and save them to `output.txt`.

## Example

```bash
$ PhraseLister.py -o mywordlist.txt
Enter words related to your target to generate a customized wordlist. ( Separate each word with "," ) 

 ~~> admin 2024 secure
```

Example output in `mywordlist.txt`:

```
admin
2024
secure
admin2024
secureadmin
adminsecure2024
...
```


## Installation

Clone the repository:

```bash
git clone https://github.com/o-sec/PhraseLister.git
cd PhraseLister
```
Change file permission:

```bash
chmod +x PhraseLister.py
```
Run the script:

```bash
PhraseLister.py -o wordlist.txt
```
## Screenshots 

- PhraseLister 
<img src='https://raw.githubusercontent.com/o-sec/PhraseLister/main/Screenshot_PhraseLister.png' />

- output

<img src='https://raw.githubusercontent.com/o-sec/PhraseLister/main/Screenshot_Output.png' />

## Disclaimer

This tool is intended for educational and research purposes only. The creator does not condone or support any illegal or unethical use of this tool. Users are responsible for ensuring that their use complies with all applicable laws and regulations.
