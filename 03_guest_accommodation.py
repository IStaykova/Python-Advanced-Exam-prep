def accommodate(*args, **kwargs):
    successful_accommodations = {}
    unsuccessful_accommodations = 0

    rooms = sorted(kwargs.items(), key=lambda x: (x[1], x[0]))

    for guests in args:
        is_accommodated = False

        for room_key, capacity in rooms:
            if capacity >= guests:
                room_number = room_key.split("_")[1]
                if room_number not in successful_accommodations:
                    successful_accommodations[room_number] = guests
                    rooms.remove((room_key, capacity))
                    is_accommodated = True
                    break
        if not is_accommodated:
            unsuccessful_accommodations += guests

    if successful_accommodations:
        result = [f"A total of {len(successful_accommodations)} accommodations were completed!"]
        for room_number in sorted(successful_accommodations.keys()):
            result.append(f"<Room {room_number} accommodates {successful_accommodations[room_number]} guests>")
    else:
        result = ["No accommodations were completed!"]

    if unsuccessful_accommodations > 0:
        result.append(f"Guests with no accommodation: {unsuccessful_accommodations}")
    if rooms:
        result.append(f"Empty rooms: {len(rooms)}")
    return "\n".join(result).strip()

print(accommodate(5, 4, 2, room_305=6, room_410=5, room_204=2))
print(accommodate(10, 9, 8, room_307=6, room_802=5))









