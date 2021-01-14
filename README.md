# hydrotools

Various tools written in python3 to convert hydrogen to other formats.

```sh
hydro2sfz <HYDROKIT_FILE> <SFZ_FILE>          # generate SFZ file
hydro2sf2 <HYDROKIT_FILE> <SF2_FILE>          # generate SF2 file
hydro2renoise <HYDROKIT_FILE> <RENOISE_FILE>  # generate renoise instrument
getallkits                                    # download all public kits
```

## WIP

I'm still working on it.

- `hydro2renoise` - still needs work, but it can do simple drumkits
- `hydro2sfz` - rudimentary. Seems to work with simple drumkits
- `hydro2sf2` - not implemented

## usage

In order to use these, you'll need python3 and other dependencies:

```sh
pip3 install -r requirements.txt
```
