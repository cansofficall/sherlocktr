import requests
import argparse

def check_username(platform, url_template, username):
    url = url_template.format(username=username)
    response = requests.get(url)

    if response.status_code == 200:
        return True
    return False

def main():
    parser = argparse.ArgumentParser(description="Check username availability across platforms.")
    parser.add_argument("username", help="The username you want to check.")
    parser.add_argument("-a", "--platform", help="Specific platform to check against. If not provided, checks all platforms.", defa>
    parser.add_argument("-L", "--list", help="Check username on all platforms.", action="store_true")

    args = parser.parse_args()

    platforms = {
        "GitHub": "https://github.com/{username}",
        "Instagram": "https://www.instagram.com/{username}",
        "Twitter": "https://twitter.com/{username}",
        "Threads.net": "https://threads.net/{username}",
        "TikTok": "https://www.tiktok.com/@{username}",
        "Reddit": "https://www.reddit.com/user/{username}",
        "Pinterest": "https://www.pinterest.com/{username}/",
        "Facebook": "https://www.facebook.com/{username}",
        "YouTube": "https://www.youtube.com/user/{username}",
        "Tumblr": "https://{username}.tumblr.com",
        "Vimeo": "https://vimeo.com/{username}",
        "Blogger": "https://{username}.blogspot.com",
        "Steam": "https://steamcommunity.com/id/{username}",
        "SoundCloud": "https://soundcloud.com/{username}",
        "VK": "https://vk.com/{username}",
        "Spotify": "https://open.spotify.com/user/{username}",
        "Gravatar": "https://www.gravatar.com/{username}",
        "VirusTotal": "https://www.virustotal.com/user/{username}/",
        "Wattpad": "https://www.wattpad.com/user/{username}",
        "YouNow": "https://www.younow.com/{username}/",
        "Giphy": "https://giphy.com/{username}/",
        "Pastebin": "https://pastebin.com/u/{username}",
        "Wikia": "https://{username}.fandom.com",
        "Keybase": "https://keybase.io/{username}",
        "Minecraft": "https://minecraft.net/en-us/profile/name/{username}/",
        "TurkHackTeam": "https://www.turkhackteam.org/members/?username={username}",
        "Cracked.io": "https://cracked.to/{username}",
        "Roblox": "https://www.roblox.com/users/profile?username={username}",
        "WordPress": "https://{username}.wordpress.com",
        "Dribbble": "https://dribbble.com/{username}",
        "Behance": "https://www.behance.net/{username}",
        "Flickr": "https://www.flickr.com/photos/{username}/",
        "SlideShare": "https://www.slideshare.net/{username}",
        "Foursquare": "https://foursquare.com/{username}",
        "Medium": "https://medium.com/@{username}",
        "TripAdvisor": "https://www.tripadvisor.com/members/{username}",
        "500px": "https://500px.com/{username}",
        "DeviantArt": "https://{username}.deviantart.com/",
        "Patreon": "https://www.patreon.com/{username}",
        "Goodreads": "https://www.goodreads.com/{username}",
        "Etsy": "https://www.etsy.com/shop/{username}",
        "Twitch": "https://www.twitch.tv/{username}",
        "Imgur": "https://imgur.com/user/{username}",
        "Kickstarter": "https://www.kickstarter.com/profile/{username}",
        "Vine": "https://vine.co/{username}",
        "Snapchat": "https://www.snapchat.com/add/{username}",
        "Mixcloud": "https://www.mixcloud.com/{username}/",
        "Ask.fm": "https://ask.fm/{username}",
        "Last.fm": "https://www.last.fm/user/{username}",
        "Kik": "https://kik.me/{username}",
        "Bitbucket": "https://bitbucket.org/{username}/",
        "GitLab": "https://gitlab.com/{username}",
        "Reverbnation": "https://www.reverbnation.com/{username}",
        "HubPages": "https://hubpages.com/@{username}",
        "Redbubble": "https://www.redbubble.com/people/{username}",
        "DailyMotion": "https://www.dailymotion.com/{username}"
    }

    if args.platform:
        if args.platform in platforms:
            exists = check_username(args.platform, platforms[args.platform], args.username)
            if exists:
                print(f"{args.username} exists on {args.platform}.")
            else:
                print(f"{args.username} does not exist on {args.platform}.")
        else:
            print(f"{args.platform} is not supported or not in the list.")
            return

    if args.list:
        for platform, url_template in platforms.items():
            exists = check_username(platform, url_template, args.username)
            if exists:
                print(f"{args.username} exists on {platform}.")
            else:
                print(f"{args.username} does not exist on {platform}.")

if __name__ == "__main__":
    main()
