cdef extern from "struct_test.h":
    ctypedef struct myStruct:
        int a

    cdef void initStruct(myStruct *mst)
    cdef void showStruct(myStruct *mst)

def test_struct():
    cdef myStruct mst
    initStruct(&mst)
    showStruct(&mst)
    return mst

