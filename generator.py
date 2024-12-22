
import argparse
import sys


def generator(name:str, lower=False) -> str:
    """
    takes a name (firstname lastname) 
    and does common name conventions on it. 
    Returns a list of abrivations.
    Used for generating windows AD common usernames 
    """
    result = ""

    if lower:
        name = name.lower()
    name = name.strip()
    data = name.split(' ')

    try:
    #3 first chars of firstname, 3 lastname
        result+=data[0][:3]+data[1][:3]+"\n"
    except IndexError:
        pass

    # 3 first char of 
    try:
        result+=data[0][:3]+'.'+data[1][:3]
    except IndexError:
        pass
    
    #1 first char [dot] lastname
    try:
        result+=data[0][0]+'.'+data[1]+"\'n"
    except IndexError:
        pass

    #2 first char + lastname 
    try:
        result+= data[0][:2]+data[1]+"\n"
    except IndexError:
        pass

    return result

def generate_names() -> Bool:
    with open(args.output,"w") as out_file:
        with open(args.input, "r") as in_file:
            for name in in_file:
                n.write(generator(name, args.lowercase))


def main():

    parser = argparse.ArgumentParser(prog='namegenerator', 
                                     usage="%(prog)s [-i input -o output [options]]")
    
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


    if len(sys.argv) < 3:
        parser.print_help()
        sys.exit(0)
    
    else:
        generate_names()

    

if __name__ == "__main__":
    main()