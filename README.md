Introduction
------------

Proton-cachyos is a version of Proton-GE with specific tweaks.

[The problem is gplasync support was removed in 10.0-20260312 version of Proton-catchyos](https://github.com/CachyOS/proton-cachyos/blob/cachyos_main/CHANGELOG.md#:~:text=gplasync%20has%20been%20removed%20from%20our%20alternative%20DXVK%2C%20and%20with%20it%20PROTON%5FDXVK%5FGPLASYNC%2E%20PROTON%5FDXVK%5FLOWLATENCY%20remains%2C%20and%20it%20is%20the%20only%20option%20now
)


gplasync is a way to get Asynchronous shaders in DXVK. This would prevent some shader compilation stutter which can be helpful in certain cases at the cost of potentially having some graphical glitches.


Using a older version of Proton is not a good idea for performance, or compatibility concerns. For example missing out on the video playback improvements in Proton-GE 11. This is why this fork was made.

It is used by applying `DXVK_ASYNC=1 %command%`  as a launch option in Steam after installing this custom version of Proton in Steam/compatibilitytools.d/

A correct local tool installation should look similar to this:
```
compatibilitytools.d/my_proton/
├── compatibilitytool.vdf
├── filelock.py
├── LICENSE
├── proton
├── proton_dist.tar
├── toolmanifest.vdf
├── user_settings.sample.py
└── version
```


DXVK handles DirectX 8, 9, 10, and 11 calls. 



## To do

It may be possible to combine the [gplasync patches with DXVK Low Latency](https://github.com/Digger1955/dxvk-gplall) but right now using one disables the other. 

Add UE4 Async mods for certain DX12 games (Source code is needed, perhaps by reverse engineering, as the idea of inserting random closed source DLLs is not a good one.)


Examples :

- https://www.nexusmods.com/finalfantasy7rebirth/mods/2107
- https://gamebanana.com/mods/687363





