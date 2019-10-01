from django.shortcuts import render
from django.db import transaction

from .models import Group

# Create your views here.

app_prefix = "transaction 1 -"

def save_with_exception(request):
    g1=Group()
    s_info = 'save with exception'
    g1.name='%s %s' % (app_prefix,s_info)
    g1.save()

    raise Exception("Error")
    # g1 is not stored to db

def save_without_exception(request):
    g1=Group()
    s_info = 'save without exception'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()
    # g1 is stored to db

@transaction.non_atomic_requests # ignore atomic request for this view
def non_atomic(request):
    g1=Group()
    s_info = 'non atomic request'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    raise Exception("Error")
    # g1 is stored to db

def save_outside():
    g1=Group()
    s_info = 'save outside'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

def outside(request):
    save_outside()
    raise Exception("Error")
    # g1 is not stored to db

def exception_in_try_except_block(request):
    try:
        g1=Group()
        s_info='exception in try except block'
        g1.name='%s %s' % ( app_prefix, s_info)
        g1.save()

        raise Exception("Error")
    except:
        pass

    #g1 is stored to db

def outer_inner_1(request):
    g1=Group()
    s_info='outer transaction no exception 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic(): # context manager
            g2=Group()
            s_info='inner transaction with exception 1'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()
            raise Exception("Error") #this obj is not stored to db
    except:
        pass

    #g1 is stored to db
    #g2 is not stored to db

def outer_inner_2(request):
    g1=Group()
    s_info = 'outer transaction no exception 2'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic(): # context manager
            g2=Group()
            s_info = 'inner transaction with exception 2'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()

        raise Exception("Error")
    except:
        pass

    #g1, g2 are stored to db

def atomic_1(resquest):
    g1=Group()
    s_info = 'atomic_1 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    with transaction.atomic():
        g2=Group()
        s_info = 'atomic_1 save 2'
        g2.name='%s %s' % ( app_prefix, s_info)
        g2.save()

    g3=Group()
    s_info = 'atomic_1 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    #g1, g2, g3 are stored to db

def atomic_2(resquest):
    g1=Group()
    s_info = 'atomic_2 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            s_info = 'atomic_2 save 2'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()

            raise Exception("Error")
    except Exception as e:
        pass

    g3=Group()
    s_info = 'atomic_2 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    #g1, g3 are stored to db
    #g2 is not stored to db

def atomic_3(resquest):
    g1=Group()
    s_info = 'atomic_3 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            s_info = 'atomic_3 save 2'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()

            raise Exception("Error 1")
    except Exception as e:
        pass

    g3=Group()
    s_info = 'atomic_3 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    raise Exception("Error 2")

    # g1, g2, g3 are not stored to db

def atomic_4(resquest):
    g1=Group()
    s_info = 'atomic_4 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    with transaction.atomic():
        g2=Group()
        s_info = 'atomic_4 save 2'
        g2.name='%s %s' % ( app_prefix, s_info)
        g2.save()

    g3=Group()
    s_info = 'atomic_4 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    raise Exception("Error 2")

    # g1, g2, g3 are not stored to db

def atomic_5(resquest):
    g1=Group()
    s_info = 'atomic_5 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            s_info = 'atomic_5 save 2'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()

        raise Exception("Error 1")
    except Exception as e:
        pass

    g3=Group()
    s_info = 'atomic_5 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    # g1, g2, g3 are stored to db

@transaction.atomic
def atomic_6(resquest):
    g1=Group()
    s_info = 'atomic_6 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    with transaction.atomic():
        g2=Group()
        s_info = 'atomic_6 save 2'
        g2.name='%s %s' % ( app_prefix, s_info)
        g2.save()

    g3=Group()
    s_info = 'atomic_6 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    # g1, g2, g3 are stored to db

@transaction.atomic
def atomic_7(resquest):
    g1=Group()
    s_info = 'atomic_7 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            s_info = 'atomic_7 save 2'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()

            raise Exception("Error")
    except Exception as e:
        pass

    g3=Group()
    s_info = 'atomic_7 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    #g1, g3 are stored to db
    #g2 is not stored to db

@transaction.atomic
def atomic_8(resquest):
    g1=Group()
    s_info = 'atomic_8 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    try:
        with transaction.atomic():
            g2=Group()
            s_info = 'atomic_8 save 2'
            g2.name='%s %s' % ( app_prefix, s_info)
            g2.save()

            raise Exception("Error 1")
    except Exception as e:
        pass

    g3=Group()
    s_info = 'atomic_8 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    raise Exception("Error 2")

    #g1, g2, g3 are not stored to db

@transaction.atomic
def atomic_9(resquest):
    g1=Group()
    s_info = 'atomic_9 save 1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    with transaction.atomic():
        g2=Group()
        s_info = 'atomic_9 save 2'
        g2.name='%s %s' % ( app_prefix, s_info)
        g2.save()

    g3=Group()
    s_info = 'atomic_9 save 3'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    raise Exception("Error 2")

    #g1, g2, g3 are not stored to db

def autocommit_1(request):
    autocommit_flag = transaction.get_autocommit()
    print("auto commit state : %s" % (autocommit_flag,))
    transaction.set_autocommit(autocommit_flag)

@transaction.non_atomic_requests
def autocommit_2(request):
    autocommit_flag = transaction.get_autocommit()
    print("auto commit state : %s" % (autocommit_flag,))
    #transaction.set_autocommit(autocommit_flag)

def autocommit_3(request):
    autocommit_flag = transaction.get_autocommit()
    print("auto commit state : %s" % (autocommit_flag,))
    #transaction.set_autocommit(autocommit_flag)
    g1=Group()
    s_info = 'autocommit 3'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

@transaction.non_atomic_requests
def autocommit_4(request):
    autocommit_flag = transaction.get_autocommit()
    print("auto commit state : %s" % (autocommit_flag,))
    transaction.set_autocommit(False)
    autocommit_flag2 = transaction.get_autocommit()
    print("auto commit state : %s" % (autocommit_flag2,))

@transaction.non_atomic_requests
def autocommit_5(request):
    autocommit_flag = transaction.get_autocommit()
    print("auto commit state : %s" % (autocommit_flag,))

@transaction.non_atomic_requests
def autocommit_6(request):
    autocommit_stat = transaction.get_autocommit()
    print("autocommit status : %s" % (autocommit_stat,)) # autocommit could be True or False

    with transaction.atomic():
        autocommit_stat2 = transaction.get_autocommit()
        print("autocommit status : %s" % (autocommit_stat2,)) # in atomic block, autocommit is always False

@transaction.non_atomic_requests
def transaction_1(request):
    autocommit_flag = transaction.get_autocommit()
    if autocommit_flag:
        transaction.set_autocommit(False)

    g1=Group()
    s_info = 'transaction_1 a'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    g2=Group()
    s_info = 'transaction_1 b'
    g2.name='%s %s' % ( app_prefix, s_info)
    g2.save()
    transaction.commit()

    g3=Group()
    s_info = 'transaction_1 c'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    g4=Group()
    s_info = 'transaction_1 d'
    g4.name='%s %s' % ( app_prefix, s_info)
    g4.save()
    transaction.rollback()

    g5=Group()
    s_info = 'transaction_1 e'
    g5.name='%s %s' % ( app_prefix, s_info)
    g5.save()

    g6=Group()
    s_info = 'transaction_1 f'
    g6.name='%s %s' % ( app_prefix, s_info)
    g6.save()
    transaction.commit()

    if autocommit_flag:
        transaction.set_autocommit(autocommit_flag)

    # g1, g2, g5, g6 are saved
    # g3, g4 are not saved

@transaction.atomic
def savepoint_1(request):
    #transaction.set_autocommit(False) #forbidden when atomic block is active
    #transaction.set_autocommit(True) #forbidden when atomic block is active
    autocommit_flag = transaction.get_autocommit()
    print("autocommit state : %s" % (autocommit_flag,))

    sid1 = transaction.savepoint()

    g1=Group()
    s_info = 'savepoint_1 a'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    g2=Group()
    s_info = 'savepoint_1 b'
    g2.name='%s %s' % ( app_prefix, s_info)
    g2.save()

    transaction.savepoint_commit(sid1)

    sid2 = transaction.savepoint()

    g3=Group()
    s_info = 'savepoint_1 c'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    g4=Group()
    s_info = 'savepoint_1 d'
    g4.name='%s %s' % ( app_prefix, s_info)
    g4.save()

    transaction.savepoint_rollback(sid2)

    sid3 = transaction.savepoint()

    g5=Group()
    s_info = 'savepoint_1 e'
    g5.name='%s %s' % ( app_prefix, s_info)
    g5.save()

    g6=Group()
    s_info = 'savepoint_1 f'
    g6.name='%s %s' % ( app_prefix, s_info)
    g6.save()

    transaction.savepoint_commit(sid3)

    transaction.clean_savepoints()

    # g1, g2, g5, g6 are saved
    # g3, g4 are not saved

@transaction.atomic
def savepoint_2(request):
    autocommit_flag = transaction.get_autocommit()
    print("autocommit state : %s" % (autocommit_flag,))

    rollback_stat = transaction.get_rollback()
    print("rollback status : %s" % (rollback_stat,))

    sid1 = transaction.savepoint()

    g1=Group()
    s_info = 'savepoint_2 a'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    g2=Group()
    s_info = 'savepoint_2 b'
    g2.name='%s %s' % ( app_prefix, s_info)
    g2.save()

    transaction.savepoint_commit(sid1)

    sid2 = transaction.savepoint()

    g3=Group()
    s_info = 'savepoint_2 c'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    g4=Group()
    s_info = 'savepoint_2 d'
    g4.name='%s %s' % ( app_prefix, s_info)
    g4.save()

    transaction.savepoint_rollback(sid2)

    sid3 = transaction.savepoint()

    g5=Group()
    s_info = 'savepoint_2 e'
    g5.name='%s %s' % ( app_prefix, s_info)
    g5.save()

    g6=Group()
    s_info = 'savepoint_2 f'
    g6.name='%s %s' % ( app_prefix, s_info)
    g6.save()

    transaction.savepoint_commit(sid3)

    transaction.clean_savepoints()

    raise Exception("Error")

    # no object is saved

@transaction.non_atomic_requests
def savepoint_3(request):
    autocommit_flag = transaction.get_autocommit()
    print("autocommit state : %s" % (autocommit_flag,))

    sid1 = transaction.savepoint()

    g1=Group()
    s_info = 'savepoint_3 a'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    g2=Group()
    s_info = 'savepoint_3 b'
    g2.name='%s %s' % ( app_prefix, s_info)
    g2.save()

    transaction.savepoint_commit(sid1)

    sid2 = transaction.savepoint()

    g3=Group()
    s_info = 'savepoint_3 c'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    g4=Group()
    s_info = 'savepoint_3 d'
    g4.name='%s %s' % ( app_prefix, s_info)
    g4.save()

    transaction.savepoint_rollback(sid2) # not working since autocommit is active

    sid3 = transaction.savepoint()

    g5=Group()
    s_info = 'savepoint_3 e'
    g5.name='%s %s' % ( app_prefix, s_info)
    g5.save()

    g6=Group()
    s_info = 'savepoint_3 f'
    g6.name='%s %s' % ( app_prefix, s_info)
    g6.save()

    transaction.savepoint_commit(sid3)

    transaction.clean_savepoints()

    # all objects are saved

@transaction.non_atomic_requests
def savepoint_4(request):
    autocommit_stat = transaction.get_autocommit()
    print("autocommit status : %s" % (autocommit_stat,))

    #rollback_stat = transaction.get_rollback() #The rollback flag doesn't work outside of an 'atomic' block
    #print("rollback status : %s" % (rollback_stat,))

    #transaction.set_rollback(False)

    sid1 = transaction.savepoint()

    g1=Group()
    s_info = 'savepoint_4 a'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    g2=Group()
    s_info = 'savepoint_4 b'
    g2.name='%s %s' % ( app_prefix, s_info)
    g2.save()

    transaction.savepoint_commit(sid1)

    sid2 = transaction.savepoint()

    g3=Group()
    s_info = 'savepoint_4 c'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    g4=Group()
    s_info = 'savepoint_4 d'
    g4.name='%s %s' % ( app_prefix, s_info)
    g4.save()

    transaction.savepoint_rollback(sid2) # not working

    sid3 = transaction.savepoint()

    g5=Group()
    s_info = 'savepoint_4 e'
    g5.name='%s %s' % ( app_prefix, s_info)
    g5.save()

    g6=Group()
    s_info = 'savepoint_4 f'
    g6.name='%s %s' % ( app_prefix, s_info)
    g6.save()

    transaction.savepoint_commit(sid3)

    transaction.clean_savepoints()

    raise Exception("Error")

    # all objects are saved

@transaction.non_atomic_requests
def savepoint_5(request):
    transaction.set_autocommit(False)
    autocommit_flag = transaction.get_autocommit()
    print("autocommit state : %s" % (autocommit_flag,))

    sid1 = transaction.savepoint()

    g1=Group()
    s_info = 'savepoint_5 a'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

    g2=Group()
    s_info = 'savepoint_5 b'
    g2.name='%s %s' % ( app_prefix, s_info)
    g2.save()

    transaction.savepoint_commit(sid1)


    sid2 = transaction.savepoint()

    g3=Group()
    s_info = 'savepoint_5 c'
    g3.name='%s %s' % ( app_prefix, s_info)
    g3.save()

    g4=Group()
    s_info = 'savepoint_5 d'
    g4.name='%s %s' % ( app_prefix, s_info)
    g4.save()

    transaction.savepoint_rollback(sid2)


    sid3 = transaction.savepoint()

    g5=Group()
    s_info = 'savepoint_5 e'
    g5.name='%s %s' % ( app_prefix, s_info)
    g5.save()

    g6=Group()
    s_info = 'savepoint_5 f'
    g6.name='%s %s' % ( app_prefix, s_info)
    g6.save()

    transaction.savepoint_commit(sid3)

    transaction.clean_savepoints()

    # no objects are saved

def after_commit_1(request):
    transaction.on_commit(lambda : print("========commit berhasil!!!!========"))
    g1=Group()
    s_info = 'on_commit_1'
    g1.name='%s %s' % ( app_prefix, s_info)
    g1.save()

def after_commit_2(request):
    s_info1 = 'commit_2 (luar)'
    transaction.on_commit(lambda : print("========%s berhasil!!!!========" % (s_info1,)))
    g1=Group()
    g1.name='%s %s' % ( app_prefix, s_info1)
    g1.save()

    try:
        with transaction.atomic():
            s_info2 = 'commit_2 (dalam)'
            transaction.on_commit(lambda : print("========%s berhasil!!!!========" % (s_info2,)))
            g2=Group()
            g2.name='%s %s' % ( app_prefix, s_info2)
            g2.save()
    except Exception as e:
        pass

def after_commit_3(request):
    s_info1 = 'commit_3 (luar)'
    transaction.on_commit(lambda : print("========%s berhasil!!!!========" % (s_info1,)))
    g1=Group()
    g1.name='%s %s' % ( app_prefix, s_info1)
    g1.save()

    try:
        with transaction.atomic():
            s_info2 = 'commit_3 (dalam)'
            transaction.on_commit(lambda : print("========%s berhasil!!!!========" % (s_info2,)))
            g2=Group()
            g2.name='%s %s' % ( app_prefix, s_info2)
            g2.save()

            raise Exception("Error")
    except Exception as e:
        pass

def after_commit_4(request):
    s_info1 = 'commit_4 (luar)'
    transaction.on_commit(lambda : print("========%s berhasil!!!!========" % (s_info1,)))
    g1=Group()
    g1.name='%s %s' % ( app_prefix, s_info1)
    g1.save()

    try:
        with transaction.atomic():
            s_info2 = 'commit_4 (dalam)'
            transaction.on_commit(lambda : print("========%s berhasil!!!!========" % (s_info2,)))
            g2=Group()
            g2.name='%s %s' % ( app_prefix, s_info2)
            g2.save()

        raise Exception("Error")
    except Exception as e:
        pass

def after_commit_5(request):
    s_info1 = 'commit_5 (luar)'
    transaction.on_commit(lambda : print("========%s berhasil!!!!========" % (s_info1,)))
    g1=Group()
    g1.name='%s %s' % ( app_prefix, s_info1)
    g1.save()

    try:
        with transaction.atomic():
            s_info2 = 'commit_5 (dalam)'
            transaction.on_commit(lambda : print("========%s berhasil!!!!========" % (s_info2,)))
            g2=Group()
            g2.name='%s %s' % ( app_prefix, s_info2)
            g2.save()
    except Exception as e:
        pass

    raise Exception("Error")
