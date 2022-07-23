if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/HerleyfilterBot/Harley-Quinn-Public /Harley Quinn
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Ajax
fi
cd /Ajax
pip3 install -U -r requirements.txt
echo "ʟᴀᴜɴᴄʜ ʜᴀʀʟᴇʏ Qᴜɪɴɴ 🚀"
python3 bot.py
