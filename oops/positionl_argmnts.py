#==> *args---passed parameters accept as tuple
#==> **kwargs----passed parameters accept as dictionary
#===========================================================

# def create_person(*args):
#     print(args)

# create_person("anu",25,"tvm","ekm")

#============================================================

def create_person(**kwargs):
    print(kwargs)

create_person(name="hari",age=26,n_place="tvm",w_place="ekm")