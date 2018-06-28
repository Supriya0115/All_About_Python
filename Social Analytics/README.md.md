
Problem Statement:
    
I have to program a Python script to perform sentiment analysis of the Twitter activity of news outlets - BBC, CBS, CNN, Fox, and New York times - and present findings visually.

![image.png](attachment:image.png)

![TweetPolarity_NewsOutlet.png](attachment:TweetPolarity_NewsOutlet.png)
![TweetPolarity_TweetsAgo.png](attachment:TweetPolarity_TweetsAgo.png)

Step 1 : I import the libraries and packages (a.k.a tools of trade!) for my analysis.


```python
# Import dependencies

import tweepy
import json
import numpy as np
import pandas as pd

from datetime import date
import matplotlib.pyplot as plt
import seaborn as sns


# Twitter API Keys

consumer_key = "aoCDolf5adnIaw8yzMmxy1EH4"
consumer_secret = "LBmKVfpZoqOT6YVsWcjXa1ZyXjZ2i8hu4LhbnvVOBwwvu6hjF8"
access_token = "161980186-vjLsfGo6lCe92ttUonuaTxUAOsy9J5eDDOjH2sjf"
access_token_secret = "M1XVIyVrdx6nVI8ty59O4zbSEx6mkEX5guhF1yeT9wjl2"

# Import and Initialize Sentiment Analyzer

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
```

Step 2 : I set up tweepy authetication to take my API keys and grant me authorization to use API results.


```python
# Setup Tweepy API Authentication

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())
```

Step 3: I assign and define variables - hold target accounts, empty list to hold sentiments.


```python
# Define target accounts for BBC, CBS, CNN, Fox, and New York times

target_user = ["BBCWorld","CBSNews","CNN","FoxNews","nytimes"]
```


```python
# Lists to hold sentiments

sentiments = []
```

Step 4: I define the logic to retrieve tweets and analyze their sentiments. Also, the first 100 tweets for each target account is printed to the console. 


```python
# Grab 100 tweets for each target user and loop through it 

for target in target_user:
    
    at_target = "@" + target
    public_tweets = api.user_timeline(at_target, count=100, result_type="recent")
    counter = 1
    
    for tweet in public_tweets:
        
        # Run Vader Analysis on each tweet
        
        results = analyzer.polarity_scores(tweet["text"])
        compound = results["compound"]
        pos = results["pos"]
        neu = results["neu"]
        neg = results["neg"]

        # Add sentiments for each tweet into a list
        
        sentiments.append({"Date": tweet["created_at"], 
                           "News_Source":target,
                           "Compound": compound,
                           "Positive": pos,
                           "Negative": neu,
                           "Neutral": neg,
                           "Tweets_Ago": counter,
                           "Tweet":tweet["text"]})
        
        
        Tweet_Text = tweet["text"]
        
        # Print Tweet Text and increment the counter 
        
        print(f"Tweet {counter} for {target}: {Tweet_Text} \n")
        
        counter = counter + 1

```

    Tweet 1 for BBCWorld: Is India really the most dangerous country for women? https://t.co/XbSKKQbaO3 
    
    Tweet 2 for BBCWorld: What do European governments want from the EU Summit? https://t.co/4EHTLBtXHm 
    
    Tweet 3 for BBCWorld: World Cup 2018: Mexico fans celebrate South Korean 'brothers' https://t.co/NgkaKULS9w 
    
    Tweet 4 for BBCWorld: Europe's migration crisis: Could it finish the EU? https://t.co/DVhyHlFgCQ 
    
    Tweet 5 for BBCWorld: Revamped drug could save lives of many new mothers - WHO https://t.co/dXPz5nf1pD 
    
    Tweet 6 for BBCWorld: Supreme Court: Why a fight over US abortion law now looms https://t.co/dQIagzjGu1 
    
    Tweet 7 for BBCWorld: Five attempts to make toys more inclusive https://t.co/q0TD2r1nlH 
    
    Tweet 8 for BBCWorld: Asylum seekers in Ireland to be allowed to work https://t.co/733eZAPPjj 
    
    Tweet 9 for BBCWorld: Flamingo that escaped a zoo in 2005 spotted in Texas https://t.co/jHKFQFdCxg 
    
    Tweet 10 for BBCWorld: Antwon Rose: Pittsburgh officer charged with criminal homicide https://t.co/WKZw6ZUuuq 
    
    Tweet 11 for BBCWorld: RT @awzurcher: Your daily “elections have consequences” reminder. If Hillary Clinton had won we’d be looking at a 6-3 liberal majority on t… 
    
    Tweet 12 for BBCWorld: Trump Supreme Court pick: Why is the US top court so important? https://t.co/580QVujKIz 
    
    Tweet 13 for BBCWorld: Trump-Putin summit agreed by US and Russia in principle https://t.co/H20hvks2hD 
    
    Tweet 14 for BBCWorld: RT @awzurcher: Without Anthony Kennedy on the US Supreme Court, there really won't be a swing justice. Whoever replaces him will move the C… 
    
    Tweet 15 for BBCWorld: Migrant rescue ship Lifeline docks in Malta after days at sea https://t.co/pLQhBmVTbl 
    
    Tweet 16 for BBCWorld: RT @BBCBreaking: A Supreme Court justice is to retire, giving President Trump the chance to reshape the top US court https://t.co/OC80dTFbCL 
    
    Tweet 17 for BBCWorld: US Supreme Court judge to retire https://t.co/Q2SoQLC0HF 
    
    Tweet 18 for BBCWorld: Where are heterosexual civil partnerships legal? https://t.co/L4EW8Xrfai 
    
    Tweet 19 for BBCWorld: Thailand cave rescue: How would you survive in a cave? https://t.co/eOxaFwfBXL 
    
    Tweet 20 for BBCWorld: Saudi TV presenter investigated over 'indecent' clothing https://t.co/R3piggod6s 
    
    Tweet 21 for BBCWorld: Chemical weapons: New watchdog powers an important step https://t.co/tO3e5qzzB4 
    
    Tweet 22 for BBCWorld: Joe Jackson: Patriarch of Jackson family dies aged 89 https://t.co/J4f5joitPL 
    
    Tweet 23 for BBCWorld: Galapagos' Sierra Negra volcano eruption triggers evacuation https://t.co/oZchuUuOJI 
    
    Tweet 24 for BBCWorld: OPCW chemical watchdog gains power to assign blame https://t.co/AZW3dyG0SG 
    
    Tweet 25 for BBCWorld: RT @BBCSport: Auf Wiedersehen...
    
    DEFENDING CHAMPIONS GERMANY ARE OUT OF THE #WORLDCUP!
    
    FT: #KOR 2-0 #GER 
    
    https://t.co/ukXULQ5cJx
    #KORGE… 
    
    Tweet 26 for BBCWorld: RT @BBCSport: GOAL!
    
    Another for #KOR! Manuel Neuer surrenders possession in the opposing half, South Korea hoof it up and tuck it into an… 
    
    Tweet 27 for BBCWorld: RT @BBCSport: FT #MEX 0-3 #SWE 
    
    Incredible from Sweden. They're through to the #WorldCup knockout stages after thrashing Mexico.
    
    Full-tim… 
    
    Tweet 28 for BBCWorld: RT @BBCSport: GOAL!
    
    IT'S BEEN GIVEN!
    
    #KOR 1-0 #GER 
    
    VAR has given Kim's goal and Germany are heading out!
    
    https://t.co/ukXULQ5cJx #Worl… 
    
    Tweet 29 for BBCWorld: Isle of Man diocese to review alleged abuse by clergy https://t.co/F3jTZRmnrD 
    
    Tweet 30 for BBCWorld: RT @bbcweather: Severe storms hit Greece https://t.co/jBX3GXCaPz Jo https://t.co/AJcQvJwSYY 
    
    Tweet 31 for BBCWorld: RT @BBCPolitics: Thank goodness he didn't do the crotch grab! 😳 Culture secretary @MattHancock learns to moonwalk at the opening of the Mic… 
    
    Tweet 32 for BBCWorld: Leo Varadkar defends the newly appointed Garda chief https://t.co/ZT9YnZ6wZw 
    
    Tweet 33 for BBCWorld: Jersey to introduce same sex marriage from 1 July https://t.co/kdVcj1c37S 
    
    Tweet 34 for BBCWorld: Spain 'new wolf pack' gang held over Gran Canaria sex attack https://t.co/fubEnFklpI 
    
    Tweet 35 for BBCWorld: Syria war: Air strikes knock out hospitals in Deraa https://t.co/dZIJabp0JT 
    
    Tweet 36 for BBCWorld: RT @BBCSport: Just look at it 😍
    
    A new match ball will be used for the knockout stage of the #WorldCup, Fifa has announced. 
    
    👉 https://t.c… 
    
    Tweet 37 for BBCWorld: Algeria's powerful police chief Gen Abdelghani Hamel sacked https://t.co/2KrFJOJoAp 
    
    Tweet 38 for BBCWorld: RT @bbcstories: ⚡️ “The FBI said I was my parents' stolen baby - but I found the truth”
    
    https://t.co/jWFvOfCDxM 
    
    Tweet 39 for BBCWorld: Belize praised for 'visionary' steps to save coral reef https://t.co/0HS4Pr3fRQ 
    
    Tweet 40 for BBCWorld: RT @BBC_HaveYourSay: Has your name been mispronounced at an important event in your life? Tweet us your story or email: haveyoursay@bbc.co.… 
    
    Tweet 41 for BBCWorld: The St George sculpture before... and after 🎨
    
    Botched art restoration at Spanish church criticised… https://t.co/RxhIX7BRm8 
    
    Tweet 42 for BBCWorld: Malaysia 1MDB: Seized tiaras, cash and Hermes bags 'worth $273m' https://t.co/yVca9C025a 
    
    Tweet 43 for BBCWorld: Poland to scrap Holocaust law jail threat https://t.co/79CToMjp41 
    
    Tweet 44 for BBCWorld: Alexandria Ocasio-Cortez: Millennial beats veteran Democrat https://t.co/yeesjNz1FG 
    
    Tweet 45 for BBCWorld: RT @BBCSteveR: On the day Trump’s national security advisor visits Moscow, one Russian paper calls John Bolton “chief hawk of the White Hou… 
    
    Tweet 46 for BBCWorld: Myanmar military leaders 'guilty of crimes against humanity' https://t.co/HiVUCI8S4i 
    
    Tweet 47 for BBCWorld: Irish Ferries cancels some Dublin to Holyhead sailings https://t.co/IaxJHyukRu 
    
    Tweet 48 for BBCWorld: Can India become an AI hub for the developing world? https://t.co/0z6b0IylFQ 
    
    Tweet 49 for BBCWorld: Rebel Wilson ordered to repay millions in defamation case https://t.co/lpCAfm2JUT 
    
    Tweet 50 for BBCWorld: RT @BBCSport: What's on the #WorldCup schedule for today?
    
    Watch, read and listen with @BBCSport and @5LiveSport:
    
    15:00 #MEX v #SWE 📺💻📻
    15… 
    
    Tweet 51 for BBCWorld: RT @BBCSport: It's great news for Argentina in more ways than one...
    
    Diego Maradona says he is "fine" after being seen by a doctor during… 
    
    Tweet 52 for BBCWorld: Thailand cave rescue: Troops race to reach youth football team https://t.co/aSuRqQrYDM 
    
    Tweet 53 for BBCWorld: Zimbabwe's Mnangagwa believes political faction tried to kill him https://t.co/lmQf5n99zj 
    
    Tweet 54 for BBCWorld: Deadly explosion at Texas hospital leaves one dead https://t.co/6TnisIKaNr 
    
    Tweet 55 for BBCWorld: Letter from Africa: Snapping at the heels of Zimbabwe's 'crocodile' https://t.co/YgNmOVyWpN 
    
    Tweet 56 for BBCWorld: Ronald dela Rosa: 'The Rock' behind Duterte's drugs war https://t.co/yhuZQ1CfLs 
    
    Tweet 57 for BBCWorld: Merkel's Bavarian ally threatens mutiny on migrants https://t.co/eAxkw9FUGp 
    
    Tweet 58 for BBCWorld: RT @richard_conway: Reports emerging here in St Petersburg that Diego Maradona was taken to hospital after Argentina’s game tonight. 
    
    Tweet 59 for BBCWorld: France: Butchers demand protection from vegans https://t.co/h0krY6YrBV 
    
    Tweet 60 for BBCWorld: Canada tycoon's son Blake Leibel jailed for 'savage' murder https://t.co/g8k1ingzK9 
    
    Tweet 61 for BBCWorld: RT @BBCSport: Hector Cuper has left his role as Egypt manager after they were knocked out of the #WorldCup 
    
    Full story: https://t.co/nwr8l… 
    
    Tweet 62 for BBCWorld: NSA contractor Reality Winner admits leak https://t.co/uqiSN5PWqw 
    
    Tweet 63 for BBCWorld: RT @BBCSport: FT #NGA 1-2 #ARG 
    
    14' ⚽ Lionel Messi
    51' ⚽ Victor Moses
    86' ⚽ Marcos Rojo
    
    An unlikely hero for Argentina, but it doesn't ma… 
    
    Tweet 64 for BBCWorld: RT @BBCSport: FT: #ISL 1-2 #CRO 
    
    For the first time ever, Croatia have won three #WorldCup games in a row! 
    
    Iceland bow out.
    
    Reaction: h… 
    
    Tweet 65 for BBCWorld: RT @BBCSport: GOAL! #NGA 1-2 #ARG
    
    Marcos Rojo?! What a finish from the defender. Argentina are back in the driving seat!
    
    Follow #NGAARG l… 
    
    Tweet 66 for BBCWorld: RT @BBCSport: GOAL!
    
    Looks like it'll be three out of three for Croatia!
    
    Ivan Perisic drives a finish into the far corner.
    
    #ISL 1-2 #CRO… 
    
    Tweet 67 for BBCWorld: Migrant family separations: States sue Trump administration https://t.co/flWhRvUMb3 
    
    Tweet 68 for BBCWorld: RT @BBCSport: GOAL!
    
    Now then...
    
    Gylfi Sigurdsson fires a penalty into the roof of the net!
    
    #ISL 1-1 #CRO 
    
    Live: https://t.co/aeMK9g0ELv… 
    
    Tweet 69 for BBCWorld: RT @BBCSport: GOAL!
    
    Straight after rattling the crossbar, Milan Badelj drives in the opener! 
    
    #ISL 0-1 #CRO 
    
    Live: https://t.co/aeMK9g0E… 
    
    Tweet 70 for BBCWorld: Indiana child fires handgun found in sofa at Ikea https://t.co/2WsnrEnVzS 
    
    Tweet 71 for BBCWorld: RT @BBCSport: HT: #ISL 0-0 #CRO 
    
    Croatia will be relieved to head into the break with it goalless after a very, very strong finish to the… 
    
    Tweet 72 for BBCWorld: US college quarterback 'had brain disorder' before suicide https://t.co/SczLaFmFL0 
    
    Tweet 73 for BBCWorld: Abiy Ahmed becomes Ethiopia's prime minister https://t.co/jNoIEHoKGK 
    
    Tweet 74 for BBCWorld: Noura Hussein: Appeals court overturns death sentence https://t.co/RDLgFoYi8J 
    
    Tweet 75 for BBCWorld: No BBC Sports News Correspondents were harmed in the making of this film 😀
    
    Follow the build-up to #NGAARG… https://t.co/bTg01yQpQS 
    
    Tweet 76 for BBCWorld: RT @BBCSport: FT #AUS 0-2 #PER 
    
    18' ⚽ Andre Carrillo
    50' ⚽ Paolo Guerrero
    
    Peru get their first win at the #WorldCup finals in 40 years. A… 
    
    Tweet 77 for BBCWorld: RT @BBCSport: FT: #DEN 0-0 #FRA 
    
    From start to finish, a very slow game - the first goalless draw of the #WorldCup 
    
    Reaction: https://t.c… 
    
    Tweet 78 for BBCWorld: Guernsey airline Waves cancels flights for two months https://t.co/J2GHDGepTK 
    
    Tweet 79 for BBCWorld: RT @BBCSport: The rags to riches story of the man who saved a Cristiano Ronaldo penalty.
    
    Iran goalkeeper Alireza Beiranvand has come a lon… 
    
    Tweet 80 for BBCWorld: Teenager helps deaf and blind man to communicate on flight https://t.co/NK958WcHEj 
    
    Tweet 81 for BBCWorld: Marree Man: The enduring mystery of a giant outback figure https://t.co/eHf0ujmQIu 
    
    Tweet 82 for BBCWorld: Ottawa Bluesfest preparations obstructed by nesting bird https://t.co/8WXtcXOyXx 
    
    Tweet 83 for BBCWorld: Ethiopia offers Eritrea chance to end Africa's longest war https://t.co/jkEGxPSfmW 
    
    Tweet 84 for BBCWorld: New Zealand man shot after 'flying to US to attack teenager' https://t.co/7GhI4ljjBk 
    
    Tweet 85 for BBCWorld: It's a big day at the World Cup and we've already had a goal
    
    #AUSPER #DENFRA
    
    https://t.co/Ledbaj9Ie4 https://t.co/yhVpPIEfY0 
    
    Tweet 86 for BBCWorld: RT @BBCMonitoring: VAR! What is it good for? #WorldCup
    https://t.co/bckchMpWxD 
    
    Tweet 87 for BBCWorld: Trump travel ban: What does this ruling mean? https://t.co/My2sno3EC9 
    
    Tweet 88 for BBCWorld: RT @BBCSport: HT #AUS 0-1 #PER 
    
    18' ⚽ Andre Carrillo
    
    A wonderful volley from the Peru winger is the difference at the halfway mark. Austr… 
    
    Tweet 89 for BBCWorld: Eritrea and Ethiopia open first high-level talks in 20 years https://t.co/tFjP29Yfxo 
    
    Tweet 90 for BBCWorld: DR Congo's Kasai crisis: War crimes committed by both sides, UN says https://t.co/pNp6LaLcS0 
    
    Tweet 91 for BBCWorld: US Supreme Court upholds Trump's travel ban https://t.co/gdKK9xrp5i 
    
    Tweet 92 for BBCWorld: RT @BBCSport: GOAL! #AUS 0-1 #PER
    
    What a strike! Andre Carrillo scores Peru's first goal at a #WorldCup in 36 years.
    
    Follow #AUSPER live… 
    
    Tweet 93 for BBCWorld: "Most people don't talk about organ donations when they're alive, but thankfully Phil did talk about it."  https://t.co/mkegh8J61p 
    
    Tweet 94 for BBCWorld: Syria war: Government forces make gains in south-west https://t.co/P3RenLLxyw 
    
    Tweet 95 for BBCWorld: 'Stolen babies' case: Spanish doctor Vela goes on trial https://t.co/8gFZXKRnWk 
    
    Tweet 96 for BBCWorld: Jane Subachus: Family makes desperate appeal for stem cell donor https://t.co/mlG6ZklUOQ 
    
    Tweet 97 for BBCWorld: PSNI's Drew Harris appointed Garda commissioner https://t.co/2nEbR5ygac 
    
    Tweet 98 for BBCWorld: Police in South Korea have arrested one of the owners of a notorious revenge porn site https://t.co/pHGMJCrmAp 
    
    Tweet 99 for BBCWorld: Japan unveils Hello Kitty-themed bullet train https://t.co/mzvzrMvnlE 
    
    Tweet 100 for BBCWorld: Soldiers in Myanmar have been accused of raping Rohingya women 
    
    This is one woman's story https://t.co/J4GvJOlzah https://t.co/xREMCmcuEe 
    
    Tweet 1 for CBSNews: At North Dakota stop, President Trump claims his rallies are the reason why NFL ratings are down: "They find this m… https://t.co/D0SIEmWRxp 
    
    Tweet 2 for CBSNews: Pittsburgh officer charged in shooting death of unarmed black teen https://t.co/JiGvVQw3sk https://t.co/nSdFZkyPz2 
    
    Tweet 3 for CBSNews: LIVE: President Trump greets supporters at rally in Fargo, North Dakota https://t.co/ln7yjZwJKQ https://t.co/jz8YqjNBaG 
    
    Tweet 4 for CBSNews: President Trump says he will pick retiring Supreme Court Justice Kennedy's replacement from a list the White House… https://t.co/m3fiLvMyYy 
    
    Tweet 5 for CBSNews: Ten-term Democratic Congressman Joe Crowley was defeated in New York City by newcomer 28-year-old Alexandria Ocasio… https://t.co/UmcOboxwca 
    
    Tweet 6 for CBSNews: The U.S. was just ranked as one of the top 10 most dangerous countries for women for the first time ever:… https://t.co/0VgA8p9SSN 
    
    Tweet 7 for CBSNews: Sen. Schumer says it would be the "height of hypocrisy" for the Senate to vote on a new Supreme Court justice befor… https://t.co/a1oYJ6MriW 
    
    Tweet 8 for CBSNews: FIRST LOOK: See Kristen Wiig as the villain Barbara Minerva, also known as Cheetah, in a scene from "Wonder Woman 1… https://t.co/9ZKzGeNFlh 
    
    Tweet 9 for CBSNews: It is no secret former President George H.W. Bush loves wearing distinctive socks. 
    
    Where does he get them?… https://t.co/tXokiifVtp 
    
    Tweet 10 for CBSNews: The fate of a dozen youth soccer players and their coach in Thailand has captivated people around the world. Millio… https://t.co/E6CDyc8XVo 
    
    Tweet 11 for CBSNews: Pennsylvania authorities released video of the drive-by shooting shooting that led to the fatal police shooting of… https://t.co/dKgkGXGf96 
    
    Tweet 12 for CBSNews: Near the Texas border, @DavidBegnaud rode along as officials busted a migrant smuggling stash house. https://t.co/5T60uzt6TA 
    
    Tweet 13 for CBSNews: .@Ocasio2018 beat veteran New York Congressman Joe Crowley in a Democratic primary. If elected in November, she wou… https://t.co/NMfI7QZz8u 
    
    Tweet 14 for CBSNews: The president has his eyes set on a meeting with his Russian counter-part, Vladimir Putin. The date and location wi… https://t.co/jqw89dThaN 
    
    Tweet 15 for CBSNews: Justice Anthony Kennedy said today he is retiring after three decades on the high court. Kennedy, who is 81 now, he… https://t.co/zLKlAplslO 
    
    Tweet 16 for CBSNews: "Permit Patty" steps down as CEO of cannabis company after massive internet backlash resulted in her products being… https://t.co/nPTqV9CyIo 
    
    Tweet 17 for CBSNews: Long considered a swing vote on the court, Justice Kennedy was often the deciding vote in cases that changed the co… https://t.co/nQajiKI5EN 
    
    Tweet 18 for CBSNews: "[Rep. Crowley] doesn't live there. And she turned that into a very compelling campaign message about the need for… https://t.co/NVMqwW3IF0 
    
    Tweet 19 for CBSNews: RT @CBSEveningNews: One famous customer helped put this entrepreneur on the map. @JimAxelrod introduces you to John Cronin, who with his da… 
    
    Tweet 20 for CBSNews: Elwood on Justice Kennedy's legacy: "I think his legacy is one of liberty –– being a champion for the liberty of Am… https://t.co/fk8YKHC0X7 
    
    Tweet 21 for CBSNews: Lifeguards in Florida are warning beachgoers about sea lice — microscopic pests that cause nasty rashes underneath… https://t.co/Fu6UjaLIjN 
    
    Tweet 22 for CBSNews: "[Democrats] want it out there and they want it part of the conversation that Republicans set up some rules and the… https://t.co/G0ZFBz4KSe 
    
    Tweet 23 for CBSNews: WATCH: CBS News airs first unfiltered look inside a facility for immigrant children separated from their families.… https://t.co/Zmr0CJonCG 
    
    Tweet 24 for CBSNews: .@daveweigel on significance of President Trump nominating second Supreme Court justice: "Well, it's -- it's someth… https://t.co/vtU8vtFtBQ 
    
    Tweet 25 for CBSNews: @CBSNews Elwood on Justice Kennedy: "I think the last time I spoke with him was probably at our law clerk reunion.… https://t.co/4WD85JkxIC 
    
    Tweet 26 for CBSNews: John Elwood, former clerk for Justice Kennedy, on why he decided to retire: "Well it's the right time for him. He's… https://t.co/lTcym2ZL56 
    
    Tweet 27 for CBSNews: Q: Do you expect this confirmation [for Justice Kennedy's replacement] to happen before the midterms? 
    
    @JanCBS: Ye… https://t.co/RC0b5s8TsW 
    
    Tweet 28 for CBSNews: Justice Kennedy's most pivotal swing votes and what his retirement means for the future of the Supreme Court on a s… https://t.co/uiSvfY3Q4E 
    
    Tweet 29 for CBSNews: A 12-year-old boy, who went viral for his Michael Jackson dance moves, received "thrilling" gift from a police offi… https://t.co/ExpV9ubLjb 
    
    Tweet 30 for CBSNews: American farmers are killing themselves in staggering numbers and the reasons why are tragic https://t.co/dhR5kWs9oJ https://t.co/VK4KUVMiWa 
    
    Tweet 31 for CBSNews: Justice Kennedy's departure will be a massive change for the high court, where he has been the crucial swing vote f… https://t.co/XsK7B9VAUH 
    
    Tweet 32 for CBSNews: Atlanta 6-year-old with lemonade stand raises $13,000 for separated migrant families https://t.co/Tj0u6SfVOF https://t.co/X0kItvafL2 
    
    Tweet 33 for CBSNews: President Trump calls retiring Justice Kennedy a "spectacular man," says search for his replacement will "begin imm… https://t.co/CWgdkQ103O 
    
    Tweet 34 for CBSNews: Justice Anthony Kennedy, a key swing vote on the Supreme Court, has announced his retirement, handing President Tru… https://t.co/r7CoKExGYm 
    
    Tweet 35 for CBSNews: "We will vote to confirm Justice Kennedy's successor this fall," Sen. Mitch McConnell says https://t.co/2qLebqsuKo https://t.co/Y1I1tQ1WXp 
    
    Tweet 36 for CBSNews: NASA shares awe-inspiring photo of blue sand dune on Mars 👽https://t.co/i4cE5O7ZNc https://t.co/UZE89pWe2i 
    
    Tweet 37 for CBSNews: “That was a shocker for Crowley to lose that election… I can’t say I was disappointed because I was never a big fan… https://t.co/nnMwOqNDXx 
    
    Tweet 38 for CBSNews: "I have a suggestion, if you're going to meet Mr. Putin," the president of Portugal tells @POTUS. "Don't forget [to… https://t.co/1tzExEZM9X 
    
    Tweet 39 for CBSNews: "We believe families should be together," @POTUS says. "But what we really do believe is in very strong borders, no… https://t.co/BX87JSMbLr 
    
    Tweet 40 for CBSNews: "John Bolton is over there [in Russia] right now... he's met with President Putin. I haven't gotten the full report… https://t.co/ZNyF50p7ud 
    
    Tweet 41 for CBSNews: "I think [Russia is] doing a fantastic job with the World Cup right now... My son loves soccer and he loves watchin… https://t.co/c9kAsDG5pg 
    
    Tweet 42 for CBSNews: "He is a man who has displayed great vision, tremendous vision and tremendous heart. And he will be missed," @POTUS… https://t.co/DH0NzTcEhA 
    
    Tweet 43 for CBSNews: "Our search for a new Justice will begin immediately," @POTUS says after Justice Kennedy announces his plan to reti… https://t.co/XdSlxRz4R1 
    
    Tweet 44 for CBSNews: How long will it take to fill Justice Kennedy's Supreme Court seat?
    
    "Not that long. I would expect you will see a… https://t.co/1PGoJsjFTG 
    
    Tweet 45 for CBSNews: "Justice Kennedy was a conservative, no doubt," @JanCBS says. However, "sometimes he would side with liberals on th… https://t.co/pHo221aN9b 
    
    Tweet 46 for CBSNews: “Justice Kennedy had been saying privately that he was considering retirement... This gives Pres. Trump his 2nd nom… https://t.co/W2pNTUFohj 
    
    Tweet 47 for CBSNews: MORE: 81-year-old Kennedy has widely been seen as a moderate swing vote on the court https://t.co/2qLebqsuKo https://t.co/Ndmf7FTvXC 
    
    Tweet 48 for CBSNews: JUST IN: Supreme Court Justice Anthony Kennedy announces he is retiring, effective July 31, giving President Trump… https://t.co/TM4ilY1aei 
    
    Tweet 49 for CBSNews: JUST IN: House vote on GOP immigration bill fails, 121-301 https://t.co/aYg8cInOx8 https://t.co/Na0DLrLT1H 
    
    Tweet 50 for CBSNews: Jeff Sessions mocks liberals on "lunatic fringe" over family separation: "They want borders in their lives but not… https://t.co/GMjyg2PJzO 
    
    Tweet 51 for CBSNews: Suspect in deadly 2017 Charlottesville car rampage charged with federal hate crimes https://t.co/oS0UBLSUwA https://t.co/WCroC1hLc1 
    
    Tweet 52 for CBSNews: WATCH: Russian President Putin and National Security Adviser John Bolton have met for the first time — and decided… https://t.co/X8qHyFHLRr 
    
    Tweet 53 for CBSNews: Oklahoma voters approve medical marijuana despite bitter opposition https://t.co/SMeB3q4VXR https://t.co/R3fhzYNFJB 
    
    Tweet 54 for CBSNews: FINAL FAREWELL: Thousands gather for the funeral of NY teen Lesandro "Junior" Guzman-Feliz, who was killed in the B… https://t.co/zpkKHLHMV5 
    
    Tweet 55 for CBSNews: Joe Jackson, father of the late Michael Jackson and Janet Jackson and the mastermind behind The Jackson 5, has died… https://t.co/gQzMVFEL1n 
    
    Tweet 56 for CBSNews: "You are not afraid to speak the truth, and the truth as you know it. And to stand up for what you know is right, e… https://t.co/bPfp9HjXoi 
    
    Tweet 57 for CBSNews: "Let the rich guys do it. We have all these rich guys, they love rockets...Bezos and Elon Musk and all of them, the… https://t.co/jElZKMPo2a 
    
    Tweet 58 for CBSNews: WATCH: President Trump is making remarks at an event for young Americans. About 100 generation Z and millennials ar… https://t.co/BZw9K59rWx 
    
    Tweet 59 for CBSNews: TEACHER TO THE END: In lieu of flowers, this teacher asked people to fill her funeral with backpacks of school supp… https://t.co/iFy1yjvAMw 
    
    Tweet 60 for CBSNews: WATCH: Officials in Pittsburgh are giving an update on charges against the police officer accused of shooting and k… https://t.co/1xDuI4tg0K 
    
    Tweet 61 for CBSNews: Investigators arrested while probing Ivanka Trump's Chinese suppliers now off bail https://t.co/tXoXohnTOT https://t.co/KC7Ek8sLgZ 
    
    Tweet 62 for CBSNews: NEW: East Pittsburgh Officer Michael Rosfeld has been charged with criminal homicide in the death of 17-year-old An… https://t.co/IQmBv8meoK 
    
    Tweet 63 for CBSNews: The 5-4 decision by the Supreme Court could devastate clout of public sector unions in states including Illinois, N… https://t.co/spT15ftRa2 
    
    Tweet 64 for CBSNews: NEW: The Supreme has ruled that states can't force non-union workers to pay union fees. This is seen as a major set… https://t.co/te9Ivz3r4j 
    
    Tweet 65 for CBSNews: Russia calls for retaliation against U.S. steel, aluminum tariffs https://t.co/ET5BgJnGSn https://t.co/wJ0jxXPJtI 
    
    Tweet 66 for CBSNews: Bargain basement bud: Pot shops in California are cutting prices ahead of new rules https://t.co/I30Gpl0R6R https://t.co/SIwYieS71D 
    
    Tweet 67 for CBSNews: Tracy Morgan warns his younger self about the one thing that can stop him (via @CBSThisMorning)… https://t.co/Wz1m5Rejgz 
    
    Tweet 68 for CBSNews: Alexandria Ocasio-Cortez describes "astonishing" primary upset against Rep. Joe Crowley https://t.co/LHX8M8DGvM https://t.co/ynUloMYorM 
    
    Tweet 69 for CBSNews: Who is Alexandria Ocasio-Cortez? The 28-year old just defeated powerful 10-term Democratic Rep. Joe Crowley in a st… https://t.co/SVriJU6cxR 
    
    Tweet 70 for CBSNews: Former Cambridge Analytica employee says "there were more" apps that collected user data: https://t.co/EXUSemmpEs https://t.co/GBM3DZZAxg 
    
    Tweet 71 for CBSNews: Danny Meyer is the founder of the burger joint Shake Shack and CEO of Union Square Hospitality, which owns 17 New Y… https://t.co/1jA5qZAJmo 
    
    Tweet 72 for CBSNews: CBS News has obtained cellphone video from inside the Cayuga Centers in New York -- the first unfiltered look insid… https://t.co/LUXNDWXu3y 
    
    Tweet 73 for CBSNews: CBS News has obtained cellphone video from inside the Cayuga Centers in New York showing children huddled in what l… https://t.co/kT8cywqWQw 
    
    Tweet 74 for CBSNews: President Trump’s “administration is a form of extremism. We shouldn’t be afraid to be very bold and very strong in… https://t.co/8GQcQAvEbu 
    
    Tweet 75 for CBSNews: Alexandria Ocasio-Cortez says she was not following the primary results until she arrived at watch party: "We had f… https://t.co/Y0XvwNLuSU 
    
    Tweet 76 for CBSNews: Alexandria Ocasio-Cortez on her message to the Democratic establishment:  “I think that it is time that we reassert… https://t.co/mD6u6vwBG9 
    
    Tweet 77 for CBSNews: Alexandria Ocasio-Cortez, who defeated 10-term Democratic Rep. Joe Crowley in a stunning upset in Tuesday’s primari… https://t.co/9ivdKlOYfw 
    
    Tweet 78 for CBSNews: My pleasure to SAVE you: Chick-fil-A employee comes to the rescue of a choking customer and it wasn't even his firs… https://t.co/ZwJSKabrY8 
    
    Tweet 79 for CBSNews: NEW: The East Pittsburgh Police officer who fatally shot 17-year-old Antwon Rose Jr. on June 19 has been charged, a… https://t.co/o2qVrWU9z4 
    
    Tweet 80 for CBSNews: Brittany Kaiser, a former official at Cambridge Analytica, is sharing what she considers some of the data firm's qu… https://t.co/tHqwzPGnIx 
    
    Tweet 81 for CBSNews: RT @CBSThisMorning: For the first time last night, @ColbertLateShow and @FallonTonight aired the same opening. @StephenAtHome &amp; @JimmyFallo… 
    
    Tweet 82 for CBSNews: Tristan Beaudette was shot before dawn last Friday while camping with his two young daughters. Detectives are revie… https://t.co/CtdWAhnC10 
    
    Tweet 83 for CBSNews: The woman dubbed "Permit Patty" for threatening to call police on an 8-year-old black girl selling water on the str… https://t.co/yms6GuVah5 
    
    Tweet 84 for CBSNews: There will be a funeral this morning for a New York City teen, allegedly stabbed to death by gang members. Hundreds… https://t.co/jX9YSOr878 
    
    Tweet 85 for CBSNews: Passengers on a JetBlue flight were terrified when officers stormed their plane in New York’s JFK Airport. It was a… https://t.co/NQ8uDrzVor 
    
    Tweet 86 for CBSNews: President Trump is claiming vindication after the Supreme Court allowed his travel ban to stay in place. The court'… https://t.co/6BwY9Pim0t 
    
    Tweet 87 for CBSNews: A federal judge in California ruled the Trump administration must reunite separated immigrant families within 30 da… https://t.co/GWE2DpXzhN 
    
    Tweet 88 for CBSNews: A stunning upset rocked the midterm elections Tuesday. Rep. Joe Crowley was defeated by Alexandria Ocasio-Cortez, a… https://t.co/X4m2lc33J7 
    
    Tweet 89 for CBSNews: The body of a third-party contractor was found inside a beer cooler at SunTrust Park before Tuesday's Atlanta Brave… https://t.co/h5B4s61Vo8 
    
    Tweet 90 for CBSNews: RT @CBSThisMorning: WATCH: Here's a preview of what you can expect on @CBSThisMorning. https://t.co/p8YblTdQ9r 
    
    Tweet 91 for CBSNews: AHEAD on @CBSThisMorning: The Trump administration has up to 30 days to reunite separated immigrant families. We'll… https://t.co/rLpRQQBxBJ 
    
    Tweet 92 for CBSNews: Ben Rhodes: "We could have done more" to explain Russia's information war https://t.co/EHY88GX35o https://t.co/KRwLMZTQbY 
    
    Tweet 93 for CBSNews: WATCH: Comedian @RealTracyMorgan reflects on his life and sends a heartfelt message to his 6-year-old self.
    
    📺 See… https://t.co/KqyOqpyTnv 
    
    Tweet 94 for CBSNews: Rain continues to fall and water levels keep rising inside a cave in northern Thailand, frustrating the search for… https://t.co/KjiLYrhvk0 
    
    Tweet 95 for CBSNews: Childish Gambino's manager denies accusation of plagiarism over "This is America" https://t.co/k5lkfXMDsa https://t.co/x6YEYe09p7 
    
    Tweet 96 for CBSNews: Bronx teen reportedly killed over sex tape in apparent case of mistaken identity https://t.co/nptuyHK0hw https://t.co/dIN7oN3Vyv 
    
    Tweet 97 for CBSNews: "It's OK to not be OK": Suicide attempt survivors offer insight and advice https://t.co/Nlwy2gAiv8 https://t.co/d38pwNwugu 
    
    Tweet 98 for CBSNews: World War II hero Garlin Murl Conner's widow remembers his extraordinary life https://t.co/4yfPN9gLpd https://t.co/gCcEJh3yTg 
    
    Tweet 99 for CBSNews: Prosecutors to retry ex-deputy's husband in fatal confrontation outside Denny's https://t.co/RumlBZUX6i https://t.co/mZnKR2n7gM 
    
    Tweet 100 for CBSNews: 8th arrest in fatal stabbing of Bronx teenager outside bodega https://t.co/IoSKVBIVIf https://t.co/pkV0JUgMj7 
    
    Tweet 1 for CNN: "So many people across the country are inspired by this win and inspired about this race because of what it represe… https://t.co/VwrdWR4YPD 
    
    Tweet 2 for CNN: Money isn't everything in a political race “if you really understand your community," Alexandria Ocasio-Cortez says… https://t.co/aYylUfAQuq 
    
    Tweet 3 for CNN: Senate Democrats are powerless to stop Trump SCOTUS pick https://t.co/wR3A8bDIJj | Analysis by Chris Cillizza https://t.co/XoMCpBzzJa 
    
    Tweet 4 for CNN: Ben Jealous, a former NAACP leader endorsed by Bernie Sanders, moved a step closer to becoming Maryland's first bla… https://t.co/2jUyBLvNIe 
    
    Tweet 5 for CNN: The Netherlands is banning face coverings, including burqas and niqabs, in public spaces such as schools, hospitals… https://t.co/VkwfiLLjXe 
    
    Tweet 6 for CNN: Google's eerily human phone bot is ready for the real world https://t.co/Y5dD19nsZR 
    
    Tweet 7 for CNN: Beer is being rationed in the UK because of a shortage of carbon dioxide https://t.co/K56oMw0jBP 
    
    Tweet 8 for CNN: Report highlights gender discrimination, lack of female representation in Justice Department https://t.co/BjDzDUUb9d https://t.co/OvyJmlPnJK 
    
    Tweet 9 for CNN: Trump "has been the one that has caused what we see happening today where people are trying to push back on his pol… https://t.co/X3vBWK988W 
    
    Tweet 10 for CNN: Trump "has been the one that has caused what we see happening today where people are trying to push back on his pol… https://t.co/zDfrHdUigV 
    
    Tweet 11 for CNN: When one of his customers was choking, this Chick-fil-A employee stepped in to save him https://t.co/zrAZWw7NNB https://t.co/ULfqKipgDB 
    
    Tweet 12 for CNN: Boeing's hypersonic passenger plane could get you from New York to London in 2 hours https://t.co/eqgR0d4td7 https://t.co/TQMnwnbR5Y 
    
    Tweet 13 for CNN: In the 9 months leading up to this weekend's presidential election in Mexico, 130 candidates have been killed… https://t.co/8bTYXy45eK 
    
    Tweet 14 for CNN: The Supreme Court “should be made up of people who can base their decisions on the law, the facts, precedent, and u… https://t.co/GU0B9jSyAn 
    
    Tweet 15 for CNN: Marrying a Syrian means breaking up with America, writes Anna Lekas Miller for @CNNOpinion https://t.co/I59xCsE5pp https://t.co/1PEt45Z5yg 
    
    Tweet 16 for CNN: Secretary of State Mike Pompeo tells US lawmakers that North Korea remains a nuclear threat, but defends President… https://t.co/SEujGpN7RL 
    
    Tweet 17 for CNN: "Every time I'm talking with my mom, and she gives the phone to my baby brother, he doesn't know who I am."
    
    After… https://t.co/7L2mOZu40d 
    
    Tweet 18 for CNN: Broward County, where the Parkland attack happened, votes to put armed personnel in every school… https://t.co/tkE3SSn5MK 
    
    Tweet 19 for CNN: President Trump: When considering tariffs, think like a Harley-Davidson rider https://t.co/YytoocOaPb (via… https://t.co/NVgkt4rF0l 
    
    Tweet 20 for CNN: November is going to be a referendum on Trump, writes Errol Louis for @CNNOpinion https://t.co/xaQHAlTLG4 https://t.co/lAfobHCpZe 
    
    Tweet 21 for CNN: Migrant rescue ship Lifeline to dock in Malta after being stranded for 5 days in the Mediterranean… https://t.co/I42dGGKx3t 
    
    Tweet 22 for CNN: When one of his customers was choking, this Chick-fil-A employee stepped in to save him https://t.co/48G98T9vMe https://t.co/1y9RX8QOTG 
    
    Tweet 23 for CNN: Meet Alexandria Ocasio-Cortez, the 28-year-old Latina and Democratic socialist who is now a new face for the Democr… https://t.co/EnfaxwgKvZ 
    
    Tweet 24 for CNN: Here's everything you need to know about tonight's Strawberry Moon https://t.co/X51oi9eWCg https://t.co/HwR8rcSMEm 
    
    Tweet 25 for CNN: A man who couldn't swim sacrifices his life to save a boy from drowning https://t.co/WZcEuIuPkZ https://t.co/cFfikmBGY4 
    
    Tweet 26 for CNN: Why I'm burying a beer can in the backyard https://t.co/QaDmBv89Dg (via @CNNOpinion) https://t.co/QjtqRjVc45 
    
    Tweet 27 for CNN: Could life exist on Saturn's moon Enceladus? https://t.co/zOZbFyHXy5 https://t.co/tjHGMOnDQB 
    
    Tweet 28 for CNN: Texas steel pipe manufacturer becomes casualty of President Trump's trade war https://t.co/GOaXARleoc https://t.co/WKs6n7eZFV 
    
    Tweet 29 for CNN: Senate Judiciary Chairman Chuck Grassley dismisses calls by Democrats to punt on a Supreme Court nominee until afte… https://t.co/2B6PN5vYOD 
    
    Tweet 30 for CNN: Democratic congressional candidate Alexandria Ocasio-Cortez endorses New York gubernatorial hopeful Cynthia Nixon,… https://t.co/CflSvxUXkE 
    
    Tweet 31 for CNN: Democratic Sen. Dianne Feinstein urges Congress to wait until after the midterm elections to select a replacement f… https://t.co/Wgnd7tE6op 
    
    Tweet 32 for CNN: Justice Anthony Kennedy's retirement just confirmed every Republican's dream scenario for President Trump… https://t.co/Hyc8OoSgai 
    
    Tweet 33 for CNN: Senate Majority Leader Mitch McConnell says his chamber will work to replace Justice Anthony Kennedy before the mid… https://t.co/hTIcbbfWmh 
    
    Tweet 34 for CNN: These are potential Supreme Court nominees that could replace Justice Kennedy https://t.co/6zYySjh2dJ https://t.co/0en7ks7H7U 
    
    Tweet 35 for CNN: "They are conservative ideologues, not mainstream jurists. We cannot and will not accept them to serve on the highe… https://t.co/1MbxoP3I2A 
    
    Tweet 36 for CNN: "Our Republican colleagues in the Senate should follow the rule they set in 2016 — not to consider a Supreme Court… https://t.co/hLVPGqvI4b 
    
    Tweet 37 for CNN: Read Justice Anthony Kennedy's retirement letter to President Trump https://t.co/ayuwi97MR2 https://t.co/xlWFrpWZaB 
    
    Tweet 38 for CNN: Republican Sen. Chuck Grassley hails Justice Kennedy's service, saying he is a "staunch defender of First Amendment… https://t.co/X1AXlSA5i8 
    
    Tweet 39 for CNN: Democratic Sen. Dick Durbin has called on the Senate to wait to consider Trump's nominee to replace Justice Kennedy… https://t.co/MCnrcADQS6 
    
    Tweet 40 for CNN: "Now we’ll have to find a worthy successor." Republican Sen. Lindsey Graham says President Trump has a lot of "good… https://t.co/h6wPu3lo2G 
    
    Tweet 41 for CNN: President Trump says he has a list of 25 people that will be considered to replace Justice Anthony Kennedy on the S… https://t.co/pzUY6F4e9W 
    
    Tweet 42 for CNN: "He’s been a great justice of the Supreme Court." President Trump took a few moments to address the retirement of S… https://t.co/222pifAMgX 
    
    Tweet 43 for CNN: "We will vote to confirm Justice Kennedy's successor this fall," says Majority Leader Sen. Mitch McConnell after Ju… https://t.co/jjzm56eBil 
    
    Tweet 44 for CNN: President Trump will push for the swift confirmation of a Supreme Court justice "before the midterm elections," a s… https://t.co/GoJKdqOTN5 
    
    Tweet 45 for CNN: Here's a brief timeline of Justice Anthony Kennedy's key Supreme Court decisions https://t.co/0k0RUeFosd https://t.co/282cDaGB6d 
    
    Tweet 46 for CNN: A Japanese spacecraft has reached a diamond-shaped asteroid three years after setting off on its mission to learn a… https://t.co/XJLb6zE2NH 
    
    Tweet 47 for CNN: Anthony Kennedy's decision to step down from the Supreme Court gives President Trump a second opportunity to nomina… https://t.co/UqUIT7CLb7 
    
    Tweet 48 for CNN: House Democrats are in shock as they assess what Joe Crowley's loss to a 28-year-old political newcomer means for l… https://t.co/B3auAMM2Bl 
    
    Tweet 49 for CNN: BREAKING: Justice Anthony Kennedy, a conservative who provided key votes for same sex-marriage, abortion access and… https://t.co/p9Jn6p6BL2 
    
    Tweet 50 for CNN: JUST IN: House overwhelmingly rejects Republican immigration bill, despite last-minute push by President Trump to s… https://t.co/6lHY4YY0Yp 
    
    Tweet 51 for CNN: This Colorado Democrat could become first openly gay man elected governor in US https://t.co/hgiOXjsOUB https://t.co/H6aSP5gMYo 
    
    Tweet 52 for CNN: Here's what we've learned about 'Oumuamua, the cigar-shaped interstellar visitor that was spotted in October tumbli… https://t.co/MgMOwK1wWc 
    
    Tweet 53 for CNN: A funeral was held for Junior Guzman-Feliz, a 15-year-old killed in a gang stabbing in New York last week that has… https://t.co/HADmIUGcnh 
    
    Tweet 54 for CNN: What does America's falling birth rate mean for the economy? Just look at Arizona https://t.co/Oy7GT3RhoB https://t.co/xE4NFTGRLL 
    
    Tweet 55 for CNN: In a six-day span, only six children were reunited with their families after being separated at the US border. More… https://t.co/zEFZtN4Gg4 
    
    Tweet 56 for CNN: A federal grand jury indicted the suspect behind last summer's deadly vehicle incident in Charlottesville, Virginia… https://t.co/B9BJhAMrU3 
    
    Tweet 57 for CNN: BREAKING: Joe Jackson, the patriarch who launched the Jackson family dynasty, has died, a source close to the famil… https://t.co/WefGb7Q7gb 
    
    Tweet 58 for CNN: President Trump is speaking at a White House event after the Supreme Court's union ruling 
    
    Watch live: https://t.co/T3E0vuOqsj 
    
    Tweet 59 for CNN: Changes to a 16th-century polychrome statue of San Jorge (St George) provoked anger among some art experts and inev… https://t.co/gj2iwiHKxA 
    
    Tweet 60 for CNN: A 6-year-old's lemonade stand helped raise $13,000 for separated migrant families https://t.co/UjkonfhV3X https://t.co/gV1W52XK3y 
    
    Tweet 61 for CNN: Senate Majority Leader Mitch McConnell says the win by Alexandria Ocasio-Cortez, a 28-year-old running her first ca… https://t.co/OZDGwAhTJe 
    
    Tweet 62 for CNN: A judge denied rapper Meek Mill's petition for a new trial, despite the district attorney's office recommending tha… https://t.co/BFQhWcfekN 
    
    Tweet 63 for CNN: The Smithsonian has unveiled a design for the National Native American Veterans Memorial, which will be placed on t… https://t.co/dCwD3oAtJ7 
    
    Tweet 64 for CNN: Facebook has abandoned an ambitious plan to design and produce its own drones. https://t.co/OsmYnonbis 
    
    Tweet 65 for CNN: Former government contractor Reality Winner pleads guilty to leaking classified material https://t.co/xPDaOkB47K https://t.co/V4FIWATsB2 
    
    Tweet 66 for CNN: "We are committing human rights abuses on this border in separating children from their families," says New York co… https://t.co/0JsvHEAZXn 
    
    Tweet 67 for CNN: White House press secretary Sarah Sanders is expected to receive Secret Service protection https://t.co/J9L7pDzbIs https://t.co/kF76b1GP2b 
    
    Tweet 68 for CNN: The Virginia restaurant owner who asked White House press secretary Sarah Sanders to leave has resigned from the to… https://t.co/LlHIYmjiGB 
    
    Tweet 69 for CNN: Alexandria Ocasio-Cortez's win will likely make her the youngest person in Congress in 2019 https://t.co/pMUjLQSfR6 https://t.co/zMoh38VPDb 
    
    Tweet 70 for CNN: JUST IN: The Supreme Court deals a major blow to public-sector unions in a case that could shake their financial st… https://t.co/WesRgtLab3 
    
    Tweet 71 for CNN: The restaurant owner who asked Sarah Sanders to leave has resigned from the top post of a local business group https://t.co/etysLMTrW7 
    
    Tweet 72 for CNN: A Japanese spacecraft has reached a diamond-shaped asteroid three years after setting off on its mission to learn a… https://t.co/U0XVLYP4pB 
    
    Tweet 73 for CNN: "We are committing human rights abuses on this border in separating children from their families," says New York co… https://t.co/9OTv5cGPUg 
    
    Tweet 74 for CNN: RT @CNNPolitics: Alexandria Ocasio-Cortez will not say if she would support Nancy Pelosi for speaker if she wins in November and Democrats… 
    
    Tweet 75 for CNN: RT @CNNPolitics: "We won because we organized. We won because I think we had a very clear, winning message and we took that message to door… 
    
    Tweet 76 for CNN: New York Democrat Alexandria Ocasio-Cortez discusses her primary night win. Watch live: https://t.co/vhkaPaA3uB https://t.co/lYNj8K8WhK 
    
    Tweet 77 for CNN: What Alexandria Ocasio-Cortez's victory says about the Democratic Party and 2020 | Analysis by Harry Enten… https://t.co/pnoOjHEmb3 
    
    Tweet 78 for CNN: JUST IN: A Pittsburgh-area officer has been charged with criminal homicide in the death of Antwon Rose, an unarmed… https://t.co/rVPbXFSYLP 
    
    Tweet 79 for CNN: On the Mexico border, Latino Republicans back President Trump's immigration plans https://t.co/M0cK75CTAv https://t.co/4KaNigqwhb 
    
    Tweet 80 for CNN: JUST IN: White House decides against outright limits on Chinese investment https://t.co/MqMrx3PyoJ https://t.co/vdhUECfX8v 
    
    Tweet 81 for CNN: Mars is often referred to as the Red Planet, but pictures from one of NASA's orbiters showed what appeared to be a… https://t.co/9KBq3JSYch 
    
    Tweet 82 for CNN: A mother has shot a man who flew from New Zealand to the US to confront her 14-year-old daughter whom he had met on… https://t.co/IBRznGQjVE 
    
    Tweet 83 for CNN: A piece of chewing gum, a bottle of water and new DNA technology may have just solved a teacher's murder… https://t.co/mZz14hTK6f 
    
    Tweet 84 for CNN: Galvanized by the issue of teachers pay and school funding, Oklahoma teachers marched and protested in the state Ca… https://t.co/hZy59EsrpY 
    
    Tweet 85 for CNN: A fire raging in northern England has prompted the evacuation of dozens of homes and forced firefighters to work in… https://t.co/UUW42Sxcz3 
    
    Tweet 86 for CNN: US President Donald Trump's national security adviser John Bolton will meet Russian President Vladimir Putin during… https://t.co/jw627xJ1i3 
    
    Tweet 87 for CNN: A British heterosexual couple who objected to the "patriarchal" institution of marriage have won a legal claim for… https://t.co/RhJZs9Z514 
    
    Tweet 88 for CNN: If a progressive war against the Democratic establishment is coming, Tuesday's primaries were the first shots fired https://t.co/SPDWqYPGM5 
    
    Tweet 89 for CNN: US companies operating in China are likely to find themselves in the firing line as the trade fight between Washing… https://t.co/lQSvlqDtS8 
    
    Tweet 90 for CNN: Football legend Diego Maradona has reassured fans that he is fine after he was treated by doctors during Argentina'… https://t.co/n9BL7HWXy3 
    
    Tweet 91 for CNN: US Secretary Defense James Mattis met with Chinese President Xi Jinping inside the Great Hall of the People in Beij… https://t.co/Cy7Eo2ikbv 
    
    Tweet 92 for CNN: She is only ranked 183rd in the world, but Serena Williams has been seeded 25th for next week's Wimbledon Champions… https://t.co/oZGjkfYyca 
    
    Tweet 93 for CNN: Cave rescuers are "working around the clock" to try and locate a group of missing teenage soccer players and their… https://t.co/r4GDBZ1hm1 
    
    Tweet 94 for CNN: This is the moment Alexandria Ocasio-Cortez, a 28-year-old Latina running her first campaign, discovered she had ou… https://t.co/UaTHY1RP3P 
    
    Tweet 95 for CNN: In Utah, 2012 Republican presidential nominee Mitt Romney won the Senate primary and is now poised to cruise to ele… https://t.co/Ah9X2iQRKq 
    
    Tweet 96 for CNN: What it's like in the 7 countries on Trump's travel ban list https://t.co/h8rOqzGYEd https://t.co/FQy0qLkZVq 
    
    Tweet 97 for CNN: From the brink of defeat and a humiliating World Cup exit, Argentina survive and live on at Russia 2018… https://t.co/jNDeYp8vWs 
    
    Tweet 98 for CNN: Alexandria Ocasio-Cortez's win on Tuesday caps off a remarkable ascent -- which will likely make her the youngest p… https://t.co/QNWF6Wa0W7 
    
    Tweet 99 for CNN: A mother has shot a man who flew from New Zealand to the US to confront her 14-year-old daughter whom he had met on… https://t.co/CW3exdNZ4W 
    
    Tweet 100 for CNN: Trump plots controversial Putin meeting and leaves NATO allies guessing https://t.co/f7d4Kag4nD https://t.co/mOC6nzJyz4 
    
    Tweet 1 for FoxNews: President @realDonaldTrump: "The travel ban ruling underscores just how critical it is to confirm judges who will s… https://t.co/QFsqDLlzVd 
    
    Tweet 2 for FoxNews: President @realDonaldTrump: "A vote for any Democrat in November is a vote for @SenSchumer, @NancyPelosi and… https://t.co/GGTJanlJks 
    
    Tweet 3 for FoxNews: President @realDonaldTrump: "You need a senator who doesn't just talk like they're from North Dakota, but votes lik… https://t.co/4tQNXEc1Mp 
    
    Tweet 4 for FoxNews: President @realDonaldTrump: "ObamaCare is essentially dead." https://t.co/SVlX3KlugG 
    
    Tweet 5 for FoxNews: President @realDonaldTrump on health care: "We are coming out with so many health care plans that are so much bette… https://t.co/OD7MVeoXoU 
    
    Tweet 6 for FoxNews: .@RepKevinCramer: "All I can say is, Mr. President, on behalf of all of the thousands of people in this arena, and… https://t.co/uIogWwz8h0 
    
    Tweet 7 for FoxNews: .@POTUS holds a "Make America Great Again" rally in Fargo, North Dakota. https://t.co/Bxk0nLbwIj 
    
    Tweet 8 for FoxNews: .@BenShapiro on Socialist Who Upset NY Primary: Just Like Bernie, She Has Radical Ideas That Can Never Be Paid For. https://t.co/f64BRv8hzG 
    
    Tweet 9 for FoxNews: Bill Shine, former Fox News co-president, to take on senior communications role at White House. https://t.co/33ZNi2jUTA 
    
    Tweet 10 for FoxNews: Firefighters in Maine helped a 97-year-old widow of a World War II veteran with the patriotic task of raising a new… https://t.co/x1hWo6uK5N 
    
    Tweet 11 for FoxNews: .@gen_jackkeane on upcoming @POTUS meeting with Russian President Putin: "A meeting like this does give [Putin] a s… https://t.co/GTThjAfrpC 
    
    Tweet 12 for FoxNews: .@RepGoodlatte on the hearing with embattled FBI agent Peter Strzok: "Unfortunately the FBI counsel in the room has… https://t.co/8wNf54TZZL 
    
    Tweet 13 for FoxNews: .@benshapiro: "I think the next wave of Democrats are going to be much closer @BernieSanders brand Democrats than e… https://t.co/wh7X126Fcz 
    
    Tweet 14 for FoxNews: .@POTUS arrives in Fargo, North Dakota for a campaign rally. (Courtesy: KXJB) https://t.co/z4rJZ3bwor 
    
    Tweet 15 for FoxNews: Reacting to the retirement of Supreme Court Justice Kennedy, @SenSchumer said that Republicans "in the Senate shoul… https://t.co/7tVMU2Kosh 
    
    Tweet 16 for FoxNews: Nonprofit operator of shelters for immigrant kids tells of bomb threats, staff harassment. https://t.co/PqbaVSGv0X 
    
    Tweet 17 for FoxNews: .@mercedesschlapp on a time frame for @POTUS' Supreme Court justice nomination: "He wants to move quickly on this."… https://t.co/LwxRvkhK0B 
    
    Tweet 18 for FoxNews: .@mercedesschlapp on @POTUS' meeting with Justice Kennedy: "The president was incredibly thankful for Justice Kenne… https://t.co/io1XItu3Ep 
    
    Tweet 19 for FoxNews: New York Times details conditions of Obama-era family detention center: 'No place for human beings' https://t.co/hhjytlYXjl 
    
    Tweet 20 for FoxNews: Charles Hurt on replacing Justice Kennedy: "The greatest 'Never-Trumper' has to admit that Neil Gorsuch was a huge… https://t.co/yLgXv8VXm2 
    
    Tweet 21 for FoxNews: .@jonathanvswan on replacing Justice Kennedy: "[@POTUS] now knows both the political force of this decision and the… https://t.co/1H2j2UyO4J 
    
    Tweet 22 for FoxNews: Maine firefighters help military widow, 97, 'proudly' raise American flag https://t.co/Hvnk9wlZIx 
    
    Tweet 23 for FoxNews: President @realDonaldTrump is traveling the country to endorse candidates in the GOP primaries. @pdoocy has the sto… https://t.co/wWNBysi26Q 
    
    Tweet 24 for FoxNews: Justice Anthony Kennedy in 1988: "It is appropriate to recognize an essential truth, and that is that the Constitut… https://t.co/6aQ8yI8sf5 
    
    Tweet 25 for FoxNews: A political storm is brewing as President @realDonaldTrump looks to replace Supreme Court Justice Anthony Kennedy.… https://t.co/XLRzMUOUKh 
    
    Tweet 26 for FoxNews: A seat on the Supreme Court is opening up as Justice Anthony Kennedy gets ready to retire. @ShannonBream has the la… https://t.co/M273ec1d6V 
    
    Tweet 27 for FoxNews: Leonard Leo on Justice Kennedy retiring: "[@POTUS] had enormous success in nominating Neil Gorsuch to the court. An… https://t.co/kbcddSdAfX 
    
    Tweet 28 for FoxNews: New York man witnesses daughter's marriage days before losing battle to cancer https://t.co/hZrWXHR7dV 
    
    Tweet 29 for FoxNews: THURSDAY: @BretBaier and @marthamaccallum moderate the Florida GOP gubernatorial debate at 6:30p ET on Fox News Cha… https://t.co/RDhzC2eu3Z 
    
    Tweet 30 for FoxNews: Hawaii emergency workers slept on the job, emails showed in aftermath of the fake missile alert. https://t.co/EVzIMJzvge 
    
    Tweet 31 for FoxNews: Maxine Waters, Kathy Griffin, Samantha Bee, others targeted in RNC campaign ad criticizing the 'unhinged left' https://t.co/vnWVPRywel 
    
    Tweet 32 for FoxNews: Janoris Jenkins' brother is charged with manslaughter in the death at the NFL star's home, officials say. https://t.co/4L0kg5khCb 
    
    Tweet 33 for FoxNews: Moments ago, @VP thanked Justice Anthony Kennedy for his service on the U.S. Supreme Court following Kennedy's anno… https://t.co/45qnpf5Nrf 
    
    Tweet 34 for FoxNews: .@kimguilfoyle on @repjoecrowley's primary loss: "He should have showed up for everything and not mailed it in, he… https://t.co/yMKIiA2aLb 
    
    Tweet 35 for FoxNews: California man, 77, accused of killing fire captain, charged with capital murder. https://t.co/sSc72Q4prH 
    
    Tweet 36 for FoxNews: .@JesseBWatters: "This definitely moves the court to the right and it really puts the pressure on [Justice] Ginsbur… https://t.co/UHqvV4zFkv 
    
    Tweet 37 for FoxNews: An all-new season of 'OBJECTified' premieres this Sunday with NBA legend @MagicJohnson! Tune in to Fox News Channel… https://t.co/1Q0L8B3ZKj 
    
    Tweet 38 for FoxNews: Benghazi mastermind sentenced to 22 years in prison on federal terrorism charges. https://t.co/33Y6lI7LAE 
    
    Tweet 39 for FoxNews: Janoris Jenkins' brother is person of interest in death at NFL star's home, reports say https://t.co/q7Y9XdOY5l 
    
    Tweet 40 for FoxNews: .@SenSchumer Demands Congress Use 'Biden Rule' in Choosing Kennedy Replacement https://t.co/gyJCSfYRGq 
    
    Tweet 41 for FoxNews: Bob Vander Plaats on Justice Kennedy retiring: "I think this is an opportunity to restore a culture of life in this… https://t.co/hzQHiOR22k 
    
    Tweet 42 for FoxNews: Bob Vander Plaats on Justice Kennedy retiring: "If [Justice Neil] Gorsuch is a standard, we'd like to see another G… https://t.co/VgYpLsLUNp 
    
    Tweet 43 for FoxNews: .@RandPaul on Justice Kennedy's retirement: "No matter who President @realDonaldTrump picks will be divided along p… https://t.co/GkyXVcBsrH 
    
    Tweet 44 for FoxNews: Who are the Supreme Court justices? https://t.co/0VMFK0PBoY 
    
    Tweet 45 for FoxNews: Tom Dupree: "Justice Kennedy has been the swing vote on the Supreme Court for the last decade plus. We are going to… https://t.co/QwQhPaCQYf 
    
    Tweet 46 for FoxNews: .@johnrobertsFox on Justice Kennedy retiring: "[@POTUS] has the opportunity to cement a 5-4 conservative majority a… https://t.co/1qcFCg8FtA 
    
    Tweet 47 for FoxNews: Supreme Court Justice Anthony Kennedy announced Wednesday that he's retiring at the end of July. @ShannonBream has… https://t.co/8mttwhZRbT 
    
    Tweet 48 for FoxNews: .@SenateMajLdr on Justice Kennedy retiring: "First and foremost, I want to pause and express our gratitude for the… https://t.co/vhk5eHGtCm 
    
    Tweet 49 for FoxNews: .@AmbJohnBolton visits Moscow to talk possible US-Russia summit @ShepNewsTeam https://t.co/q1k8BHCj3W https://t.co/MODPY7wg2A 
    
    Tweet 50 for FoxNews: Sen. @ChuckGrassley, chairman of @senjudiciary, speaks after the announcement of Supreme Court Justice Kennedy's re… https://t.co/ybqvasevub 
    
    Tweet 51 for FoxNews: North Korea continues construction of nuclear research facility despite agreement to 'denuclearize': report https://t.co/jmGYjmVDpv 
    
    Tweet 52 for FoxNews: Supreme Court Justice Kennedy in his retirement letter to @POTUS: "For a member of the legal profession it is the h… https://t.co/hFqMcH8XcJ 
    
    Tweet 53 for FoxNews: Kennedy replacement could face battles seen by the hotly contested nominations of Bork and Thomas. https://t.co/NkZZl3fR3L 
    
    Tweet 54 for FoxNews: .@SenSchumer: "Our Republican colleagues in the Senate should follow the rule they set in 2016: not to consider a S… https://t.co/0YuO4g9srk 
    
    Tweet 55 for FoxNews: Supreme Court Justice Anthony Kennedy released this statement Wednesday after announcing his retirement.… https://t.co/pQWz7XYB7u 
    
    Tweet 56 for FoxNews: Chris Wallace on Justice Kennedy's retirement and the next Supreme Court pick: "I think this is the biggest moment… https://t.co/EQiWkTYJu7 
    
    Tweet 57 for FoxNews: .@SenateMajLdr on Justice Kennedy retiring: "Today the Senate and the nation thank Justice Kennedy for his years of… https://t.co/BqOAYAW39y 
    
    Tweet 58 for FoxNews: President @realDonaldTrump on immigration: "We believe in very strong borders, no crime. And the Democrats believe… https://t.co/g3kBid4vX0 
    
    Tweet 59 for FoxNews: President @realDonaldTrump on meeting with Vladimir Putin: "It would look like we will probably be meeting sometime… https://t.co/VVuUqncwry 
    
    Tweet 60 for FoxNews: President @realDonaldTrump on immigration: "We believe that families should be together." https://t.co/Rdhl3AQGWv 
    
    Tweet 61 for FoxNews: President @realDonaldTrump: "We have a list of 25 people that I actually had during my election."… https://t.co/Jg9saPTf1E 
    
    Tweet 62 for FoxNews: President @realDonaldTrump on Justice Kennedy retiring: "Hopefully we're gonna pick somebody who will be as outstan… https://t.co/3Df7Rh5Gpu 
    
    Tweet 63 for FoxNews: President @realDonaldTrump on Justice Kennedy retiring: "We will begin our search for a new justice of the United S… https://t.co/kg0zzcBlS4 
    
    Tweet 64 for FoxNews: President @realDonaldTrump on Justice Kennedy retiring: "He is a man who has displayed tremendous vision and tremen… https://t.co/Wr8WzbxJZD 
    
    Tweet 65 for FoxNews: President @realDonaldTrump on Justice Kennedy retiring: "He's a man that I've known for a long time and a man that… https://t.co/VTE5XuJPMs 
    
    Tweet 66 for FoxNews: .@SenateMajLdr: "It's imperative that @POTUS' nominee be considered fairly and not subjected to personal attacks."… https://t.co/xJChrD9tC3 
    
    Tweet 67 for FoxNews: .@SenateMajLdr: "As in the case of Justice Gorsuch, senators will have the opportunity to meet with @POTUS' nominee… https://t.co/YIL0l6JHaT 
    
    Tweet 68 for FoxNews: .@POTUS speaks as Justice Anthony Kennedy says he's retiring effective July 31. https://t.co/7Do7LBbAzT  https://t.co/N78qS5Orid 
    
    Tweet 69 for FoxNews: .@SenateMajLdr: "We will vote to confirm Justice Kennedy's successor this fall." https://t.co/7Do7LBbAzT https://t.co/tnxDRWAfdx 
    
    Tweet 70 for FoxNews: .@SenateMajLdr: "The Senate stands ready to fulfill its constitutional role by offering advice and consent on Presi… https://t.co/Y3SuRrRslS 
    
    Tweet 71 for FoxNews: .@SenateMajLdr: "As Justice Kennedy concludes his tenure on the court, we wish him, his wife Mary and their family… https://t.co/opa1tx9wTQ 
    
    Tweet 72 for FoxNews: Chris Wallace on Justice Kennedy retiring: "A Supreme Court nominee can either be a huge legacy builder for a presi… https://t.co/30pMea3hUI 
    
    Tweet 73 for FoxNews: Chris Wallace on Justice Kennedy retiring: "Replacing him with a solid conservative is enormously important."… https://t.co/A2qQOmui4P 
    
    Tweet 74 for FoxNews: Justice Kennedy announces plan to retire https://t.co/7Do7LBbAzT @dailybriefing https://t.co/SVSrt1St0V 
    
    Tweet 75 for FoxNews: Justice Kennedy announces plan to retire https://t.co/7Do7LBbAzT https://t.co/9qB5Mn3u41 
    
    Tweet 76 for FoxNews: Supreme Court Justice Anthony Kennedy says he's retiring effective July 31. Kennedy stepping down would mark a seco… https://t.co/O7D0XkDXsw 
    
    Tweet 77 for FoxNews: BREAKING NEWS: Supreme Court Justice Anthony Kennedy to retire. https://t.co/7Do7LBbAzT https://t.co/3BWyEvTm8k 
    
    Tweet 78 for FoxNews: .@GOP compromise immigration bill defeated on House floor https://t.co/PFqehcwp8b 
    
    Tweet 79 for FoxNews: Strawberry Moon and Saturn to put on dazzling display this week https://t.co/dQRUiwUF78 
    
    Tweet 80 for FoxNews: House voting on @GOP immigration bill #OutnumberedOT https://t.co/pf5VaiSrVR 
    
    Tweet 81 for FoxNews: Delaware police find abandoned home -- in the middle of the road
    https://t.co/vMOSNb2IXE 
    
    Tweet 82 for FoxNews: THURSDAY: @BretBaier and @marthamaccallum moderate the Florida GOP gubernatorial debate at 6:30p ET on Fox News Cha… https://t.co/dVtQIGyy27 
    
    Tweet 83 for FoxNews: Halo Top is 'dramatically' under-filling pints, lawsuit alleges https://t.co/KKweNTKPFU 
    
    Tweet 84 for FoxNews: University ends restrictive campus speech policy after student group's lawsuit (via @calebparke) https://t.co/4zxwcTSwFx 
    
    Tweet 85 for FoxNews: OPINION: @LizPeek: Trump's success has Democrats freaking out – But that's still no excuse for bad behavior https://t.co/A4EzI9jySn 
    
    Tweet 86 for FoxNews: Joe Jackson's life and career: 3 things to know about the famous patriarch https://t.co/LDYI7aaZfX 
    
    Tweet 87 for FoxNews: RT @FoxBusiness: .@POTUS: "Thanks to our massive tax cuts, young men and women entering the workforce are keeping more and more of the mone… 
    
    Tweet 88 for FoxNews: RT @FoxBusiness: .@POTUS: "Unemployment for people under the age of 24 is the lowest in almost 50 years." https://t.co/BkFj7J9Xmy 
    
    Tweet 89 for FoxNews: RT @FoxBusiness: .@POTUS: "Our economy is booming. Confidence is soaring. There's never been a  better time to be young and to be American.… 
    
    Tweet 90 for FoxNews: Joe Jackson reportedly dead at 89: Celebs react to the loss of the famous patriarch https://t.co/xD7E4YtygS https://t.co/WDW1ZThHBY 
    
    Tweet 91 for FoxNews: RT @FoxBusiness: .@POTUS: "We must honor and respect our great American Flag." https://t.co/HMkUF7dw7Y 
    
    Tweet 92 for FoxNews: RT @FoxBusiness: .@POTUS: "You have to believe in protecting the entire Constitution, as written, including the right to free speech. And t… 
    
    Tweet 93 for FoxNews: RT @FoxBusiness: .@POTUS: "We believe in free speech on college campuses, not censorship. Institutions of higher learning should be forms f… 
    
    Tweet 94 for FoxNews: RT @FoxBusiness: .@POTUS: "From a military standpoint, space. You know all about 'space force.' Space is a very big factor in the Trump adm… 
    
    Tweet 95 for FoxNews: JUST IN: Man accused of driving into crowd at Charlottesville rally, killing 1 person, charged with federal hate cr… https://t.co/aS4zIhAcGy 
    
    Tweet 96 for FoxNews: U.S. National Security Advisor John Bolton holds a news conference. https://t.co/kzBKUo0UVJ 
    
    Tweet 97 for FoxNews: .@POTUS delivers remarks at the "Face-to-Face With Our Future" event. https://t.co/CmtgwMhNMK 
    
    Tweet 98 for FoxNews: RT @FoxBusiness: Larry Kudlow: "President Trump is a trade reformer...Don't blame him for all the evils and the breakdown of the WTO and ot… 
    
    Tweet 99 for FoxNews: RT @FoxBusiness: Larry Kudlow: "[President Trump] is a free trader and he would like to see a new world trading system. The current one is… 
    
    Tweet 100 for FoxNews: RT @FoxBusiness: Larry Kudlow on his health: "I feel great. Great to be back. To quote one of my heroes Mark Twain: 'Rumors of my demise we… 
    
    Tweet 1 for nytimes: On a big day in the World Cup, here’s a diversion: We removed the ball from photos of group-stage games. See if you… https://t.co/PjBxxz2DxG 
    
    Tweet 2 for nytimes: RT @emilybazelon: Well, here are my thoughts on the retirement of Justice Kennedy.
    
    https://t.co/4vEYBgHMZK 
    
    Tweet 3 for nytimes: A Kansas City immigration lawyer said she broke her foot after being pushed to the ground by an ICE officer. She wa… https://t.co/utMRWvXuEX 
    
    Tweet 4 for nytimes: The front-runners and full list of potential Supreme Court nominees https://t.co/zxRZ41GWLu 
    
    Tweet 5 for nytimes: Terry Crews says he won't be in "The Expendables 4" after a producer tried to get him to drop his sexual assault la… https://t.co/zTlHKBR7KL 
    
    Tweet 6 for nytimes: RT @nytopinion: My father, Fred Korematsu, would have been upset that the court overturned his case only to uphold President Trump’s travel… 
    
    Tweet 7 for nytimes: In 1983, the slashed, scarred body of a 23-year-old black man was discovered in a grassy roadside area in a Georgia… https://t.co/k51to4KlDm 
    
    Tweet 8 for nytimes: Evening Briefing: Here's what you need to know at the end of the day https://t.co/ejfYV4pKni 
    
    Tweet 9 for nytimes: The world’s tropical forests lost roughly 39 million acres of trees last year, an area roughly the size of Banglade… https://t.co/3xx3rdpeNY 
    
    Tweet 10 for nytimes: RT @nytvideo: “Women like me aren’t supposed to run for office,” Alexandria Ocasio-Cortez said in a campaign video last month. In a stunnin… 
    
    Tweet 11 for nytimes: Germany, the defending World Cup champion, took its earliest exit from the tournament since 1938 https://t.co/e0hFEMidIb 
    
    Tweet 12 for nytimes: RT @NYTSports: For women who work as sports reporters, #MeToo isn’t just a movement, it’s often their everyday reality. https://t.co/o0YbUp… 
    
    Tweet 13 for nytimes: 13 years after escaping from a Wichita zoo, No. 492 is the flamingo that keeps on surviving https://t.co/7uhrgQx1hJ 
    
    Tweet 14 for nytimes: RT @malachybrowne: A peek behind our investigation into claims by Syrian and Russian officials that the chemical weapons attack in Douma on… 
    
    Tweet 15 for nytimes: A year and a half after a New York Times correspondent was kicked out of Venezuela, he returned to see how people a… https://t.co/7jChD5QJC5 
    
    Tweet 16 for nytimes: On the streets of Caracas, homeless kids play with a wad of bolívar bills like it’s Monopoly money. All of this isn… https://t.co/a27fQZPuyJ 
    
    Tweet 17 for nytimes: Runaway inflation has thrown Venezuela into chaos and made food and medicine desperately scarce… https://t.co/p8Vk9of1Z1 
    
    Tweet 18 for nytimes: The police officer who killed Antwon Rose failed basic police procedures and made statements to investigators that… https://t.co/yLyFUvUOwL 
    
    Tweet 19 for nytimes: Trump administration officials that it would be difficult to comply with the timetable in a federal court order req… https://t.co/WnK6hCWr9w 
    
    Tweet 20 for nytimes: Stories of how we communicate about sex and intimacy are rare. That’s where you come in. https://t.co/WgP4PnJa0m 
    
    Tweet 21 for nytimes: Breaking News: Senate Majority Leader Mitch McConnell promised a quick vote on a Supreme Court nominee by fall. Dem… https://t.co/5TmPPJ6Glh 
    
    Tweet 22 for nytimes: Teachers’ unions could lose up to a third of their members and funding as a result of the Supreme Court decision https://t.co/cPDS7sOlgc 
    
    Tweet 23 for nytimes: Thousands of fans gathered in Florida for a memorial service to mourn the controversial rapper XXXTentacion https://t.co/S7EzgTBuL1 
    
    Tweet 24 for nytimes: RT @nytopinion: What does the Supreme Court decision on unions mean? Several takes here:
    
    "Workers are standing up and fighting, and they h… 
    
    Tweet 25 for nytimes: Mitch McConnell said the Senate would vote to replace Justice Anthony Kennedy this fall https://t.co/DbdzxTgpnE 
    
    Tweet 26 for nytimes: Switzerland dominated possession in the first half of their match against Costa Rica. But as Germany showed earlier… https://t.co/DU2HxkLmhp 
    
    Tweet 27 for nytimes: Benicio Del Toro is now one of only a few Latinos to headline a film franchise released by Hollywood https://t.co/Uxz6HFiZhH 
    
    Tweet 28 for nytimes: There are over 100,000 people on the waiting list to join the dating app Raya https://t.co/FLQ5gZWbm5 
    
    Tweet 29 for nytimes: The U.S. Open is revamping its seeding process to protect women returning to the court after giving birth. Serena W… https://t.co/NULz1eKCTz 
    
    Tweet 30 for nytimes: Breaking News: Anthony Kennedy is retiring from the Supreme Court. He was often the swing vote, and President Trump… https://t.co/ojdg7urbeq 
    
    Tweet 31 for nytimes: Breaking News: The House overwhelmingly rejected a major immigration overhaul. A last-minute plea from President Tr… https://t.co/FaJ105bHjK 
    
    Tweet 32 for nytimes: Here’s a look at how each team can make the round of 16 https://t.co/FF4ZdmV9tn 
    
    Tweet 33 for nytimes: Both Brazil and Serbia are looking for a win in order to advance to the World Cup round of 16. Expect a competitive… https://t.co/R0oPoZy7sv 
    
    Tweet 34 for nytimes: A member of Brazil's soccer federation was sent home to Brazil after smashing a glass on a fan's head. And you thou… https://t.co/Y4Qp3sr2BZ 
    
    Tweet 35 for nytimes: Joe Jackson, the father and manager of the Jackson 5, has died https://t.co/ZWhxupoKYU 
    
    Tweet 36 for nytimes: The man accused of driving his car into people protesting a white supremacist rally in Charlottesville, Virginia wa… https://t.co/uxsXz1QqDB 
    
    Tweet 37 for nytimes: Breaking News: President Trump and President Vladimir Putin of Russia will hold a summit soon. The planned meeting… https://t.co/gdRwE4Gd1z 
    
    Tweet 38 for nytimes: Breaking News: The Justice Department approved Disney's $71 billion bid for 21st Century Fox's assets. The decision… https://t.co/zWAST0A14E 
    
    Tweet 39 for nytimes: Bill Shine, ousted from Fox News for his handling of sexual harassment scandals, is expected to be offered the top… https://t.co/TZhweMpySJ 
    
    Tweet 40 for nytimes: The California Supreme Court calls it a “barbaric” rule from a “bygone age." But the felony murder rule is still th… https://t.co/q7lRQibKIB 
    
    Tweet 41 for nytimes: Germany, the defending World Cup champion, lost to South Korea and failed to advance out of the group stage. Mexico… https://t.co/ath6QUMX4R 
    
    Tweet 42 for nytimes: Video review has come to the World Cup, and it probably just knocked the defending champion Germany out of the tour… https://t.co/Jl9sDRbvIG 
    
    Tweet 43 for nytimes: RT @nytopinion: Does Donald Trump fear foreigners invading America like he fears germs contaminating his body? Watch Episode 3 of @realtrum… 
    
    Tweet 44 for nytimes: Because Slack is down and you might have to actually talk to your coworkers ¯\_(ツ)_/¯ https://t.co/W52HIDHdEf 
    
    Tweet 45 for nytimes: A police officer was charged with criminal homicide in the fatal shooting of teenager Antwon Rose  https://t.co/0qvGG0RSQ4 
    
    Tweet 46 for nytimes: RT @randyNYT: Notice the accent marks on Mexico's World Cup jerseys? A New York Times editor @apchavira did that: https://t.co/7169yQMwqw 
    
    Tweet 47 for nytimes: Germany probably advances in the World Cup with a win, but might not, and probably doesn’t advance with a loss, but… https://t.co/jAi6tGii3T 
    
    Tweet 48 for nytimes: RT @HannaIngber: Our politics editor, @patrickhealynyt, is inviting readers to ask him questions about how we're covering the midterms. Ple… 
    
    Tweet 49 for nytimes: Russia demonstrated that one response to fielding an unwelcome question is to ask a different question. And another… https://t.co/uaabtuxMS1 
    
    Tweet 50 for nytimes: RT @mattfleg: Was just going back through some notes from our chat w/ @Ocasio2018 many weeks ago. This stood out: "There’s this weird mascu… 
    
    Tweet 51 for nytimes: "The violent act of a fan is sad," she wrote, but what is even worse, she added, is the reaction of those who do no… https://t.co/FYiFx0HKyj 
    
    Tweet 52 for nytimes: Mexico and Sweden are hoping to clinch advancement to the second round of World Cup. Chicharito (Javier Hernandez)… https://t.co/gad8LqyAW5 
    
    Tweet 53 for nytimes: RT @mwolgelenter: “The enemies of a meat-based diet want to consign humanity to grains.” @alissanyt, on French butchers seeking protection… 
    
    Tweet 54 for nytimes: Breaking News: The Supreme Court dealt a major blow to labor unions, ruling 5-4 that government workers can’t be re… https://t.co/Iyqs5AYU82 
    
    Tweet 55 for nytimes: RT @fstockman: A primer for what happened last night in NY. ‘Yes, I’m Running as a #Socialist.’ Why Candidates Are Embracing the Label in 2… 
    
    Tweet 56 for nytimes: RT @NYTSports: The Mexican player known as "Chucky" has been a nightmare for opponents at the World Cup. And there may be more like him on… 
    
    Tweet 57 for nytimes: The murals started appearing quietly in Paris last week. Now they're confirmed as the work of Banksy — and the race… https://t.co/eZoGJjSDeq 
    
    Tweet 58 for nytimes: The search for a dozen boys and their soccer coach trapped in a flooded cave complex has captivated Thailand https://t.co/1LQB1CFzM0 
    
    Tweet 59 for nytimes: A year and a half after a New York Times correspondent was kicked out of Venezuela, he returned to see how people a… https://t.co/HtNogoyDhd 
    
    Tweet 60 for nytimes: Morning Briefing: Here's what you need to know to start your day https://t.co/EfR5ZryQxl https://t.co/zqewCJApCz 
    
    Tweet 61 for nytimes: A shooting in which a woman gunned down four of her relatives, killing two, has rattled Hong Kong, a city where suc… https://t.co/xaDP4Jo42X 
    
    Tweet 62 for nytimes: President Trump has chosen a more moderate approach to limit Chinese investments in the United States, rejecting mo… https://t.co/K423hIY9vc 
    
    Tweet 63 for nytimes: "The unfortunate reality is that under the present system, migrant children are not accounted for with the same eff… https://t.co/bx2vRTeyEn 
    
    Tweet 64 for nytimes: A political revolution — or something like it — just rippled through New York City https://t.co/Y0F0wPNONI 
    
    Tweet 65 for nytimes: The Korematsu ruling was an exceedingly rare modern example in which the Supreme Court explicitly upheld government… https://t.co/yUWSZBmg3Y 
    
    Tweet 66 for nytimes: Justice Sonia Sotomayor condemned the travel ban as "harrowing" and "motivated by hostility and animus toward the M… https://t.co/JqxzB2lrOo 
    
    Tweet 67 for nytimes: RT @nytgraphics: Charts illustrating some of the effects of Trump's travel ban so far:  https://t.co/6a3wAmRUPn https://t.co/eqWjGnfI8r 
    
    Tweet 68 for nytimes: What the Supreme Court's endorsement of the travel ban says about the extent of the president's power https://t.co/jsDBQuSBQD 
    
    Tweet 69 for nytimes: Fact check: No, Democrats don't want "open borders" https://t.co/91CrZV9ahM 
    
    Tweet 70 for nytimes: Results for elections in 7 states https://t.co/MAme5UnNmP https://t.co/sXLPiAvuny 
    
    Tweet 71 for nytimes: "I knew that it was long odds, and I knew that it was uphill, but I always knew it was possible," Alexandria Ocasio… https://t.co/Nhy8yHPad6 
    
    Tweet 72 for nytimes: The seized items included $30 million in cash, 2,800 pairs of earrings, 2,200 rings, 2,100 bangles, 1,600 brooches,… https://t.co/zRJ8B871Xz 
    
    Tweet 73 for nytimes: Morning Briefing: Here's what you need to know to start your day https://t.co/aTMTe1uUWB https://t.co/e8MWX047Hr 
    
    Tweet 74 for nytimes: "The odds are that Trump will deliver a G-7 performance. And I fear that we will come out of this summit with symbo… https://t.co/ARkcwTr80i 
    
    Tweet 75 for nytimes: "It's surreal," Alexandria Ocasio-Cortez said as the votes were being tallied https://t.co/9QOMSSi0yQ 
    
    Tweet 76 for nytimes: "There was no divine intervention here. Just hard, human work. Argentina made it. Messi made it," @RorySmith writes https://t.co/4vq9QC4Yhc 
    
    Tweet 77 for nytimes: French butchers wrote that "physical, verbal, and moral violence” against them was "neither more nor less than a fo… https://t.co/ma5AGPkE3G 
    
    Tweet 78 for nytimes: RT @nytimesworld: Remember the "ecce homo" in Spain that was one of the worst restoration projects in modern history? It has new competitio… 
    
    Tweet 79 for nytimes: There's a lot of trash in the ocean these days. But which of these items is most frequently found on beaches?
    • Str… https://t.co/816BGF7zsk 
    
    Tweet 80 for nytimes: RT @nytimesworld: Malta says it will let a rescue ship carrying hundreds of African migrants dock — if other European countries agree to ta… 
    
    Tweet 81 for nytimes: McKinsey is a keeper of secrets the world over. But in South Africa, its culture of confidentiality helped ensnare… https://t.co/fe85ixkHpJ 
    
    Tweet 82 for nytimes: These photos from the World Cup are missing one important element – the ball. See if you can guess where it was.… https://t.co/yTduHCwFOO 
    
    Tweet 83 for nytimes: The murals started appearing quietly in Paris last week. Now they're confirmed as the work of Banksy — and the race… https://t.co/5a5tfayiCs 
    
    Tweet 84 for nytimes: 500 died. 50 villages destroyed. Tens of thousands displaced. Yet this is not a war zone. It is farm country in Nig… https://t.co/affhI8Tseq 
    
    Tweet 85 for nytimes: Who Is Alexandria Ocasio-Cortez? A Democratic Giant Slayer https://t.co/RKe0g4XUGF 
    
    Tweet 86 for nytimes: A dozen Australian politicians were treated to lavish overseas trips by a Chinese technology company that is alread… https://t.co/8vhhubGV8B 
    
    Tweet 87 for nytimes: RT @NYTScience: How spiders ride the wind https://t.co/OJJBFK9q1c https://t.co/xL9BUcotqG 
    
    Tweet 88 for nytimes: In Italy, Immigrants Evoke Fear, Not Racism https://t.co/kLelNBZD33 
    
    Tweet 89 for nytimes: Remember the "ecce homo" painting in Spain that was called one of the worst restoration projects in modern history?… https://t.co/wZkdcsNXEr 
    
    Tweet 90 for nytimes: RT @nytimesarts: "You are causing suffering and division," David Lynch wrote to President Trump on Facebook. https://t.co/LGrlem92wF 
    
    Tweet 91 for nytimes: President Trump has often lauded Harley-Davidson as a U.S. icon and job creator. Now he's lashing out over its plan… https://t.co/4GXnm6bdzP 
    
    Tweet 92 for nytimes: Scientists have captured the clearest and most detailed image yet of Zika. The work could contribute to the develop… https://t.co/Te0E7JwNZd 
    
    Tweet 93 for nytimes: RT @nytimesarts: The American Library Association is dropping Laura Ingalls Wilder’s name from a prestigious children’s literature award be… 
    
    Tweet 94 for nytimes: The U.S. must stop taking migrant children from their parents at the border and reunite separated families within 3… https://t.co/ROVpKjDX27 
    
    Tweet 95 for nytimes: McKinsey rolled the dice on South Africa and lost. Here’s the story behind the biggest mistake in the consulting fi… https://t.co/w7TlqHkQQy 
    
    Tweet 96 for nytimes: RT @nytpolitics: Chief Justice John Roberts spoke clinically. Justice Stephen Breyer spoke analytically. Then it was Justice Sonia Sotomayo… 
    
    Tweet 97 for nytimes: Rare White Alligator Stolen During Fire That Killed 43 Reptiles, Officials Say https://t.co/PniipSRw1Z 
    
    Tweet 98 for nytimes: Here's the 2018 election calendar 
    https://t.co/x9wJt4d8o3 
    
    Tweet 99 for nytimes: RT @nytopinion: From last week, the @nytopinion Editorial Board: Joseph Crowley has decades of experience that can serve his constituents w… 
    
    Tweet 100 for nytimes: Utah election live results
    https://t.co/90ls5wda5g 
    
    

Step 5: I create dataframes to hold the data extracted from the logic above, and clean the data.


```python
# Convert sentiments to DataFrame

sentiments_pd = pd.DataFrame.from_dict(sentiments)

# Replace the Twitter Handles with identifiable news outlets

sentiments_pd.News_Source = sentiments_pd.News_Source.replace({"BBCWorld":"BBC",
                                                               "CNN": "CNN",
                                                               "FoxNews":"Fox",
                                                               "nytimes" :"New_York_Times",
                                                               "CBSNews":"CBS"})
# Display the 5 outlets to validate

sentiments_pd["News_Source"].value_counts()
```




    CNN               100
    Fox               100
    CBS               100
    BBC               100
    New_York_Times    100
    Name: News_Source, dtype: int64




```python
# Rearrange the dataframe and define it in a new dataframe

sentiments_pd_clean = sentiments_pd[["News_Source","Tweet","Date","Compound","Positive","Neutral","Negative","Tweets_Ago"]]

sentiments_pd_clean.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 500 entries, 0 to 499
    Data columns (total 8 columns):
    News_Source    500 non-null object
    Tweet          500 non-null object
    Date           500 non-null object
    Compound       500 non-null float64
    Positive       500 non-null float64
    Neutral        500 non-null float64
    Negative       500 non-null float64
    Tweets_Ago     500 non-null int64
    dtypes: float64(4), int64(1), object(3)
    memory usage: 31.3+ KB
    

Step 5: I use seaborn libraries -lmplot, barplot - to visualize the results.


```python
# Define the lmplot structure

sns.set()

sns.set_context("notebook")

    
sns_plot1 = sns.lmplot( x="Tweets_Ago", y="Compound", data = sentiments_pd_clean,fit_reg=False, 
           hue="News_Source", legend=False, palette=dict(CBS="#0343df",Fox="#01ff07",CNN="#e50000",
                                                         BBC="#ed0dd9",New_York_Times="#fac205" ))

Today_Date = str(date.today())


# Label the plot and set the axes limit

Plot_Title = f"Sentiment Analysis of Media Tweets: {Today_Date}"

plt.title(Plot_Title)

plt.ylabel("Tweet Polarity")
plt.xlabel("Tweets Ago")

plt.xlim(105,-5)
plt.ylim(-1.2, 1.2)

plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0)

# Save the image and display

plt.savefig("../Images/TweetPolarity_TweetsAgo.png",bbox_inches="tight")

plt.show(sns_plot1)

```


![png](output_15_0.png)



```python
# Display the sentiments dataframe grouped by News_Source

sentiments_pd_grouped = sentiments_pd_clean.groupby(["News_Source"],as_index=False).mean()

sentiments_pd_grouped[["News_Source","Compound","Positive","Neutral","Negative"]]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>News_Source</th>
      <th>Compound</th>
      <th>Positive</th>
      <th>Neutral</th>
      <th>Negative</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BBC</td>
      <td>-0.005757</td>
      <td>0.09058</td>
      <td>0.11100</td>
      <td>0.79843</td>
    </tr>
    <tr>
      <th>1</th>
      <td>CBS</td>
      <td>0.049551</td>
      <td>0.10253</td>
      <td>0.08998</td>
      <td>0.80750</td>
    </tr>
    <tr>
      <th>2</th>
      <td>CNN</td>
      <td>0.090970</td>
      <td>0.10308</td>
      <td>0.06798</td>
      <td>0.82899</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Fox</td>
      <td>0.211329</td>
      <td>0.15845</td>
      <td>0.07510</td>
      <td>0.76642</td>
    </tr>
    <tr>
      <th>4</th>
      <td>New_York_Times</td>
      <td>-0.061773</td>
      <td>0.06710</td>
      <td>0.08917</td>
      <td>0.84375</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Define the lmplot structure

sns.set_style("darkgrid")

sns_plot2 = sns.barplot(x="News_Source", y="Compound", data=sentiments_pd_grouped,errwidth=0)

for index, row in sentiments_pd_grouped.iterrows():
    sns_plot2.text(row.name,-0.15, round(row.Compound,2), color='black', ha="center", rotation ='horizontal')

# Label the plot and set axes limit

Plot_Title = f"Overall Media Sentiment - Twitter: {Today_Date}"

plt.title(Plot_Title)

plt.ylim(-0.20, .1)

plt.xlabel("News Outlet")

plt.ylabel("Tweet Polarity")

# Save the image and display

plt.savefig("../Images/TweetPolarity_NewsOutlet.png")

plt.show(sns_plot2)

```


![png](output_17_0.png)


Step 7: I save the resulting data frame to a CSV.


```python
# Export file as a CSV, without the Pandas index, but with the header

sentiments_pd_clean.to_csv("../Resources/MediaSentiments.csv", index=False, header=True)
```
