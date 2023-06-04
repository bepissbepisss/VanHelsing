global var
var = {}

var['bruh'] = 1
var['kek'] = 2

def func():
    if 'bruh' in var:
        var.pop('bruh', None)
    else:
        if 'kek' in var:
            print('no work')
    if 'kek' in var:
        print('it work')


func()
