a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

def check(L, W, l1, w1, l2, w2):
    if (l1 + l2 <= L) and max(w1, w2) <= W:
        return True
    if (w1 + w2 <= W) and max(l1, l2) <= L:
        return True
    return False

possible = False

for frame_l, frame_w in [(a, b), (b, a)]:
    for p1_l, p1_w in [(c, d), (d, c)]:
        for p2_l, p2_w in [(e, f), (f, e)]:
            if check(frame_l, frame_w, p1_l, p1_w, p2_l, p2_w):
                possible = True
                break
        if possible: break
    if possible: break

if possible:
    print("YES")
else:
    print("NO")