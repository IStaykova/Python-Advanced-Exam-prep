def list_roman_emperors(*success_status, **rule_length):
    successful_emperors = {}
    unsuccessful_emperors = {}

    for emperor, success in success_status:
        if success:
            successful_emperors[emperor] = rule_length[emperor]
        else:
            unsuccessful_emperors[emperor] = rule_length[emperor]

    sorted_successful_emperors = sorted(
        successful_emperors.items(), key=lambda x: (-x[1], x[0])
    )
    sorted_unsuccessful_emperors = sorted(
        unsuccessful_emperors.items(), key=lambda x: (x[1], x[0])
    )

    result = [f"Total number of emperors: {len(success_status)}"]
    if successful_emperors:
        result.append("Successful emperors:")
        for name, years in sorted_successful_emperors:
            result.append(f"****{name}: {years}")
    if unsuccessful_emperors:
        result.append("Unsuccessful emperors:")
        for name, years in sorted_unsuccessful_emperors:
            result.append(f"****{name}: {years}")

    return "\n".join(result)

print(list_roman_emperors(("Augustus", True), ("Nero", False), Augustus=40, Nero=14,))
print(list_roman_emperors(("Augustus", True), ("Trajan", True), ("Nero", False), ("Caligula", False), ("Pertinax", False), ("Vespasian", True), Augustus=40, Trajan=19, Nero=14, Caligula=4, Pertinax=4, Vespasian=19,))