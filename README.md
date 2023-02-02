# plover-retro-untranslator

Converts the last X translations to a specified format consisting of raw steno and/or a translation 


# Examples

put these into your dictionary:

```json
{
"RA*UD": "=retro_stroke:`%r`"
"STRO*EBGD": "=retro_stroke:`%T` → `%r`"
}
```

example stroke ⇒ output:

```
KWRURPB/RA*UD ⇒ \`KWRURPB\`
KWRURPB/STRO*EBGD ⇒ \`yes, your Honor\` → \`KWRURPB\`
```

# Configuration

(literally the same thing as tapey-tape)

| Code | Item           | Example                                 |
|:-----|:---------------|:----------------------------------------|
| `%r` | raw steno      | `KWRURPB`                               |
| `%T` | translation    | `Yes, your Honor`                       |
| `%%` | an actual `%`  | `%`                                     |



# Prerequisites

- Download plover and find the executable
	- see this [website](https://plover.readthedocs.io/en/latest/cli_reference.html) for finding the location of plover depending on which platform you are using (Linux, Windows, etc.)

# Installation

- Now run this command to install the library
``` bash
<plover_executable> -s plover_plugins install plover-retro-untranslator
```

# Developers

- This section shows how you can have an editable version of this project
- Firstly, fork this repository (in GitHub), then clone it:

``` bash
git clone https://github.com/your_user_name/plover-retro-untranslator
```

- cd into this repo
- Then install for use!
	- Note that "plover" is the executable that you downloaded to make Plover work in the first place
	- See this [[https://plover.readthedocs.io/en/latest/cli_reference.html][website]] for the different locations depending on which platform you are using (Linux, Windows, etc)

``` bash
cd plover-retro-translator
plover -s plover_plugins install -e .
```

# Acknowledgments

Sachac's [plover-retro-stroke](https://github.com/sachac/plover_retro_stroke) for motivating the creation of this plugin
rabbitgrowth's [tapey-tape](https://github.com/rabbitgrowth/plover-tapey-tape) for motivating the format of this plugin
