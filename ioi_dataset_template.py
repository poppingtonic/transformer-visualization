import random
from names import PERSON, OBJECTS, PLACES


objects = [] # 20
places = [] # 20

templates = [
    "Then, {B} and {A} went to the {PLACE}. {B} gave a {OBJECT} to {A}",
    "Then, {B} and {A} had a lot of fun at the {PLACE}. {B} gave a {OBJECT} to {A}",
    "Then, {B} and {A} were working at the {PLACE}. {B} decided to give a {OBJECT} to {A}",
    "Then, {B} and {A} were thinking about going to the {PLACE}. {B} wanted to give a {OBJECT} to {A}",
    "Then, {B} and {A} had a long argument, and afterwards {B} said to {A}",
    "After {B} and {A} went to the {PLACE}, {B} gave a {OBJECT} to {A}",
    "When {B} and {A} got a {OBJECT} at the {PLACE}, {B} decided to give it to {A}",
    "When {B} and {A} got a {OBJECT} at the {PLACE}, {B} decided to give the {OBJECT} to {A}",
    "While {B} and {A} were working at the {PLACE}, {B} gave a {OBJECT} to {A}",
    "While {B} and {A} were commuting to the {PLACE}, {B} gave a {OBJECT} to {A}",
    "After the lunch, {B} and {A} went to the {PLACE}. {B} gave a {OBJECT} to {A}",
    "Afterwards, {B} and {A} went to the {PLACE}. {B} gave a {OBJECT} to {A}",
    "Then, {B} and {A} had a long argument. Afterwards {B} said to {A}",
    "The {PLACE} {B} and {A} went to had a {OBJECT}. {B} gave it to {A}",
    "Friends {B} and {A} found a {OBJECT} at the {PLACE}. {B} gave it to {A}",
]
templates = [
    "Then, {A} and {B} went to the {PLACE}. {B} gave a {OBJECT} to {A}",
    "Then, {A} and {B} had a lot of fun at the {PLACE}. {B} gave a {OBJECT} to {A}",
    "Then, {A} and {B} were working at the {PLACE}. {B} decided to give a {OBJECT} to {A}",
    "Then, {A} and {B} were thinking about going to the {PLACE}. {B} wanted to give a {OBJECT} to {A}",
    "Then, {A} and {B} had a long argument, and afterwards {B} said to {A}",
    "After {A} and {B} went to the {PLACE}, {B} gave a {OBJECT} to {A}",
    "When {A} and {B} got a {OBJECT} at the {PLACE}, {B} decided to give it to {A}",
    "When {A} and {B} got a {OBJECT} at the {PLACE}, {B} decided to give the {OBJECT} to {A}",
    "While {A} and {B} were working at the {PLACE}, {B} gave a {OBJECT} to {A}",
    "While {A} and {B} were commuting to the {PLACE}, {B} gave a {OBJECT} to {A}",
    "After the lunch, {A} and {B} went to the {PLACE}. {B} gave a {OBJECT} to {A}",
    "Afterwards, {A} and {B} went to the {PLACE}. {B} gave a {OBJECT} to {A}",
    "Then, {A} and {B} had a long argument. Afterwards {B} said to {A}",
    "The {PLACE} {A} and {B} went to had a {OBJECT}. {B} gave it to {A}",
    "Friends {A} and {B} found a {OBJECT} at the {PLACE}. {B} gave it to {A}",
]
def gen_person_a() -> List[str]:
    """randomly select 50 names from PERSON and put them in variable A, without repeats
    """
    A = []
    while len(A) < 50:
        name = random.choice(PERSON)
        if name not in A:
            A.append(name)
    return A

def gen_person_b(A: List[str]) -> List[str]:
    """randomly select 50 names from PERSON and put them in variable B, without repeats in A
    """
    B = []
    while len(B) < 50:
        name = random.choice(PERSON)
        if name not in A and name not in B:
            B.append(name)
    return B

person_a_names = gen_person_a() # 50
person_b_names = gen_person_b(person_a_names) # 50

def generate_names(inp: list[str]):
    """
    Generate 20 common object names and a way to select them randomly without repeats
    """
    random.shuffle(names)
    return names

def get_name(names):
    """
    Get a name from the list of names
    """
    
    if len(names) == 0:
        return None
    else:
        return names.pop()

for template in templates:
    print(template.format(A=random.choice(person_a_names),
                          B=random.choice(person_b_names),
                          OBJECT=random.choice(OBJECTS),
                          PLACE=random.choice(PLACES))
         )