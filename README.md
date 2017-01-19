# Twitch_emote_bot
<h2>Introduction</h2>
This is a script that traverses Reddit (using its API) to find comments which miscapitalizes twitch emotes, and replies them with the correct capitalization. It also provides the link to the corresponding emote page on twitchemotes.com. An example (V1.01) is shown below: <br>
![alt text](https://github.com/lukevastus/Twitch_emote_bot/blob/master/Example_1.png?raw=true "Example_1")

<h2>How to run</h2>
<ul>
<li>Upgrade pip (using <code>pip install -U pip setuptools</code> on Linux/OS X or <code>python -m pip install -U pip setuptools</code> on Windows) if you haven't.</li>
<li>Make sure you have all the modules listed in <code>requirements.txt</code> installed on your computer. If not, use <code>pip install -r /path/to/requirements.txt</code>.</li>
<li>Complete your <a href="https://www.reddit.com/prefs/apps">script application</a>, enabling yourself to use Reddit's API via your Reddit account (<a href="https://praw.readthedocs.io/en/latest/getting_started/authentication.html">here</a> is a detailed tutorial). Fill in the OAuth2 credentials in <code>Main.py</code>.</li>
<li>Optional: edit your local <code>praw.ini</code> file so that your credentials are saved locally. Please refer to <a href="https://praw.readthedocs.io/en/latest/getting_started/configuration/prawini.html">this</a> article.</li>
<li>Run <code>Main.py</code>. <b>GLHF</b>.</li>
</ul>
