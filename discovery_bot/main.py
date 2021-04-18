import requests
import csv
from keywords import categories_to_keywords

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"


def get_categories(caption):
    categories = []
    for c, keywords in categories_to_keywords.items():
        for k in keywords:
            if k.is_present_in(caption):
                categories.append(c)
                break
    return categories


if __name__ == "__main__":
    tag = 'lasvegasfoodies'
    x = requests.get(
        'https://www.instagram.com/explore/tags/' + tag + '/?__a=1', headers={"user-agent": USER_AGENT})
    response = x.json()
    posts = response.get('graphql', {}).get('hashtag', {}).get(
        'edge_hashtag_to_media', {}).get('edges', {})

    with open('output.csv', mode='w') as csv_file:
        fieldnames = ['Caption', 'Food Types', 'Post']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for p in posts:
            # Skip anything that isn't a post
            if p.get('node', {}).get('__typename') != 'GraphImage':
                continue

            caption_edges = p.get('node', {}).get(
                'edge_media_to_caption', {}).get('edges', [])
            if len(caption_edges) > 0:
                caption = caption_edges[0].get('node', {}).get('text', '')
                categories = get_categories(caption)
                categories_string = ','.join(categories)
                url_builder = 'https://www.instagram.com/p/' + \
                    p.get('node', {}).get('shortcode', '') + '/'

                writer.writerow(
                    {'Caption': caption, 'Food Types': categories_string, 'Post': url_builder})
    # print(posts)
