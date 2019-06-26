from django.shortcuts import render
from . import validator

def quadratic_equation_solutions(request):
    a = request.GET['a']
    b = request.GET['b']
    c = request.GET['c']
    a_html = validator.validate_a(a)
    b_html = validator.validate(b)
    c_html = validator.validate(c)
    context_dict = {
        'a_html':a_html,
        'b_html':b_html,
        'c_html':c_html,
        }
    if a_html['is_valid'] and b_html['is_valid'] and c_html['is_valid']:
        context_dict['d_html'] = discriminant(a, b, c)
        context_dict['x1_html'] = x1_calc(a, b, c)
        context_dict['x2_html'] = x2_calc(a, b, c)
    return render(request, "results.html", context_dict)
                    
def discriminant(a, b, c):
    return int(b)**2 - 4*int(a)*int(c)
        
def x1_calc(a, b, c):
    return (-int(b) + discriminant(a, b, c)**0.5)/(2*int(a))

def x2_calc(a, b, c):
    return (-int(b) - discriminant(a, b, c)**0.5)/(2*int(a))


    
        

    
