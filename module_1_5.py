immutable_var = 1, True, 'string', 0.5
print(immutable_var)
# immutable_var[0] = 2 кортежи неизменяемые, потому что изменить можно списки. Это от природы такая двойственность
# print(immutable_var) ERROR!!!!
mutable_list = [1, False, 'string', 0.5]
mutable_list[0] = 9999
print(mutable_list)