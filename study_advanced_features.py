from collections import Iterable


# iteratable : 可执行for循环语句
# list tuple dict set str  are Iterable
print(isinstance('123', Iterable))

# generator : 也是Iterator，因为可执行next方法，但是生成器不是Iterable
L = [x * x for x in range(10)]
print(L)  # list
print(type(L))

g = (x * x for x in range(10))
print(g)  # generator


# Iterator : 可执行next方法, 它的作用是一次产生一个数据项，直到没有为止
# 迭代器是一个数据流，一直往前执行，直到执行到最后一个
# 调用iter()方法可将一个Iterable对象变为一个Iterator
print(iter('123'))

# 总结：凡是可以执行for循环的都是Iterable， 返回可执行next方法的都是Iterator
# generator即可执行for，也可执行next

