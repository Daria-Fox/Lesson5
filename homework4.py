immutable_var = (1, 5, "hello", 1.5, "love")
print(immutable_var)
#значения элементов immutable_var нельзя изменить, т.к. эта переменная
#является кортежем, следовательно элементы в ней неизменяемы
mutable_list = [2, 6, "hi", 2.5, "big love"]
mutable_list[2] = ("ok")
mutable_list[3] = (15.9)
print(mutable_list)