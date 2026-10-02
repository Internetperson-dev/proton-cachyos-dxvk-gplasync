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

## Recomendations 


If you are using this solution to deal with shader compilation stutter, it is a good idea to enable shader-pre caching in Steam, and ensure you have an adequate shader cache size 

<img width="850" height="722" alt="image" src="https://github.com/user-attachments/assets/0b1e7155-00e4-4b2c-8607-4d08d713fc8e" />

```
cat > ~/environment.d/gaming.conf <<'EOF'
# Increase Nvidia shader cache size to 120GB
__GL_SHADER_DISK_CACHE_SIZE=120000000000

# Increase AMD's/Intel's? shader cache size to 12GB
MESA_SHADER_CACHE_MAX_SIZE=12G
EOF

cp -p ~/.config/environment.d .var/app/com.valvesoftware.Steam/.config  ; cp -p .config/environment.d .var/app/com.heroicgameslauncher.hgl/.config ; p -p .config/environment.d .var/app/com.github.Matoking.protontricks/.config


flatpak override --user \
  --env=MESA_SHADER_CACHE_MAX_SIZE=120G \
  --env=__GL_SHADER_DISK_CACHE_SIZE=120000000000 \
  com.valvesoftware.Steam
```

## To do

It may be possible to combine the [gplasync patches with DXVK Low Latency](https://github.com/Digger1955/dxvk-gplall) but right now using one disables the other. 

Add UE4 Async mods for certain DX12 games (Source code is needed, perhaps by reverse engineering, as the idea of inserting random closed source DLLs is not a good one.)


Examples :

- https://www.nexusmods.com/finalfantasy7rebirth/mods/2107
- https://gamebanana.com/mods/687363





