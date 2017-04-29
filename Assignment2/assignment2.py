import sys
import re
import time

graphRE=re.compile("(\\d+)\\s(\\d+)")
edgeRE=re.compile("(\\d+)\\s(\\d+)\\s(-?\\d+)")

vertices=[]
edges=[]

def BellmanFord(G):
    pathPairs=[]
    # Fill in your Bellman-Ford algorithm here
    # The pathPairs list will contain the list of vertex pairs and their weights [((s,t),w),...]
    for j in vertices:
        distList = []  
        src = 0

        #step 1
        for i in vertices:
            distList.append(float("inf")) 
        #end for 
        distList[src] = 0  
        
        #step 2
        #i = from, e = to
        for i in range(0, len(vertices) -1):   
            for v in range(0, len(vertices)): 
                for e in range(0, len(edges)): 
                    if distList[v] + float(G[1][v][e]) < distList[e]: 
                        distList[e] = distList[v] + float(G[1][v][e])
                        s = v+1 
                        t = e+1
                        element = '(('+ str(s) + ',' + str(t) +'),' + str(distList[e]) + ')'
                        pathPairs.append(element)
                    #end if
                #end for
            #end for
        #end for
        #print pathPairs
        #print distList

        #step 3
        for v in range(0, len(vertices)): 
            for e in range(0, len(edges)):
                if distList[i] + float(G[1][i][e]) < distList[e]: 
                    print "Graph contains negative weight cycle"   
                #end if
            #end for
        #end for
    #end for 
    return pathPairs

def FloydWarshall(G):
    pathPairs=[]
    # Fill in your Floyd-Warshall algorithm here
    # The pathPairs list will contain the list of vertex pairs and their weights [((s,t),w),...]
    pathPairs = G

    for i in range(len(vertices)):
        for j in range(len(vertices)):
            for k in range(len(vertices)): 
                pathPairs[1][j][k] = min(float(pathPairs[1][j][k]), float(pathPairs[1][j][i]) + float(pathPairs[1][i][k]))
    return pathPairs
    
def readFile(filename):
    global vertices
    global edges
    # File format:
    # <# vertices> <# edges>
    # <s> <t> <weight>
    # ...
    inFile=open(filename,'r')
    line1=inFile.readline()
    graphMatch=graphRE.match(line1)
    if not graphMatch:
        print(line1+" not properly formatted")
        quit(1)
    vertices=list(range(int(graphMatch.group(1))))
    edges=[]
    for i in range(len(vertices)):
        row=[]
        for j in range(len(vertices)):
            row.append(float("inf"))
        edges.append(row)
    for line in inFile.readlines():
        line = line.strip()
        edgeMatch=edgeRE.match(line)
        if edgeMatch:
            source=edgeMatch.group(1)
            sink=edgeMatch.group(2)
            if int(source) > len(vertices) or int(sink) > len(vertices):
                print("Attempting to insert an edge between "+source+" and "+sink+" in a graph with "+vertices+" vertices")
                quit(1)
            weight=edgeMatch.group(3)
            edges[int(source)-1][int(sink)-1]=weight
    return (vertices,edges)

def main(filename,algorithm):
    algorithm=algorithm[1:]
    G=readFile(filename)
    # G is a tuple containing a list of the vertices, and a list of the edges
    # in the format ((source,sink),weight)
    if algorithm == 'b' or algorithm == 'B':
        start=time.time()
        BellmanFord(G)
        end=time.time() 
        BFTime = end-start
        print("Bellman-Ford timing: "+str(BFTime)) 
    if algorithm == 'f' or algorithm == 'F':
        FloydWarshall(G)
    if algorithm == "both":
        start=time.time()
        BellmanFord(G)
        end=time.time()
        BFTime=end-start
        start=time.time()
        FloydWarshall(G)
        end=time.time()
        FWTime=end-start
        print("Bellman-Ford timing: "+str(BFTime))
        print("Floyd-Warshall timing: "+str(FWTime))

    #print G[1][0][1]
    #Debugging
    #for i in G:
        #print(i)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("python assignment2.py -<f|b> <input_file>")
        quit(1)
    if len(sys.argv[1]) < 2:
        print('python assignment2.py -<f|b> <input_file>')
        quit(1)
    main(sys.argv[2],sys.argv[1])

