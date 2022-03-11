import os

screen_width = 131
screen_height = 62
cs = -2 + 1j
ce = -cs
scaleX = (ce.real - cs.real) / screen_width
scaleY = (ce.imag - cs.imag) / screen_height
while True:
    y = 0
    screen = ''
    for y in range(screen_height):
        x = 0
        for x in range(screen_width):
            c = complex(cs.real + scaleX * x, cs.imag + scaleY * y)
            z = 0
            for i in range(100):
                z = complex(z.real**2-z.imag**2, -2*z.real*z.imag) + c
                if abs(z) >= 2:
                    match i % 6:
                        case 0:
                            screen += "██"
                        case 1:
                            screen += "▓▓"
                        case 2:
                            screen += "▒▒"
                        case 3:
                            screen += "░░"
                        case 4:
                            screen += "▒▒"
                        case 5:
                            screen += "▓▓"
                    break
            if abs(z) < 2:
                screen += "  "
        screen += "\n"
    print(screen)
    match input():
        case 'a':
            cs -= scaleX * 10
            ce -= scaleX * 10
        case 'd':
            cs += scaleX * 10
            ce += scaleX * 10
        case 'w':
            cs -= scaleY * 10j
            ce -= scaleY * 10j
        case 's':
            cs += scaleY * 10j
            ce += scaleY * 10j
        case 'z':
            csr = (cs + ce) / 2
            cs = (cs - csr) * 0.7 + csr
            ce = (ce - csr) * 0.7 + csr
            scaleX = (ce.real - cs.real) / screen_width
            scaleY = (ce.imag - cs.imag) / screen_height
        case 'x':
            csr = (cs + ce) / 2
            cs = (cs - csr) / 0.7 + csr
            ce = (ce - csr) / 0.7 + csr
            scaleX = (ce.real - cs.real) / screen_width
            scaleY = (ce.imag - cs.imag) / screen_height
        case 'c':
            cs = -2 + 1j
            ce = -cs
            scaleX = (ce.real - cs.real) / screen_width
            scaleY = (ce.imag - cs.imag) / screen_height
    os.system('CLS')
