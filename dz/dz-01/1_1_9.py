paint_price = int(input("цена краски "))
cans = int(input())
brush_price = int(input())
brushes = int(input())
full_paint = paint_price * cans
full_brush = brush_price * brushes
full = full_paint + full_brush
print(f"Краска: {full_paint} руб.")
print(f"Кисти: {full_brush} руб.")
print(f"Всего: {full} руб.")