from collections import deque

suggested_links = deque([int(el) for el in input().split()])  #FIFO
featured_articles = [int(el) for el in input().split()]       #LIFO
target_engagement_value = int(input())
final_feed = []

while suggested_links and featured_articles:
    current_link = suggested_links[0]
    current_article = featured_articles[-1]

    if current_link > current_article:
        difference_num = current_link % current_article
        final_feed.append(-difference_num)
        suggested_links.popleft()
        featured_articles.pop()
        if difference_num == 0:
            continue
        suggested_links.append(difference_num * 2)

    elif current_article > current_link:
        difference_num = current_article % current_link
        final_feed.append(difference_num)
        featured_articles.pop()
        suggested_links.popleft()
        if difference_num == 0:
            continue
        featured_articles.append(difference_num * 2)

    else:
        final_feed.append(0)
        suggested_links.popleft()
        featured_articles.pop()


total_engagement_value = sum(final_feed)

print(f"Final Feed: {', '.join([str(el) for el in final_feed])}")

if total_engagement_value >= target_engagement_value:
    print(f"Goal achieved! Engagement Value: {total_engagement_value}")
else:
    print(f"Goal not achieved! Short by: {target_engagement_value - total_engagement_value}")







