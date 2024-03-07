def cal_gradient(x1, y1, x2, y2):
    if x1-x2 == 0:
        return 'inf'
    return (y1-y2)/(x1-x2)

def cal_length(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5

def sol():
    xa,ya,xb,yb,xc,yc = map(int,input().split())

    gab = cal_gradient(xa,ya,xb,yb)
    gac = cal_gradient(xa,ya,xc,yc)
    gbc = cal_gradient(xb,yb,xc,yc)

    if gab == gac == gbc:
        return -1

    arr = sorted([cal_length(xa,ya,xb,yb), cal_length(xa,ya,xc,yc), cal_length(xb,yb,xc,yc)])
    return 2*(arr[2] - arr[0])

print(sol())