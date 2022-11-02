def bestCoordinate(towers: list[list[int]], radius: int) -> list[int]:
    x_max = max(t[0] for t in towers)
    y_max = max(t[1] for t in towers)
    cx = cy = max_quality = 0
    for x in range(x_max + 1):
        for y in range(y_max + 1):
            quality = 0
            for tx, ty, q in towers:
                d = (x - tx) ** 2 + (y - ty) ** 2
                if d <= radius ** 2:
                    quality += int(q / (1 + d ** 0.5))
            if quality > max_quality:
                cx, cy, max_quality = x, y, quality
    return [cx, cy]

print(bestCoordinate([[1,2,5],[2,1,7],[3,1,9]],2))