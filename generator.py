
import argparse
import sys

def generator(name:str, lower=False) -> str:
    """
    takes a name (firstname lastname) 
    and does common name conventions on it. 
    returns a list of abrivations
    """
    result = ""

    if lower:
        name = name.lower()
    name = name.strip()
    data = name.split(' ')

    #3 first chars of firstname, 3 lastname
    result+=data[0][:3]+data[1][:3]+"\n"
    
    #1 first char . lastname
    result+=data[0][0]+'.'+data[1]+"\n"

    #2 first char + lastname d
    result+= data[0][:2]+data[1]+"\n"

    return result

def main():

    parser = argparse.ArgumentParser(prog='namegenerator', 
                                     usage="%(prog)s [options]")
    
    parser.add_argument("-o","--output",
                        help="output file",
                        type=str,
                        metavar=""
                        )
    parser.add_argument("-i","--input",
                        help="input file",
                        type=str,
                        metavar=""
                        )
    parser.add_argument("-l","--lowercase",
                        action="store_true",
                        help="all lowercase",
                        default=False
                        )
    
    args = parser.parse_args()

    if args.help:
        parser.print_help()
        sys.exit(0)

    with open(args.output,"w") as n:
        with open(args.input, "r") as f:
            for name in f:
                n.write(generator(name, args.lowercase))


if __name__ == "__main__":
    main()