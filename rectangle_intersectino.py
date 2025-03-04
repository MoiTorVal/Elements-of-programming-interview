import collections

Rect = collections.namedtuple('Rect', ('x', 'y', 'width', 'height'))

def intersect_rectangle(r1: Rect, r2: Rect) -> Rect:
    def is_intersect(r1, r2):
        return (
            r1.x < r2.x + r2.width # condition 1
        and 
            r1.x + r1.width > r2.x # condition 2 
        and
            r1.y < r2.y + r2.height 
        and 
            r1.y + r1.height > r2.y)
    
    if not is_intersect(r1, r2):
        return Rect(0, 0, -1, -1)

    return Rect(
        max(r1.x, r2.x),
        max(r1.y, r2.y),
        min(r1.x + r1.width, r2.x + r2.width) - max(r1.x, r2.x),
        min(r1.y + r1.height, r2.y + r2.height) - max(r1.y, r2.y)
    )


rect1 = Rect(1,2,5,4)
rect2 = Rect(5,3,2,4)
print(intersect_rectangle(rect1, rect2))



