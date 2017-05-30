# Overlay CIMSS Satellite Images
## Introduction
The program helps you combine (overlay) [CIMSS satellite images](http://tropic.ssec.wisc.edu/tropic.php) of different regions into a larger domain. Manipulation includes both real time (currently shown in CIMSS website) and historical (downloaded from [CIMSS Data Archive](http://tropic.ssec.wisc.edu/archive/)) observation (images). Images over Indian Ocean, western North Pacific and west Australia are chosen and overlaid so far.

Here's an [example](http://i.imgur.com/DPZJ5OB.png)

__This programs are tested and run well under GNU/Linux, MacOS and Windows (7 or higher)__

## Prerequisite
1. Python 2.7.x ([Official website](https://www.python.org))
2. Imagemagick ([Official website](https://www.imagemagick.org/script/index.php))


 - *GNU/Linux users*: Python may be a built-in software and install Imagemagick via package manager (apt, dnf, etc) of your distro. 
 - *MacOS users*: Install Python and Imagemagick through [Homebrew](https://brew.sh).
 - *Windwos users*: Download Python 2.7.x and "ImageMagick-7.0.5-9-Q16-x64-dll.exe" from their website. **Notice, remember to enable "add python.exe to path" during Python installation.** 
 
 ## How to Use?
 Execute via terminal (GNU/Linux and MacOS) or PowerShell (Windows)
 #### Real time Observation
 Just run "realtime_cimss_IR_EH_overlay.py" from terminal or PowerShell
 ```bash
 $ python realtime_cimss_IR_EH_overlay.py
 ```
 File "overlaid_cimss_IR_latest.png" is the combined picture.
 
 #### Historical Observation
 1. Download historical satellite image bundle from [CIMSS Data Archive](http://tropic.ssec.wisc.edu/archive/). 
 2. Extract images from the bundle and you'll get directory "data". In "data", there are folders named the region of your interest.
 3. **To decide the period for historical images to combine, you need to modify the first 4 lines in "historical_cimss_IR_EH_overlay.py"**
 ```python
startd = datetime.datetime(2017,5,1)
endd = datetime.datetime(2017,5,29)
deltad = datetime.timedelta(days=+1) 
subt = ["00", "12"] # 00Z 12Z
 ```
 where *startd* and *endd* are the start and end date. *deltad* is interval between each date. *subt* are observations per day.
 4. Place "historical_cimss_IR_EH_overlay.py" under "data". and execute it.
 ```bash
 $ python historical_cimss_IR_EH_overlay.py
 ```
 5. The output combined images are placed in "overlaid" under "data".
 
 ## Appendix
 1. Is IR oberservation the only product available? <br>
 Ans: One can modify the link following "urllib.urlretrieve" in "realtime_cimss_IR_EH_overlay.py" or paths in "historical_cimss_IR_EH_overlay.py". You can look up the paths from the extracted bundle.
 Here's the combined [water vapor observation](http://i.imgur.com/IIvcwSC.png)
