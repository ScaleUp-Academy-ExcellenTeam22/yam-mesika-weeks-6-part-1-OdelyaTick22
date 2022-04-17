def my_filter(function, iterable):
    for item in iterable:
        if function(item):
            yield item


if __name__ == '__main__':
    def is_mature(age):
        return age >= 18


    ages = [0, 1, 4, 10, 20, 35, 56, 84, 120]
    mature_ages = my_filter(is_mature, ages)
    print(tuple(mature_ages))
