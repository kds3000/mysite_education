def validate(param):
    error = {'is_valid': True, 'msg':"", 'param':param}
    try:
        int(param)
    except ValueError:
        error['msg'] = 'коэффициент не целое число'
        error['is_valid'] = False
    if param == '':
        error['msg'] = 'коэффициент не определен'
        error['is_valid'] = False
    return error

def validate_a(param):
    error = {'is_valid': True, 'msg':"", 'param':param}
    try:
        int(param)
    except ValueError:
        error['msg'] = 'коэффициент не целое число'
        error['is_valid'] = False
    if param == '':
        error['msg'] = 'коэффициент не определен'
        error['is_valid'] = False
    elif param == '0':
        error['msg'] = 'коэффициент при первом слагаемом уравнения не может быть равным нулю'
        error['is_valid'] = False
    return error