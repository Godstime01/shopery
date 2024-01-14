from django import template
register = template.Library()

@register.inclusion_tag('partials/buttons.html')
def Button(type='button', text=None, size='small', style='fill', has_icon=False, is_rounded=True):
    """
        style = fill, border, shadow
        size = small, medium, large

    """
    print(is_rounded)
    classes = 'rounded-4xl '

    if size == 'small':
        classes += 'px-5 py-1'
    elif size == 'medium':
        classes += 'px-8 py-1.5'
    elif size == 'large':
        classes += 'px-12 py-2' 

    if style == 'fill':
        classes += ' bg-primary text-white hover:bg-primary-hard'
    elif style == 'border':
        classes += ' bg-white border-2 border-primary text-primary hover:border-primary-hard hover:text-primary-hard'
    elif style == 'shadow':
        classes += ' bg-[#56AC591A] text-primary hover:text-primary-hard hover:bg-[#2C742F33]'

    if is_rounded == False:
        print('removing rounded-4xl')
        classes = classes.replace('rounded-4xl', '')
    
    print(classes)

    return {
        'text': text,
        'size': size,
        'style': style,
        'classes': classes,
        'has_icon': has_icon, 
        'type': type
        }


@register.inclusion_tag('product_card.html')
def product_card(image=None):
    return 