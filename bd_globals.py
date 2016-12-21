#!/usr/bin/env python
# encoding: utf-8
# Alexander Kucera
# babylondreams.de

# Description
"""

The idea when I am done is for this to be the central repository of all things pipeline.

Release Notes:

V0.1 Initial Release

"""

import traceback
import json


# FUNCTIONS -----------------------------------------------

# END FUNCTIONS -----------------------------------------------

# MAIN PROGRAM --------------------------------------------
def main():

    with open('/Volumes/ProjectsRaid/x_Pipeline/x_AppPlugins/bd_pipeline/global_config.json') as json_data:
        babvars = json.load(json_data)

    print(json.dumps(babvars, sort_keys=True, indent=4))

    with open("/Volumes/ProjectsRaid/x_Pipeline/x_AppPlugins/bd_pipeline/global_config_test.json", "w") as outfile:
        json.dump(babvars, outfile, sort_keys=True, indent=4)

    return babvars


# END MAIN PROGRAM -----------------------------------------------

if __name__ == '__main__':

    try:
        main()  # call the script with any arguments here.

    except:
        traceback.format_exc()
