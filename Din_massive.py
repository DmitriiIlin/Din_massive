import ctypes,math
class DynArray:
    
    def __init__(self):
        self.count = 0
        self.capacity = 16
        self.array = self.make_array(self.capacity)

    def __len__(self):
        return self.count

    def make_array(self, new_capacity):
        return (new_capacity * ctypes.py_object)()

    def __getitem__(self,i):
        if i < 0 or i >= self.count:
            raise IndexError('Index is out of bounds')
        return self.array[i]

    def resize(self, new_capacity):
        new_array = self.make_array(new_capacity)
        for i in range(self.count):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity 

    def append(self, itm):
        if self.count == self.capacity:
            self.resize(2*self.capacity)
        self.array[self.count] = itm
        self.count += 1

    def insert(self,i,itm):
        new_capacity=self.capacity
        if (self.count+1)>=self.capacity:
            new_capacity=2*self.capacity
           # self.resize(new_capacity)
        new_array=self.make_array(new_capacity)
        if i < 0 or i >= (self.count):
            raise IndexError('Index is out of bounds')
        for j in range(self.count):
            new_array[j]=self.array[j]
            if (i==j):
                new_array[j]=itm
                for jj in range(j+1,self.count+1):
                    new_array[jj]=self.array[jj-1]
                break
        self.array=new_array
        self.count+=1

    def delete(self,i):
        new_capacity=self.capacity
        if (2*(self.count-1))<=self.capacity:
            new_capacity=math.ceil(self.capacity/2)
            if self.capacity<16:
                self.capacity=16
        new_array=self.make_array(new_capacity)
        if i < 0 or i >= (self.count):
            raise IndexError('Index is out of bounds')
        for j in range(self.count):
            new_array[j]=self.array[j]
            if (j==i):
                for jj in range(j,self.count-1):
                    new_array[jj]=self.array[jj+1]
                break
        self.array=new_array
        self.count-=1    








da=DynArray()
for i in range(4):
    da.append(i)
    print(da[i])
    print("*****")
da.insert(3,44)
print(da.__len__(),'lenght')

print('**insert 44**')
for i in range(da.__len__()):
    print(da[i])

da.insert(3,446)
print('**446**')
for i in range(da.__len__()):
    print(da[i])
print('***delete 2***')
print(da.__len__(),'lenght before delete')
da.delete(2)
print(da.__len__(),'lenght after delete')
for i in range(da.__len__()):
    print(da[i])
print('******')
da.delete(3)
print(da.__len__(),'lenght after delete second time')
for i in range(da.__len__()):
    print(da[i])
print('******')
