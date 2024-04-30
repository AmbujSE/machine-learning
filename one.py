from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pytube import YouTube
import time


def download_youtube_video(search_term):
    # Set up Selenium WebDriver (ensure the WebDriver for your browser is installed and path is set)
    driver = webdriver.Chrome()  # You can use other browsers like Firefox, Edge, etc.

    # Open YouTube
    driver.get("https://www.youtube.com")

    # Find the search bar and enter the search term
    search_box = driver.find_element(By.XPATH, "//input[@id='search']")
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.RETURN)

    # Wait for search results to load
    driver.find_element(By.XPATH, "//*[@id='filter-button']/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]").click()
    driver.implicitly_wait(10)

    # Find the first video.py element
    video_element = driver.find_element(By.XPATH, '//a[@id="video.py-title"]')

    # Get the URL of the video.py
    video_url = video_element.get_attribute("href")

    # Close the browser
    driver.quit()

    # Download the video.py using pytube
    try:
        yt = YouTube(video_url)
        best_stream = yt.streams.get_highest_resolution()
        best_stream.download()
        print("Video downloaded successfully!")
    except Exception as e:
        print("Error downloading video.py:", e)


if __name__ == "__main__":
    search_term = input("Enter the search term: ")
    download_youtube_video(search_term)
