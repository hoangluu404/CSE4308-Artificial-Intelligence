import sys

'''
python_file_name
input_text
source_city
destination_city
h_text
'''

visited = []

def print_output(route, info):

    print('nodes expanded: ' + str(info[0]))
    print('nodes generated: ' + str(info[1]))
    print('distance: ' + str(info) + ' km')
    print('route: ' + str(route) )
    for node in route:
        print( node + ' to ' + node + ', ' + str(info) +' km')

def isVisited(current_city):
    try:
        visited.index(current_city)
        print(current_city + ' is already visited')
        return True
    except:
        visited.append(current_city)
        print(current_city + ' not yet visited')
        return False

def next_city(fringe, cost, city_map, destination, route, node):
    if( len(fringe)==0):
        return
    current_city = fringe.pop(0)
    print('node ' + str(node))
    print(str(fringe) + '----------------')
    
    if(isVisited(current_city)):
        print('going back to previous city')
        node = node -1
        return
    route.append(current_city)
    if(current_city==destination):
        print('destination reached, cost = ' + str(cost))
        print('route = ' + str(route))
        print('node expanded = ' + str(node))

    try:
        city_map[current_city]
    except:
        return

    print('currently in ' + str(current_city) + ', cost = ' + str(cost))
    for city in city_map[current_city]:
        #if(not isVisited(city)):    
        fringe.insert(0, city)
        print(city + ' added into fringe')
        
    for i in range( len(city_map[current_city]) ):
        print(current_city + ' to ' + fringe[0])
        print(str(fringe) + '~~~~~~~~~~~~~~~~')
        

        try:
            node = node +1
            next_city(fringe, cost+int(city_map[current_city][fringe[0]]), city_map, destination, route, node)
        except:
            fringe.pop(0)
            next_city(fringe, cost+int(city_map[current_city][fringe[0]]), city_map, destination, route, node)
            return

    

    
    
# depth first seach LIFO
def uninformed_search(city_map, source, destination):
    print('UNINFORMED')

    fringe = [source]
    route = []
    node = 0
    next_city(fringe, 0, city_map, destination, route, node)
    #print_output(['City1', 'City2', 'City3', 'City4'], [0,0])







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
        cities.setdefault( temp[0], {})[temp[1]] = temp[2]
        cities.setdefault( temp[1], {})[temp[0]] = temp[2]
        cities2.update({temp[0]:1})
        cities2.update({temp[1]:1})
        temp = f.readline()
    return [cities, cities2]

    

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
    city_map = temp[0]
    cities = temp[1]
    
    # check to see whether city exists
    try:
        cities[source]
    except:
        print(source + ': does not exist')
        try:
            cities[destination]
        except:
            print(destination + ': does not exist')
            return
    try:
        cities[destination]
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



