color_input=input("enter colors:")
clr=[c.strip() for c in color_input.split(',')]
if clr:
    print(clr[0])
    print(clr[-1])
