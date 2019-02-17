
import csv
import math
from operator import itemgetter
x_train =[]
y_train = []
test_data =[]
def data_clean():
    with open("akk.csv",encoding='utf-8-sig') as csvfile:
        rows = csv.reader(csvfile,delimiter=',')
        data = [data for data in rows]


    for x in range(len(data)):
        ins = []
        for y in range(3):
            ins.append(data[x][y])
        y_train.append(data[x][y+1])
        x_train.append(ins)


    with open("test.csv",encoding='utf-8-sig') as csvfile:
        rows = csv.reader(csvfile,delimiter=',')
        dota = [dota for dota in rows]

    for x in range(len(dota)):
        ins = []
        for y in range(3):
            ins.append(dota[x][y])

        test_data.append(ins)




def calculate_distance(x,y):
    dist = 0

    for i in range(len(y)):


        dist += pow((int(y[i]) - int(x[i])), 2)

    return math.sqrt(dist)

def k_nearest_neighbors(k,x_train,y_train,test_data):
    data_clean()

    rank = []
    neighbour = []

    for i in range(len(x_train)):

        distance = calculate_distance(test_data[0],x_train[i])

        rank.append([distance,y_train[i]])


    rank.sort(key=itemgetter(0))
    print("rank is,", rank)
    count_m = 0
    count_w = 0
    for i in range(k):
        #print("i+1 is ",i+1)
        neighbour.append([i+1,rank[i][1]])
        print("rank[i][1]",rank[i][1])
        if(rank[i][1] == 'M'):
            count_m += 1
        else:
            count_w += 1
    print("count of male for given k value  is",count_m)
    print("count of female for given k value is",count_w)
    if count_m > count_w:
        result = " The test data is classified as M(male)"
        return result

    else:
        result = " The test data is classified as W(female)"
    return result






res = k_nearest_neighbors(1,x_train,y_train,test_data)
print(res)
