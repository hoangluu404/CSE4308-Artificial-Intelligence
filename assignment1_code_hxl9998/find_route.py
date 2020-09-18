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
        #print(current_city + ' is already visited')
        return True
    except:
        visited.append(current_city)
        #print(current_city + ' not yet visited')
        return False

def sort(cities):
    if(len(cities)<2):
        print('nothing to sort')
        return cities

    temp = []
    
    print(cities)
    for num in cities:
        #if(len(temp)==0):
            #temp.append(cities.pop())

        '''
        if(len(temp)==0):
            temp.append(cities.pop(0))
        else:
            holder = []
            for i in range (len(cities)):
                if( temp and cities[0] < temp[len(temp)-1]):
                    temp.append(cities.pop(0))
                    print('\ntemp = ' + str(temp))

                elif( temp and cities[0] > temp[len(temp)-1]):
                    while( temp and cities[0] > temp[len(temp)-1] ):
                        holder.append(temp.pop(len(temp)-1))
                        print('\ntemp = ' + str(temp))
                        print('holder = ' + str(holder))
                    
                    print('-------------')
                    temp.append(cities.pop(0))
                    while( holder ):
                        temp.append(holder.pop(len(holder)-1))
                        print('\ntemp = ' + str(temp))
                        print('holder = ' + str(holder))  
                        '''  
    temp.reverse()    
    return temp

def next_city(fringe, cost, city_map, destination, route, node, path_found):
    

    print('next' + str(path_found))
    if( len(fringe)==0):
        return

    

    current_city = fringe.pop(0)
    #print('node ' + str(node))
    #print(str(fringe) + '----------------')
    
    if(isVisited(current_city)):
        #print('going back to previous city')
        return
    route.append(current_city)
    if(current_city==destination):

        path_found = True
        print('path found = ' + str(path_found))
        print('destination reached, cost = ' + str(cost))
        print('route = ' + str(route))
        print('node expanded = ' + str(node))
        return True
    if(path_found):
        return True

    try:
        city_map[current_city]
    except:
        return
    
    sorted_city = sort(city_map[current_city])
    print('currently in ' + str(current_city) + ', cost = ' + str(cost))
    for city in city_map[current_city]:
        #if(not isVisited(city)):    


        fringe.insert(0, city)
        print(city + ' added into fringe')
    
    for i in range( len(city_map[current_city]) ):
        print(current_city + ' to ' + fringe[0])
        #print(str(fringe) + '~~~~~~~~~~~~~~~~')


 
    return next_city(fringe, cost+int(city_map[current_city][fringe[0]]), city_map, destination, route, node, path_found)

    

    
    
# depth first seach LIFO
def uninformed_search(city_map, source, destination):
    print('UNINFORMED')

    fringe = [source]
    route = []
    node = 0
    path_found = False
    #sort(city_map['Frankfurt'])
    result = next_city(fringe, 0, city_map, destination, route, node, path_found)
    
    
    #print_output(['City1', 'City2', 'City3', 'City4'], [0,0])
    
    if(result): # if found
        print('path found')
    else: # if not found
        print('path not found')
    




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



