import requests
from bs4 import BeautifulSoup


def check_same_page(url, page_list):
    target_url_page = url[-1]
    if target_url_page in page_list:
        return True
    return False


def get_film_name_and_link(url):
    page_list = []
    film_data = {}
    while True:
        film_name = []
        page_number = url[-1]
        page_list.append(page_number)
        resp = requests.get(url)
        resp.encoding = "utf-8"
        soup = BeautifulSoup(resp.text, "html.parser")
        basic_result = soup.select("div.release_movie_name")
        for i in range(0, len(basic_result)):
            film_information = basic_result[i].select("a.gabtn")[0]
            film_title = str(basic_result[i].select(
                "a.gabtn")[0].text).strip()
            film_name.append(film_title)
            film_link = film_information["href"]
            url_temp_dict = {}
            url_temp_dict["url"] = film_link
            film_data[film_title] = url_temp_dict

        movie_time = soup.find_all(
            "a", attrs={"class": "btn_s_time gabtn"})
        for i in range(0, len(movie_time)):
            film_data[film_name[i]
                      ]["movie_time"] = movie_time[i]["href"]

        img_data = soup.select("img.lazy-load")
        for i in range(0, len(img_data)):
            film_data[film_name[i]
                      ]["img_url"] = img_data[i]["data-src"]

        url = soup.find_all("a")[-7]["href"]
        if check_same_page(url, page_list):
            return film_data


# url = "https://movies.yahoo.com.tw/movie_intheaters.html?page=1"
# print(get_film_name_and_link(url).keys())

# resp = requests.get(url)
# resp.encoding = "utf-8"
# soup = BeautifulSoup(resp.text, "html.parser")
# result = soup.select("div.release_movie_name")
# for i in range(0, len(result)):
#     print("No.", i)
#     film_information = result[i].select("a.gabtn")[0]
#     film_title = str(result[i].select("a.gabtn")[0].text).strip()
#     film_link = film_information["href"]
#     print(result[i])
#     print("\n")

# movie_html = soup.find_all("a", attrs={"class": "btn_s_time gabtn"})
# for i in range(0, len(movie_html)):
#     print(movie_html[i]["data-ga"].split("'")[-2])
#     print(movie_html[i]["href"])

# print(i["data-ga"].split("'")[-2])
# print(i["href"])
