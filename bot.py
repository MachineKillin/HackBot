import interactions, time, requests, json, asyncio, os, random, re, json, string, hashid, whois as whoiz, datetime, uwuify, hashlib, dns.resolver, importlib, hashes
from interactions import SlashCommandOption, OptionType, SlashContext, Embed, slash_command, Button, Activity, SlashCommandChoice, Modal, ParagraphText, ShortText, ModalContext, StringSelectMenu, ActionRow
from collections import defaultdict
from datetime import datetime
from bs4 import BeautifulSoup
from interactions.api.events import GuildJoin, GuildLeft

ready = False
bot = interactions.Client()
cooldowns = defaultdict(dict)
footertxt = "HackBot by killinmachine"
footericon = "https://i.redd.it/841krdvmenb61.png"
statuses = []
agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

def notify(message, ctx: SlashContext):
    if ctx.guild: message+=f" in __{ctx.guild.name}__[{ctx.guild.member_count}] | Owner: <@{ctx.guild._owner_id}>"
    else: message+=f" in __DMS__"
    try:
        requests.post("yourwebhook", data=json.dumps({"content": message}), headers={"Content-Type": "application/json"})
    except:
        print("there was an error sending the webhook notification: "+message)

@interactions.listen()
async def on_startup():
    global ready
    print(bot.user.username+" is ready!")
    #notify(f"HackBot successfully started!", None)
    await newstatus()
    newstatus.start()
    status.start()
    ready = True

#@interactions.listen(GuildJoin) this doesnt work
#async def botJoin(guild: GuildJoin):
#    if ready:
#        message = f"{bot.user.username} joined {guild.guild.name} owned by <@{guild.guild._owner_id}>"
#        requests.post("yourwebhook", data=json.dumps({"content": message}), headers={"Content-Type": "application/json"})

#@interactions.listen(GuildLeft) this does
#async def botJoin(guild: GuildLeft):
#    if ready:
#        message = f"{bot.user.username} left {guild.guild.name} owned by <@{guild.guild._owner_id}>"
#        requests.post("yourwebhook", data=json.dumps({"content": message}), headers={"Content-Type": "application/json"})

@interactions.Task.create(interactions.IntervalTrigger(hours=24))
async def newstatus():
    global statuses
    statuses.clear()
    pick = [        
        "type /iplog to log ips :)",
        "do /doggo to see some cute pups",
        "do /gato to see a cute kitty",
        "/uwu m-modify youwr text to m-make u uwu~",
        "type /phone to get someones name from a phone number",
        "use /email to see your breached passwords",
        "type /proxy to get a free proxylist",
        "try /scan to see if your email has been logged",
        "check if your password is good with /pwned",
        "suggest new commands with /suggestion",
        "use /inbox to create a temporary email inbox",
        "use /hash to hash some secret text",
        "use /bincheck to get info about that bin",
        "pick a random number with /randomnumber",
        "dont know the hash type? use /indentify",
        "use /whois to find who owns your favorite domain",
        "type /ip to get info about an ip address"
    ]
    statuses = random.sample(pick, 3)
    pick2 = [
        "ty killinmachine for coding me",
        "type /help to start hackin",
        "made with ❤️ by killinmachine"
    ]
    statuses.extend(random.sample(pick2, 1))

@interactions.Task.create(interactions.IntervalTrigger(seconds=5))
async def status():
    activity = Activity.create(name=random.choice(statuses), url='https://www.youtube.com/watch?v=dQw4w9WgXcQ', type=interactions.ActivityType.STREAMING)
    await bot.change_presence(activity=activity)

async def cmd_cooldown(ctx, duration):
    command_name = ctx.command.name
    user_id = ctx.author.id
    current_time = time.time()
    if command_name in cooldowns and user_id in cooldowns[command_name]:
        if current_time < cooldowns[command_name][user_id]:
            remaining_time = cooldowns[command_name][user_id] - current_time
            await ctx.send(f"Command is on cooldown. Try again in {remaining_time:.2f} seconds.")
            return True
    cooldowns[command_name][user_id] = current_time + duration
    return False

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

@slash_command(name="phone", description="Get information about a phone number.", options = [
    SlashCommandOption(name="country", description="Country the number is in.", type=OptionType.STRING, required=True, choices=[
        SlashCommandChoice(name="USA [+1]", value="+1"),
        SlashCommandChoice(name="Australia [+61]", value="+61"),
        SlashCommandChoice(name="Canada [+1]", value="+1"),
        SlashCommandChoice(name="France [+33]", value="+33"),
        SlashCommandChoice(name="Germany [+49]", value="+49"),
        SlashCommandChoice(name="India [+91]", value="+91"),
        SlashCommandChoice(name="Italy [+39]", value="+39"),
        SlashCommandChoice(name="Netherlands [+31]", value="+31"),
        SlashCommandChoice(name="New Zealand [+64]", value="+64"),
        SlashCommandChoice(name="Singapore [+65]", value="+65"),
        SlashCommandChoice(name="Spain [+34]", value="+34"),
        SlashCommandChoice(name="United Kingdom [+44]", value="+44")
    ]),
    SlashCommandOption(name="number", description="Number to search.", type=OptionType.STRING, required=True)
])
async def phone(ctx: SlashContext, country: str, number: str):
    if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{country}{number}`", ctx)
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Length": "35",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://www.numlookup.com",
        "Referer": "https://www.numlookup.com/search",
        "Sec-Ch-Ua": '"Chromium";v="118", "Microsoft Edge";v="118", "Not=A?Brand";v="99"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57",
        "X-Requested-With": "XMLHttpRequest"
    }
    try:
        number = number.replace("-", "").replace("(", "").replace(")", "").replace(" ", "")
        reqt = requests.post('https://www.numlookup.com/verify_user_for_captcha', data={"dialCode":country,"dialNumber":number}, headers=headers).text
        verifyuser = json.loads(reqt)
        if verifyuser.get("captcha") == "1": raise Exception("Captcha Blockage.")
        data = {
            "dialNumber": number,
            "dialCode": country,
            "user_agent[SCREEN_WIDTH]": "1920",
            "user_agent[SCREEN_HEIGHT]": "1080",
            "user_agent[SCREEN_DEPTH]": "24",
            "user_agent[SYSTEM_FONT]": "",
            "user_agent[PLUGINS]": "5",
            "user_agent[platform]": "Win32",
            "user_agent[user_agent]": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57",
            "user_agent[app_version]": "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.57",
            "user_agent[vendor]": "Google Inc.",
            "user_agent[lang]": "en-US",
            "user_agent[time_zone]": "240",
            "user_agent[webgl_renderer]": "ANGLE (Intel, Intel(R) HD Graphics 630 (0x00005912) Direct3D11 vs_5_0 ps_5_0, D3D11)",
            "captcha_key": "1",
            "log_id": str(verifyuser["id"]),
            "request_start_time": str(verifyuser["start_time"])
        }
        data = requests.post("https://www.numlookup.com/phone_lookup", data=data, headers=headers).text
        embed = Embed(title=f"Info Found About `{country}{number}`:", color=0x34c0eb)
        risk = ""
        try: 
            name = " ".join(re.search(r"(?<=<p class=\"ownername-block\"><span style=\"font-weight:600; font-size:40px;\" class=\"text-dark\">).+?(?=<)", data).group(0).split()[::-1]).lower()
            embed.add_field(name="Name:", value=name, inline=True)
        except: name = "unknown"
        try: 
            type = re.search(r"(?<=<divclass=\"col-sm-8mb-0mb-sm-0\">).+?(?=<)", data.strip().replace(" ", "").replace("\n", "")).group(0).lower()
            embed.add_field(name="Type:", value=type, inline=True)
        except: type = "unknown"
        try:
            embed.image = re.search(r"(?<=<img alt='' src=').+?(?='>)", data).group(0)
        except: carrier = "unknown"
        try:
            carrier = re.search(r"(?<=<div class=\"col-sm-8 mb-0 mb-sm-0\"><span>).+?(?=</span>)", data.strip().replace("\n", "").replace("  ", "")).group(0)
            embed.add_field(name="Carrier:", value=carrier, inline=True)
        except: carrier = "unknown"
        try:
            bad = "<span class=\"h3\"><span style=\""+re.search(r"(?<=<div class=\"mb-2\"><span class=\"h3\"><span style=\").+?(?=\")", data).group(0)+"\">"
            risk = re.search(r"(?<=\">).+?(?=</span></span></div>)", data).group(0).replace(bad, "").lower().split(" ")[0]
            embed.add_field(name="Risk:", value=risk, inline=True)
        except: risk = "unknown"
        try: 
            summary = re.search(r"(?<=Summary</span></div> <p>).+?(?=<strong style=)", data.replace("\n", "").replace("  ", "")).group(0)+risk+"."
            embed.description = summary
        except: summary = "unknown"
        embed.set_footer(text=footertxt, icon_url=footericon)
        await ctx.send(embeds=embed)
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

@slash_command(name="ip", description="Get information about a IP.", options = [SlashCommandOption(name="ip", description="IP to search.", type=OptionType.STRING, required=True)])
async def ip(ctx: SlashContext, ip: str):
    if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{ip}`", ctx)
    try:
        reqt = requests.get('https://ipgeolocation.io/ip-location/'+ip, headers=agent).text
        soup = BeautifulSoup(reqt, 'html.parser')
        ip_info_table = soup.find('table', {'id': 'ipInfoTable'})
        embed = Embed(title=f"Info Found About `{ip}`:", color=0x34c0eb)
        info = {}
        for row in ip_info_table.find_all('tr'):
            columns = row.find_all('td')
            if len(columns) == 2:
                key = columns[0].text.strip()
                value = columns[1].text.strip()
                if key != 'Country Flag': info[key] = value
                else:
                    flag_img = columns[1].find('img', class_='country__flag')
                    if flag_img:
                        embed.add_image(flag_img['src'])
        blacklist = ["IP", "Hostname", "Continent Code", "Country Code (ISO 3166-1 alpha-2)", "Country Code (ISO 3166-1 alpha-3)", "AS Number", "Currency", "Currency Symbol", "Is DST?"]
        for key, value in info.items():
            if key not in blacklist:
                if value != "":
                    embed.add_field(name=key, value=value, inline=True)
        embed.set_footer(text=footertxt, icon_url=footericon)
        await ctx.send(embeds=embed)
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

@slash_command(name="proxy", description="Returns a list of scraped proxies.", options = [
    SlashCommandOption(name="type", description="Proxytype to scrape.", type=OptionType.STRING, required=True, choices=[
        SlashCommandChoice(name="HTTP", value="http"),
        SlashCommandChoice(name="SOCKS4", value="socks4"),
        SlashCommandChoice(name="SOCKS5", value="socks5"),
    ])
])
async def proxies(ctx: SlashContext, type: str):
    if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** for: `{type}`", ctx)
    file = type+"-"+generate_random_string(10)+".txt"
    count = 0
    try:
        proxylist = requests.get(f"https://api.proxyscrape.com/?request=getproxies&protocol={type}&timeout=10000&country=all&ssl=all&anonymity=all").content
        count = len(proxylist.decode('utf-8').splitlines())
        with open(file, "bw") as f: f.write(proxylist)
        await ctx.send(f"Scraped `{count}` {type.upper()} proxies!", file=file)
        os.remove(file)
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

@slash_command(name="identify", description="Identify a hash's type.", options = [SlashCommandOption(name="hash", description="Hash to identify.", type=OptionType.STRING, required=True)])
async def identify(ctx: SlashContext, hash: str):
    #if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{hash}`", ctx)
    try:
        embed = Embed(title=f"Possible Hash Algorithms for `{hash}`:", color=0x34c0eb)
        hasher = hashid.HashID()
        output = hasher.identifyHash(hash)
        count = 0
        for out in output:
            if not out.extended:
                count+=1
                embed.add_field(name=str(count)+". "+out.name, value=" ", inline=True)
        embed.set_footer(text=footertxt, icon_url=footericon)
        await ctx.send(embeds=embed)
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

def domainexist(domain):
    record_types = ['A', 'AAAA', 'MX', 'NS', 'CNAME', 'TXT']
    for record_type in record_types:
        try:
            dns.resolver.resolve(domain, record_type)
            return True
        except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
            _=''
    return False

@slash_command(name="whois", description="Get info about a website.", options = [SlashCommandOption(name="domain", description="Domain of the website to search.", type=OptionType.STRING, required=True)])
async def whois(ctx: SlashContext, domain: str):
    if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{domain}`", ctx)
    try:
        if domainexist(domain):
            embed = Embed(title=f"Information About `{domain}`:", color=0x34c0eb)
            whois_info = whoiz.whois(domain)
            for key, value in whois_info.items():
                if value is not None and "REDACTED" not in str(value) and key != "status":
                    if isinstance(value, list):
                        value = ', '.join(str(item) for item in value)
                    embed.add_field(name=key, value=value, inline=True)
            embed.set_footer(text=footertxt, icon_url=footericon)
            await ctx.send(embeds=embed)
        else:
            await ctx.send(f'The domain "{domain}" does not exist.')
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer):
        await ctx.send("Failed to execute command.")

@slash_command(name="scan", description="Scan through logs for your email.", options = [SlashCommandOption(name="email", description="Email to search for.", type=OptionType.STRING, required=True)])
async def scan(ctx: SlashContext, email: str):
    if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{email}`", ctx)
    try:
        parsed_data = json.loads(requests.get("https://cavalier.hudsonrock.com/api/json/v2/preview/search-by-login/osint-tools?email="+email).text)
        embed = Embed(title=f"Data Found for `{email}`:", color=0x34c0eb)
        data = parsed_data["data"]
        date_uploaded = data[0]["date_uploaded"]
        date_compromised = data[0]["date_compromised"]
        #employeeAt = data[0]["employeeAt"]
        #clientAt = data[0]["clientAt"]
        #ip = data[0]["ip"]
        computer_name = data[0]["computer_name"]
        operating_system = data[0]["operating_system"]
        antiviruses = data[0]["antiviruses"]
        embed.description = f"Compromised at: `{date_compromised}`\nLogged at: `{date_uploaded}`\nComputer Name: `{computer_name}`\nOperating System: `{operating_system}`\nAntiviruses: `{antiviruses}`\n\n**Credentials:**"
        credentials = data[0]["credentials"]
        count = 1
        for credential in credentials:
            credential_type = credential["type"]
            url = credential["url"]
            domain = credential["domain"]
            username = credential["username"]
            password = credential["password"]
            embed.add_field(name=str(count)+"."+f" Type: `{credential_type}` | Site: `{url}` | Username: `{username}` | Password: `{password}`", value=" ", inline=True)
            count+=1
        embed.set_footer(text=footertxt, icon_url=footericon)
        await ctx.send(embeds=embed)
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

#@slash_command(name="person", description="Get info about a name.", options = [
#    SlashCommandOption(name="name", description="Persons name to search.", type=OptionType.STRING, required=True), 
#    SlashCommandOption(name="optional", description="City, State or Zip .", type=OptionType.STRING, required=False)
#])
async def peoplesearch(ctx: SlashContext, name: str, optional: str = ""):
    if await cmd_cooldown(ctx, 5): return
    try:
        lookup = ""
        lookup = name.replace(" ", "-")
        if optional != "":
            lookup += "_"+optional.replace(" ", "-")
            notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{name} {optional}`", ctx)
        else:
            notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{name}`", ctx)
        cookie = requests.get("https://www.fastpeoplesearch.com/", headers=agent).cookies
        datas = requests.get("https://www.fastpeoplesearch.com/name/"+lookup, headers=agent, cookies=cookie).text
        with open("test.txt", "w") as f: f.write(datas)
        soup = BeautifulSoup(datas, 'html.parser')
        script_tags = soup.find_all('script', {'type': 'application/ld+json'})
        embed = Embed(title=f"Information Found for `{name}`:", color=0x34c0eb)
        for script_tag in script_tags:
            data = json.loads(script_tag.string)
            if isinstance(data, list) and all(isinstance(item, dict) for item in data):
                person_info = data[0]
                age_element = soup.find('h3', text='Age:')
                if age_element:
                    age_value = age_element.find_next('br').previous_sibling.strip()
                    embed.add_field(name=f"Age: {age_value}", value=" ", inline=False)
                person_info = data[0]
                embed.add_field(name=f"{name} goes by {person_info.get('name')}", value=" ", inline=False)
                embed.add_field(name=f"Numbers:", value=', '.join(person_info.get("telephone")), inline=False)
                embed.add_field(name=f"Other Names:", value=', '.join(person_info.get("additionalName")), inline=False)
                embed.add_field(name=f"Related To:", value=', '.join(person_info.get("relatedTo")), inline=False)
                locs = ""
                for location in person_info.get("HomeLocation").range(0, 3):
                    address = location.get("address")
                    description = location.get("description")
                    street_address = address.get("streetAddress")
                    locality = address.get("addressLocality")
                    region = address.get("addressRegion")
                    latitude = location.get("geo").get("latitude")
                    longitude = location.get("geo").get("longitude")
                    loc += f"{description} - {street_address} | {locality} {region} | Latitude: {latitude} | Longitude: {longitude}\n"
                embed.add_field(name=f"Home Locations:", value=locs.strip(), inline=False)
        embed.set_footer(text=footertxt, icon_url=footericon)
        await ctx.send(embeds=embed)
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

@slash_command(name="uwu", description="uwuify text.", options = [SlashCommandOption(name="text", description="Text you want to uwuify.", type=OptionType.STRING, required=True)])
async def uwu(ctx: SlashContext, text: str):
    #if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{text}`", ctx)
    try:
        await ctx.send(uwuify.uwu(text, flags=random.choice([uwuify.SMILEY, uwuify.STUTTER, uwuify.YU])))
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

@slash_command(name="gato", description="Returns a random cat picture.")
async def gato(ctx: SlashContext):
    if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}**", ctx)
    try:
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        await ctx.send(response.json()[0]['url'])
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

@slash_command(name="doggo", description="Returns a random dog picture.")
async def doggo(ctx: SlashContext):
    if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}**", ctx)
    try:
        response = requests.get("https://dog.ceo/api/breeds/image/random")
        await ctx.send(response.json()['message'])
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

@slash_command(name="randomnumber", description="Random number between two numbers.", options = [SlashCommandOption(name="min", description="First number.", type=OptionType.INTEGER, required=True), SlashCommandOption(name="max", description="Second number.", type=OptionType.INTEGER, required=True)])
async def randomnumber(ctx: SlashContext, min: int, max: int):
    #if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{min} - {max}`", ctx)
    try:
        await ctx.send("Your Number: "+str(random.randint(min, max)))
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

@slash_command(name="pwned", description="Check if your password has been breached.", options = [SlashCommandOption(name="password", description="Password to check.", type=OptionType.STRING, required=True)])
async def pwned(ctx: SlashContext, password: str):
    if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{password}`", ctx)
    try:
        sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        first5_char, tail = sha1password[:5], sha1password[5:]
        url = 'https://api.pwnedpasswords.com/range/' + first5_char
        response = requests.get(url)        
        hashes = (line.split(':') for line in response.text.splitlines())
        count = next((int(count) for h, count in hashes if h == tail), 0)
        if count:
            await ctx.send(f'{password} was found `{count}` times. You should probably change your password.')
        else:
            await ctx.send(f'{password} was not found. GG!')
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

@slash_command(name="suggestion", description="Suggest a command to add.")
async def suggestion(ctx: SlashContext):
    if await cmd_cooldown(ctx, 60): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}**", ctx)
    suggestmodal = Modal(
        ShortText(label="Command Name:", custom_id="name"),
        ParagraphText(label="Function(s)", custom_id="function"),
        title="Suggest a Command",
    )
    await ctx.send_modal(modal=suggestmodal)
    modal_ctx: ModalContext = await ctx.bot.wait_for_modal(suggestmodal)
    message = f"||@everyone|| New Suggestion For HackBot:\nCommand Name: `{modal_ctx.responses['name']}`\nCommand Function: `{modal_ctx.responses['function']}`\nSubmitted by: <@{str(modal_ctx.author.id)}> | {modal_ctx.author.username}"
    try:
        requests.post("YOURWEBHOOKHERE", data=json.dumps({"content": message}), headers={"Content-Type": "application/json"})
        await modal_ctx.send(f"Suggestion Sent to KillinMachine", ephemeral=True)
    except:
        print("there was an error sending the webhook notification: "+message)
        await modal_ctx.send(f"Suggestion Failed on sending to KillinMachine", ephemeral=True)

@slash_command(name="portscan", description="Scan an ip address for open ports.", options = [SlashCommandOption(name="ip", description="Ip address to scan.", type=OptionType.STRING, required=True)])
async def portscan(ctx: SlashContext, ip: str):
    if await cmd_cooldown(ctx, 15): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{ip}`", ctx)
    try:
        create = requests.post('https://hidemy.io/api/nmap.php?out=js&post', data={'host':ip,'ports':''}).json()
        id = create['id']
        embed = Embed(title=f"Queued...", color=0x34c0eb)
        embed.set_footer(text=footertxt, icon_url=footericon)
        message = await ctx.send(embeds=embed)
        Finished = False
        while not Finished:
            try:
                check = requests.get('https://hidemy.io/api/nmap.php?out=js&get='+str(id)).json()
                progress = check['progress']
                if progress == "working":
                    eembed = Embed(title=f"Waiting...", color=0x34c0eb)
                    stats = check['stats']
                    eembed.description = f"**Progress:** `{stats[0]}`\n**Passed:** `{stats[1]}`\n**Left:** `{stats[2]}`"
                    eembed.set_footer(text=footertxt, icon_url=footericon)
                    await message.edit(embeds=eembed)
                if progress == "done":
                    eembed = Embed(title=f"Finished!", color=0x34c0eb)
                    eembed.description = check['text']
                    eembed.set_footer(text=footertxt, icon_url=footericon)
                    await message.edit(embeds=eembed)
                    Finished = True
            except: _=''
            await asyncio.sleep(1)
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

def getipval(out, name, second = ""):
    try:
        if second != "": return out[name][second]
        else: return out[name]
    except: return "Unknown"

async def watch(id, token, auth):
    user = await bot.fetch_user(id, force=True)
    saved_parsed_incidents = []
    for _ in range(10 * 60 // 5):
        try:
            history = requests.get(f'https://canarytokens.org/history?token={token}&auth={auth}', headers=agent).text
            soup = BeautifulSoup(history, 'lxml')
            incident_items = soup.find_all('div', class_='incident-item')
            parsed_incidents = []
            for incident_item in incident_items:
                details_header = incident_item.find('p', class_='details-header')
                if details_header:
                    incident_data = {}
                    incident_data['Date'] = details_header.b.next_sibling.strip()
                    incident_data['IP'] = details_header.find_all('b')[1].next_sibling.strip()
                    incident_data['Channel'] = details_header.find_all('b')[2].next_sibling.strip()
                    geo_info_table = incident_item.find('table', class_='table-striped')
                    if geo_info_table:
                        geo_info_rows = geo_info_table.find_all('tr', class_='info_row')
                        geo_info = {}
                        for row in geo_info_rows:
                            cells = row.find_all('td')
                            if len(cells) == 2:
                                key = cells[0].text.strip()
                                value = cells[1].text.strip()
                                geo_info[key] = value
                        incident_data['Geo Info'] = geo_info
                    basic_info_table = incident_item.find_next('table', class_='table-bordered')
                    if basic_info_table:
                        basic_info_rows = basic_info_table.find_all('tr', class_='info_row')
                        basic_info = {}
                        for row in basic_info_rows:
                            cells = row.find_all('td')
                            if len(cells) == 2:
                                key = cells[0].text.strip()
                                value = cells[1].text.strip()
                                basic_info[key] = value
                        incident_data['Basic Info'] = basic_info
                    additional_info_table = basic_info_table.find_next('table', class_='table-bordered')
                    if additional_info_table:
                        additional_info_rows = additional_info_table.find_all('tr', class_='info_row')
                        additional_info = {}
                        for row in additional_info_rows:
                            cells = row.find_all('td')
                            if len(cells) == 2:
                                key = cells[0].text.strip()
                                value = cells[1].text.strip()
                                additional_info[key] = value
                        incident_data['Additional Info'] = additional_info
                    parsed_incidents.append(incident_data)
            if parsed_incidents != saved_parsed_incidents:
                out = json.loads(json.dumps(parsed_incidents))[-1]
                embed = Embed(title="A person clicked on your ip logger:", color=0x34c0eb)
                datatosend = f'''**Date:** `{getipval(out, 'Date')}`
                **IP:** `{getipval(out, 'IP')}`
                **Channel:** `{getipval(out, 'HTTP')}`
                **Geo Info:**
                Country: `{getipval(out, 'Geo Info', 'Country')}`
                City: `{getipval(out, 'Geo Info', 'City')}`
                Region: `{getipval(out, 'Geo Info', 'Region')}`
                Organisation: `{getipval(out, 'Geo Info', 'Organisation')}`
                **Tor:** `{getipval(out, 'Basic Info', 'Known Exit Node')}`
                **User Agent:** `{getipval(out, 'Additional Info', 'useragent')}`
                **Request Headers:** `{getipval(out, 'Additional Info', 'request_headers')}`
                '''
                embed.description = datatosend
                embed.set_footer(text=footertxt, icon_url=footericon)
                await user.send(embeds=embed)
                saved_parsed_incidents = parsed_incidents
        except:
            _ = ""
        await asyncio.sleep(5)
    await user.send(f"IP logger session has expired. You have grabbed a total of `{len(saved_parsed_incidents)}` IP(s).")

@slash_command(name="iplog", description="Creates an ip logger and get notified on actions.", options = [SlashCommandOption(name="redriect", description="Website the logger will redirect the person to. (https://google.com)", type=OptionType.STRING, required=True)])
async def iplog(ctx: SlashContext, redriect: str):
    if await cmd_cooldown(ctx, 10 * 60): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{redriect}`", ctx)
    try:
        hear = {'type':'slow_redirect',
            'email':generate_random_string(7)+'@'+generate_random_string(5)+'.com',
            'webhook_url':'',
            'fmt':'',
            'sql_server_sql_action':'',
            'azure_id_cert_file_name':'',
            'cmd_process':'',
            'clonedsite':'',
            'sql_server_table_name':'TABLE1',
            'sql_server_view_name':'VIEW1',
            'sql_server_function_name':'FUNCTION1',
            'sql_server_trigger_name':'TRIGGER1',
            'redirect_url': redriect,
            'memo':generate_random_string(5)
        }
        start = requests.post('https://canarytokens.org/generate', data=hear).text
        data = json.loads(start)
        grabberurl = data['token_url']
        token = data['token']
        auth_token = data['auth_token']
        embed = Embed(title="Logger created:", color=0x34c0eb)
        embed.description = f"Url: `{grabberurl}`\nThis ip grabber will be online for the next 10 minutes.\nYou will be direct messaged for any IP's grabbed."
        #print(grabberurl.split('canarytokens.com/')[1].split('/'+token)[0])
        #print(grabberurl.split(token+'/')[1])
        #components: list[ActionRow] = [
        #    ActionRow(
        #       StringSelectMenu("articles", "traffic", "images", "terms", "tags", "feedback", "stuff", "about", "static",
        #            placeholder=grabberurl.split('canarytokens.com/')[1].split('/'+token)[0],
        #            min_values=1,
        #            max_values=1,
        #        ),
        #        StringSelectMenu("index.html", "payments.js", "contact.php", "post.jsp", "submit.aspx",
        #            placeholder=grabberurl.split(token+'/')[1],
        #            min_values=1,
        #            max_values=1,
        #        )
        #    )
        #]
        embed.set_footer(text=footertxt, icon_url=footericon)
        await ctx.send(embeds=embed) #components=components
        await watch(ctx.author.id, token, auth_token)
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

@slash_command(name="bincheck", description="Get information about a bin.", options = [SlashCommandOption(name="bin", description="Bin to check.", type=OptionType.STRING, required=True)])
async def bincheck(ctx: SlashContext, bin: str):
    if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{bin}`", ctx)
    try:
        embed = Embed(title=f"Information Found on `{bin}`:", color=0x34c0eb)
        txt = requests.get("https://iplogger.org/bin-checker/?bin="+bin, headers=agent).text
        soup = BeautifulSoup(txt, 'html.parser')
        binn = soup.find('div', string='BIN').find_next('div', class_='copy').string
        country = soup.find('div', string='Country').find_next('span').string
        brand = soup.find('div', string='Brand').find_next('div').string.strip()
        type = soup.find('div', string='Type').find_next('div').string.strip()
        level = soup.find('div', string='Level').find_next('div').string.strip()
        name = soup.find('div', string='Bank name').find_next('div').string.strip()
        contacts_div = soup.find('div', string='Bank contacts').find_next('div')
        phone = contacts_div.find('div', string='phone').find_next('div').string.strip()
        site = contacts_div.find('div', string='site').find_next('div').string.strip()
        embed.description = f"**Bin:** `{binn}`\n**Country:** `{country}`\n**Brand:** `{brand}`\n**Type:** `{type}`\n**Level:** `{level}`\n**Name:** `{name}`\n**Bank Contacts:**\n   **Phone:** `{phone}`\n   **Site:** `{site}`"
        embed.set_footer(text=footertxt, icon_url=footericon)
        await ctx.send(embeds=embed)
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

@slash_command(name="email", description="Get breached passwords for an email.", options = [SlashCommandOption(name="email", description="Get breached passwords for an email.", type=OptionType.STRING, required=True)])
async def emailsearch(ctx: SlashContext, email: str):
    if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{email}`", ctx)
    try:
        embed = Embed(title=f"Passwords Found for `{email}`:", color=0x34c0eb)
        txt = requests.get(f"https://saucesec.tech/api/combo/lookup?comboToLookUp={email}&limit=100&exactMatch=true", headers={'X-Session-Key':'Developer'}).text
        out = ""
        try:
            passwords = json.loads(txt)[email]
            for password in passwords:
                out+=password+"\n"
            embed.description = out
        except:
            embed.description = f'No passwords found for the email "{email}"'
        embed.set_footer(text=footertxt, icon_url=footericon)
        await ctx.send(embeds=embed)
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

async def watche(id, email):
    user = await bot.fetch_user(id, force=True)
    save = ""
    for _ in range(10 * 60 // 5):
        try:
            history = requests.get('https://inboxes.com/api/v2/inbox/'+email, headers=agent).text
            data = json.loads(history)
            uid = data['msgs'][0]['uid']
            if uid != save:
                emaildata = requests.get('https://inboxes.com/api/v2/message/'+uid, headers=agent).text
                data = json.loads(emaildata)
                embed = Embed(title=f"New email received on `{email}`:", color=0x34c0eb)
                datatosend = f'''**From:** {data['ff'][0]['address']} {data['ff'][0]['name']}
                **Subject:** {data['s']}
                **Text:** 
                {data['text']}
                *{datetime.strptime(data['cr'], "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%Y-%m-%d %H:%M:%S")}* ***{data['rr']}***
                '''
                embed.description = datatosend
                embed.set_footer(text=footertxt, icon_url=footericon)
                await user.send(embeds=embed)
                save = uid
        except: _=':('
        await asyncio.sleep(5)
    await user.send(f"Inbox session has expired. You will now no longer receive anymore emails sent to {email}.")

domains = []
try:
    text = requests.get('https://inboxes.com/api/v2/domain').text
    if text != "":
        data = json.loads(text)
        domains = [entry['qdn'] for entry in data['domains']]
except: _ = ""
opti = []
choices = [SlashCommandChoice(name=domain, value=domain) for domain in domains]
opti.extend(choices)
@slash_command(name="inbox", description="Creates a temporary email and sends you all emails received.", options = [SlashCommandOption(name="prefix", description="prefix@example.com.", type=OptionType.STRING, required=False), SlashCommandOption(name="emaildomain", description="Domain for your email.", type=OptionType.STRING, required=False, choices=opti)])
async def inbox(ctx: SlashContext, prefix: str = "", emaildomain: str = ""):
    if await cmd_cooldown(ctx, 10 * 60): return
    if prefix == "": prefix = ''.join(char for char in generate_random_string(5) if char.isalpha() or char.isspace()).lower()
    if emaildomain == "": emaildomain = random.choice(domains)
    email = prefix+"@"+emaildomain
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{email}`", ctx)
    try:
        embed = Embed(title=f"Temporary Inbox Created:", color=0x34c0eb)
        embed.description = f"**Email:** `{email}`\nThis email will be valid for 10 minutes.\nYou will be direct messaged any emails sent to {email}."
        embed.set_footer(text=footertxt, icon_url=footericon)
        await ctx.send(embeds=embed)
        await watche(ctx.author.id, email)
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

async def hashall(text):
    hash_functions = [
        hashes.mysql1323,
        hashes.mysql141,
        hashes.mssql2000,
        hashes.mssql2005,
        hashes.md4,
        hashes.md5,
        hashes.sha1,
        hashes.Sha224,
        hashes.Sha256,
        hashes.Sha384,
        hashes.Sha512,
        hashes.Ripemd160,
        hashes.Whirlpool,
        hashes.crc32,
        hashes.adler32,
        hashes.des,
        hashes.Bsdi_Crypt,
        hashes.Bigcrypt,
        hashes.Crypt16,
        hashes.Md5_crypt,
        hashes.Sha1_crypt,
        hashes.Sha256_crypt,
        hashes.Sha512_crypt,
        hashes.Sun_md5,
        hashes.apache_md5,
        hashes.phppass,
        hashes.Cryptaculars_PBDF2,
        hashes.Dwine_PBDF2,
        hashes.Atlassians_PBKDF2,
        hashes.Django_sha1,
        hashes.django_sha256,
        hashes.grup_pbkdf2,
        hashes.SCRAM,
        hashes.FreeBSD_nthash,
        hashes.oracle11,
        hashes.lanManager,
        hashes.nthash,
        hashes.cisco_type_7,
        hashes.fhsp
    ]
    tasks = [func(text) for func in hash_functions]
    results = await asyncio.gather(*tasks)
    return results

options = [SlashCommandChoice(name="mysql1323", value="mysql1323"), 
    SlashCommandChoice(name="mysql141", value="mysql141"),
    SlashCommandChoice(name="mssql2000", value="mssql2000"),
    SlashCommandChoice(name="mssql2005", value="mssql2005"),
    SlashCommandChoice(name="md4", value="md4"),
    SlashCommandChoice(name="md5", value="md5"),
    SlashCommandChoice(name="sha1", value="sha1"),
    SlashCommandChoice(name="Sha224", value="Sha224"),
    SlashCommandChoice(name="Sha256", value="Sha256"),
    SlashCommandChoice(name="Sha384", value="Sha384"),
    SlashCommandChoice(name="Sha512", value="Sha512"),
    SlashCommandChoice(name="Ripemd160", value="Ripemd160"),
    SlashCommandChoice(name="Whirlpool", value="Whirlpool"),
    SlashCommandChoice(name="crc32", value="crc32"),
    SlashCommandChoice(name="adler32", value="adler32"),
    SlashCommandChoice(name="des", value="des"),
    SlashCommandChoice(name="Bigcrypt", value="Bigcrypt"),
    SlashCommandChoice(name="Crypt16", value="Crypt16"),
    SlashCommandChoice(name="Md5 crypt", value="Md5_crypt"),
    SlashCommandChoice(name="Sha1 crypt", value="Sha1_crypt"),
    SlashCommandChoice(name="Sha256 crypt", value="Sha256_crypt"),
    SlashCommandChoice(name="Sha512 crypt", value="Sha512_crypt"),
    SlashCommandChoice(name="Sun md5", value="Sun_md5"),
    SlashCommandChoice(name="apache md5", value="apache_md5"),
    SlashCommandChoice(name="phppass", value="phppass")
]
@slash_command(name="hash", description="Hash text by a hash algorithm.", options = [SlashCommandOption(name="text", description="Text to hash.", type=OptionType.STRING, required=True), SlashCommandOption(name="hash", description="Hash algorithm.", type=OptionType.STRING, required=False, choices=options)])
async def hash(ctx: SlashContext, text: str, hash: str = ""):
    if await cmd_cooldown(ctx, 5): return
    notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: {hash} `{text}`", ctx)
    try:
        if hash != "":
            func = getattr(importlib.import_module("hashes"), hash)
            await ctx.send(func(text.encode()))
        else:
            await ctx.send("Please wait. Hashing through 39 algorithms takes a few seconds.")
            all = await hashall(text.encode())
            embed = Embed(title=f"Hashed by all algorithms:", color=0x34c0eb)
            allem = f'''**mysql1323:** `{all[0]}`
            **mysql141:** `{all[1]}`
            **mssql2000:** `{all[2]}`
            **mssql2005:** `{all[3]}`
            **md4:** `{all[4]}`
            **md5:** `{all[5]}`
            **sha1:** `{all[6]}`
            **Sha224:** `{all[7]}`
            **Sha256:** `{all[8]}`
            **Sha384:** `{all[9]}`
            **Sha512:** `{all[10]}`
            **Ripemd160:** `{all[11]}`
            **Whirlpool:** `{all[12]}`
            **crc32:** `{all[13]}`
            **adler32:** `{all[14]}`
            **des:** `{all[15]}`
            **Bsdi Crypt:** `{all[16]}`
            **Bigcrypt:** `{all[17]}`
            **Crypt16:** `{all[18]}`
            **Md5 crypt:** `{all[19]}`
            **Sha1 crypt:** `{all[20]}`
            **Sha256 crypt:** `{all[21]}`
            **Sha512 crypt:** `{all[22]}`
            **Sun md5:** `{all[23]}`
            **apache md5:** `{all[24]}`
            **phppass:** `{all[25]}`
            **Cryptaculars PBDF2:** `{all[26]}`
            **Dwine PBDF2:** `{all[27]}`
            **Atlassians PBKDF2:** `{all[28]}`
            **Django sha1:** `{all[29]}`
            **django sha256:** `{all[30]}`
            **grup pbkdf2:** `{all[31]}`
            **SCRAM:** `{all[32]}`
            **FreeBSD nthash:** `{all[33]}`
            **oracle11:** `{all[34]}`
            **lanManager:** `{all[35]}`
            **nthash:** `{all[36]}`
            **cisco type 7:** `{all[37]}`
            **fhsp:** `{all[38]}`
            '''
            embed.description = allem
            embed.set_footer(text=footertxt, icon_url=footericon)
            await ctx.send(embeds=embed)
    except Exception as e:
        await ctx.send("Failed to execute command. Error: `"+str(e)+"`")

@slash_command(name="help", description="List's commands and what they do.", options = [
    SlashCommandOption(name="category", description="Category of commands.", type=OptionType.STRING, required=False, choices=[
        SlashCommandChoice(name="osint", value="osint"),
        SlashCommandChoice(name="utils", value="utils"),
        SlashCommandChoice(name="fun", value="fun")
    ])
])
async def help(ctx: SlashContext, category = ""):
    if category == "":
        notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}**", ctx)
        embed = Embed(color=0x34c0eb)
        osint = '''**/phone** - Get information about a phone number.
        **/ip** - Get information about a IP.
        **/whois** - Get info about a website.
        **/scan** - Scan through logs for your email.
        **/email** - Get breached passwords for an email.
        '''
        embed.add_field(name="__Osint:__", value=osint)
        
        utils = '''**/proxy** - Returns a list of scraped proxies.
        **/identify** - Identify a hash's type.
        **/randomnumber** - Random number between two numbers.
        **/pwned** - Check if your password has been breached.
        **/suggestion** - Suggest a command to add.
        **/portscan** - Scan an ip address for open ports.
        **/bincheck** - Get information about a bin.
        **/iplog** - Creates an ip logger and get notified on actions.
        **/inbox** - Creates a temporary email and sends you all emails received.
        **/hash** - Hash text by a hash algorithm.
        '''
        embed.add_field(name="__Utils:__", value=utils)

        fun = '''**/gato** - Returns a random cat picture.
        **/doggo** - Returns a random dog picture.
        **/uwu** - uwuify text.
        '''
        embed.add_field(name="__Fun:__", value=fun)

        embed.set_footer(text=footertxt, icon_url=footericon)
        await ctx.send(embeds=embed)
    else: notify(f"<@{ctx.author.id}> | `{ctx.author.username}` used **/{ctx.command.name}** on: `{category}`", ctx)
    if category == "osint":
        embed = Embed(title="__Osint Commands:__", color=0x34c0eb)
        embed.add_field(name="/phone", value="Get information about a phone number.")
        embed.add_field(name="/ip", value="Get information about a IP.")
        embed.add_field(name="/whois", value="Get info about a website.")
        embed.add_field(name="/scan", value="Scan through logs for your email.")
        embed.add_field(name="/email", value="Scan through logs for your email.")
        #embed.add_field(name="/person", value="Get info about a name.")
        embed.set_footer(text=footertxt, icon_url=footericon)
        await ctx.send(embeds=embed)
    elif category == "utils":
        embed = Embed(title="__Util Commands:__", color=0x34c0eb)
        embed.add_field(name="/proxy", value="Returns a list of scraped proxies.")
        embed.add_field(name="/identify", value="Identify a hash's type.")
        embed.add_field(name="/randomnumber", value="Random number between two numbers.")
        embed.add_field(name="/pwned", value="Check if your password has been breached.")
        embed.add_field(name="/suggestion", value="Suggest a command to add.")
        embed.add_field(name="/portscan", value="Scan an ip address for open ports.")
        embed.add_field(name="/bincheck", value="Get information about a bin.")
        embed.add_field(name="/iplog", value="Creates an ip logger and get notified on actions.")
        embed.add_field(name="/inbox", value="Creates a temporary email and sends you all emails received.")
        embed.add_field(name="/hash", value="Hash text by a hash algorithm.")
        embed.set_footer(text=footertxt, icon_url=footericon)
        await ctx.send(embeds=embed)
    elif category == "fun":
        embed = Embed(title="__Fun Commands:__", color=0x34c0eb)
        embed.add_field(name="/gato", value="Returns a random cat picture.")
        embed.add_field(name="/doggo", value="Returns a random dog picture.")
        embed.add_field(name="/uwu", value="uwuify text.")
        embed.set_footer(text=footertxt, icon_url=footericon)
        await ctx.send(embeds=embed)

bot.start("yourtoken")
