import os

# 131 62
screen_width = 131
screen_height = 62
cs = -2 + 1j
ce = -cs
scaleX = (ce.real - cs.real) / screen_width
scaleY = (ce.imag - cs.imag) / screen_height
while True:
    y = 0
    screen = ''
    s3d2 = 0.8660254
    for y in range(screen_height):
        x = 0
        for x in range(screen_width):
            Zx = cs.real + scaleX * x
            Zy = cs.imag + scaleY * y
            for i in range(100):
                Zxn = Zx
                Zyn = Zy
                Zx1 = 3 * (Zxn * Zxn - Zyn * Zyn)
                Zy1 = 3 * (2 * Zxn * Zyn)
                Zx2 = 2 * (Zxn * Zxn * Zxn - 3 * Zxn * Zyn * Zyn) + 1
                Zy2 = 2 * (-Zyn * Zyn * Zyn + 3 * Zyn * Zxn * Zxn)
                Zx = (Zx1 * Zx2 + Zy1 * Zy2) / (Zx1 * Zx1 + Zy1 * Zy1)
                Zy = (Zx1 * Zy2 - Zx2 * Zy1) / (Zx1 * Zx1 + Zy1 * Zy1)

                if (Zx - Zxn) * (Zx - Zxn) + (Zy - Zyn) * (Zy - Zyn) < 0.0001:
                    break
            dist1 = (Zx + 1.0) * (Zx + 1.0) + Zy * Zy
            dist2 = (Zx - 0.5) * (Zx - 0.5) + (Zy - s3d2) * (Zy - s3d2)
            dist3 = (Zx - 0.5) * (Zx - 0.5) + (Zy + s3d2) * (Zy + s3d2)
            if (dist1 > dist2) & (dist1 > dist3):
                screen += "██"
            if (dist2 > dist1) & (dist2 > dist3):
                screen += "▓▓"
            if (dist3 > dist2) & (dist3 > dist1):
                screen += "▒▒"

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
