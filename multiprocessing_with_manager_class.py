## This takes care of any python data type. But is slower than shared memory implementation

import multiprocessing
def get_data(data_list):
    for data in data_list:
        print(f"Name: {data[0]},\nScore: {data[1]}")

def add_data(new_data,data_list):
    data_list.append(new_data)
    print('New Data added!')

if __name__ == '__main__':
    with multiprocessing.Manager() as manager:
        database=(manager.list([('Abby',90),('Kumar',92),('Shantam',20)]))
        new_data=('Leroy',76)
        p1=multiprocessing.Process(target=add_data,args=(new_data,database))
        p2=multiprocessing.Process(target=get_data,args=(database,))
        p1.start()
        p2.start()

        p1.join()
        p2.join()

        print('Data right now: ',database)

