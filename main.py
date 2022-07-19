from functions.functions import print_hey
from basics.basics import area_of_circle

def main():
    print_hey('bobo')
    print_hey('jeep')
    print_hey('sam')
    print(area_of_circle(2))
    colors = ['red', 'blue', 'green', 'black']
    print(colors[3])    ## red
    print(colors[1])
    print(colors[2])    ## green
    print(len(colors))  ## 3


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
