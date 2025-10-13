from collections import deque

contestant = deque([int(el) for el in input().split()]) #FIFO
pie_pieces = [int(el) for el in input().split()] #LIFO

while contestant and pie_pieces:
    current_contestant_pieces = contestant[0]
    current_pie_pieces = pie_pieces[-1]

    if current_contestant_pieces >= current_pie_pieces:
        current_contestant_pieces = current_contestant_pieces - current_pie_pieces
        if current_contestant_pieces == 0:
            contestant.popleft()
            pie_pieces.pop()
        else:
            contestant.append(current_contestant_pieces)
            contestant.popleft()
            pie_pieces.pop()
    elif current_contestant_pieces < current_pie_pieces:
        current_pie_pieces -= current_contestant_pieces
        pie_pieces.pop()
        pie_pieces.append(current_pie_pieces)
        if current_pie_pieces == 1 and len(pie_pieces) >= 2:
            pie_pieces[-2] += current_pie_pieces
            pie_pieces.pop()
        contestant.popleft()

if contestant:
    print(f"We will have to wait for more pies to be baked!\nContestants left: {', '.join([str(el) for el in contestant])}")
if pie_pieces:
    print(f"Our contestants need to rest!\nPies left: {', '.join([str(el) for el in pie_pieces])}")
if not contestant and not pie_pieces:
    print("We have a champion!")








#contestant pieces: 5 8 4 6
# pie pieces :      3 7 2 9
