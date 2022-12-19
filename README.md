# hydrotools

Various tools written in python3 to convert hydrogen to other formats.

```sh
hydro2sfz <HYDROKIT_FILE> <SFZ_FILE>          # generate SFZ file
hydro2sf2 <HYDROKIT_FILE> <SF2_FILE>          # generate SF2 file
hydro2renoise <HYDROKIT_FILE> <RENOISE_FILE>  # generate renoise instrument
getallkits                                    # download all public kits
```

## WIP

I'm still working on it. None of these are really done, but they have the start of some ideas:

- `hydro2renoise` - Renoise instrument
- `hydro2sfz` - SFZ soundfont. 
- `hydro2pti` - Polyend Tracker beat-sliced instrument
- `hydro2sf2` - SF2 sound-font

## usage

In order to use these, you'll need python3 and other dependencies:

```sh
pip3 install -r requirements.txt
```
