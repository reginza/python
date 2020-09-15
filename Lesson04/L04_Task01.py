import sys
# from Lesson04 import my_mod

def calculate(output_in_hours, one_hours, prize):
    try:
        output_in_hours = float(output_in_hours)
        one_hours = float(one_hours)
        prize = float(prize)
        return (output_in_hours * one_hours) + prize
    except TypeError:
        return


file, output_in_hours, one_hours, prize = sys.argv

# print(my_mod.calculate(int(output_in_hours), int(one_hours), int(prize)))
print(calculate(int(output_in_hours), int(one_hours), int(prize)))
