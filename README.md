# Vivaldy

🎼 Your obligatory Python addition dedicated to the tastefully improvement of
your waiting experience while running long and/or slow scripts.

Keywords: music on hold, musique d'attente, ASSEDIC, Vivaldi

🎹 Developed and maintained by Yann,
inspired by an original idea from Jeanne and Thomas.

> 🎧 **Stay tuned!** Vivaldy is being actively developed; new features may be
added any time.

## Description

Vivaldy is to your Python code what Vivaldi is to your phone calls to public
administration and other serious organisations. It is a natural and unmissable
addition to any Python code that requires a long waiting time when running.

It is _scientifically proven™_
([Hul _et al._ 1997](https://doi.org/10.1016/S0022-4359%2897%2990016-6))
that waiting music has a positive impact on the user experience.

Be careful, however, as the valence of your selected waiting music may
influenced the perceived waiting time: it has been established that "perceived
duration was longest for subjects exposed to positively valenced (major key)
music, and shortest for negatively valenced (atonal) music"
[Kellaris & Kent (1992)](https://doi.org/10.1016/S1057-7408%2808%2980060-5).

Short historical background (en français):
<https://www.rtbf.be/article/mozart-et-vivaldi-les-stars-de-la-musique-d-attente-telephonique-11284821>

## Installation

If needed, create a dedicated environment:

```
conda create -n vivaldy
```

Alternatively, for testing purpose, you may want to clone an existing
environment:

```
conda create -n myenv_with_vivaldy --clone myenv
```

Activate the environment you just created, or another existing environment of
your choice:

```
conda activate MY_ENV_FOR_VIVALDY
```

Then, from within `vivaldy` base folder:

```
conda install -c conda-forge --yes --file requirements.txt
pip install -r pip_requirements.txt
pip install .
```

Ensure everything is working properly by trying to import and run `vivaldy`:

```python
import vivaldy
music = vivaldy.MusicOnHold().start()
music.stop()
```

You shouldn't get any error running this short script.

## Documentation

More coming sooner or later. For now, it is as simple as it can get:

```python
## Vivaldy toy example
import vivaldy
import time # only for testing

# Let's start waiting!
music = vivaldy.MusicOnHold()
music.start()
# ...or simply vivaldy.MusicOnHold().start() with no handler

for i in range(10):
    print(f"Processing {i+1:d}/10...")
    # Some very important processing...
    time.sleep(5)

# And now we are done
music.done() # This line is not required

# Use music.wait() to wait till the end of the music
# (not recommended due to potential productivity loss)
```

## Known major or minor bugs

No tonal bugs in there.

## Future

- Restart music while needed
- Periodic announcements about estimated waiting time
- Integrate with `tqdm`

## Tools used

- Coding: Emacs with Spacemacs config
- Python packages: see (pip_)requirements.txt

## Licence

This software is licensed under the [EUPL](LICENSE.md).

## Acknowledgements

Many thanks to all the current and future beta-testers!

To Vivaldi and Mozart as well, and of course to
[Alfred Levy](https://en.wikipedia.org/wiki/Music_on_hold).

