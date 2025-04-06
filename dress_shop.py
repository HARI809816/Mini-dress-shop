class shop:
    all_products={'shirt':[20,399],'pant':[20,599],'shoes':[20,200]}
    

    def __init__(self,name,ph_no,location):
          self.name=name
          self.ph_no=ph_no
          self.location=location
          self.cart={}
    @classmethod
    def dis_all(cls):
         print()
         print('\t\t----------ALL PRODUCT IN SHOP----------')
         print()
         for product in cls.all_products:
              print("\t\t",product,cls.all_products[product][0],cls.all_products[product][1],sep="\t")
         print()
         print("\t\t------------XXXXX----------------")
         print()
     
    def main(self):
          
          print("\t\t===================****WELCOME****=======================")
          print()
          while True:
               print("\t\t -----------ENTER 1 TO DISPLAY ALL ITEMS-------------")
               print("\t\t -----------ENTER 2 TO DISPLAY YOUR DETAILS----------")
               print("\t\t -----------ENTER 3 TO ADD ITEMS IN YOUR CART--------")
               print("\t\t -----------ENTER 4 TO REMOVE ITEM FROM YOUR CART----")
               print("\t\t -----------ENTER 5 TO EXITE FROM SHOP---------------")
               print()
               print("\t\t\t------------XXXXX----------------")
               print()

               en=int(input("\t\tchoose any one : "))
               print()
               
               if en == 1:
                    self.dis_all()
               elif en == 2:
                    self.customer_details()
               elif en == 3:
                    self.add_product()
               elif en == 4:
                    self.remove_product()
               elif en == 5:
                    break

              
    def customer_details(self):
        print("\t\t============================")
        print("\t\tCUSTOMER NAME : ",self.name)
        print("\t\tPHONE NUMBER :",self.ph_no)
        print("\t\tLOCATION : ",self.location)
        if self.cart=={}:
             print()
             print("\t\tYOUR CART IS EMPTY")
             print()
             print("\t\t------------XXXXX----------------")
             print()
        else:
             tot=0
             print("\t\tTHE CUSTOMER CART IS : ")
             print("\t\t-----------------------")
             for i in self.cart:
                  tot+=self.cart[i][0]*shop.all_products[i][1]
                  print('\t',i,self.cart[i][0],shop.all_products[i][1],sep="\t")
             print()
             print("\t\tTHE TOTAL PRICE IS :",tot)
             print()
             print("\t\t------------XXXXX----------------")
             print()
    
    
    def add_product(self):
         print("\t\t===========================")
         a=input('\t\tENTER TYPE : ')
         b=int(input("\t\tENTER QUANTITY : "))
         if a  in self.all_products:
               if b > self.all_products[a][0]:
                    print("\t\tTHE GIVEN QUANTITY IS MORE GIVE LESS QUANTITY")
                    s1.add_product()
               self.cart[a]=[b]
               shop.all_products[a][0]-=b
               print("\t\t------------XXXXX----------------")
               print()
         else:
               print("\t\tTHIS PRODUCT IS NOT AVAILABLE")
               print()
               print("\t\t------------XXXXX----------------")
               print()
    def remove_product(self):
          print("\t\t===========================")
          p=input('\t\tENTER TYPE : ')
          q=int(input("\t\tENTER QUANTITY TO REMOVE: "))
          if p in self.all_products:
                if q > self.all_products[p][0]:
                    print("\t\tTHE GIVEN QUANTITY IS MORE GIVE LESS QUANTITY")
                    s1.remove_product
                self.cart[p][0]-=q
                shop.all_products[p][0]+=q
                print("\t\t------------XXXXX----------------")
                print()
          else:
               print("\t\tTHIS PRODUCT IS NOT IN YOUR CART")
               print()
               print("\t\t------------XXXXX----------------")
               print()

               
         
         
s1=shop("HARI",9089778865,"CHROMPET")
s1.main()
