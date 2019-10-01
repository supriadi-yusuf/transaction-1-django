from django.conf.urls import url
from .views import save_with_exception, save_without_exception, \
    non_atomic, outside, exception_in_try_except_block, \
    outer_inner_1, outer_inner_2, atomic_1, atomic_2, atomic_3, \
    atomic_4, atomic_5, atomic_6, atomic_7, atomic_8, atomic_9, \
    autocommit_1, autocommit_2, autocommit_3, \
    autocommit_4, autocommit_5, autocommit_6, \
    transaction_1, \
    savepoint_1, savepoint_2, savepoint_3, savepoint_4, \
    savepoint_5, \
    after_commit_1, after_commit_2, after_commit_3, \
    after_commit_4, after_commit_5
#from django.contrib import admin

urlpatterns = [
    url(r'^exception/$', save_with_exception),
    url(r'^no_exception/$', save_without_exception),
    url(r'^non_atomic/$', non_atomic),
    url(r'^outside/$', outside),
    url(r'^exception_in_try_except_block/$', exception_in_try_except_block),
    url(r'^outer_inner_1/$', outer_inner_1),
    url(r'^outer_inner_2/$', outer_inner_2),
    url(r'^autocommit_1/$', autocommit_1),
    url(r'^autocommit_2/$', autocommit_2),
    url(r'^autocommit_3/$', autocommit_3),
    url(r'^autocommit_4/$', autocommit_4),
    url(r'^autocommit_5/$', autocommit_5),
    url(r'^autocommit_6/$', autocommit_6),
    url(r'^transaction_1/$', transaction_1),
    url(r'^savepoint_1/$', savepoint_1),
    url(r'^savepoint_2/$', savepoint_2),
    url(r'^savepoint_3/$', savepoint_3),
    url(r'^savepoint_4/$', savepoint_4),
    url(r'^savepoint_5/$', savepoint_5),
    url(r'^atomic_1/$', atomic_1),
    url(r'^atomic_2/$', atomic_2),
    url(r'^atomic_3/$', atomic_3),
    url(r'^atomic_4/$', atomic_4),
    url(r'^atomic_5/$', atomic_5),
    url(r'^atomic_6/$', atomic_6),
    url(r'^atomic_7/$', atomic_7),
    url(r'^atomic_8/$', atomic_8),
    url(r'^atomic_9/$', atomic_9),
    url(r'^after_commit_1/$', after_commit_1),
    url(r'^after_commit_2/$', after_commit_2),
    url(r'^after_commit_3/$', after_commit_3),
    url(r'^after_commit_4/$', after_commit_4),
    url(r'^after_commit_5/$', after_commit_5),
]
