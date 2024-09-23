import argparse

def load(filepath):
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError:
        print("Filepath is invalid")


def main():
    parse = argparse.ArgumentParser(
    description="Dunder Mifflin Rewards CLI",
    epilog="Enjoy and use with cautious.", 
    )
    parse.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to run",
        choices=("load","show","send"),
        default="help",
        
    )
    parse.add_argument(
        "filepath",
        type=str,
        help="File path to load",
        default=None
    )
    args = parse.parse_args()
  
    globals()[args.subcommand](args.filepath)
   
    
if __name__== "__main__":
    main()
