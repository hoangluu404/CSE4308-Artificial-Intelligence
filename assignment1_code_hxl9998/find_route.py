import sys

'''
## USER INPUTS ##
python_file_name
input_text
source_city
destination_city
h_text
'''

# perform recursive Uniform Cost Search (UCS)
# return shortest path and its distance
# also return node generated and node visited
def uniform_cost_search(fringe, visited, city_map, source, destination, nodes, path):

    # if fringe empty, return -1
    if( not fringe ): return [[-1, nodes]]

    # compare and find minimum distance in the fringe
    else:
        closest_city = min(fringe, key=(lambda k:fringe[k][0]))

        # count node visited
        nodes[0] = nodes[0]+1
        
        # if that minimum element is destination, return cost of the path
        if( closest_city == destination ):
            #print(str(source) + ' to ' + str(closest_city) + ' with distance ' + str(fringe[closest_city]))
            return [fringe[closest_city], nodes]

        # put that element into visited to be visited
        cost_current = fringe.pop(closest_city)
        visited[closest_city] = cost_current

        # expand that element and added into fringe
        for city in city_map[closest_city]:
            nodes[1]=nodes[1]+1

            # if it is not visited or in the fringe
            if( not (city in visited or city in fringe)):
                
                fringe[city] = [ cost_current[0] + city_map[closest_city][city], [cost_current[1],city] ]
            # # else if it is visited
            # elif( city in visited):
            #     if(visited[city][0] > cost_current[0] + city_map[closest_city][city]):
            #         fringe[city] = [cost_current[0] + city_map[closest_city][city],[cost_current[1], city]]
            #         visited.pop(city)
                
            # # else if it is in the fringe
            # elif( city in fringe):
            #     if(fringe[city][0] > cost_current[0] + city_map[closest_city][city]):
            #         fringe[city] = [cost_current[0] + city_map[closest_city][city], [cost_current[1], city]]
            # 
            elif ( city in (fringe or visited)):
                if( city in visited and visited[city][0] > cost_current[0] + city_map[closest_city][city]):
                    visited[city] = [cost_current[0] + city_map[closest_city][city],[cost_current[1], city]]
                    fringe[city] = visited.pop(city)
                elif( city in fringe and fringe[city][0] > cost_current[0] + city_map[closest_city][city]):
                    fringe[city] = [cost_current[0] + city_map[closest_city][city], [cost_current[1], city]]

    return uniform_cost_search(fringe, visited, city_map, source, destination, nodes, path)
    
# extract route from nested list
def extract_route(route, path):
    if( not route): return path
    if( len(route) == 1): 
        path.append(route[0])
    else:
        path.append(route[1])
        route = route[0]
        extract_route(route, path)
        return path


def uninformed_search(city_map, source, destination):
    
    result = uniform_cost_search(
        {source: [0,[source]] },
        {},
        city_map,
        source,
        destination,
        [0, 0],
        [source])
    
    # if path found
    if(result[0][0] > -1):
        print('nodes expanded: ' + str(result[1][0]) + '\nnodes generated: ' + str(result[1][1]) )
        print('distance: ' + str(result[0][0]) + ' km')
        print('route:')
        route = result[0][1]
        route = extract_route(route, [])
        if(route):
            route.reverse()
            for i in range (len(route)-1) :
                print(route[i], 'to' , route[i+1], city_map[route[i]][route[i+1]], 'km')
        else: print(source, 'to', str(destination) + ',', result[0][0] ,'km')
 

    # if path not found
    else:
        print(result)
        print('nodes expanded: ' + str(result[0][1][0]) + '\nnodes generated: ' + str(result[0][1][1]) )
        print('distance: infinity')
        print('route:\nnone')


def informed_search(city_map, source, destination, h_file):
    print('TODO: informed search from',source, 'to', destination, 'with', h_file)


# read file and return cities dictionary
def read_map(input_file):
    try:
        f = open( input_file , "r")
    except:
        print('input file not found')
        return False
    temp = f.readline()
    cities = {}
    while(temp != "END OF INPUT"):
        temp = temp.split()       
        cities.setdefault( temp[0], {})[temp[1]] = float(temp[2])
        cities.setdefault( temp[1], {})[temp[0]] = float(temp[2])
        temp = f.readline()
    return cities


def main():
    #print( str(sys.argv) + '\n' )
    print('================================')
    if( len(sys.argv) < 4):
        print('not enough arguments')
        print('================================\n')
        return
    input_file = sys.argv[1]
    source = sys.argv[2]
    destination = sys.argv[3]
    if(len(sys.argv)>4):
        h_file = sys.argv[4]
    # list of all connected cities and its distance
    city_map = read_map(input_file)
    if( not city_map ):
        return

    # check to see if source and destination exist
    if( not source in city_map ):
        print(source, 'does not exist')
        if( not destination in city_map ):
            print(destination, 'does not exist')
        print('================================\n')    
        return
    elif( not destination in city_map ):
        print(destination, 'does not exist')
        print('================================\n')
        return
    if( len(sys.argv) == 4): # no h_file -> uninformed search
        uninformed_search(city_map, source, destination)
        
    elif( len(sys.argv) > 4): # if has h_file -> informed search
        informed_search(city_map, source, destination, h_file)
    print('================================\n')

if __name__ == "__main__":
    main()



