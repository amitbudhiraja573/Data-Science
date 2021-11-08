# We need to store both the values
'''
list_val=[[1,100],[4,12],[3,121]]
for i in list_val:
    if(i[0]==3):
        print(i[1])
'''


# Note - If we have a million records than this code is not efficient as the complexity = O(n)
# Best way to use the dictionary instead

# dict_val={1:100,4:12,3:121}
# print(dict_val[3])              # complexity O(1)

'''
class Hash_table:
    def __init__(self):
        self.Max=10
        self.arr=[None for i in range(self.Max)]

    def get_hash(self,key):
        count=0
        for i in key:
            count+=ord(i)
        return count % self.Max

    def __setitem__(self, key, value):
        h=self.get_hash(key)
        self.arr[h]=value

    def __getitem__(self, key):
        h=self.get_hash(key)
        if(self.arr[h]!=None):
            return self.arr[h]
        else:return None

    def __delitem__(self, key):
        h=self.get_hash(key)
        self.arr[h]=None

h=Hash_table()
h['march 9']=100
h['march 12']=12
print(h['march 12'])
'''

# Now implementing the hash table to solve collison

class Hash_table:
    def __init__(self):
        self.Max=10
        self.arr=[[] for i in range(self.Max)]

    def get_hash(self,key):
        count=0
        for i in key:
            count+=ord(i)
        return count % self.Max

    def __setitem__(self, key, value):
        h=self.get_hash(key)
        found=False
        for ind,element in enumerate(self.arr[h]):
            if(len(element)==2 and element[0]==key):
                found=True
                self.arr[h][ind]=value
        if not found:
            self.arr[h].append((key,value))


    def __getitem__(self, key):
        h=self.get_hash(key)
        for element in self.arr[h]:
            if(element[0]==key):
                return element[1]


    def __delitem__(self, key):
        h=self.get_hash(key)
        for ind,element in enumerate(self.arr[h]):
            if(element[0]==key):
                del self.arr[h][ind]



h=Hash_table()
h['march 17']=12
h['march 6']=10
h['march 1']=1
h['march 3']=23
h['march 9']=20
print(h.arr)
h.__delitem__('march 17')




# Using Channing
class Hash_table:
    def __init__(self):
        self.Max=10
        self.arr=[None for i in range(self.Max)]

    def get_hash(self,key):
        count=0
        for i in key:
            count+=ord(i)
        return count % self.Max

    def __setitem__(self, key, value):
        h=self.get_hash(key)
        if(self.arr[h]==None):
            self.arr[h]=(key,value)
            return
        else:
            index=self.get_index_empty(key)
            self.arr[index]=(key,value)

    def get_index_empty(self,key):
        h=self.get_hash(key)
        while(True):
            if(self.arr[h]==None):
                return h
            h=(h+1)%self.Max

    def __getitem__(self, key):
        h=self.get_hash(key)
        if(self.arr[h]!=None):
            while(True):
                if(self.arr[h][0]==key):
                    return self.arr[h][1]
                h=(h+1)%self.Max

        else:
            return None



    def __delitem__(self, key):
        h=self.get_hash(key)
        if(self.arr[h]!=None):
            while(True):
                if(self.arr[h][0]==key):
                    self.arr[h]=None
                    break
                h=(h+1)%self.Max



h=Hash_table()
h['march 6']=12
h['march 17']=20
h['march 12']=2000
print(h['march 6'])
h.__delitem__('march 17')
print(h.arr)