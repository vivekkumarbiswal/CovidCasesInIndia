import csv
# from os import read, stat

def main():
    newdict={}  #empty dictionary
    read_doc(newdict)
    get_state_from_user(newdict)

def read_doc(newdict):
    with open("covid_19_india.csv") as f:
        reader = csv.DictReader(f)
        for line in reader:
            state = line['State/UnionTerritory']
            recovered = line['Cured']
            deaths = line['Deaths']
            total_confirmed_cases = line['Confirmed']
            newdict[state] = [total_confirmed_cases,recovered,deaths]


def get_state_from_user(newdict):
    print("Lets see the INDIA's Covid data of a State")
    state = input("Enter a State name: ") 
    
    print("\n-------------",state,"-------------\n")

    print("Total confirmed cases ------>",newdict[state][0])
    print("Total patients recovered------>",newdict[state][1])
    print("Total deaths ------>",newdict[state][2])
    print()


if __name__ == '__main__':
    main()