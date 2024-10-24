# hometask-wap
![](https://github.com/az2rt/hometask-wap/blob/main/video.gif)

Installation:
I use the following setup:
- macOS Sequoia 15.0.1
- python 3.9.6

This script should work on other platforms as well, as Python has built-in cross-platform support. However, I can't verify this.

Before run make next commands:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run test:
```bash
python -m pytest -s
```

Structure:

`pages` - folder with base & main file for PageObject pattern.

`tests` - folder with tests

`./conftest.py` - default file for fixture



After that you can see 'test.png' file in root directory of project. 