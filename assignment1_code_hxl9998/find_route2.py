import sys

'''
python_file_name
input_text
source_city
destination_city
h_text
'''

def uniform_cost_search(fringe, visited, city_map, source, destination):
    # if fringe empty, return 'No path found'
    if( not fringe ): return print('No path found')

    # compare and find minimum distance in the fringe
    if( fringe ):
        closest_city = min(fringe, key=fringe.get)
        # if that minimum element is destination, return cost of the path
        if( closest_city == destination ):
            print(str(source) + ' to ' + str(closest_city) + ' with distance ' + str(fringe[closest_city]))
            return

        # put that element into visited to be visited
        cost = fringe.pop(closest_city)
        visited[closest_city]= cost
        
        # expand that element and added into fringe
        for city in city_map[closest_city]:
            if( not (city in visited or city in fringe)):
                fringe.update({city: cost+city_map[closest_city][city]})
            elif( city in visited):
                if(visited[city]> cost+city_map[closest_city][city]):
                    visited[city]= cost+city_map[closest_city][city]
            elif( city in fringe):
                if(fringe[city]> cost+city_map[closest_city][city]):
                    fringe[city]= cost+city_map[closest_city][city]

                #if(fringe[city] < cost+city_map[closest_city][city] ):

    uniform_cost_search(fringe, visited, city_map, source, destination)

def uninformed_search(city_map, source, destination):
    print('Searching...')
    fringe = {}
    visited = {}
    fringe.update({source: 0})


    # return the shortest distance between source and destination
    uniform_cost_search(fringe, visited, city_map, source, destination)
    
    




def informed_search():
    print('INFORMED')
    #print_output(['City1', 'City2', 'City3', 'City4'], [0,0])

# read file and return cities dictionary
def read_file(input_file):
    f = open( input_file , "r")
    temp = f.readline()
    cities = {}
    cities2 = {}
    while(temp != "END OF INPUT"):
        temp = temp.split()       
        cities.setdefault( temp[0], {})[temp[1]] = int(temp[2])
        cities.setdefault( temp[1], {})[temp[0]] = int(temp[2])
        cities2.update({temp[0]:1})
        cities2.update({temp[1]:1})
        temp = f.readline()
    return cities

def main():
    print( sys.argv )
    if( len(sys.argv) < 4):
        print('not enough arguments')
        return
    input_file = sys.argv[1]
    source = sys.argv[2]
    destination = sys.argv[3]
    
    # list of all connected cities and its distance
    temp = read_file(input_file)
    city_map = temp
    
    # check to see whether city exists
    try:
        city_map[source]
    except:
        print(source + ': does not exist')
        try:
            city_map[destination]
        except:
            print(destination + ': does not exist')
            return
    try:
        city_map[destination]
    except:
        print(destination + ': does not exist')
        return
    
    print(city_map[source])
    
    if( len(sys.argv) == 4): # no h_file -> uninformed search
        uninformed_search(city_map, source, destination)
        
    elif( len(sys.argv) > 4): # if has h_file -> informed search
        informed_search()
    






if __name__ == "__main__":
    main()



