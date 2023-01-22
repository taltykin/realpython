universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500] 
]



def enrollment_stats(universities):
    enrolled_list = []
    payment_list = []
    for item in universities:
        enrolled_list.append(item[1])
        payment_list.append(item[2])

    return enrolled_list, payment_list

totals = enrollment_stats(universities)


def mean(values):
    return (sum(values)) / len(values)

def median(values):
    values.sort()
    if len(values) % 2 == 1:
        center_index = int(len(values) / 2)
        return values[center_index]        
    else:
        right_index = len(values) + 1 // 2
        left_index = len(values) - 1 // 2
    return mean([values[left_index], values[right_index]])


# mean(enrolled_list, payment_list)
# median(enrolled_list, payment_list)

print(f"Total students: {sum(totals[0])}")
print(f"Total tuition: $ {sum(totals[1])}")
print(f"Student mean: {mean(totals[0])}")
print(f"Student median: {median(totals[0])}")
print(f"Tuition mean: {mean(totals[1])}")
print(f"Tuition median: {median(totals[1])}")
# print(f"Student mean: {avg_student}")