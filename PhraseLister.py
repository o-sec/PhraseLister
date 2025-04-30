#!/usr/bin/python3

import argparse
import random
import sys
import os


class Wordlister():
    def __init__(self) -> None :
        
        # initialize the arguments parser
        self.parser = argparse.ArgumentParser(description="custom wordlist generator")
        self.parser.add_argument("-fs", "--fs", required=False, help="field seperator ( ' ' by default ) ")
        self.parser.add_argument("-o", "--output", required=True, help="save output to a file")
        # parse arguments
        self.args = self.parser.parse_args()
        # colors
        self.Y = "\033[93m"
        self.R = "\033[91m"
        self.W = "\033[97m"
        self.G = "\033[92m"
        self.Res = "\033[0m"


    # parse the given info
    def parseInfo(self, info, field_separator) -> list :
        try:
            self.fs = field_separator
            return info.rstrip().split(self.fs) * 5
        except Exception as e:
            print(str(e))
            
    # generate wordlist         
    def generateWordlist(self, words, filename) -> None :
        try:
            one_word_list = [word for word in words]
            two_words_list = ["".join(random.sample(words,2)) for _ in range(len(words) * 50)]
            three_words_list = ["".join(random.sample(words,3)) for _ in range(len(words) * 50)]
            four_words_list = ["".join(random.sample(words,4)) for _ in range(len(words) * 50)]
            # puting all the above lists togather
            wordlist = one_word_list + two_words_list + three_words_list + four_words_list
            wordlist = list(set(wordlist))
            # savig the wordlist to a file
            with open(filename, 'a') as wordlist_file:
                for word in wordlist:
                    wordlist_file.write(word+"\n")
        
        except Exception as e:
            print(str(e))
            exit()  

    def main(self) -> None:
    
        try:
            fs = self.args.fs if self.args.fs else ' '
            filename = self.args.output
            
            prompt = f"""\n{self.G} Enter words related to your target to generate a customized wordlist. ( {self.Y}Separate each word with "{fs}"{self.G} ) \n\n ~~> {self.Res}"""

            info = input(prompt)
            print("\n")
            print(f"[{self.G}info{self.Res}] - parsing the {self.G}data{self.Res}...")
            words = self.parseInfo(info, fs)
            print(f"[{self.G}info{self.Res}] - generating the {self.G}wordlist{self.Res}...")
            self.generateWordlist(words, filename)
            print(f"[{self.G}info{self.Res}] - {self.G}wordlist{self.Res} successfully created  ")
                
        
        except KeyboardInterrupt as ki:
            print(f"\n{self.W}[{self.R}exit{self.W}] - keyboardInterrupt ! {self.Res}")
            exit(3)


if __name__ == "__main__":
    wordlister = Wordlister()
    wordlister.main()

