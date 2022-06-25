<img src="https://github.com/ZanClifton/python-autoclicker/blob/main/images/mouse.png" width=250px align=right alt="Mouse Ascii Art"/>

# Python Autoclicker

[Universal Paperclips](https://www.decisionproblem.com/paperclips/index2.html) is a game I love, but I don't love the constant elevated risk of carpal tunnel syndrome from all the clicking!

I wanted to install an autoclicker to, um... 'optimise my efficiency' (ahem) but I also wanted to understand exactly what it was doing. Plus I'm running Ubuntu and I wasn't sure where to find an autoclicker that was reliable and safe. So I pulled on my big coder pants and had a go (with a little help from [GitHub Copilot](https://github.com/features/copilot/) for the first - and possibly the last until I'm a lot more experienced - time).

## Run the Autoclicker Locally

### ✔️ 1. CLONE THE REPO
```
$ git clone https://github.com/ZanClifton/python-autoclicker.git
$ cd python-autoclicker
```

### ✔️ 2. INSTALL PYNPUT
```
$ pip install pynput
```

### ✔️ 3. USAGE
Run the script from your terminal using the following command.
```
$ python3 autoclicker.py
```
You will be prompted to enter how long you would like to wait between clicks. Providing an integer will mean a wait of that number of seconds between clicks. You can provide a floating point number to indicate a number in milliseconds, e.g. 0.01 is a gap of 10ms between clicks.

Hover your mouse over whatever it is you wish to click, and press the start key, "s", to begin. Stop the clicker with the same command. Exit the script by pressing "e".

Enjoy your pain free button mashing!

#
<div align=right>
  <h6>Ascii Art: <i><a href="https://ascii.co.uk/art/mouse">Mouse</a></i> by Philip Kaulfuss</h6>
</div>
