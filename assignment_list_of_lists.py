import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(uni):
    se = []
    tf = []
    for each in uni:
        se.append(each[1])
        tf.append(each[2])
    return se, tf


def mean(datapoints):
    return sum(datapoints) / len(datapoints)


def middle(info):
    return statistics.median(info)


my_enrollment_stats = enrollment_stats(universities)
se_data = my_enrollment_stats[0]
tf_data = my_enrollment_stats[1]

print("Total students: ", sum(se_data))
print("Total tuition: $", sum(tf_data))

print("Student mean: ", round(mean(se_data)))
print("Student median: ", middle(se_data))

print("Tuition mean: $", round(mean(tf_data)))
print("Tuition median: $", middle(tf_data))
