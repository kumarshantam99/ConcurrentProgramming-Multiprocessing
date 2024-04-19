import multiprocessing

squares=[]

def square_list(numlist,result,square_sum):

    for idx,val in enumerate(numlist):
        result[idx]=val*val

    square_sum.value=sum(result)

result=multiprocessing.Array('i',4)

square_sum=multiprocessing.Value('i')

if __name__ == '__main__':
    num_list=[1,2,3,4]
    p=multiprocessing.Process(target=square_list,args=(num_list,result,square_sum))
    p.start()
    p.join()

    print(list(result))
    print(square_sum.value)

    
"""
Restrictions: using shared memory between processes is restricted to data types coressponding to ctypes only.
Example we cannot use dictionary in shared space.
"""