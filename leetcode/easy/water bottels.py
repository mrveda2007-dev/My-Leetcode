class water:
    def drink(self,drinkable_bottels,Exchangebottels):
        empty = 0
        count = 0
        while drinkable_bottels != 0:
            for i in range(drinkable_bottels):
                drinkable_bottels-=1
                count+=1
                empty+=1
            while empty >= Exchangebottels:
                empty -= Exchangebottels
                drinkable_bottels +=1
        return count

drinkable_bottels=int(input("num bottels:"))
Exchangebottels=int(input("exchangeable bottel count:"))

w = water()
print(w.drink(drinkable_bottels,Exchangebottels))






