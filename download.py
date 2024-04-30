from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pytube import YouTube


def download_video(url, output_path):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        if stream:
            print("Downloading:", yt.title)
            stream.download(output_path=output_path)
            print("Download completed!")
        else:
            print("No progressive stream available.")
    except Exception as e:
        print("An error occurred:", str(e))


def get_top_videos(search_term, num_videos):
    driver = webdriver.Chrome()  # Use your appropriate webdriver
    driver.get("https://www.youtube.com/")
    search_box = driver.find_element(By.XPATH, "//input[@id='search']")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    # Clicking on filter to sort by view count
    driver.find_element(By.XPATH, "//*[@id='filter-button']/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]").click()
    driver.find_element(By.XPATH, "//span[contains(text(),'Sort by')]//parent::button").click()
    driver.find_element(By.XPATH, "//yt-formatted-string[contains(text(),'View count')]").click()

    time.sleep(5)  # Let the page load

    video_links = driver.find_elements(By.XPATH, "//a[@id='video.py-title']")
    video_url = [link.get_attribute('href') for link in video_links]

    driver.quit()

    return video_url[:num_videos]


if __name__ == "__main__":
    search_term = input("Enter the search term: ")
    num_videos = 6
    output_path = "./downloads/"  # Change this to your desired output path

    video_urls = get_top_videos(search_term, num_videos)
    print("Top", num_videos, "videos for the search term:", search_term)

    for i, url in enumerate(video_urls, start=1):
        print(f"{i}. {url}")
        download_video(url, output_path)
