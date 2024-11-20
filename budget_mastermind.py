# Goal create a buget tracker

def prompt_user() -> str:
    money:str = input("Please enter an amount ($) and specify if it is an income or an expense !\nAs an example: 54 income.\n").lower()
    source: str = input("What is the source (for income) or the category (for expenses) of the specified amount ? ")
    get_out: str = input("Would you like to finish entering amounts ? (yes/no): ")
    return money, source, get_out


def fill_dictionnaries(target_dict:dict, source: str, money:str) -> None:
    if target_dict.get(source):
        target_dict[source].append(float(money.split()[0]))
    else:
        list_temp = []
        list_temp.append(float(money.split()[0]))
        target_dict[source] = list_temp

def calculate_total(target_dict:dict) -> int:
    multiple = []
    single = 0
    for key, value in target_dict.items():
        if isinstance(value, list):
            multiple += value
        else:
            single += value
    return sum(multiple) + single

is_on = True

income = dict()
expenses = dict()

while is_on:
    money, source, get_out = prompt_user()

    if get_out == "yes":
        is_on = False
    try:
        if money.split()[1] == "income":
            fill_dictionnaries(income, source, money)
        else:
            fill_dictionnaries(expenses, source, money)
    except Exception as e:
        print(f"The error is {e}")
        break


total_income = calculate_total(income)
total_expenses = calculate_total(expenses)

print(f"Your total balance is {total_income-total_expenses}")

# a nice addition would be to store everything in a file or database 