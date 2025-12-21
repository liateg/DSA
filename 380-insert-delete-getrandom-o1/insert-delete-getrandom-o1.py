import random

class RandomizedSet:
    def __init__(self):
        self.d_list = [] 
        self.f_dic={}    

    def insert(self, val):
        if val in self.f_dic:
            return False
        self.f_dic[val]=len(self.d_list)
        self.d_list.append(val)
        return True
      

    def remove(self, val):
        if val not in self.f_dic:
            return False
        i=self.f_dic[val]
        self.d_list[i]=self.d_list[-1]
        del self.f_dic[self.d_list[-1]]
        self.f_dic[self.d_list[i]]=i
        self.d_list.pop()
        del self.f_dic[val]
        
        return True


       

    def getRandom(self):
        return random.choice(self.d_list)
