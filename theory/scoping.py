# implicity python interpreter creates a hash table for each scope,
# such as module, class, function.

# module_scope = {
#    'var1': 'something'
#    'var2': 3.14
#    'funcA': ... code block ...,
#    'funcB': ... code block ...,
#    'name': "Nastya",
# }

var1 = "something"
var2 = 3.14

# global
# local

# 1. reading from variable
# 2. writing to variable

name = "Alex"


def funcA():
    global name
    # funcA_scope = {
    #    @parent = module_scope,
    #    'localVar1': "local value",
    #    'nestedFunc': ... code block ...,
    # }
    localVar1 = "local value"
    name = 'Nastya'
    print(name)

    def nestedFunc():
        # nestedFunc_scope = {
        #    @parent = funcA_scope,
        #    'nestedVar1': "haha",
        # }
        nestedVar1 = "haha"
        pass


def funcB():
    print(var2)


# lexical scoping vs dynamic scoping

numbers = 'one', 'two', 'three'
funcs = []
for n in numbers:
    funcs.append(lambda n=n: print(n))

for f in funcs:
    f()

# ------------------------------ inside python ---------------------------------

# scope_chain is a dict with extra field @parent
#
# def find_name(scope_chain, name):
#     while scope_chain is not None:
#         value = scope_chain[name]
#         if value is not None: return value
#         scope_chain = scope_chain.parent
#     raise NameError(f"name {name} is not defined")
