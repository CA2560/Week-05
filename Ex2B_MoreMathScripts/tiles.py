l = int(input("What is the length of the room in feet? "))
w = int(input("What is the width of the room in feet? "))

room_area = l * w

tiles = 1
box_of_tiles = 12 

needed_boxes = room_area / (tiles * box_of_tiles)

boxes_accidents = needed_boxes *.10
print(f"You will need {round(needed_boxes)} boxes of tiles to cover a room that is {l} feet long and {w} feet wide.")
print(f"To account for accidents, you should purchase {round(boxes_accidents)} boxes of tiles.")