                                                   #pyramid pattern problem with f string

#normal pyramid
print("\innormal pyramid")
for i in range(5):
    x='* '
    x=x*i
    print(f'{x:^10}')

# invert pyramid
print("\invert pyramid\n")
for i in range(5):
    x='* '
    x=x*(5-i)
    print(f'{x:^10}')

# left sided pyramid

print("\nleft sided pyramid")
for i in range(5):
    x='* '
    x=x*i
    print(f'{x:<10}')


# right sided pyramid

print("\nright sided pyramid")
for i in range(5):
    x='* '
    x=x*i
    print(f'{x:>10}')


#using string to do python pattern
    my_string="celsi"
    x=0
    for i in my_string:
        x=x+1
        print(my_string[0:x])
for i in my_string:
    x=x-1
    print(my_string[0:x])
