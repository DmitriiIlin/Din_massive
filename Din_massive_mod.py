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

    def insert(self,i,itm):
        new_array=self.make_array(self.capacity)
        if (self.count)>=self.capacity:
            self.resize(2*self.capacity)
            new_array=self.make_array(2*self.capacity)
        if i < 0 or i >(self.count):
            raise IndexError('Index is out of bounds')
        for j in range(self.count+1):
            if (i==j):
                new_array[j]=itm
                for jj in range(j+1,self.count+1):
                    new_array[jj]=self.array[jj-1]
                break
            new_array[j]=self.array[j]
        self.array=new_array
        self.count+=1
    
    def append(self,itm):
        self.insert(self.count,itm)

    def delete(self,i):
        new_capacity=self.capacity
        if (2*(self.count-1))<=self.capacity and self.capacity>16:
            new_capacity=int(self.capacity/2)
        else:
            self.capacity=16
            new_capacity=self.capacity
        new_array=self.make_array(new_capacity)
        if i < 0 or i >= (self.count):
            raise IndexError('Index is out of bounds')
        for j in range(self.count-1):
            new_array[j]=self.array[j]
            if (j==i):
                for jj in range(j,self.count-1):
                    new_array[jj]=self.array[jj+1]
                break
        self.array=new_array
        self.count-=1
        self.resize(new_capacity)
           
