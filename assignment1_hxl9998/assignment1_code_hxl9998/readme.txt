Name: Hoang Luu
UTA ID: 1000969998
Programming Language: Python3, not yet tested on Omega

Code structure:
main():
    get user inputs and decide if it is valid for Uninformed or Informed search
    call read_map() to extract all path inside an input file, return as dictionary
    call either Informed or Uninformed search

read_map():
    take an input file name as parameter
    scan through the file and add the cities and its route to a dictionary
    return the dictionary

informed_search():
    city routes, source, destination, and h_file as input
    does not do anything, not yet implement

uninformed_search():
    city routes, source, and destination
    call uniform_cost_search()
    if uniform_cost_search() return success
        call extract_route() to extract all routes from the returned nested list
        print out results (routes and cost)
    else if it return -1
        print out results (no path found)

uniform_cost_search():
    take in city routes, source, destination, fringe, visited, and path
    perform uniform_cost_search by calling itself recursively
    add its current cost and route into fringe and/or visited
    also keep track of how many node visited and generated
    when destination is reached,
        return fringe and number of node visited and generated
    if destination is not reached (aka no path found)
        it return -1, and number of node visited and generated

extract_route():
    take in nested route list
    recursively calling itself to extract each layer of the nested route list
    return the extracted route as a list

To run the code:
python3 find_route.py [input_file] [source] [destination] [h_file]

NOTE:
    I did not do the extra credit for this assignment
    But it will handle when h_file is given
