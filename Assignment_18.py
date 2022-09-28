#1. Write a python program to create and print a dictionary which stores your information.(name, age, gender …..)
my_self={"name":'Soumik',"age":'17',"gender":'male'}
print(my_self)
#2. Write a python program to access the items of a dictionary by referring to its key name.
person={"name":'Rohit',"country":'IND',"mobile no.":12364789}
print(person["name"])
print(person.get("mobile no."))
#3. Write a python program to get a list of the values from a dictionary.
st_data={"name":"soumik","class":12,"marks_11":'89_persentage'}
print(*st_data.values())#list(st_data.values())
#4. Write a python program to change the value of a specific item by referring to its key name.
person={"name":'Mohit',"country":'USA',"mobile no.":987456321}
person["name"]="Rahul"#person.update({"name":'Rahul'})
print(person)
#5. Write a python program to print all key names in the dictionary, one by one.
house={"color":'White',"Room":8,"playground":1}
for key in house:
    print(key)
#6. Write a python program to create a dictionary that contains three dictionaries.(nested)
person={'person':{"name":'Rohit',"gender":'male',"age":28,"mobile no.":12364789},'company':{"1st":'Google',"2nd(now)":"TATA"},'address':{"Country":"India","State":"Bengal","City":"BUrdwan"}}
print(person)
#7. Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.
rohit={"name":'Rohit',"country":'IND',"mobile no.":12364789}
mohit={"name":'Mohit',"country":'USA',"mobile no.":987456321}
rahul={'name': 'Rahul', 'country': 'CANADA', 'mobile no.': 789456123}
class_12={'student1':rohit,'student2':mohit,"student3":rahul}
print(class_12)
print("Student 2 name ",class_12["student3"]["name"])    
print("Student 3 mobile_no ",class_12["student3"]["mobile no."])    
#8. Write a python program to convert two lists into a dictionary in a way that item from
#list1 is the key and item from list2 is the value.
lst1=['rohit','soham','kali']
lst2=['Bengal','Bihar','Delhi']
d=dict(zip(lst1,lst2))
print(d)
#9. Write a python program to merge two python dictionaries into one dictionary.
rohit={"name":'Rohit',"gender":'male',"age":28,"mobile no.":12364789}
address={"Country":"India","State":"Bengal","City":"BUrdwan"}
person={'person':rohit,'address':address}
print(person)
#10. Write a python program to get the key of lowest value from the dictionary.
#sample_dict = {'C': 92,'Java': 66,'Python': 85}

sample_dict = {'C': 92,'Java': 66,'Python': 85}
val=min(sample_dict.values())
[print("the key of lowest value from the dictionary=",key) for key in sample_dict if sample_dict[key]==val]



