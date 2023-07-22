print("for instagram type 1 ")
print("for youtube video type 2")
t=input("type what want: ")
if t=="1"or t=="2":
    if t=="1":
        import instaloader
        ig=instaloader.Instaloader()
        username=input("enter your user name:")
        password=input("enter your password:")
        print("To get follower type:1")
        print("To get total number of post type :2")
        print("To get biography of the profile:3")
        print("To download profile pic type:4")
        qu=input("Type what you want:")
        ig.login(username,password)
        profile = instaloader.Profile.from_username(ig.context,username)
        if qu=="1" or qu=="2" or qu=="3" or qu=="4":

            if qu=="1":

                followers = profile.get_followers()
                
                for follower in followers:
                    print(follower)
            
            elif qu=="2":
                media=profile.mediacount
                print(media)
            elif qu=="3":
                bio=profile.biography
                print(bio)
            elif qu=="4":
                ig.download_profile(username,profile_pic_only=True)
                
        else:
            print("Type Valid Input")
    elif t=="2":
        from pytube import YouTube

        link = input("Paste the video link: ")
        yt = YouTube(link)
        print("If you want download only audio type 1")
        print("If you want download video and audio type ")
        q=input("type vaid number")
        if q=="1" or q=="2":
            if q=="1":

                video = yt.streams.get_audio_only()
                video.download("Desktop")
            elif q=="2":
                video = yt.streams.get_highest_resolution()
                video.download("Desktop") 
        else:
            print("Type valid input ")
else:
    print("type valid input ")   
