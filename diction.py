# First, create a dictionary that consists of - id, name, class and subject integration of students. Then, write a program to retrieve unique entries and eliminate the rest
diction = {
    "id1": {
        "name": "you",
    "subject": "trigonometry",
    "class": "grade 5a"
    },
    "id2": {
        "name": "him",
    "subject": "calculus",
    "class": "grade 7a"
    },
    "id3": {
        "name": "car",
    "subject": "hahaha",
    "class": "grade catb"
    },
    "id4": {
        "name": "garnell",
    "subject": "four",
    "class": "grade x7(*2)//3"  
    
    }
}
print(len(diction))
for u in diction:
    print(u)
print((diction["id4"]))