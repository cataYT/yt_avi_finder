import subprocess
from googleapiclient.discovery import build
import random
import csv

with open("key.txt", "r") as f: 
    API_KEY: str = f.readline().strip()
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def search_videos(query, max_results=5):
    # Initialize YouTube API client
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=API_KEY)
    
    # Make a search request
    request = youtube.search().list(
        q=query,
        part='snippet',
        type='video',
        maxResults=max_results
    )
    response = request.execute()
    
    # Collect results as a list of tuples (Title, URL)
    results = []
    for item in response.get('items', []):
        title = item['snippet']['title']
        video_id = item['id']['videoId']
        url: str = f"https://www.youtube.com/watch?v={video_id}"
        results.append((title, url))
    
    return results

def write_results(number=random.randint(1000, 9999)) -> None:
    # Generate a random query
    num: int = number
    query: str = f"{num}.avi"
    results = search_videos(query, max_results=5)

    # Write results to a CSV file
    with open("results.csv", "a", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        
        # Check if the file is empty to write the header
        f.seek(0, 2)  # Move to the end of the file
        if f.tell() == 0:
            writer.writerow(["Title", "URL"])  # Write the header
        
        # Write each row
        writer.writerows(results)

    subprocess.run([
        "python",
        "display_results.py"
    ])

def main() -> None:
    try:
        manual_input = int(input("Enter specific number (leave for random): "))
        write_results(manual_input)
    except ValueError:
        write_results()

if __name__ == "__main__":
    main()