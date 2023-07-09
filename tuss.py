import os
import concurrent.futures
import requests
import json
import xml.etree.ElementTree as ET
from tabulate import tabulate
from requests.exceptions import RequestException, Timeout

HEADER = "--------------------- The Ultimate Social Scanner ---------------------\n" \
         "--------------------- Made with Love by Rocksiz ---------------------\n" \
         ""


def check_website(session, url):
    try:
        response = session.get(url, allow_redirects=True, timeout=5)
        if response.status_code == requests.codes.ok:
            return url
    except (RequestException, Timeout) as e:
        print(f"Error occurred while checking {url}: {str(e)}")

    return None


def check_username_on_websites(username):
    social_media_websites = [
        {"name": "Instagram", "url": f"https://www.instagram.com/{username}"},
        {"name": "Facebook", "url": f"https://www.facebook.com/{username}"},
        {"name": "Twitter", "url": f"https://twitter.com/{username}"},
        {"name": "LinkedIn", "url": f"https://www.linkedin.com/in/{username}"},
        {"name": "TripAdvisor", "url": f"https://www.tripadvisor.com/members/{username}"},
        {"name": "Tumblr", "url": f"https://{username}.tumblr.com/"},
        {"name": "VSCO", "url": f"https://vsco.co/{username}/gallery"},
        {"name": "Wikipedia", "url": f"https://en.wikipedia.org/wiki/User:{username}"},
        {"name": "Wordpress", "url": f"https://{username}.wordpress.com/"},
        {"name": "YouTube", "url": f"https://www.youtube.com/user/{username}"},
        {"name": "GitHub", "url": f"https://github.com/{username}"},
        {"name": "Snapchat", "url": f"https://www.snapchat.com/add/{username}"},
        {"name": "Reddit", "url": f"https://www.reddit.com/user/{username}"},
        {"name": "TikTok", "url": f"https://www.tiktok.com/@{username}"},
        {"name": "Pinterest", "url": f"https://www.pinterest.com/{username}"},
        {"name": "Steam", "url": f"https://steamcommunity.com/id/{username}"},
        {"name": "Tumblr", "url": f"https://{username}.tumblr.com/"},
        {"name": "Medium", "url": f"https://medium.com/@{username}"},
        {"name": "Soundcloud", "url": f"https://soundcloud.com/{username}"},
        {"name": "Flickr", "url": f"https://www.flickr.com/people/{username}"},
        {"name": "DeviantArt", "url": f"https://{username}.deviantart.com/"},
        {"name": "Vimeo", "url": f"https://vimeo.com/{username}"},
        {"name": "Dribbble", "url": f"https://dribbble.com/{username}"},
        {"name": "500px", "url": f"https://500px.com/{username}"},
        {"name": "Weibo", "url": f"https://weibo.com/{username}"},
        {"name": "VK", "url": f"https://vk.com/{username}"},
        {"name": "Quora", "url": f"https://www.quora.com/profile/{username}"},
        {"name": "SlideShare", "url": f"https://www.slideshare.net/{username}"},
        {"name": "Gravatar", "url": f"https://gravatar.com/{username}"},
        {"name": "Fiverr", "url": f"https://www.fiverr.com/{username}"},
        {"name": "Product Hunt", "url": f"https://www.producthunt.com/@{username}"},
        {"name": "AngelList", "url": f"https://angel.co/u/{username}"},
        {"name": "Blogger", "url": f"https://{username}.blogspot.com/"},
        {"name": "About.me", "url": f"https://about.me/{username}"},
        {"name": "Goodreads", "url": f"https://www.goodreads.com/{username}"},
        {"name": "Keybase", "url": f"https://keybase.io/{username}"},
        {"name": "Yelp", "url": f"https://www.yelp.com/user_details?userid={username}"},
        {"name": "TripAdvisor", "url": f"https://www.tripadvisor.com/members/{username}"},
        {"name": "IMDb", "url": f"https://www.imdb.com/user/{username}"},
        {"name": "Scribd", "url": f"https://www.scribd.com/{username}"},
        {"name": "Houzz", "url": f"https://www.houzz.com/user/{username}"},
        {"name": "Slack", "url": f"https://{username}.slack.com"},
        {"name": "Behance", "url": f"https://www.behance.net/{username}"},
        {"name": "Zhihu", "url": f"https://www.zhihu.com/people/{username}"},
        {"name": "Academia.edu", "url": f"https://www.academia.edu/{username}"},
        {"name": "ResearchGate", "url": f"https://www.researchgate.net/profile/{username}"},
        {"name": "Myspace", "url": f"https://myspace.com/{username}"},
        {"name": "Wattpad", "url": f"https://www.wattpad.com/user/{username}"},
        {"name": "About.me", "url": f"https://about.me/{username}"},
        {"name": "Bandcamp", "url": f"https://bandcamp.com/{username}"},
        {"name": "Carrd", "url": f"https://{username}.carrd.co"},
        {"name": "Coub", "url": f"https://coub.com/{username}"},
        {"name": "Crunchyroll", "url": f"https://www.crunchyroll.com/user/{username}"},
        {"name": "Disqus", "url": f"https://disqus.com/by/{username}"},
        {"name": "Etsy", "url": f"https://www.etsy.com/shop/{username}"},
        {"name": "Imgur", "url": f"https://imgur.com/user/{username}"},
        {"name": "Kickstarter", "url": f"https://www.kickstarter.com/profile/{username}"},
        {"name": "Meetup", "url": f"https://www.meetup.com/members/{username}"},
        {"name": "Mixcloud", "url": f"https://www.mixcloud.com/{username}"},
        {"name": "Patreon", "url": f"https://www.patreon.com/{username}"},
        {"name": "Roblox", "url": f"https://www.roblox.com/user.aspx?username={username}"},
        {"name": "Shopify", "url": f"https://{username}.myshopify.com"},
        {"name": "Spotify", "url": f"https://open.spotify.com/user/{username}"},
        {"name": "Twitch", "url": f"https://www.twitch.tv/{username}"},
        {"name": "Xbox", "url": f"https://account.xbox.com/en-US/Profile?gamertag={username}"},
        {"name": "Giphy", "url": f"https://giphy.com/{username}"},
        {"name": "NPM", "url": f"https://www.npmjs.com/~{username}"},
        {"name": "Ravelry", "url": f"https://www.ravelry.com/people/{username}"},
        {"name": "Redbubble", "url": f"https://www.redbubble.com/people/{username}"},
        {"name": "Society6", "url": f"https://society6.com/{username}"},
        {"name": "Zazzle", "url": f"https://www.zazzle.com/{username}"},
        {"name": "Coub", "url": f"https://coub.com/{username}"},
        {"name": "Skoob", "url": f"https://www.skoob.com.br/usuario/{username}"},
        {"name": "Badoo", "url": f"https://badoo.com/en/{username}"},
        {"name": "ReverbNation", "url": f"https://www.reverbnation.com/{username}"},
        {"name": "Instructables", "url": f"https://www.instructables.com/member/{username}"},
        {"name": "Codecademy", "url": f"https://www.codecademy.com/profiles/{username}"},
        {"name": "Kaggle", "url": f"https://www.kaggle.com/{username}"},
        {"name": "Hackerrank", "url": f"https://www.hackerrank.com/{username}"},
        {"name": "FreeCodeCamp", "url": f"https://www.freecodecamp.org/{username}"},
        {"name": "DZone", "url": f"https://dzone.com/users/{username}"},
        {"name": "KhanAcademy", "url": f"https://www.khanacademy.org/profile/{username}"},
        {"name": "Kofi", "url": f"https://ko-fi.com/{username}"},
        {"name": "Lichess", "url": f"https://lichess.org/@/{username}"},
        {"name": "Pastebin", "url": f"https://pastebin.com/u/{username}"},
        {"name": "PlayStation", "url": f"https://my.playstation.com/profile/{username}"},
        {"name": "Stack Overflow", "url": f"https://stackoverflow.com/users/{username}"},
        {"name": "Repl.it", "url": f"https://replit.com/@{username}"},
        {"name": "Weheartit", "url": f"https://weheartit.com/{username}"},
        {"name": "YouNow", "url": f"https://www.younow.com/{username}"},
        {"name": "imgsrc.ru", "url": f"https://imgsrc.ru/main/user.php?user={username}"},
        {"name": "last.fm", "url": f"https://www.last.fm/user/{username}"},
        {"name": "Slack", "url": f"https://{username}.slack.com"},
        {"name": "FortniteTracker", "url": f"https://fortnitetracker.com/profile/all/{username}"},
        {"name": "mastodon.cloud", "url": f"https://mastodon.cloud/@{username}"},
        {"name": "Promodj", "url": f"https://promodj.com/{username}"},
        {"name": "ok.ru", "url": f"https://ok.ru/{username}"},
        {"name": "Itemfix", "url": f"https://www.itemfix.com/c/{username}"},
        {"name": "Keakr", "url": f"https://www.keakr.com/en/profile/{username}"},
        {"name": "Myminifactory", "url": f"https://www.myminifactory.com/users/{username}"},
        {"name": "Myanimelist", "url": f"https://myanimelist.net/profile/{username}"},
        {"name": "livelib.ru", "url": f"https://www.livelib.ru/reader/{username}"},
        {"name": "Kooapp", "url": f"https://www.kooapp.com/profile/{username}"},
        {"name": "spletnik.ru", "url": f"https://www.spletnik.ru/user/{username}"},
        {"name": "Dailykos", "url": f"https://www.dailykos.com/user/{username}"},
        {"name": "Needrom", "url": f"https://www.needrom.com/author/{username}"},
        {"name": "Newgrounds", "url": f"https://{username}.newgrounds.com/"},
        {"name": "Notabug", "url": f"https://notabug.org/{username}"},
        {"name": "lobste.rs", "url": f"https://lobste.rs/u/{username}"},
        {"name": "Livejournal", "url": f"https://{username}.livejournal.com/"},
        {"name": "linux.org.ru", "url": f"https://www.linux.org.ru/people/{username}/profile"},
        {"name": "Devrant", "url": f"https://devrant.com/users/{username}"},
        {"name": "Trakt.tv", "url": f"https://trakt.tv/users/{username}"},
        {"name": "Zoomit", "url": f"https://www.zoomit.ir/user/{username}/"},
        {"name": "Spletnik", "url": f"https://www.spletnik.ru/user/{username}"},
        {"name": "Opennet", "url": f"https://www.opennet.ru/~{username}"},
        {"name": "career.habr", "url": f"https://career.habr.com/{username}"},
        {"name": "mstdn.io", "url": f"https://mstdn.io/@{username}"},
        {"name": "Osu", "url": f"https://osu.ppy.sh/users/{username}"},
        {"name": "Gumroad", "url": f"https://gumroad.com/{username}"},
        {"name": "icq.im", "url": f"https://icq.im/{username}"},
        {"name": "Hubski", "url": f"https://hubski.com/user/{username}"},
        {"name": "Asciinema", "url": f"https://asciinema.org/@@{username}"},
        {"name": "anilist.co", "url": f"https://anilist.co/user/{username}"},
        {"name": "AppleDev", "url": f"https://developer.apple.com/forums/profile/{username}"},
        {"name": "AppleDiscussions", "url": f"https://discussions.apple.com/profile/{username}"},
        {"name": "Bikemap", "url": f"https://www.bikemap.net/en/u/{username}"},

    ]

    responding_websites = []

    with requests.Session() as session:
        session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"})

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_website = {executor.submit(check_website, session, website["url"]): website for website in social_media_websites}

            total_websites = len(social_media_websites)
            completed_count = 0

            for future in concurrent.futures.as_completed(future_to_website):
                completed_count += 1
                progress = f"Scanning ({completed_count} of {total_websites})"
                print(progress, end="\r")

                website = future_to_website[future]
                name = website["name"]

                try:
                    result = future.result()
                    if result:
                        responding_websites.append((name, result))
                except Exception as e:
                    print(f"Error occurred while processing {name}: {str(e)}")


    print() 
    return responding_websites


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_results(username, responding_sites):
    clear_screen()
    print(HEADER)
    print(f"\nResponding social media websites for {username}:\n")
    if responding_sites:
        table_data = [(site[0], site[1]) for site in responding_sites]
        headers = ["Website", "URL"]
        print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
    else:
        print("No responding websites found for the username.")


def prompt_user_input():
    clear_screen()
    print(HEADER)
    username = input("Enter the username to check: ")
    return username


def save_results(username, responding_sites):
    while True:
        user_input = input("\nPlease select the file format to save the results:"
                           "\n1. JSON"
                           "\n2. XML"
                           "\n3. TXT"
                           "\n99. Go back"
                           "\n0. Exit"
                           "\nEnter your choice: ")

        if user_input == "1":
            save_as_json(username, responding_sites)
        elif user_input == "2":
            save_as_xml(username, responding_sites)
        elif user_input == "3":
            save_as_txt(username, responding_sites)
        elif user_input == "99":
            return
        elif user_input == "0":
            exit()
        else:
            print("Invalid input. Please try again.")


def save_as_json(username, responding_sites):
    file_name = f"{username}_results.json"

    data = {
        "username": username,
        "responding_sites": responding_sites
    }

    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

    print(f"Results saved as JSON to {file_name} successfully.")


def save_as_xml(username, responding_sites):
    file_name = f"{username}_results.xml"

    root = ET.Element("results")
    username_element = ET.SubElement(root, "username")
    username_element.text = username

    for site in responding_sites:
        site_element = ET.SubElement(root, "site")
        name_element = ET.SubElement(site_element, "name")
        name_element.text = site[0]
        url_element = ET.SubElement(site_element, "url")
        url_element.text = site[1]

    tree = ET.ElementTree(root)
    tree.write(file_name)

    print(f"Results saved as XML to {file_name} successfully.")


def save_as_txt(username, responding_sites):
    file_name = f"{username}_results.txt"

    with open(file_name, "w") as file:
        file.write(f"Responding social media websites for {username}:\n\n")
        if responding_sites:
            for site in responding_sites:
                file.write(f"{site[0]}: {site[1]}\n")
        else:
            file.write("No responding websites found for the username.")

    print(f"Results saved as TXT to {file_name} successfully.")


def main():
    while True:
        username = None
        while username is None:
            clear_screen()
            print(HEADER)
            username = input("Enter the username to check (Press '0' to exit): ")
            if username == "0":
                exit()

        print("Processing...")
        responding_sites = check_username_on_websites(username)
        print_results(username, responding_sites)

        user_input = input("\nPlease select an option:"
                           "\n1. Make a new search"
                           "\n2. Save the result"
                           "\n0. Exit"
                           "\nEnter your choice: ")

        if user_input == "1":
            continue
        elif user_input == "2":
            save_results(username, responding_sites)
        elif user_input == "0":
            clear_screen()
            break
        else:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()
