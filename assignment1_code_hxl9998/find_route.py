import sys

'''
python_file_name
input_text
source_city
destination_city
h_text
'''







# perform recursive Uniform Cost Search (UCS)
# return total distance and nodes expanded and nodes generated and the cities expanded
# return [ distance, [ nodes expanded, nodes generated ], [ cities ] ]
def uniform_cost_search(fringe, visited, city_map, source, destination, nodes, route, path):

    # if fringe empty, return -1
    if( not fringe ): return [-1, nodes, route]

    # compare and find minimum distance in the fringe
    if( fringe ):
        closest_city = min(fringe, key=fringe.get)
        nodes[0] = nodes[0]+1

        route.append(closest_city)
        
        # if that minimum element is destination, return cost of the path
        if( closest_city == destination ):
            print(str(source) + ' to ' + str(closest_city) + ' with distance ' + str(fringe[closest_city]))
            print('\n\n')
            
            return [fringe[closest_city], nodes, route]

        # put that element into visited to be visited
        cost_current = fringe.pop(closest_city)
        visited[closest_city] = cost_current

        # expand that element and added into fringe
        for city in city_map[closest_city]:
            nodes[1]=nodes[1]+1

            # if it is not visited or in the fringe
            if( not (city in visited or city in fringe)):
                
                fringe[city] = [ cost_current[0] + city_map[closest_city][city], [cost_current[1],city] ]
            # else if it is visited
            elif( city in visited):
                if(visited[city][0] > cost_current[0] + city_map[closest_city][city]):
                    visited[city]= cost_current[0] + city_map[closest_city][city]

            # else if it is in the fringe
            elif( city in fringe):
                if(fringe[city][0] > cost_current[0] + city_map[closest_city][city]):
                    fringe[city] = [cost_current[0] + city_map[closest_city][city], [cost_current[1], city]]

            
    print(fringe)
    return uniform_cost_search(fringe, visited, city_map, source, destination, nodes, route, path)
    

def print_route(route):
    if( not route): return
    if( len(route) == 1): print(route[0])
    else:
        print(route[1])
        route = route[0]
        print_route(route)


def uninformed_search(city_map, source, destination):
    fringe = {}
    visited = {}
    #route = []
    fringe.update({source: [0,[source]] })
    path = [source]
    # return the shortest distance between source and destination if available
    result = uniform_cost_search(fringe, visited, city_map, source, destination, [0, 0], [], [source])
    
 
    if(result[0][0]>-1):
        print('nodes expanded: ' + str(result[1][0]) + '\nnodes generated: ' + str(result[1][1]) )
        print('distance: ' + str(result[0][0]) + ' km')
        print('route:')
        route = result[0][1]
        route = print_route(route)
        print(route)
    else:
        print('nodes expanded: ' + str(result[1][0]) + '\nnodes generated: ' + str(result[1][1]) )
        print('distance: infinity')
        print('route:\nnone')

    print('')
    # fringe = []

    # fringe.append(source)
    # new_map = {}
    # for city in route:
    #     new_map[city] = city_map[city]

    
    #print(new_map)

    #route = []
    #print(dfs(fringe, new_map, destination, [], 0, result[0], source))
    #print(cost)




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
        cities.setdefault( temp[0], {})[temp[1]] = float(temp[2])
        cities.setdefault( temp[1], {})[temp[0]] = float(temp[2])
        cities2.update({temp[0]:1})
        cities2.update({temp[1]:1})
        temp = f.readline()
    return cities

def main():
    print( str(sys.argv) + '\n' )
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
    
    if( len(sys.argv) == 4): # no h_file -> uninformed search
        uninformed_search(city_map, source, destination)
        
    elif( len(sys.argv) > 4): # if has h_file -> informed search
        informed_search()
    






if __name__ == "__main__":
    main()



