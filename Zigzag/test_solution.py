from Zigzag import Solution


def _check(s, num_rows, expected):
    ret = Solution().convert(s, num_rows)
    assert ret == expected, f'Wrong answer for input "{s}", {num_rows}'


def test_1():
    _check('', 0, '')


def test_2():
    s = 'abcdefghijklmnopqrstuvwxyz'
    _check(s, 1, s)


def test_3():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'acegikmoqsuwybdfhjlnprtvxz'
    _check(s, 2, e)


def test_4():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'aeimquybdfhjlnprtvxzcgkosw'
    _check(s, 3, e)


def test_5():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'agmsybfhlnrtxzceikoquwdjpv'
    _check(s, 4, e)


def test_6():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'aiqybhjprxzcgkoswdflntvemu'
    _check(s, 5, e)


def test_7():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'akubjltvcimswdhnrxegoqyfpz'
    _check(s, 6, e)


def test_8():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'amyblnxzckowdjpveiqufhrtgs'
    _check(s, 7, e)


def test_9():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'aobnpcmqdlrzeksyfjtxgiuwhv'
    _check(s, 8, e)


def test_10():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'aqbprcosdntemuflvgkwhjxziy'
    _check(s, 9, e)


def test_11():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'asbrtcqudpveowfnxgmyhlzikj'
    _check(s, 10, e)


def test_12():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'aubtvcswdrxeqyfpzgohnimjlk'
    _check(s, 11, e)


def test_13():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'awbvxcuydtzesfrgqhpiojnkml'
    _check(s, 12, e)


def test_14():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'aybxzcwdveuftgshriqjpkolnm'
    _check(s, 13, e)


def test_15():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abzcydxewfvguhtisjrkqlpmon'
    _check(s, 14, e)


def test_16():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdzeyfxgwhviujtkslrmqnpo'
    _check(s, 15, e)


def test_17():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdefzgyhxiwjvkultmsnroqp'
    _check(s, 16, e)


def test_18():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdefghziyjxkwlvmuntosprq'
    _check(s, 17, e)


def test_19():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdefghijzkylxmwnvouptqsr'
    _check(s, 18, e)


def test_20():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdefghijklzmynxowpvqurts'
    _check(s, 19, e)


def test_21():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdefghijklmnzoypxqwrvsut'
    _check(s, 20, e)


def test_22():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdefghijklmnopzqyrxswtvu'
    _check(s, 21, e)


def test_23():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdefghijklmnopqrzsytxuwv'
    _check(s, 22, e)


def test_24():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdefghijklmnopqrstzuyvxw'
    _check(s, 23, e)


def test_25():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdefghijklmnopqrstuvzwyx'
    _check(s, 24, e)


def test_26():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdefghijklmnopqrstuvwxzy'
    _check(s, 25, e)


def test_27():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdefghijklmnopqrstuvwxyz'
    _check(s, 26, e)


def test_28():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdefghijklmnopqrstuvwxyz'
    _check(s, 27, e)


def test_29():
    s = 'abcdefghijklmnopqrstuvwxyz'
    e = 'abcdefghijklmnopqrstuvwxyz'
    _check(s, 100, e)