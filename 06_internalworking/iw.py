#internal working of python
#reference count -> in python there is a reference count which is not visibble obv but it is present 

# ex- a= 10 and a_score = 10 so here 10 has  12 reference count 
# in python  a= 10 iska matlab 10 memory mai gya hai naa ki a mai  a se to bas reference mai hai 

# a= 10 hai aur ab a = "rishabh " kardia to ab jo 10 hai usko garbage collector aayega aur leke jaayega   par yaha ek eception hai   ye a ko immediately collect nhi karta hai kaafi late karta hai


# note - h1=[1,2,3] h2=h1 [:] //yaha h2 mai slicing kari hai to vo h1 ki ek copy bana lega 
# aur agar humne ab h1 mai change kiya hai  to h2 same rahega pehle jaisa par agar slicing nhi hoti
# h1=[1,2,3]  h2= h1 kiya to h1 mai change pe h2 bhi change hoga 